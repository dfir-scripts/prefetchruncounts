#! /usr/bin/env python3
# Parse and extract a sortable list of basic Windows Prefetch file information based on "last run" timestamps 
# Outputs the last and most recent 8 run times for Windows 10 and later(Earlier prefetch versions only show the most recent run time)  
# Uses pyscca to decompress pf MAM files and list files executed in a separate file

# Expects either a file path or directory and will parse automatically
#Creates 2 files by default  
#   Prefetch_run_counts.csv
#   Prefetch_strings.csv
#
# Output file name "Prefetch" can be changed witht the "-o" switch

# examples

#   python prefetch.py /media/usb/Prefetch/WWAHOST.EXE-776591F6.pf
#   python prefetch.py /media/usb/Prefetch/
#   python prefetch.py /media/usb/Prefetch/ -o Win10x385

#
# Based on pyscca, plaso, prefetch.py and  w10pfdecomp.py, w10pf_parse.py 
# 

import csv
import argparse
import os
import pyscca

def parse_file(prefetch_file,outpath):
    try:
        #open prefetch file with pyscca and get values
        everything = []
        prefetch_values = []
        pf_file_name = os.path.basename(prefetch_file)
        scca = pyscca.open(prefetch_file)
        prefetch_version = str(scca.format_version)
        executable_file_name = str(scca.executable_filename)
        prefetch_hash = format(scca.prefetch_hash, 'x').upper()
        run_count = (scca.run_count) 
        number_of_volumes = str(scca.number_of_volumes)
        number_of_files = str(scca.number_of_file_metrics_entries)
        # Access encoded strings and send to file
        count=1
        all_strings = []
        for entry_index, file_metrics in enumerate(scca.file_metrics_entries):            
            mapped_file_string = file_metrics.filename
            strings = (pf_file_name,executable_file_name,count, number_of_files,mapped_file_string)
            count = (count + 1)
            all_strings.append(strings)
            stringsfile = (outpath + '_strings.csv')
            strings_file = open(stringsfile, 'a+')
            with strings_file:
                write = csv.writer(strings_file) 
                write.writerows(all_strings) 
        #Parse last run timestamps for each last run value
        for exe_timestamp in range(8):            
            if scca.get_last_run_time_as_integer(exe_timestamp) > 0:
                time = (scca.get_last_run_time(exe_timestamp).strftime("%Y-%m-%d %H:%M:%S"))
                run_count_number = (str(run_count - exe_timestamp) +"_of_"+ str(run_count)) 
                prefetch_values = [time,executable_file_name,prefetch_hash,run_count_number,pf_file_name,prefetch_version,number_of_volumes]
                # Find volume information for each prefetch file and append to prefetch output                 
                for volume_information in iter(scca.volumes):
                    volume_serial_number = format(volume_information.serial_number,'x').upper()                                        
                    volume_device_path = str(volume_information.device_path)
                    volume_timestamp = volume_information.creation_time.strftime("%Y-%m-%d %H:%M:%S")
                    prefetch_values.append(volume_timestamp)
                    prefetch_values.append(volume_device_path)
                    prefetch_values.append(volume_serial_number)
                #print run counts results to stdout and send to file   
                print(','.join(prefetch_values))
                everything.append(prefetch_values)
                runcountsfile = (outpath + '_run_count.csv')
                run_count_file = open(runcountsfile, 'a+')
                with run_count_file:     
                    write = csv.writer(run_count_file)
                    write.writerows(everything)                 
    except:
        pass

def main():
    # Set arguments to parse input path
    parser = argparse.ArgumentParser(description='Extracts Prefetch metadata and strings based run count.  csv output as 2 files')
    parser.add_argument('file_or_directory', help="Prefetch file or directory")
    parser.add_argument('-o','--output', default='Prefetch', help="Name output files base name, Default=Prefetch (Prefetch_runcounts.csv, Prefetch_strings.csv)")
    args = parser.parse_args()
    argspath = args.file_or_directory
    outpath = args.output

    #Create header for output files
    pf_header="last_run_time,exe_file,pf_hash,pf_run_count,pf_version,pf_file,volume_count,volume_timestamp,volume_dev_path,volume_serial_number,volume_timestamp,volume_dev_path,volume_serial_number"
    pf_strings_header="pf_file,pf_executable_file,file_sequence,total_files,files_loaded"  
    print(pf_header)

    #Write header information for 2 output files
    strings_file = open((outpath + '_strings.csv'), "w")
    writer = csv.DictWriter(strings_file, fieldnames=[pf_strings_header])
    writer.writeheader()
    strings_file.close()
    run_counts_file = open((outpath + '_run_count.csv'), "w")
    writer = csv.DictWriter(run_counts_file, fieldnames=[pf_header])
    writer.writeheader()
    run_counts_file.close()

    #Enumerate and verify files in directory path, then send to parser
    if (os.path.isdir(args.file_or_directory)):
        for dir_item in os.listdir(args.file_or_directory):
            file_to_parse = os.path.join(args.file_or_directory, dir_item)
            if os.path.isfile(file_to_parse):
               parse_file(file_to_parse,outpath)
    #Enumerate and verify file in input string, then send to parser
    elif os.path.isfile(args.file_or_directory):
        if  args.file_or_directory.lower().endswith('pf'):
            file_to_parse = args.file_or_directory
            parse_file(file_to_parse,outpath)
    else:
        print("invalid path!!") 

if __name__ == "__main__":
    main()
