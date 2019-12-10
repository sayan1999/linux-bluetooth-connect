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

### Optional
 open ./btcon/btcon on text-editor and replace line 67: device="FC:58:FA:D8:60:95" with device="xx:xx:xx:xx:xx:xx" where xx:xx:xx:xx:xx:xx is your device(most frequently used) ssid; save changes.

### Installation with script 

1. Execute script ./install.sh inside the directory.

2. Add $HOME/.local/bin to your $PATH.

### Manual Installation

1. First open terminal and cd into the project directory. Then,

2. Run the following commands on the same terminal.

```bash
cp ./command/btcon ~/.local/bin/btcon
chmod +x ~/.local/bin/btcon
cp ./btcon/btcon ~/.local/lib/btcon
chmod +x ~/.local/lib/btcon
```
3. Add $HOME/.local/bin to your $PATH

## Usage

| Command | Description |
| --- | --- |
| btcon | connects to your default device, set accordingly the method mentioned under optional header |
| btcon -n xx:xx:xx:xx:xx:xx | adds new device ssid to the config file $HOME/.btcon/btcon (creates if not existing)|
| btcon <num> | reads ssid of <num>th device in the config file $HOME/.btcon/btcon and connects to it |