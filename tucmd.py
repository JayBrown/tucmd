#!/usr/bin/python3

########################################################################
# This program is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# This program is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.#
#                                                                      #
# Copyright (c) 2014 by marcomg                                        #
# Modification: Copyright (c) 2021 by Joss Brown (pseud.)              #
########################################################################

# from std library
import argparse
import os

# from local library
import tulib

# @var float - program version
VERSION = 2.0;

argParse = argparse.ArgumentParser(description='A program to upload files to tinyupload.com', prog='tucmd.py')
argParse.add_argument('-v', '--version', action='version', version='%(prog)s v' + str(VERSION))
argParse.add_argument('upload', action='store', type=str, help='Upload local file');
argParse.add_argument('-f', '--file', action='store', type=str, help='Local filepath')
args = argParse.parse_args()

if args.upload == 'upload':
	try:
		localFile = args.file
		downloadURL = tulib.upload(localFile)
		print(downloadURL)
	except FileNotFoundError:
		print('ERROR - missing file: %s' % (localFile))
	except ResourceWarning:
		print('ERROR - upload: %s' % (localFile))

else:
	print('Unknown command "%s": use "--help" for more details' % (args.command))
