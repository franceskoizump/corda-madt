##To run:

1. Download and start MADT
```
cd ~
git clone --recursive https://github.com/dltcspbu/madt/
mkdir ~/madt/labs && export MADT_LABS_DIR=$HOME/madt/labs
mkdir ~/madt/sockets && export MADT_LABS_SOCKETS_DIR=$HOME/madt/sockets

cd madt
sudo pip3 install -r ./requirements.txt
sudo make && sudo make install

sudo -HE env PYTHONPATH=$HOME/madt:$PYTHONPATH SSH_PWD=demo python3 madt_ui/main.py 80  
```

2. Build images and start the lab
```
#open new terminal window
cd ~/corda-madt
#download corda
sh fetch_corda_jar.sh # ~about 20 minutes
#build corda nodes
sudo sh build-docker-nodes.sh
#run lab.py
python lab.py
```

3. Open 127.0.0.1:80
4. Login as demo:demo

## Usage

connect to node via ssh:
```
#password: test
#party-a
ssh -o StrictHostKeyChecking=no user1@localhost -o UserKnownHostsFile=/dev/null -p 2221
#party-b
ssh -o StrictHostKeyChecking=no user1@localhost -o UserKnownHostsFile=/dev/null -p 2222
#party-c
ssh -o StrictHostKeyChecking=no user1@localhost -o UserKnownHostsFile=/dev/null -p 2223
```

send Yo! to another party:
```
flow start YoFlow target: PartyB
```

inspect recieved Yo!
```
run vaultQuery contractStateType: net.corda.yo.YoState
```
