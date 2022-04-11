import os
import hashlib
from datetime import datetime
start= "/"
BLOCK_SIZE = 65536

#this list is really long because there are quite a lot of files I can not hash but I can not figure out how to be more efficient
nohash = ["dev","proc","run","sys","tmp","bin","/var/lib","/var/run","vmlinuz.old","vmlinuz","initrd.img","initrd.img.old","kali.postinst","pwsh.1.gz",".uuid","pyserial-ports","timedatectl","pyminifier","myisamchk","asmbadmincheck","atk6-fake_pim6","llvm-dwarfdump-13","myisamlog"]
dateTimeObj = str(datetime.now())

def hashfile(filename):                #function hashes files                                             
    file_hash = hashlib.sha256()
    with open(filename, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

fname = ""
for root,d_names,f_names in os.walk(start):  #works through file system recursively
    if d_names in nohash:
        continue           #ignores the folders we do not want to hash
    for f in f_names:
        if f not in nohash:
            hashed = hashfile(f)#hashes current file
        else:
            hashed = "hash unavailable"
        fname = os.path.join(root, f) + " " + hashed + " " + dateTimeObj #adds file path, hash, and timestamp as one item to list
        print(fname)
        
        
#print("fname = %s" %fname)
with open("systemLog", 'w') as sl: #writes fname to file to save for later reference.
    sl.writelines(fname)
sl.close() 
f.close()


    
    
