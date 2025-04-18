There seems to be security concerns when first trying to execute `flameshot gui` using hotkeys in GNOME

[this gist](https://gist.github.com/linuxkathirvel/5e8bb416f487b4b47a97daa42288502f) gives the answer.
You need to create a script with particular variables that GNOME doesn't pass and then call `flameshot gui`

So first create the script below ; call it `flameshot.sh`
Make sure it has correct permissions : `chmod +x flameshot.sh`
call this script in gnome keyboard hotkey configuration.

![[Pasted image 20250418164845.png]]
## script content

```bash
#!/bin/bash
export DISPLAY=:0
export WAYLAND_DISPLAY=$WAYLAND_DISPLAY
export DBUS_SESSION_BUS_ADDRESS=$DBUS_SESSION_BUS_ADDRESS
/usr/bin/flameshot gui
```
