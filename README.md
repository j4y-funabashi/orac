
Need to add the following to get access to dot3k
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
