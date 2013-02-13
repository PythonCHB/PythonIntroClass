#!/usr/bin/python

from __future__ import print_function
import re #reg expression
import xml.etree.ElementTree as ET
import hashlib
import os
import urllib2
import getpass
import base64
import sys

def get_drives(function="drives"):

	drives = {}
	lines = []

	drives_added = []
	manf_added = []
	FW_updated = []

	username = raw_input("Username: ")
	password = getpass.getpass("Password: ")
	request = urllib2.Request("https://svn.west.isilon.com/view/onefs/head/src/isilon/lib/isi_hw/drive_config.gc?view=co")
	baseStr = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % baseStr)
	try:
            f = urllib2.urlopen(request)
            for line in f.readlines():
                print (line)
                #Get the three lines for each drive
                if re.search('#|^.*}|driveconfigs|GCONFIG',line) == None:
                    if line != '\n':
                        if re.search('model|manufacturer',line) != None:
                            line = re.search('".*"', line.strip()).group(0).strip("\"")
                            line = line.replace(" ", "_")
                            lines.append(line)
                        elif re.search('fwversions',line) != None:
                            line = line.strip().replace(' ', '')
                            line = re.search('".*"', line).group(0).split(",")[-1].strip('\"')
                            lines.append(line)
        except urllib2.HTTPError as e:
            print(e, end='\n')
            sys.exit(1)

	#Make a dictionary for each Manufacturer
	#	Which contain a list of dictionary entries for each drive of each Manf
	#
	#Format: {Manf: [{Model: MODEL#, FW: FWNAME}]}
	for model, manf, FW in zip(lines[0::3], lines[1::3], lines[2::3]):
		if drives.has_key(manf):
			drives[manf].append({'Model': model, 'FW': FW})
		else:
			drives[manf] = [{'Model': model, 'FW': FW}]

        if(function == "CSV"):
		#Create a CSV file of model, FW. Sorted by Manf
		CSV = open("drives.csv", "w")
		for manf, drive in drives.items():
		    CSV.write("Manf, " + manf + ";\n")
		    for d in drive:
			CSV.write(d['Model'] + ", " + d['FW'] + ";\n")
		    CSV.write(", ;\n")
	else:
		#Build/Update the XML
		if os.path.isfile('drives.xml'): #Update
			#Create a back up
			
			tree = ET.parse('drives.xml')
			root = tree.getroot()
			for manf, drive in drives.items():
				man = root.find(manf)
				if man is None: #this manf doesn't exist, add it
					man = ET.SubElement(root, manf)
					man.tail = '\n'
					manf_added.append(manf)
				#at this point, the manf is either found or added
				for d in drive:
					driv = man.find(d['Model'])
					if driv is None: #drive doesn't exist, add it
						driv = ET.SubElement(man, d['Model'])
						driv.text = '\n         '
						driv.tail = '\n      '
						drives_added.append(d['Model'])
						fw = ET.SubElement(driv, 'FW1')
						fw.tail = '\n         '
						binary = ET.SubElement(driv, 'Binary')
						binary.tail = '\n         '
						md = ET.SubElement(driv, 'MD5')
						md.tail = '\n         '
					#at this pont, the drive is either found or added
					if (driv.find('FW1').text is None) or (driv.find('FW1').text != d['FW']):
						driv.find('FW1').text = d['FW']
						FW_updated.append(d['FW'])
			tree.write('drives.xml')
			#output the results
			print ("\nDrives added:", end='\n')
			for d in drives_added:
				print ("   " + d, end='\n')
			print ("Manf added:", end='\n')
			for m in manf_added:
				print("   " + m, end='\n')
			print ("FW Updated:", end='\n')
			for f in FW_updated:
				print("   " + f, end='\n')
			print ("", end='\n')
		else: #create
			XML = open('drives.xml', 'w')
			XML.write("<drives>\n")
			for manf, drive in drives.items():
				XML.write("   <" + manf + ">\n")
				for d in drive:
					XML.write("      <" + d['Model'] + ">\n")
					XML.write("         <FW1>" + d['FW'] + "</FW1>\n")
					XML.write("         <Binary>" + "" + "</Binary>\n")
					XML.write("         <MD5>" + "" + "</MD5>\n")
					XML.write("      </" + d['Model'] + ">\n")
				XML.write("   </" + manf + ">\n")
			XML.write("</drives>")
			print("drives.xml created.", end='\n')

def run_MD5():
	tree = ET.parse('drives.xml')
	root = tree.getroot()
	for manf in root:
		drive_man = manf.tag
		for drive in manf:
			try:
				m = hashlib.md5()
				binary = open("drivefw/" + drive_man + "/" + drive.find('Binary').text, 'r')
				m.update(binary.read())
				drive.find('MD5').text = m.hexdigest()
			except TypeError:
				drive.find('Binary').text = "None"
				drive.find('MD5').text = "None"
			except IOError:
				if drive.find('Binary').text != "None":
					print("Could not find binary " + drive.find('Binary').text + " for drive " + drive.tag, end='\n')
	tree.write('drives.xml')
	print("MD5's updated.", end='\n')

command = raw_input("Which would you like to run?\n1) Get drives\n2) MD5\n3) CSV\nSelection: ")

if(int(command) == 1):
	get_drives("drives")
elif(int(command) == 2):
	run_MD5()
else:
	get_drives("CSV")
