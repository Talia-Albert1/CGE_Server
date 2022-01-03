# cge_server

## Purpose
The purpose of this python script is to automate the execution and file management for the following Center for Genomic Epidemiology (CGE) https://www.genomicepidemiology.org/ programs.
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

## How to Use
Open the cge_server.py with a a text editor and change the database directories of each program at the top of the script (lines 15 - 21) so they reflect the location on your computer.
"""
virulencefinder_db = '/path/to/dir/CGE_server/virulencefinder/virulencefinder_db'
resfinder_db = '/path/to/dir/CGE_server/resfinder/'
mlst_db = '/path/to/dir/CGE_server/mlst/mlst_db'
serotypefinder_db = '/path/to/dir/CGE_server/serotypefinder/serotypefinder_db'
plasmidfinder_db = '/path/to/dir/CGE_server/plasmidfinder/plasmidfinder_db'
kmerfinder_db = '/path/to/dir/CGE_server/kmerfinder/kmerfinder_db'
cgmlst_db = '/path/to/dir/CGE_server/cgmlstfinder/cgmlstfinder_db'
"""
Place the script in a directory (path/to/dir/cge_server.py)create a subdirectory called "input" (/path/to/dir/input/).
Place the files to be analyzed inside the "input" subdirectory.
<br />
<img src="https://user-images.githubusercontent.com/96196923/146848038-7d549c37-1b27-4917-a2ea-fcc51e3556ce.png" width="450">
<img src="https://user-images.githubusercontent.com/96196923/146848056-1bdb6ea6-fd3a-4544-b037-bf4dfe16255e.png" width="450">
