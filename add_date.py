# this is for add date to file on head of file name.

""" usege

Input the directory name that has files you want to
add date on the head of file name.

You will see files that become like this:
    20220918_oldFileName

 """

import os
import datetime

# input directory name
print('Input the directory name that has files you want to change. Full path')
directory_name = input()
print(directory_name)

file_list = os.listdir(directory_name)
print(os.listdir(directory_name))

# get the name fo new file head like: 20220918
# get the date of today
datetime = datetime.datetime.now()
# change date to string
string_datetime = str(datetime)
# change string to list, split ' '
splited_string_datetime = string_datetime.split()
# get the name of new file head, date
head_filename_date = splited_string_datetime[0].replace('-', '')
print(f'{head_filename_date} : Hed of file name will be changed to this')


for file in file_list:
    # print full path of the file
    old_file_full_path = directory_name + '\\' + file
    print(old_file_full_path)
    
    # No change
    if '20' in file or os.path.isdir(old_file_full_path):
        print('No change: ' + file + '\n')

    # change file name
    else:
        print(f'The old filename: {file} will be changed.')
        new_file_full_path = directory_name + '\\' + head_filename_date + '_' + file

        os.rename(old_file_full_path, new_file_full_path)
        print(f'New file name: {head_filename_date}_{file}\n')
