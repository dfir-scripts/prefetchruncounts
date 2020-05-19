prefetchruncounts
Parse and extract a sortable list of basic Windows Prefetch file information based on "last run" timestamps

Parse and extract a sortable list of basic Windows Prefetch file information based on "last run" timestamps
Outputs the last and most recent 8 run times for Windows 10 and later(Earlier prefetch versions only show the most recent run time)
Uses pyscca to decompress pf MAM files and list files executed in a separate file
Expects either a file path or directory and will parse automatically
Creates 2 files
Prefetch_run_counts.csv
Prefetch_strings.csv
Output file name "Prefetch" can be changed witht the "-o" switch
example command:

python prefetch.py /media/usb/Prefetch/WWAHOST.EXE-776591F6.pf
python prefetch.py /media/usb/Prefetch/
python prefetch.py /media/usb/Prefetch/ -o Win10x385


Sample Prefetch_run_counts.csv output
last_run_time,exe_file,pf_hash,pf_run_count,pf_version,pf_file,volume_count,volume_timestamp,volume_dev_path,volume_serial_number,volume_timestamp,volume_dev_path,volume_serial_number
2019-03-21 19:15:45,MSIEXEC.EXE,A2D55CB6,9_of_9,MSIEXEC.EXE-A2D55CB6.pf,30,1,2019-01-26 19:02:56,\VOLUME{01d4b5a9bf52fda9-b8bf6d81},B8BF6D81
2019-03-18 04:06:49,MSIEXEC.EXE,A2D55CB6,8_of_9,MSIEXEC.EXE-A2D55CB6.pf,30,1,2019-01-26 19:02:56,\VOLUME{01d4b5a9bf52fda9-b8bf6d81},B8BF6D81
2019-03-17 03:09:32,MSIEXEC.EXE,A2D55CB6,7_of_9,MSIEXEC.EXE-A2D55CB6.pf,30,1,2019-01-26 19:02:56,\VOLUME{01d4b5a9bf52fda9-b8bf6d81},B8BF6D81
2019-03-13 04:39:49,MSIEXEC.EXE,A2D55CB6,6_of_9,MSIEXEC.EXE-A2D55CB6.pf,30,1,2019-01-26 19:02:56,\VOLUME{01d4b5a9bf52fda9-b8bf6d81},B8BF6D81
2019-02-19 19:41:03,MSIEXEC.EXE,A2D55CB6,5_of_9,MSIEXEC.EXE-A2D55CB6.pf,30,1,2019-01-26 19:02:56,\VOLUME{01d4b5a9bf52fda9-b8bf6d81},B8BF6D81
2019-02-09 20:51:35,MSIEXEC.EXE,A2D55CB6,4_of_9,MSIEXEC.EXE-A2D55CB6.pf,30,1,2019-01-26 19:02:56,\VOLUME{01d4b5a9bf52fda9-b8bf6d81},B8BF6D81
2019-02-09 20:50:58,MSIEXEC.EXE,A2D55CB6,3_of_9,MSIEXEC.EXE-A2D55CB6.pf,30,1,2019-01-26 19:02:56,\VOLUME{01d4b5a9bf52fda9-b8bf6d81},B8BF6D81
2019-02-09 20:34:46,MSIEXEC.EXE,A2D55CB6,2_of_9,MSIEXEC.EXE-A2D55CB6.pf,30,1,2019-01-26 19:02:56,\VOLUME{01d4b5a9bf52fda9-b8bf6d81},B8BF6D81

Sample Prefetch_strings.csv output
"pf_file,pf_executable_file,file_sequence,total_files,files_loaded"
MSIEXEC.EXE-A2D55CB6.pf,MSIEXEC.EXE,1,370,\VOLUME{01d4b5a9bf52fda9-b8bf6d81}\WINDOWS\WINSXS\AMD64_MICROSOFT-WINDOWS-A..ENCE-MITIGATIONS-C5_31BF3856AD364E35_10.0.16299.64_NONE_2F1D3EAE63651A25\ACLAYERS.DLL
MSIEXEC.EXE-A2D55CB6.pf,MSIEXEC.EXE,1,370,\VOLUME{01d4b5a9bf52fda9-b8bf6d81}\WINDOWS\WINSXS\AMD64_MICROSOFT-WINDOWS-A..ENCE-MITIGATIONS-C5_31BF3856AD364E35_10.0.16299.64_NONE_2F1D3EAE63651A25\ACLAYERS.DLL
MSIEXEC.EXE-A2D55CB6.pf,MSIEXEC.EXE,2,370,\VOLUME{01d4b5a9bf52fda9-b8bf6d81}\WINDOWS\MICROSOFT.NET\FRAMEWORK64\V4.0.30319\FUSION.DLL
MSIEXEC.EXE-A2D55CB6.pf,MSIEXEC.EXE,1,370,\VOLUME{01d4b5a9bf52fda9-b8bf6d81}\WINDOWS\WINSXS\AMD64_MICROSOFT-WINDOWS-A..ENCE-MITIGATIONS-C5_31BF3856AD364E35_10.0.16299.64_NONE_2F1D3EAE63651A25\ACLAYERS.DLL
MSIEXEC.EXE-A2D55CB6.pf,MSIEXEC.EXE,2,370,\VOLUME{01d4b5a9bf52fda9-b8bf6d81}\WINDOWS\MICROSOFT.NET\FRAMEWORK64\V4.0.30319\FUSION.DLL
MSIEXEC.EXE-A2D55CB6.pf,MSIEXEC.EXE,3,370,\VOLUME{01d4b5a9bf52fda9-b8bf6d81}\WINDOWS\MICROSOFT.NET\FRAMEWORK64\V4.0.30319\CLR.DLL

