# linux_bt_connect
A script that helps connect from to a bluetooth device fast with a known device ssid

## Dependencies
You need to have bluetoothctl package and python(both python2 and python3 are compatible) package installed 
You can install them on linux with following command:

```bash
sudo apt install bluetoothctl python
```

## Installation Guide
Check if bluetoothctl and python are installed on your machine.

The directory btcon can be moved to anywhere you want, such as I have put it
in "/home/sayan/.custom-commands/lib/" where I keep all my scripts in use.


### Run without argument
1. Navigate into the directory named "btcon"

2. Open bash-file named "btcon" and replace line 3: device="FC:58:FA:D8:60:95" with device="xx:xx:xx:xx:xx:xx" where xx:xx:xx:xx:xx:xx is your device ssid; save changes

3. Open terminal and cd into the directory named "btcon"

4. Run the command 
```bash
./btcon 
```
on your terminal

5. As the new terminal appears, press enter onto it and the bluetooth device with given ssid should have been connected to your PC so far by now.

### Run with argument
1. Open terminal and cd into the directory named "btcon"

2. Run the command

```bash
./btcon xx:xx:xx:xx:xx:xx
```
on your terminal where xx:xx:xx:xx:xx:xx is your device ssid 

3. As the new terminal appears, press enter onto it and the bluetooth device with given ssid should have been connected to your PC so far by now.

### Run as a command without navigating into the directory
1. Open the command folder inside this repo and open bash-file named "btcon" and replace line 2: "cd /home/sayan/.custom-commands/lib/btcon" with "cd path/to/btcon/dir/in/this/repo", save changes

2. Move that bash-file anywhere next to your $PATH variable, for me it's /home/sayan/.custom-commands/bin which is added to my $PATH variable

3. Run 

```bash
./btcon 
```
or

```bash
./btcon xx:xx:xx:xx:xx:xx
```
from anywhere on your terminal. You can also alias different device IDs in your .bashrc file such as 
"alias headset=xx:xx:xx:xx:xx:xx" and run

```bash
btcon headset
``` 	
on command line.