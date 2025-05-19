For this to work you must use Chrome (or edge). It's not possible to do so with firefox.

go to the following website : 

https://darkxst.github.io/silabs-firmware-builder/

for some reason, I was not able to do the update on fedora linux. I needed to do it from a windows 11 laptop.
Before I was able to flash the dongle, I needed to install the CSP210x VCP driver on windows. The webpage states to use the earlier drivers in the 6.7. I proceeded to install what was the oldest one.

Once done I could use the website.
Upon clicking on the **connect** button, the dongle could be found.

A popup will propose to choose the type of firmeware/device. The default option is the best.
From there, notice that your firmware version is to be updated and proceed to confirm. This should take roughly a minute.

### issue on fedora

Using the website with fedora, I stumbled on the problem that my dongle was connected but it couldn't read the firmware.

The website says to make sure, for linux users, that the user should be part of the dialout group. Though this didn't change anything.