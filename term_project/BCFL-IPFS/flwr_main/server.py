import os
import flwr as fl
import sys
sys.path.append("..")
from ipfs_tools.ipfstools import *


hash_path = "./ipfs_hash.txt"
ipfs_name = 'weights.tar.gz'

#Get IPFS file, untar to weights then delete the file.
if os.path.isfile(hash_path):
    print("Get IPFS file, untar to weights then delete the file.")
    hfile = open(hash_path, 'r')
    hashValue = hfile.readline()
    ipfsGetFile(hashValue, ipfs_name)
    untarFile(ipfs_name, './')
    delFile(ipfs_name)

# Start Flower server
fl.server.start_server(
    server_address="[::]:8765",
    config={"num_rounds": 3},
)

checkpoint_path = "training/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Tar the weights folder and Send to IPFS.
if os.path.isdir(checkpoint_dir):
    print("Tar the weights folder and Send to IPFS.")
    tarFile(checkpoint_dir, ipfs_name)
    hashValue = ipfsAddFile(ipfs_name)
    delFile(ipfs_name)
    print("The hash code is:")
    print(hashValue[0])
    infile = open(hash_path, 'w')
    print(hashValue[0], file=infile)
    infile.close()




