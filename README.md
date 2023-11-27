# NTFS-parser
Parses the first sector of a New Technology File System (NTFS) given address, hex, and string data in a separate file (supports paste in ntfs_sector.txt).

Given there is data in ntfs_sector.txt, the code will read-in ntfs_sector.txt, store the data in a dataframe, isolate and remove spaces from the 'hex data' colum of the dataframe, parse it, swap endianness, and print the desired variables.

![alt text](https://github.com/nwtaf/NTFS-parser/blob/main/NTFSBytes.png)
