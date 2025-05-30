---
tags:
  - encryption
---


If you want to use FIDO2 from your yubikey to decrypt a disk or partition, you need to do the following steps :
First you need to find out what is the encrypted partition :

```bash
$> lsblk
NAME                                          MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINTS
zram0                                         251:0    0     8G  0 disk  [SWAP]
nvme0n1                                       259:0    0 465,8G  0 disk
├─nvme0n1p1                                   259:1    0   600M  0 part  /boot/efi
├─nvme0n1p2                                   259:2    0     1G  0 part  /boot
└─nvme0n1p3                                   259:3    0 464,2G  0 part
  └─luks-06198e29-8743-4610-9c83-b1d1d6352516 252:0    0 464,2G  0 crypt /home
                                                                         /
```

here, **nvme0n1p3** is our candidate.

## add fido2 module for dracut

```bash
$ echo "add_dracutmodules+=\" fido2 \"" | sudo tee /etc/dracut.conf.d/fido2.conf 
```

## add the FIDO2 device

```bash
$ sudo systemd-cryptenroll --fido2-device=auto /dev/<encrypted partition>
```

of course \<encrypted partition\> must be replaced by **nvme0n1p3** that we discovered earlier in our first step.

A PIN will be asked for you to enter. This is supposed to be the PIN you've set for FIDO2

**Important** : repeat the above command to  for as many yubikey as you have ; you don't want to be stuck and unable to decrypt your partition if you lose your key, right ?

While you're at it [[How to create a recovery key for your LUKS partition ?|generate a recovery key]] if you haven't done so already.

## update /etc/crypttab

modify the /etc/crypttab and make sure you add `fido2-device=auto` at the end of the line where your partition is mentionned.

All columns have a purpose, the last one is about options to set and values must be separated with a comma.

example of entry :

> luks-06198e29-8743-4610-9c83-b1d1d6352516 UUID=06198e29-8743-4610-9c83-b1d1d6352516 none discard,**fido2-device=auto**

## rebuild initramfs

```bash
$ sudo dracut -f
```

If you've never used dracut before, don't be surprised if it takes a couple seconds

[[What is dracut ?]]

## external reference

- [Use systemd-cryptenrol with FIDO U2F or TPM2 to decrypt your disk](https://fedoramagazine.org/use-systemd-cryptenroll-with-fido-u2f-or-tpm2-to-decrypt-your-disk/)
