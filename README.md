***prefetchruncounts.py***


Parse and extract a sortable list of basic Windows Prefetch file information based on "last run" timestamps<br/><br/>

Outputs the last and most recent 8 run times for Windows 10 and later(Earlier prefetch versions only show the most recent run time)<br/>
Uses pyscca to decompress pf MAM files and list files executed in a separate file<br/><br/>


Expects either a file path or directory and will parse automatically<br/>
Creates 2 files<br/>
Prefetch_run_counts.csv<br/>
Prefetch_strings.csv<br/>
Output file name "Prefetch" can be changed witht the "-o" switch<br/>


example command:<br/>
-python prefetch.py /media/usb/Prefetch/WWAHOST.EXE-776591F6.pf<br/>
-python prefetch.py /media/usb/Prefetch/<br/>
-python prefetch.py /media/usb/Prefetch/ -o Win10x385<br/><br/>

Prefetch_run_counts.csv outputs the following fields:<br/>  
***last_run_time,exe_file,pf_hash,pf_run_count,pf_version,pf_file,volume_count,volume_timestamp,volume_dev_path,volume_serial_number,volume_timestamp,volume_dev_path,volume_serial_number***<br/><br/>


Sample Prefetch_strings.csv outputs the following fields:<br/>
***"pf_file,pf_executable_file,file_sequence,total_files,files_loaded"***

