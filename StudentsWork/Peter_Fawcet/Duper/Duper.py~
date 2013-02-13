#!/usr/bin/env python

import os
import wx
import wx.html
#from wx.lib import pydocview
import webbrowser
from DupeMods.DupeEditDlg import DupeEdit

from DupeMods.dupe_checker import DupeChecker
from DupeMods.DupeData import DupeShelve


class DuperApp(wx.App):
    def __init__(self, *args, **kwargs):
        wx.App.__init__(self, *args, **kwargs)
        # This catches events when the app is asked to activate by some other
        # process
        self.Bind(wx.EVT_ACTIVATE_APP, self.OnActivate)

    def OnInit(self):
        self.frame = DuperFrame("Duper", (50, 60), (450, 340))
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

    def BringWindowToFront(self):
        try:
            self.GetTopWindow().Raise()
        except:
            pass

    def OnActivate(self, event):
        if event.GetActive():
            self.BringWindowToFront()
        event.Skip()

    def MacOpenFile(self, filename):
        """Called for files droped on dock icon, or opened via finders context menu"""
        # Note: In some contexts 'filename' can be 'Duper.py' (or ./Duper.py).
        # Make sure we only open our db files this way... May want more custom ext...
        parts = filename.split('.')
        ext = parts[-1]
        if ext == 'db':
            self.frame.DoOpenFile(filename)

    def MacReopenApp(self):
        """Called when the doc icon is clicked, and ???"""
        self.BringWindowToFront()

## TODO list:
 # Toolbar icon for delete current clip :: IN PROGRESS
 # Toolbar icon for set single clip :: IN PROGRESS
 # Double click on clips: Edit clip name and maybe metadata :: IN PROGRESS
 ### Still searching for python audio support for aiff. wav exists.
 # Play / Pause / Stop icons
 # Build Edit Dialog. For file double clicks
 # Build Audio Playback Support.


class DuperFrame(wx.Frame):
    ## Constructor
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        self.current_dupe_file = ''  # Current shelve db file.
        self.current_scan_path = ''  # Root directories for currently loaded dupe scan.
        self.scan_dataset = {}  # Main data set. In format of key:list
        self.value_key_map = {}  # Reverse lookup of flie to hash
        self.dupe_checker = DupeChecker()  # Dupe scanner code.
        self.clip_count = 0
        self.is_dirty = False  # If a new scan is done or a file touched, set to true.
        ###  Start of wxPython UI Code:
        self.BuildToolbar()
        self.SetMenuBar(self.BuildMenubar())
        self.CreateStatusBar()
        self.SetStatusText('Welcome to Duper')
        self.CreateTree()
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    ## Dupe Tree Code ##
    ## Create the primary tree control used to display the dupe data.
    def CreateTree(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.tree = wx.TreeCtrl(self, id=-1, pos=wx.DefaultPosition,
          size=wx.DefaultSize, style=wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT,
          validator=wx.DefaultValidator, name="treeCtrl")
        sizer.Add(self.tree, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnTItemActivate, self.tree)
        self.UpdateTree()

    # Called after the data set has changed (after a scan or a db load).
    def RebuildTree(self):
        self.tree.DeleteAllItems()
        self.UpdateTree()

    # Called any time that the tree needs to paint it's data.
    def UpdateTree(self):
        root = self.tree.AddRoot("Duplicate Set")
        for key in self.scan_dataset:
            key_id = self.tree.AppendItem(root, key)
            for item in self.scan_dataset[key]:
                self.tree.AppendItem(key_id, item)
                self.value_key_map[item] = key

    ## Toolbar Code ##
    def BuildToolbar(self):
        toolbar = self.CreateToolBar()
        toolbar.SetToolBitmapSize(wx.Size(16, 16))
        self.AddTool(toolbar, 'icons/database_add.png', 'New Scan',
                     'Scan for duplicate sound files.', self.OnNewScan)
        self.AddTool(toolbar, 'icons/database_refresh.png', 'Re-Scan',
                     'Rescan the current data set to capture file system changes.', self.OnRescanDataset)
        self.AddTool(toolbar, 'icons/database_link.png', 'Validate',
                     'Revalidate current file paths (verify file existance).', self.OnRevalidateData)
        self.AddTool(toolbar, 'icons/database.png', 'Open Dupes File',
                     'Open a previously saved dupes scan.', self.OnOpenDupes)
        self.AddTool(toolbar, 'icons/disk.png', 'Save Dupes File',
                     'Save the current dupes scan data.', self.OnSaveDupes)
        toolbar.AddSeparator()
        self.AddTool(toolbar, 'icons/page_delete.png', 'Delete Selected Clip',
                     'Delete the currently selected clip.', self.OnDoFileRemove)
        self.AddTool(toolbar, 'icons/page_link.png', 'Set Single Clip',
                     'Designate one clip as master. All others will replaced with links.',
                     self.OnDoFileAliasReplace)
        toolbar.Realize()

    def AddTool(self, toolbar, icon, help_, long_help, function):
        icon_png = wx.Image(icon, wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        tool = toolbar.AddSimpleTool(wx.NewId(), icon_png, help_, long_help)
        self.Bind(wx.EVT_TOOL, function, tool)

    ## Menu Bar Code ##
    def BuildMenubar(self):
        menuFile = wx.Menu()
        self.AddMenuItem(menuFile, '&New Scan...', self.OnNewScan)
        self.AddMenuItem(menuFile, '&Save Dupe Set...', self.OnSaveDupes)
        self.AddMenuItem(menuFile, 'Save Dupe Set As...', self.OnSaveDupesAs)
        self.AddMenuItem(menuFile, '&Open Dupe Set...', self.OnOpenDupes)
        menuFile.AppendSeparator()
        self.AddMenuItem(menuFile, 'Quit', self.OnQuit, wx.ID_EXIT)
        menuEdit = wx.Menu()
        self.AddMenuItem(menuEdit, "Cut", self.OnCut, wx.ID_CUT)
        self.AddMenuItem(menuEdit, "&Copy", self.OnCopy, wx.ID_COPY)
        self.AddMenuItem(menuEdit, "Paste", self.OnPaste, wx.ID_PASTE)
        menuEdit.AppendSeparator()
        self.AddMenuItem(menuEdit, "Delete Selected Clip", self.OnDoFileRemove)
        self.AddMenuItem(menuEdit, "Set Single Clip", self.OnDoFileAliasReplace)
        menuEdit.AppendSeparator()
        self.AddMenuItem(menuEdit, "&Preferences", self.OnPrefs, wx.ID_PREFERENCES)
        menuHelp = wx.Menu()
        self.AddMenuItem(menuHelp, '&About Duper', self.OnAbout, wx.ID_ABOUT)
        self.AddMenuItem(menuHelp, 'Help', self.OnHelp)
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, '&File')
        menuBar.Append(menuEdit, '&Edit')
        menuBar.Append(menuHelp, '&Help')
        return menuBar

    def AddMenuItem(self, menu, text, function, item_id=None):
        if not item_id:
            item_id = wx.NewId()
        menu.Append(item_id, text)
        self.Bind(wx.EVT_MENU, function, id=item_id)

    ## About Box Uses AboutHTML defined below.
    def OnAbout(self, event):
        dlg = wx.Dialog(self, -1, 'About Duper', size=(440, 400))
        html = AboutHTML(dlg)
        html.SetPage(html.GetAboutTxt())
        button = wx.Button(dlg, wx.ID_OK, "Ok")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        dlg.SetSizer(sizer)
        dlg.Layout()
        dlg.ShowModal()

    def OnHelp(self, event):
        dlg = wx.Dialog(self, -1, 'About Duper', size=(440, 400))
        html = wx.html.HtmlWindow(dlg)
        html.SetPage(self.GetHelpHTML())
        button = wx.Button(dlg, wx.ID_OK, "Ok")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        dlg.SetSizer(sizer)
        dlg.Layout()
        dlg.ShowModal()

    ## Event Handlers ##
    def OnQuit(self, event):
        self.Close()

    def OnCloseWindow(self, event):
        if self.is_dirty:
            dlg = wx.MessageDialog(None,
                "The current dupe scan data has not been saved. Do you want to save this data?",
                'Unsaved Data', wx.YES_NO | wx.ICON_EXCLAMATION)
            retCode = dlg.ShowModal()
            if (retCode == wx.ID_YES):
                self.DoDataSave(self.current_dupe_file)
        self.scan_dataset = None
        self.value_key_map = None
        self.dupe_checker = None
        self.Destroy()

    def OnCut(self, event):
        pass

    def OnCopy(self, event):
        pass

    def OnPaste(self, event):
        pass

    def OnPrefs(self, event):
        pass

    def OnNewScan(self, event):
        scan_path = self.DoGetScanPath()
        if (scan_path):
            self.DoDupeScan(scan_path)
            self.current_scan_path = scan_path

    def OnRevalidateData(self, event):
        invalid_paths = []
        for key in self.scan_dataset:
            for path in self.scan_dataset[key]:
                if not os.path.exists(path):
                    invalid_paths.append(path)
        dlg = None
        if not invalid_paths:
            dlg = wx.MessageDialog(None, 'The current data files are valid.',
                             'Validation Complete', wx.OK | wx.ICON_INFORMATION)
        else:
            dlg = wx.MessageDialog(None, "The following files do not seem to exist any longer."
                             "Validatioin Complete", wx.YES_NO | wx.ICON_INFORMATION)
        retCode = dlg.ShowModal()
        if invalid_paths and retCode:
            pass
        # Display invalid data and ask what to do...

    def OnRescanDataset(self, event):
        if self.current_scan_path:
            self.DoDupeScan(self.current_scan_path)
        else:
            dlg = wx.MessageDialog(None,
                "There is no scan data to re-process.",
                'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()

    def DoGetScanPath(self):
        scan_path = ''
        dialog = wx.DirDialog(self, "Choose a directory:", defaultPath=os.getcwd(),
                              style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            scan_path = dialog.GetPath()
        dialog.Destroy()
        return scan_path

    def DoDupeScan(self, scan_path):
        self.clip_count = self.dupe_checker.pre_scan(scan_path,
                                                ('aiff', 'aif', 'wav'))
        if self.clip_count > 0:
            self.dupe_checker.do_scan()
            display_txt = "Scanning %d audio clips" % (self.clip_count)
            prog_dlg = wx.ProgressDialog("Dupe Scan Progress", display_txt, 100,
                                         style=wx.PD_CAN_ABORT | wx.PD_REMAINING_TIME |
                                         wx.PD_ELAPSED_TIME)
            current = 0
            do_more = True
            while current < self.clip_count:
                progress = (float(current) / float(self.clip_count)) * 100
                wx.Sleep(1)
                do_more = prog_dlg.Update(progress, "Scanned %d of %d clips" %
                                          (current, self.clip_count))
                if not do_more[0]:
                    self.dupe_checker.do_shutdown()
                    break
                current = self.dupe_checker.update()
            if do_more[0]:
                self.scan_dataset = self.dupe_checker.get_data()
                self.RebuildTree()
                self.is_dirty = True
            prog_dlg.Destroy()

    def OnDoFileRemove(self, event):
        item = self.tree.GetSelection()
        item_text = self.tree.GetItemText(item)
        # Verify that it's a file and not a hash.
        if item_text not in self.scan_dataset:
            dlg = wx.MessageDialog(None, 'Do you really want to simply delete the file %s?' % (item_text),
                               'Delete Confirmation',
                               wx.YES_NO | wx.ICON_EXCLAMATION)
            retCode = dlg.ShowModal()
            do_remove = False
            if (retCode == wx.ID_YES):
                do_remove = True
            dlg.Destroy()
            if do_remove:
                # Delete Item From File System, the tree and the data.
                # mark the data as dirty.
                dupe_hex = self.value_key_map[item_text]
                del self.value_key_map[item_text]
                del self.scan_dataset[dupe_hex][item_text]
                os.unlink(item_text)
                self.tree.Delete(item)
                self.is_dirty = True

    def OnDoFileAliasReplace(self):
        # Get Selected File Path from tree.
        # If Path and not Hash.
        # Do 'Are You Sure' Dlg.
        # Get Path to master file
        # Delete Sub File
        # Create Alias to master file.
        #   self.tree.Delete(item)
        pass

    def OnTItemActivate(self, event):
        item = event.GetItem()
        item_text = self.tree.GetItemText(item)
        hash_key = ''
        file_path = ''
        if item_text in self.scan_dataset:
            if self.tree.IsExpanded(item):
                self.tree.Collapse(item)
            else:
                self.tree.Expand(item)
        else:
            # Have file path
            file_path = item_text
            hash_key = self.value_key_map[item_text]
        if file_path and hash_key:
            file_name = os.path.basename(file_path)
            file_data = {"name": file_name}
            edit_dlg = DupeEdit(file_data, "Edit %s" % (file_name))
            edit_dlg.ShowModal()
            edit_dlg.Destroy()
            print "Return Data => ", str(file_data)
        ## TODO: Need to finish edit functionality

    def OnSaveDupes(self, event):
        if not self.scan_dataset:
            dlg = wx.MessageDialog(None,
                "There is no dupe scan data to save.",
                'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
        else:
            self.DoDataSave(self.current_dupe_file)

    def OnSaveDupesAs(self, event):
        if not self.scan_dataset:
            dlg = wx.MessageDialog(None,
                "There is no dupe scan data to save.",
                'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
        else:
            self.DoDataSave('', True)

    def DoOpenFile(self, filename):
        if (os.path.exists(os.path.abspath(filename))):
            print 'filename => ', filename
            d_shelve = DupeShelve()
            full_data = d_shelve.ReadDB(filename)
            self.scan_dataset = full_data['scan_data']
            self.current_scan_path = full_data['scan_path']
            self.current_dupe_file = filename
            self.RebuildTree()

    def OnOpenDupes(self, event):
        open_path = self.GetFilePath('Open Dataset', wx.OPEN)
        if (open_path):
            d_shelve = DupeShelve()
            full_data = d_shelve.ReadDB(open_path)
            self.scan_dataset = full_data['scan_data']
            self.current_scan_path = full_data['scan_path']
            self.current_dupe_file = open_path
            self.RebuildTree()

    def DoDataSave(self, in_path, is_new=False):
        if not in_path or is_new:
            dlg_txt = 'Save New Dataset'
            if is_new:
                dlg_txt = 'Save Dataset As...'
            in_path = self.GetFilePath(dlg_txt, wx.SAVE)
        if in_path:
            full_data = {}
            full_data['scan_data'] = self.scan_dataset
            full_data['scan_path'] = self.current_scan_path
            d_shelve = DupeShelve()
            d_shelve.WriteDB(in_path, full_data)
            self.is_dirty = False

    ## Helpers and utlitiy funcs ##
    def GetFilePath(self, title, dlg_type):
        save_path = ''
        allowed_types = "Python DB (*.db)|*.db|" \
                        "All files (*.*)|*.*"
        dialog = wx.FileDialog(self, title, os.getcwd(), "", allowed_types, dlg_type)
        if dialog.ShowModal() == wx.ID_OK:
            save_path = dialog.GetPath()
        dialog.Destroy()
        return save_path

    def GetHelpHTML(self):
        return """<html>
    <body>
        <h1 align="center">Duper Help</h1>
        <hr />
        <h3>Index</h3>
        <ol>
        </ol>
    </body>
</html>"""


## Helper function: Simply returns the html content for the about box...
class AboutHTML(wx.html.HtmlWindow):
    text = """
<html>
    <body bgcolor="#667D74" color="#000000">
        <table align="center">
            <tr bgcolor="#F4F7F5">
                <td align="center" color="#222A27"><h1>Duper</h1></td>
            </tr>
            <tr bgcolor="#F4F7F5">
                <td align="center">
                    <p>Duper finds duplicate audio files on your system and provides
                    an interface for resolving dupes in a variety of ways.</p>
                </td>
            </tr>
            <tr bgcolor="#F4F7F5">
                <td align="center">
                    <p>Made by <a href="http://soundsweepsby.com/" target="extern">SoundSweepsBy</a>
                </td>
            </td>
        </table>
    </body>
</html>
"""

    def __init__(self, parent):
        wx.html.HtmlWindow.__init__(self, parent, id=-1, pos=wx.DefaultPosition,
          size=wx.DefaultSize, style=wx.html.HW_SCROLLBAR_AUTO,
          name="aboutlWindow")

    def GetAboutTxt(self):
        return self.text

    def OnLinkClicked(in_type, in_link):
        webbrowser.open(in_link.Href, 2, True)
        return wx.html.HTML_BLOCK


if __name__ == '__main__':
    app = DuperApp()
    app.MainLoop()
