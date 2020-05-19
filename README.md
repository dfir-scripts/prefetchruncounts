***prefetchruncounts.py***


Parse and extract a sortable list of basic Windows Prefetch file information based on "last run" timestamps

Parse and extract a sortable list of basic Windows Prefetch file information based on "last run" timestamps
Outputs the last and most recent 8 run times for Windows 10 and later(Earlier prefetch versions only show the most recent run time)
Uses pyscca to decompress pf MAM files and list files executed in a separate file


Expects either a file path or directory and will parse automatically
-Creates 2 files
-Prefetch_run_counts.csv
-Prefetch_strings.csv
-Output file name "Prefetch" can be changed witht the "-o" switch


example command:
-python prefetch.py /media/usb/Prefetch/WWAHOST.EXE-776591F6.pf
-python prefetch.py /media/usb/Prefetch/
-python prefetch.py /media/usb/Prefetch/ -o Win10x385


Prefetch_run_counts.csv outputs the following fields:  
***last_run_time,exe_file,pf_hash,pf_run_count,pf_version,pf_file,volume_count,volume_timestamp,volume_dev_path,volume_serial_number,volume_timestamp,volume_dev_path,volume_serial_number***


Sample Prefetch_strings.csv outputs the following fields:
***"pf_file,pf_executable_file,file_sequence,total_files,files_loaded"***

