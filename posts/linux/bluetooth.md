重装ubuntu后蓝牙不能开启
```shell
sudo apt install --reinstall bluez
sudo rmmod btusb
sleep 1
sudo modprobe btusb
```

```shell
hciconfig
bluetootchctl
```
