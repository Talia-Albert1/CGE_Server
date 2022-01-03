# cge_server

## Purpose
The purpose of this python script is to automate the execution and file management for the following Center for Genomic Epidemiology (CGE) https://www.genomicepidemiology.org/ programs which are used to conduct analyses of genetic data.
There are plans to add more programs and functionality.

## Programs
* CGE Bitbucket Profile: https://bitbucket.org/genomicepidemiology/
* VirulenceFinder: https://bitbucket.org/genomicepidemiology/virulencefinder/src/master/
* ResFinder: https://bitbucket.org/genomicepidemiology/resfinder/src/master/
* MLST: https://bitbucket.org/genomicepidemiology/mlst/src/master/
* SerotypeFinder: https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/
* PlasmidFinder: https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/
* KmerFinder: https://bitbucket.org/genomicepidemiology/kmerfinder/src/master/
* cgMLSTFinder: https://bitbucket.org/genomicepidemiology/cgmlstfinder/src/master/

## Setup
Download and install each of the above programs.

Open cge_server.py with a a text editor and change the database directories of each program at the top of the script so they reflect the location on your computer.
```
virulencefinder_db = '/path/to/dir/CGE_server/virulencefinder/virulencefinder_db'
resfinder_db = '/path/to/dir/CGE_server/resfinder/'
mlst_db = '/path/to/dir/CGE_server/mlst/mlst_db'
serotypefinder_db = '/path/to/dir/CGE_server/serotypefinder/serotypefinder_db'
plasmidfinder_db = '/path/to/dir/CGE_server/plasmidfinder/plasmidfinder_db'
kmerfinder_db = '/path/to/dir/CGE_server/kmerfinder/kmerfinder_db'
cgmlst_db = '/path/to/dir/CGE_server/cgmlstfinder/cgmlstfinder_db'
```
(Note: The resfider program only links to the directory where run_resfinder.py exists)

Place the script in a directory (path/to/dir/cge_server.py) create a subdirectory called "input" (/path/to/dir/input/).
Place the files to be analyzed inside the "input" subdirectory (/path/to/dir/input/file1_r1.fastq.gz etc.)
<br />
<img src="https://user-images.githubusercontent.com/96196923/146848038-7d549c37-1b27-4917-a2ea-fcc51e3556ce.png" width="450">
<img src="https://user-images.githubusercontent.com/96196923/146848056-1bdb6ea6-fd3a-4544-b037-bf4dfe16255e.png" width="450">

## How to Use
Open the terminal and navigate to the directory with cge_server.py.
Then execute the script by entering the following command
```
python cge_server.py
```
The program will show which files will be analyzed
```
The following files will be analyzed
/path/to/dir/input/Salm_001_R1.fastq.gz
/path/to/dir/input/Salm_002_R1.fastq.gz
/path/to/dir/input/Salm_001_R2.fastq.gz
/path/to/dir/input/Salm_002_R2.fastq.gz
```
Then the species name(s) must be entered for the cgmlstfinder, mlst, and pointfinder databases. The database directories for the respective programs can be checked to determine which program name to use.

(Note: Multiple files may be analyzed at the same time, but all the files must be of the same species)
