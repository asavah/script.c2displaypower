# script.c2displaypower

This script will work **only** on **odroid-c2** boards with recent enough HK kernel.  
https://github.com/hardkernel/linux/commit/7e0aef0d72dc26708ada0e54dc89281efddd6ee8  
Proper kernel boot parameter is also needed, see http://forum.odroid.com/viewtopic.php?f=144&t=23879 for reference.

This small screensaver script for Kodi can trick your display into going into powersave mode  
after selected period of inactivity.

If your TV has CEC better use CEC and not this hack.

This was tested only on framebuffer builds of Kodi-Jarvis and it will work only
if Kodi runs under root (ie in distros like LibreELEC),
otherwise a custom udev rule to change the permissions of the relevant sysfs knobs is required.

It is possible to use 2 different sysfs knobs,  
default is fb0 mode, which can be changed by editing  
https://github.com/asavah/script.c2displaypower/blob/master/resources/lib/gui.py#L17
change self.mode = "fb0" to anything like self.mode="amhdmitx0" to use phy mode.

Known "glitch":  
I use an LG display with my c2, this display has 1 VGA and 2 hdmi inputs,
if I change inputs after the display has gone into powersaving and switch back to odroid-c2 hdmi port  
display's powersave mode is no longer active, there is nothing I can do about it  
since as far as I understand it - this is not proper DPMS,  
but just a hack to trick the display into thinking that the hdmi link is gone  
and after switching inputs display can sense the link again.
