# IT test for IPFS tools.
## 0.Pre-work
a) Install go-ipfs
b) Run ipfs daemon

## 1.Launch the IT test.
./flwr_main/run.sh


## 2.Basic flow:
a) server.py
Get IPFS file, untar to weights then delete the file.
Start Flower server.
Tar the weights folder and Send to IPFS.

b) client.py
Load the weights.
Launch the training client.


## 3.flwr_main
Modified from tensorflow example of flwr.

## 4. ipfs_tools
IPFS releated APIs.







