
### Enable SPI and i2c so python can talk to the dot3k

https://www.the-captains-shack.com/post/rpi-piglow-container/

```
# /etc/modules: kernel modules to load at boot time.
i2c-dev
i2c-bcm2708
spi-bcm2708
```

```
# /boot/config.txt
dtparam=i2c1=on
dtparam=spi=on
dtparam=i2c_arm=on
```

### Example fstab entry to mount usb drive with uuid

```
# /etc/fstab
UUID=83D8-665C /media/MUSIC vfat auto,nofail,noatime,rw 0 2
```
