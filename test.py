#! /usr/bin/env python3
# Parse and extract information from Windows prefetch files
# Outputs the 8 most recent run times of Windows 10 and newer systems
#
#
#

import sys
import argparse
import os
import pyscca

def parse_file(prefetch_file,Timeline):
    try:
        #open prefetch file with pyscca and get values
        pf_file_name = os.path.basename(prefetch_file)
        scca = pyscca.open(prefetch_file)
        #prefetch file values
        prefetch_values = []
        prefetch_version = str(scca.format_version)
        exe_file_name = str(scca.executable_filename)
        pf_hash = format(scca.prefetch_hash, 'x').upper()
        run_count = (scca.run_count) 
        number_of_volumes = str(scca.number_of_volumes)
        number_of_files = str(scca.number_of_file_metrics_entries)
        
        # Create a list and count of all files loaded with prefetch
        if not Timeline:
            count=1
            all_files = []     
            for entry_index, file_metrics in enumerate(scca.file_metrics_entries):
                padding = "_,_"
                long_file_name = str(file_metrics.filename)
                long_file_name = long_file_name[::-1].replace("\\", ",", 1)[::-1]
                file_tally = (padding,exe_file_name,pf_file_name,pf_hash,number_of_files,long_file_name)
                all_files.append(file_tally)
            for v in all_files:
                print(*v, sep=',')

        #Parse timestamps for last run value
        for pf_timestamp in range(8):            
            if scca.get_last_run_time_as_integer(pf_timestamp) > 0:
                padding = "_,_,_"
                time = (scca.get_last_run_time(pf_timestamp).strftime("%Y-%m-%d %H:%M:%S"))
                run_count_number = (str(run_count - pf_timestamp) +"_of_"+ str(run_count)) 
                pf_tally = (time,run_count_number,exe_file_name,pf_file_name,pf_hash,padding)
                prefetch_values.append(pf_tally)
                if int(prefetch_version) <26:
                    if not Timeline:
                        pf_list = [list(x) for x in prefetch_values] 
                        print(pf_list, ["Time", "Run Count", "Prefetch File",  "Executable File", "Prefetch Hash"])
                        vol_list = [list(x) for x in vol_info]
                        print(vol_list, ["Volume Path", "Volume Timestamp", "Serial Number"])                    
                        file_list = [list(x) for x in all_files]
                        print(file_list, ["Count", "Total", "File"])
                        return True
                else:
                    for v in prefetch_values:
                            print(*v, sep = ',')
                            return True    
    except:
        pass            

def main():
    # Set arguments for input and output
    parser = argparse.ArgumentParser(description='Extract Prefetch info based run count')
    parser.add_argument('file_or_directory', help="Path to Prefetch file or directory")
    parser.add_argument('-t','--timeline', default=False, action = 'store_true', help="Print run times as a timeline")
    parser.add_argument('-n','--no_header', default=False, action = 'store_true', help="Print output with no header")
    args = parser.parse_args()
    Timeline = args.timeline
    No_Header = args.no_header

    if not No_Header:
        print("time,run_count,prefetch_file,prefetch_exe,hash,number_of_files,loaded_file_path,loaded_file")

    #Enumerate and verify files in directory path, then send to parser
    if (os.path.isdir(args.file_or_directory)):
        for dir_item in os.listdir(args.file_or_directory):
            file_to_parse = os.path.join(args.file_or_directory, dir_item)
            if os.path.isfile(file_to_parse):
               parse_file(file_to_parse,Timeline)

    #Enumerate and verify file in input string, then send to parser
    elif os.path.isfile(args.file_or_directory):
        if  args.file_or_directory.lower().endswith('pf'):
            file_to_parse = args.file_or_directory
            parse_file(file_to_parse,Timeline)            
    else:
        print("invalid path!!") 

if __name__ == "__main__":
    main()
