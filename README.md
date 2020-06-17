# pyabr-server

In the name of God, the Compassionate, the Merciful
Pyabr Server (c) 2020 Mani Jamali. Free Software GNU General License v3.0

 - How to install it on Ubuntu server?
 - How to launch the cloud service on client?
 
# How to install it on Ubuntu server?

 - Git source:
 
 ```shell script
git clone https://github.com/manijamali2003/pyabr-server
 ```

 - Jump to pyabr server directory:
 
 ```shell script
cd pyabr-server
```
 - Config thr cloud service:
 
```shell script
python configure.py
```

 - Create virtual host cloud service:
 
```shell script
sudo python wizard-create.py
```

# How to launch the cloud service on client?

 - Use SSH or PuTTY
 - Run Pyabr service as command line interface:
 
 ```shell script
ssh [hostname]@[server-ip]
```

 - Run Pyabr service as graphical user interface:
 
```shell script
ssh -X [hostname]@[server-ip]
```