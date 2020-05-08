#! /usr/bin/python
# Parse and extract a sortable list of basic Windows Prefetch file information based on "last run" timestamps 
# Outputs the last most recent run times for Windows 10 Prefetch and later(Earlier prefetch versions only show the most recent run time)  
# 
# Prints csv to stdout the following prefetch fields:
#    last run timestamp
#    executable file_name
#    prefetch Hash
#    prefetch run count
#    prefetch file parsed 
#    volume count
#    volume timestamp
#    volume device path
#    volume serial number 
#
# Based on pyscca, pyscca example scripts and w10pf_parse.py by Matt Bromiley
# 

import argparse
import os
try:
    import pyscca #Import pyscca, necessary from libscca
except:
    print "Please install libscca with Python bindings"

def parse_file(prefetch_file):
    try:
        pf_file_name = os.path.basename(prefetch_file)
        scca = pyscca.open(prefetch_file)
        prefetch_version = str(scca.format_version)
        version_of_prefetch = str(scca.format_version)
        executable_file_name = str(scca.executable_filename)
        prefetch_hash = format(scca.prefetch_hash, 'x').upper()
        run_count = (scca.run_count) 
        number_of_volumes = str(scca.number_of_volumes)
        #Parse last run timestamps for each last run value
        for exe_timestamp in range(8):            
            if scca.get_last_run_time_as_integer(exe_timestamp) > 0:
                time = (scca.get_last_run_time(exe_timestamp).strftime("%Y-%m-%d %H:%M:%S"))
                run_count_number = (str(run_count - exe_timestamp) +"_of_"+ str(run_count)) 
                prefetch_values = [time,executable_file_name,prefetch_hash,run_count_number,pf_file_name,number_of_volumes]
                # Find volume information for each prefetch file and append to prefetch output                 
                volumes = []
                for volume_information in iter(scca.volumes):
                    volume_serial_number = format(volume_information.serial_number,'x').upper()                                        
                    volume_device_path = str(volume_information.device_path)
                    volume_timestamp = volume_information.creation_time.strftime("%Y-%m-%d %H:%M:%S")
                    prefetch_values.append(volume_timestamp)
                    prefetch_values.append(volume_device_path)
                    prefetch_values.append(volume_serial_number)
                print(','.join(prefetch_values))
    except:
        pass

def main():
    # Set arguments to parse input path
    parser = argparse.ArgumentParser(description='Extracts sortable list of Prefetch files based on run count')
    parser.add_argument('file_or_directory', help="Prefetch file or directory path")
    args = parser.parse_args()
    argspath = args.file_or_directory


    #Enumerate verify files from input and directories, then send to parser
    print("time,file_name,pf_hash,run_count,pf_file,volume_count,volume_timestamp,volume_dev_path,volume_serial_number,volume_timestamp,volume_dev_path,volume_serial_number")
    if (os.path.isdir(args.file_or_directory)):
        for dir_item in os.listdir(args.file_or_directory):
            file_to_parse = os.path.join(args.file_or_directory, dir_item)
            if os.path.isfile(file_to_parse):
                parse_file(file_to_parse)

    elif os.path.isfile(args.file_or_directory):
        if  args.file_or_directory.lower().endswith('pf'):
            file_to_parse = args.file_or_directory
            parse_file(file_to_parse)
    else:
        print("invalid path!!")
if __name__ == "__main__":
    main()
