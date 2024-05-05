#! /usr/bin/env python3
# Parse and extract information from Windows 8.1+ prefetch files

import sys
import argparse
import os
import pyscca
from datetime import datetime, timezone

def parse_file(prefetch_file,Timeline):
    try:
        #open prefetch file with pyscca and get values
        pf_file_name = os.path.basename(prefetch_file)
        #Get prefetch file timestamps
        file_stat = os.stat(prefetch_file)
        pf_mtime = datetime.fromtimestamp(file_stat.st_mtime, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        pf_ctime = datetime.fromtimestamp(file_stat.st_ctime, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        scca = pyscca.open(prefetch_file)
        #prefetch file values
        prefetch_values = []
        prefetch_version = str(scca.format_version)
        exe_file_name = str(scca.executable_filename)
        pf_hash = format(scca.prefetch_hash, 'x').upper()
        run_count = (scca.run_count)
        number_of_volumes = str(scca.number_of_volumes)
        number_of_files = str(scca.number_of_file_metrics_entries)

        #Parse timestamps for last run value
        for pf_timestamp in range(8):
            if scca.get_last_run_time_as_integer(pf_timestamp) > 0:
                padding = "_,_"
                time = (scca.get_last_run_time(pf_timestamp).strftime("%Y-%m-%d %H:%M:%S"))
                run_count_number = (str(run_count - pf_timestamp) +"_of_"+ str(run_count))
                pf_tally = (time,run_count_number,pf_mtime,pf_ctime,exe_file_name,pf_file_name,pf_hash,number_of_files,padding)
                prefetch_values.append(pf_tally)
            for v in prefetch_values:
                print(*v, sep = ',')

        # Create a list and count of all files loaded with prefetch
        if not Timeline:
            all_files = []
            for entry_index, file_metrics in enumerate(scca.file_metrics_entries):
                padding = "_,_,_,_"
                long_file_name = str(file_metrics.filename)
                long_file_name = long_file_name[::-1].replace("\\", ",", 1)[::-1]
                file_tally = (padding,exe_file_name,pf_file_name,pf_hash,number_of_files,long_file_name)
                all_files.append(file_tally)
            for v in all_files:
                print(*v, sep=',')
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
        print("time,run_count,pf_mtime,pf_ctime,exe_file,pf_file,pf_hash,load_count,load_file_path,load_file")

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
