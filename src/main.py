import pandas as pd
import os

# Check if the file exists
file_name = r"C:\Users\Nathan\OneDrive - Umich\Desktop\NTFS-parser\src\ntfs_sector.txt"
if not os.path.isfile(file_name):
    print(f"File {file_name} not found")
    
# Read the data from the file
data = []
with open(file_name, 'r') as f:
    data = f.readlines()

# Split the data into three parts
parts = []
for line in data:
    # Split the line by colon
    line_parts = line.split(':')
    # Get the address part
    address = line_parts[0].strip()
    # Get the hex data part
    hex_data = line_parts[1][:52].strip()
    # Get the string data part
    string_data = line_parts[1][52:].strip()
    # Remove the spaces from the hex data
    hex_data = hex_data.replace(' ', '')
    # Append the parts to the list
    parts.append({'address': address, 'hex data': hex_data, 'string data': string_data})

# Create a pandas dataframe from the parts
df = pd.DataFrame(data=parts, columns=['address', 'hex data', 'string data'])

# Print the dataframe for debug purposes
# print(df['hex data'].to_string(index=False))

first_sector = ''.join(df['hex data'])

def change_endianness(input_str):
    # Split the string into bytes
    bytes_list = [input_str[i:i+2] for i in range(0, len(input_str), 2)]
    # Reverse the list of bytes
    bytes_list.reverse()
    # Join the bytes back into a string
    reversed_hex_string = ''.join(bytes_list)
    return reversed_hex_string

# given bytes that represent addresses: 
# lower bound = given byte * 2
# upper bound = (given byte * 2) + 2.
variables = {
    "jump_to_boot_code": first_sector[:6], # indexes 0 - 5
    "oem_name": first_sector[6:22], 
    "bytes_per_sector": first_sector[22:26],
    "sectors_per_cluster": first_sector[26:28],
    "media_descriptor": first_sector[42:44],
    "total_sectors": first_sector[80:96],
    "mft_start_cluster": first_sector[96:112],
    "start_cluster_address_of_mft_mirror_data_attribute": first_sector[112:128],
    "mft_entry_size": first_sector[128:130],
    "index_record_size": first_sector[136:138],
    "serial_number": first_sector[144:160],
    "boot_code": first_sector[168:1020],
    "header": first_sector[1020:1024]
}

# Change endianness and print all variables
for name, value in variables.items():
    print(f"{name}: {change_endianness(value)}")
    # print(f"{name}: {value}")
