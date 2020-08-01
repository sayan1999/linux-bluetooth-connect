# linux_bt_connect
A script to fast connect to a bluetooth device with known device ssid.

![LINUX BT Connect](previews/linuxbtconnect.png?raw=true "linuxbtconnect.png")
## Dependencies
You need to have [blueZ](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjxyLqyronmAhWmwTgGHfVcCIYQFjAAegQIARAG&url=https%3A%2F%2Fdocs.ubuntu.com%2Fcore%2Fen%2Fstacks%2Fbluetooth%2Fbluez%2Fdocs%2Finstall-bluez&usg=AOvVaw3aNHcDP4xHohr_-uDt2-1I) package installed.
You can install it on ubuntu with following command:

```bash
sudo apt install bluez
```

## Installation Guide
Check, if bluez is installed on your machine.

The directory btcon can be moved to anywhere you want. I have put it
in "$HOME/.custom-commands/lib/" where I keep all my scripts in use.


### Run without argument
1. Navigate into the directory named "btcon"

2. Open bash-file named "btcon" and replace line 5: device="FC:58:FA:D8:60:95" with device="xx:xx:xx:xx:xx:xx" where xx:xx:xx:xx:xx:xx is your device ssid; save changes.
This will be your default device i.e. you can connect to any other device but merely running "btcon" without args will connect to this favourite device.

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

### Install the script
1. Open the command folder inside this repo and open bash-file named "btcon" and replace line 2: "cd $HOME/.custom-commands/lib/btcon" with "cd path-to-btcon-dir/", save changes.

2. Move that bash-file anywhere next to your $PATH variable, for me it's $HOME/.custom-commands/bin which is added to my $PATH variable

3. Now, run 

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


### Troubleshoot
If running the commands doesn't work, re-run them. There are high chances it will work now.

If any blocking line appears saying : "Waiting to connect to bluetothhd", Run:

```bash
btcon -t
```
It runs modprobe btusb && systemctl start bluetooth under the hood so asks for user password



### Advanced

You can add it as an application to your application menu.

1. Copy the headset-connect.desktop file to your $HOME/.local/share/applications/
2. Press Alt+f2 to launch Quick Command and run "restart". Now, Headset Connect is in your Application Menu.
3. Initially, the icon will not have logo, for that open the headset-connect.desktop file and modify 7th line:
	Icon=/home/sayan/.icons/bthdphn.png
to-> 
	Icon=path to downloaded image icon

### Usage

#### btcon [options] [args] | btcon [args]

OPTIONS:
-c xx:xx:xx:xx:xx:xx : Connects to device with ssid xx:xx:xx:xx:xx:xx
-d : Turns down bluetooth
-e xx:xx:xx:xx:xx:xx : Enlists new device in the configuration list and display config file
-s <device-name> : Searches for device of above name and connects to it
-z <device-name> : Searches for device of above name, enlists it and connects to it
-p : Show all devices elisted

ARGS:
<integer> : Connects to the device listed as the <integer>th device in the file