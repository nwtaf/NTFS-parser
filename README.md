# NTFS-parser
Parses the first sector of a New Technology (NTFS) File System given hex in a separate file (supports copy-paste into ntfs_sector.txt).

For the given bytes, the code will take a dump from ntfs_sector.txt, put it into a dataframe, isolate and remove spaces from the 'hex data' colum of the dataframe, parse it, swap endianness, and print the desired variables.

![alt text](https://github.com/nwtaf/NTFS-parser/blob/main/NTFSBytes.png)
