#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kyle Albert
email: kea5359@psu.edu
github: CGEServerADL 
"""

import os
import shutil

"""
Change these to the absolute directory on your computer
"""
virulencefinder_db = '/home/kyle/Documents/kyle_work/CGE_server/virulencefinder/virulencefinder_db'
resfinder_db = '/home/kyle/Documents/kyle_work/CGE_server/resfinder/'
mlst_db = '/home/kyle/Documents/kyle_work/CGE_server/mlst/mlst_db'
serotypefinder_db = '/home/kyle/Documents/kyle_work/CGE_server/serotypefinder/serotypefinder_db'
plasmidfinder_db = '/home/kyle/Documents/kyle_work/CGE_server/plasmidfinder/plasmidfinder_db'
kmerfinder_db = '/home/kyle/Documents/kyle_work/CGE_server/kmerfinder/kmerfinder_db'
cgmlst_db = '/home/kyle/Documents/kyle_work/CGE_server/cgmlstfinder/cgmlstfinder_db'



"""
Get files/subdirectories in current working directory. Additionally create the
output folder if it does not already exist. Create results subdirectory within
output.
"""
currentdir = os.getcwd() + '/'
currentdirfiles = os.listdir(currentdir)

if os.path.isdir(currentdir + '/output') is False:
    os.mkdir(currentdir +  'output/')

resultsdir = currentdir + 'output' + '/results/'

if os.path.isdir(resultsdir) is False:
    os.mkdir(resultsdir)
    
inputfilesdir = currentdir + 'input/'



"""
Get the files that are in the input folders, and add them without the .fast.gz
or the r1/r2 ending into a list.

Print which files will be analyzed to the user
"""
inputdirfiles = os.listdir(inputfilesdir)


print('The following files will be analyzed')   
for file in inputdirfiles:
    print(inputfilesdir + file)
print('')       



"""
The user inputs the pointfinder, mlst, and cgmlst species database names
"""
pfspeciesinput = input(
    'Input the pointfinder database species name:')

mlstspeciesinput = input(
    'Input the mlst and cgmlstfnder database species name:')
print('')



"""
Create the class for each datafiles, contains the base name, the name with r1
and r2 included, and the absolute directory for both r1 and r2 files.
"""
class datafile():
    pfspecies = pfspeciesinput
    mlstspecies = mlstspeciesinput
    def __init__(self, name, r1, r2, r1dir, r2dir):
        self.name = name
        self.r1 = r1
        self.r2 = r2
        self.r1dir = r1dir
        self.r2dir = r2dir


files = []

#Get the directory of the R1 and R2 files, as well as the "basename" for each file
for file in inputdirfiles:
    if 'r1' in file.casefold():
        tempname = os.path.splitext(file)
        
        file_extension = '.fastq'
        if tempname[1] == '.gz':
            tempname = os.path.splitext(tempname[0])
            file_extension = '.fastq.gz'
            
        if tempname[1] == '.fastq':
            tempname = tempname[0]
        
        r1index = tempname.casefold().find('r1')
        r1indexdigit = r1index + 1
        r1name = tempname
        r2name = tempname[:r1indexdigit] + '2' + tempname[r1indexdigit + 1:]
        
        underscore_index = []
        if 'R1' in tempname:
            basename_noR = tempname.replace('R1', '')
            #Check for double "__" that result from removing R1, and remove a trailing _ if one exists
            for i in range(len(basename_noR)):
                if i != len(basename_noR) - 1:
                    if basename_noR[i] == basename_noR[i + 1] == '_':
                        underscore_index.append(i + 1)
                
                if i == len(basename_noR) - 1:
                    if basename_noR[i] == '_':
                        basename_noR = basename_noR[:-1]
            
            if underscore_index != []:
                for i in range(len(underscore_index)):
                    tempindex = underscore_index[i] - i
                    basename_noR = basename_noR[:tempindex] + basename_noR[tempindex + 1:]

        elif 'r1' in tempname:
            basename_noR = tempname.replace('r1', '')
            
            for i in range(len(basename_noR)):
                if i != len(basename_noR) - 1:
                    if basename_noR[i] == basename_noR[i + 1] == '_':
                        underscore_index.append(i + 1)

                if i == len(basename_noR) - 1:
                    if basename_noR[i] == '_':
                        basename_noR = basename_noR[:-1]
            
            if underscore_index != []:
                for i in range(len(underscore_index)):
                    tempindex = underscore_index[i] - i
                    basename_noR = basename_noR[:tempindex] + basename_noR[tempindex + 1:]
        

        
        files.append(datafile(basename_noR, r1name, r2name, 
                              inputfilesdir + r1name + file_extension,
                              inputfilesdir + r2name + file_extension))


inputoptions = []
programs = ['VirulenceFinder', 'ResFinder', 'MLST', 'SerotypeFinder', 'PlasmidFinder', 'KmerFinder', 'cgMLSTFinder', 'All']
for i in range(len(programs)):
    inputoptions.append(str(i))
inputoptions.append('N')
inputoptions.append('n')
allindex = str(programs.index('All'))


"""
Print the menu for the user
"""
print('Choose which CGE program(s) you would like to analyze the files with, you can enter one program at a time, or enter ' + allindex + ' to use them all. When entering one at a time, enter "N" or "n" when finished entering programs:')
for i in range(len(programs)):
    print(str(i) + '. ' + programs[i])
choice = []




"""
Ensure the first pick is not "N" or "n", and is a valid choice.
"""
choicealpha = input('Select programs here:')
while choice == []:
    if choicealpha.casefold() == 'n' or choicealpha not in inputoptions:
        print('')
        choicealpha = input('Select programs here:')
        
        
    elif choicealpha in inputoptions:
        choice.append(choicealpha)
        if programs[int(choicealpha)] != 'All':
                    print(programs[int(choicealpha)] + ' will analyze the data')
                    
#Individually choose more programs, or have all be choosen.
while choice != []:
    if choicealpha == allindex:
        choice == [allindex]
        print('All programs will analyze the data')
        break
    
    elif choicealpha in inputoptions[:(len(programs) - 1)]:
        if choicealpha not in choice:
            choice.append(choicealpha)
            print(programs[int(choicealpha)] + ' will analyze the data')
    
    elif choicealpha.casefold() == 'N'.casefold():
        print('The following programs will analyze the data:')
        for i in range(len(choice)):
            if i+1 < len(choice):
                print(programs[int(choice[i])] + ', ', end='')
            elif i+1 == len(choice):
                print(programs[int(choice[i])])
        break
    
    print('')
    choicealpha = input('Select programs here:')

#Choices have been made, now the program needs to execute each selected program
if choice == [allindex]:
    choice = []
    for i in range(len(programs) - 1):
        choice.append(str(i))



#Create the relative output folder, since CGE server programs dont play well with absolute paths
print('')
relativeoutputdir = inputfilesdir +  'tempout/'
if os.path.isdir(relativeoutputdir) is False:
    os.mkdir(relativeoutputdir)

#Choose Which character separates the values between species name, program name, result file name
sep = '-'


def tempoutmove(finaloutputdir):
    tempoutputs = os.listdir(relativeoutputdir)
    for file in tempoutputs:
        shutil.move(os.path.join(relativeoutputdir, file), finaloutputdir)


def programcommand(progname, commandline, twofileindicator, file1name, file1rename, file2name, file2rename):
    finaloutputdir = currentdir + 'output/' + progname + '/' + files[i].name
    print('Working on:')
    print(files[i].r1dir)
    print(files[i].r2dir)
    os.mkdir(finaloutputdir)
    os.system(commandline)
    tempoutmove(finaloutputdir)

    shutil.copy(os.path.join(currentdir + 'output/' + progname + '/' + files[i].name, file1name), os.path.join(resultsdir, file1rename))
    if twofileindicator == True:
        shutil.copy(os.path.join(currentdir + 'output/' + progname + '/' + files[i].name, file2name), os.path.join(resultsdir + file2rename))


def makedir(progname):
    os.mkdir(currentdir + 'output/' + progname)
    print('Starting ' + progname)


#VirulenceFinder
if '0' in choice:
    makedir('VirulenceFinder')
    for i in range(len(files)):
        programcommand('VirulenceFinder', 'sudo docker run --rm -it -v ' + virulencefinder_db +' :/database -v ' + inputfilesdir + ':/workdir virulencefinder -o tempout -p /database/ -i ' + files[i].r1 + file_extension + ' ' + files[i].r2 + file_extension + ' -x', True, 'results.txt', files[i].name + sep + 'VirulenceFinder' + sep + 'results.txt', 'results_tab.tsv', files[i].name + sep + 'VirulenceFinder' + sep + 'results_tab.tsv')
       

#ResFinder
if '1' in choice:
    makedir('ResFinder')
    for i in range(len(files)):
        finaloutputdir = currentdir + 'output/ResFinder/' + files[i].name
        os.mkdir(finaloutputdir)
        os.system('python3 ' + resfinder_db + 'run_resfinder.py -o ' + finaloutputdir + ' -s ' + files[i].pfspecies + ' -l 0.6 -t 0.9 --acquired --point -ifq ' + files[i].r1dir + ' ' + files[i].r2dir)
        shutil.copy(currentdir + 'output/ResFinder/' + files[i].name + '/pheno_table.txt', resultsdir + files[i].name + sep + 'ResFinder' + sep + 'pheno_table.txt')

#MLST
if '2' in choice:
    makedir('MLST')
    for i in range(len(files)):
        programcommand('MLST', 'sudo docker run --rm -it -v ' + mlst_db + ':/database -v ' + inputfilesdir + ':/workdir mlst -i ' + files[i].r1 + ' ' + files[i].r2 + ' -o tempout -s ' + files[i].mlstspecies + ' -x', True, 'results.txt', files[i].name + sep + 'MLST' + sep + 'results.txt', 'results_tab.tsv', files[i].name + sep + 'MLST' + sep + 'results_tab.tsv')


#SerotypeFinder
if '3' in choice:
    makedir('SerotypeFinder')
    for i in range(len(files)):
        programcommand('SerotypeFinder', 'sudo docker run --rm -it -v ' + serotypefinder_db + ':/database -v ' + inputfilesdir + ':/workdir serotypefinder -i ' + files[i].r1 + ' ' + files[i].r2 + ' -o tempout', True, 'kma_H_type_' + files[i].r1 + '.res', files[i].name + sep + 'SerotypeFinder' + sep + 'kma_H_type.fastq.gz.res', 'kma_O_type_' + files[i].r1 + '.res', files[i].name + sep + 'SerotypeFinder' + sep + 'kma_O_type.fastq.gz.res')


#PlasmidFinder
if '4' in choice:
    makedir('PlasmidFinder')
    for i in range(len(files)):
        programcommand('PlasmidFinder', 'sudo docker run --rm -it -v ' + plasmidfinder_db + ':/database -v ' + inputfilesdir + ':/workdir plasmidfinder -i ' + files[i].r1 + ' ' + files[i].r2 + ' -o tempout -x', True, 'results.txt', files[i].name + sep + 'PlasmidFinder' + sep + 'results.txt', 'results_tab.tsv', files[i].name + sep + 'PlasmidFinder' + sep + 'results_tab.tsv')


#KmerFinder
if '5' in choice:
    makedir('KmerFinder')
    for i in range(len(files)):
        programcommand('KmerFinder', 'sudo docker run --rm -it -v ' + kmerfinder_db + ':/database -v ' + inputfilesdir + ':/workdir kmerfinder -i ' + files[i].r1 + ' ' + files[i].r2 + ' -o tempout -db /database/bacteria/bacteria.ATG -tax /database/bacteria/bacteria.tax -x', False, 'results.txt', files[i].name + sep + 'KmerFinder' + sep + 'results.txt', '', '')


#cgMLSTFinder
if '6' in choice:
    makedir('cgMLSTFinder')
    for i in range(len(files)):
        programcommand('cgMLSTFinder', 'sudo docker run --rm -it -v ' + kmerfinder_db + ':/database -v ' + inputfilesdir + ':/workdir cgmlstfinder -t temp_dir ' + files[i].r1 + ' ' + files[i].r2 + ' -o tempout -db /database/ -s ' + files[i].mlstspecies, False, 'results.txt', files[i].name + sep + 'cgMLSTFinder' + sep + 'results.txt','', '')



#Delete tempout folder
os.rmdir(relativeoutputdir)



#Move files from input folder to archive folder
archivedir = currentdir + 'archive'
archivedircheck = os.path.isdir(archivedir)
if archivedircheck is False:
    os.mkdir(archivedir)
for sample in files:
    shutil.move(sample.r1dir, archivedir)
    shutil.move(sample.r2dir, archivedir)