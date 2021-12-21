## prefetchruncounts.py

Parse and extract a sortable list of basic Windows Prefetch file information based on "last run" timestamps<br/><br/>

Outputs the last and most recent 8 run times for Windows 10 and later<br/>
(Earlier prefetch versions only show the most recent run time)<br/>
Uses pyscca to decompress pf MAM files and list dlls and other resulting file executions<br/>


usage: prefetchruncounts.py [-h] [-t] file_or_directory<br/><br/>

Extract Prefetch info based on run counts<br/>
positional arguments:<br/>
  file_or_directory  Path to Prefetch file or directory<br/><br/>

optional arguments:<br/>
  -h, --help         show this help message and exit<br/>
  -t, --timeline     Print run times as a timeline)<br/>
