# MPSGDreamSplitter

I created this simple script with the intention of splitting a file into multiple files. This will work for any text files that can be split up by line. My use case is for pentesting, splitting my list of subnets into evenly distributed files to reduce scan times.

Performs a split of a valid .txt file into a specified number of .txt files.
- inputFile - input file to be split
- number - number of files to split the input file into
- outputDirectory - output directory

Examples:
- Split one text file into 4
    
        MPSGDreamSplitter.py -inputFile subnets.txt -number 4 -outputDirectory ~/

            Input File: .TXT
            Number: 2 through 10
            Output Directory: ___
