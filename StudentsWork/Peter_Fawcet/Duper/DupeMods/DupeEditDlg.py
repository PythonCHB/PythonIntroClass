#!/usr/bin/env python

import wx


class ReqData(wx.PyValidator):
    def __init__(self, data, key):
        wx.PyValidator.__init__(self)
        self.data = data
        self.key = key

    def Clone(self):
        return ReqData(self.data, self.key)

    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        if len(text) == 0:
            wx.MessageBox("This filed must contain some text.", "Error")
            textCtrl.SetBackgroundColour("pink")
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True

    def TransferToWindow(self):
        textCtrl = self.GetWindow()
        textCtrl.SetValue(self.data.get(self.key, ""))
        return True

    def TransferFromWindow(self):
        textCtrl = self.GetWindow()
        self.data[self.key] = textCtrl.GetValue()
        return True


class OptData(wx.PyValidator):
    def __init__(self, data, key):
        wx.PyValidator.__init__(self)
        self.data = data
        self.key = key

    def Clone(self):
        return OptData(self.data, self.key)

    def Validate(self, win):
        return True

    def TransferToWindow(self):
        textCtrl = self.GetWindow()
        textCtrl.SetValue(self.data.get(self.key, ""))
        return True

    def TransferFromWindow(self):
        textCtrl = self.GetWindow()
        self.data[self.key] = textCtrl.GetValue()
        return True


class DupeEdit(wx.Dialog):
    def __init__(self, data, title="Edit Dupe Item", about_txt=""):
        wx.Dialog.__init__(self, None, -1, "Edit Dupe Item", style=wx.DEFAULT_FRAME_STYLE)
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Info text
        if about_txt:
            about = wx.StaticText(self, -1, about_txt)
            sizer.Add(about, 0, wx.ALL, 5)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.ALL, 5)
        fgs = wx.FlexGridSizer(rows=4, cols=2, hgap=6, vgap=6)
        self.make_label_field('File Name', fgs, 'name', data, ReqData)
        self.make_label_field('Artist', fgs, 'artist', data, OptData)
        self.make_label_field('BPMs', fgs, 'bpms', data, OptData)
        self.make_label_field('Length', fgs, 'length', data, OptData)
        fgs.AddGrowableCol(1)
        sizer.Add(fgs, 0, wx.EXPAND | wx.ALL, 5)
        self.make_buttons(sizer)
        self.SetSizer(sizer)
        sizer.Fit(self)

    def make_label_field(self, label, sizer, key, data, valdate):
        text_l = wx.StaticText(self, -1, ("%s:" % (label.capitalize())))
        text_c = wx.TextCtrl(self, validator=valdate(data, key), size=(400, -1))
        sizer.Add(text_l, 0, wx.ALIGN_RIGHT)
        sizer.Add(text_c, 0, wx.EXPAND)

    def make_buttons(self, sizer):
        ok_b = wx.Button(self, wx.ID_OK)
        ok_b.SetDefault()
        cancel_b = wx.Button(self, wx.ID_CANCEL)
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(cancel_b)
        btns.AddButton(ok_b)
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND | wx.ALL, 5)

if __name__ == '__main__':
    import pprint
    app = wx.PySimpleApp()
    data = {"name": "SomeAudioClip.aiff"}
    dlg = DupeEdit(data)
    mReturn = dlg.ShowModal()
    dlg.Destroy()
    wx.MessageBox("You entered these values:\n\n" + pprint.pformat(data))
    app.MainLoop()
