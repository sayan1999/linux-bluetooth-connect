# linux_bt_connect
A script to fast connect to a bluetooth device with known device ssid.

## Dependencies
You need to have [blueZ](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjxyLqyronmAhWmwTgGHfVcCIYQFjAAegQIARAG&url=https%3A%2F%2Fdocs.ubuntu.com%2Fcore%2Fen%2Fstacks%2Fbluetooth%2Fbluez%2Fdocs%2Finstall-bluez&usg=AOvVaw3aNHcDP4xHohr_-uDt2-1I) package installed 
You can install it on ubuntu with following command:

```bash
sudo apt install bluez
```

## Installation Guide
Check, if bluez is installed on your machine.

The directory btcon can be moved to anywhere you want. I have put it
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

5. As the new terminal appears, you will see scanning results and devices already paired on top. Once you find desired devicename appearing, press ctrl + c and another terminal opens with logs for pairing & connection attempt. The bluetooth device with given ssid should have been connected to your PC so far by now, press ctrl + c to exit. If it didn't work, just run that command once more, or try restarting your bluetooth device.

### Run with argument
1. Open terminal and cd into the directory named "btcon"

2. Run the command

```bash
./btcon xx:xx:xx:xx:xx:xx
```
on your terminal where xx:xx:xx:xx:xx:xx is your device ssid 

3. As the new terminal appears, you will see scanning results and devices already paired on top. Once you find desired devicename appearing, press ctrl + c and another terminal opens with logs for pairing & connection attempt. The bluetooth device with given ssid should have been connected to your PC so far by now, press ctrl + c to exit. If it didn't work, just run that command once more, or try restarting your bluetooth device.

### Run as a command without navigating into the directory
1. Open the command folder inside this repo and open bash-file named "btcon" and replace line 2: "cd /home/sayan/.custom-commands/lib/btcon" with "cd path/to/btcon/dir/", save changes

2. Move that bash-file anywhere next to your $PATH variable, for me it's /home/sayan/.custom-commands/bin which is added to my $PATH variable

3. Run 

```bash
btcon 
```
or

```bash
btcon xx:xx:xx:xx:xx:xx
```
from anywhere on your terminal. You can also alias different device IDs in your .bashrc file such as 
"alias headset=xx:xx:xx:xx:xx:xx" and run

```bash
btcon headset
``` 	
on command line.
