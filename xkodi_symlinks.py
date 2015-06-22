#!/usr/bin/python
	
""" Create xbmc/kodi config symlinks from zip file 
	Remember to have kodi AND xbmc in in seperate folders (for now)

	~/mCconfig/ should contain mCconfigs.zip and xkodi_symlinks.py

	Example: 
		"./xkodi_symlinks.py" extracts configs and sets symlinks to proper location

	Hint: "zip -r mCconfigs.zip kodi" 
	(creating zipfile containing folders: xbmc and kodi) """

import os
import zipfile
import os.path

from os.path import isfile, join, isdir, expanduser
from os import listdir

## function to create symlinks
def createSymLinks(dist, dlist, userHome):

	""" Creating symbolic links to configuration files in the distribution 
		config dir """

	target = userHome+"."+dist+"/userdata/"
	sourceLoc = os.getcwd()+"/kodi/userdata/"
	#curPath = os.getcwd()

	print "\nTarget location: ", target
	print "Source location: ", sourceLoc, "\n"

	for d in dlist:
		sourceStr = sourceLoc+d
		targetStr = target+d
		print sourceStr, " -> ", targetStr
		os.symlink(sourceStr, targetStr)
	print ""
## </createSymLinks>

## getDistribution installed on system 
def getDist(homedirs):

	""" Get installed mediacenter distribution (xbmc/kodi) """

	retValue = ""
	found = False

	for d in homedirs:
		if not found:
			if d == ".kodi":
				retValue = "kodi"
				found = True
			elif d == ".xbmc":
				retValue = "xbmc"
				found = True

	return retValue
## </getDist>

## unzipConfigFiles function 
def unzipConfigFiles(fname, unzipDir):

	""" unzip the copied file containing mediacenter config files """

	print fname, " to ", unzipDir

	zfile = zipfile.ZipFile(fname)
	for name in zfile.namelist():
		if name.endswith('/'):
			os.makedirs(name)
	zfile.extractall(unzipDir)
## </unzipConfigFiles>


####### "Real" program stuff

## zip-file with configfiles
#zfname = "mCconfigs.zip"

## file-list with config filenames
#dlist = ['advancedsettings.xml', 'sources.xml', 'keymaps/remote.xml', 'guisettings.xml']
dlist = ['advancedsettings.xml', 'sources.xml']
#print dlist

## current users home-folder 
userHome = expanduser("~/")

## unzip configuration files 
#unzipConfigFiles(zfname, os.getcwd())

## get directories in the home folder, to check installed package (xbmc/kodi)
homedirs = [ d for d in listdir(userHome) if isdir(join(userHome,d))]
#print homedirs
## get (xbmc/kodi) distribution from directory-list
localDist = getDist(homedirs)
print "\nDistribution: ", localDist		# print distribution 

createSymLinks(localDist, dlist, userHome)		# create sym-links to config files
