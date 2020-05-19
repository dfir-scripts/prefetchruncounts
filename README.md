## prefetchruncounts.py


Parse and extract a sortable list of basic Windows Prefetch file information based on "last run" timestamps<br/><br/>

Outputs the last and most recent 8 run times for Windows 10 and later<br/>
(Earlier prefetch versions only show the most recent run time)<br/>
Uses pyscca to decompress pf MAM files and list files executed in a separate file<br/><br/>

*Expects either a file path or directory and will parse automatically<br/>*
Creates 2 files<br/>
Prefetch_run_counts.csv<br/>
Prefetch_strings.csv<br/>
Output file name "Prefetch" can be changed witht the "-o" switch<br/>


***example commands:<br/>***
*python prefetch.py /media/usb/Prefetch/WWAHOST.EXE-776591F6.pf<br/>*
*python prefetch.py /media/usb/Prefetch/<br/>*
*python prefetch.py /media/usb/Prefetch/ -o Win10x385<br/><br/>*

**Prefetch_run_counts.csv outputs the following fields:<br/>**
* last_run_time<br/>  
* exe_file<br/>  
* pf_hash<br/>  
* pf_run_count<br/>  
* pf_version<br/>  
* pf_file<br/>
* volume_count<br/> 
* volume_timestamp<br/>
* volume_dev_path<br/>
* volume_serial_number<br/>
* volume_timestamp<br/>
* volume_dev_path<br/>
* volume_serial_number<br/><br/>


**Prefetch_strings.csv outputs the following fields:<br/>**
* pf_file 
* pf_executable_file
* file_sequence
* total_files
* files_loaded

