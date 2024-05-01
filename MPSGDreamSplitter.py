#!/usr/bin/env python

# NMAP Parser - A splitter of text files into evenly sized files.
#
# Description:
#   Creates files from a given text file. Input expected
#   is .txt, and output is .txt.
#
# Author:
#   Jessa (@manicPxiSIEMGirl)
#
#	Version 1.3
#	Updated: 3/12/26
#
###########################################################

###########################################################
#
# To Do:
#  1)
#
###########################################################

import codecs
import sys
import argparse
import os.path
import math

class split:
	def __init__(self, inputFile, number, outputDirectory):
		self.__inputFile = inputFile
		self.__number = number
		self.__outputDirectory = outputDirectory

	def split(self):
		try:
			with open(self.__inputFile, "r") as f:
				length = len(f.readlines())
			f.close()
			f = open(self.__inputFile,"r")
			lines = 0
			remainder = 0
		except:
			print("Input file not found. Please ensure the file is a valid .txt file stored in ",self.__inputFile)
			sys.exit(1)

		try:
			#split
			lines = int(math.floor(int(length)/int(self.__number)))
			remainder = int(length)-(int(lines)*int(self.__number))

			for i in range(0,lines):
				for j in range(0,int(self.__number)):
					fileSTR = str(self.__outputDirectory) + str(j) + ".txt"
					o = open(fileSTR,"a")
					o.write(f.readline())
					o.close()
			
			for k in range(0,remainder):
				fileSTR = str(self.__outputDirectory) + str(k) + ".txt"
				o = open(fileSTR,"a")
				o.write(f.readline())
				o.close()
			
			f.close()
		except:
			print("Failed to create output files")
			sys.exit(1)

# Process command-line arguments.
if __name__ == '__main__':
	# Explicitly changing the stdout encoding format
	if sys.stdout.encoding is None:
		# Output is redirected to a file
		sys.stdout = codecs.getwriter('utf8')(sys.stdout)
	argParser = argparse.ArgumentParser(add_help = True, description = "Performs a split of a valid .txt file "
														"into a specified number of .txt files.")
	argParser.add_argument('-inputFile', action='store', help='input nmap file in xml format')
	argParser.add_argument('-number', choices=['2','3','4','5','6','7','8','9','10'], help='number of files to split the input file into')
	argParser.add_argument('-outputDirectory', action='store' , help='output directory')

	#Error check empty expected items
	if len(sys.argv)==1:
		argParser.print_help()
		sys.exit(1)
	options = argParser.parse_args()
	if options.inputFile is None:
		print("An input file must be specified. This file should be a .txt file.")
		sys.exit(1)
	if options.number is None:
		print("Please specify the number of files to split the input file into.")
		sys.exit(1)
	if options.outputDirectory is None:
		options.outputDirectory = "./"

	#Append and handle file extensions and directory traversal
	try:
		if not(os.path.isdir(options.outputDirectory)):
			print("Please provide a valid directory path, or check permissions on the folder. The provided directory was: ",options.outputDirectory)
			sys.exit(1)
	except:
		sys.exit(1)
	if not(str(options.outputDirectory).endswith("/")):
		options.outputDirectory = options.outputDirectory + "/"
	
    #Split
	splitter = split(options.inputFile,options.number,options.outputDirectory)
	try:
		splitter.split()
	except:
		print("Splitting of file failed. This is due to a series of deeper failures. Maybe brush some salt into it?")
		sys.exit(1)