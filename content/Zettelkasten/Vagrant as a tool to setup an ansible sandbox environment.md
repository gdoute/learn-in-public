---
tags:
  - vagrant
  - ansible
---


Vagrant allows to create a config file dedicated to setup a whole cluster of VMs in a way we want it to work

### prerequisite

First make sure that you have vagrant with libvirtd running.
On a fedora it would be done like so :

```bash
sudo dnf install vagrant vagrant-libvirt
sudo systemctl enable --now libvirtd
sudo usermod -aG libvirt $(whoami)
```

switch to the new group like so :

```bash
newgrp libvirt
```

This should be good to get started and move to the next step.
From there on out, we assume that all the file will be created on a dedicated folder.
### vagrant file

This is the setup I put in place to generate 3 debian VM with very low ressource as this is meant to run on my localhost laptop.

Content of the Vagrantfile

```ruby
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provider :libvirt do |libvirt|
    libvirt.uri = "qemu:///system"
  end

  (1..3).each do |i|
    config.vm.define "debian#{i}" do |node|
      node.vm.box = "debian/bookworm64"
      node.vm.hostname = "debian#{i}"
      node.vm.network "private_network", type: "dhcp"
      node.vm.synced_folder ".", "/vagrant", disabled: true
      node.vm.provider :libvirt do |libvirt|
        libvirt.memory = 512
        libvirt.cpus = 1
      end
      node.vm.provision "shell", inline: <<-SHELL
        apt update
        apt install -y python3 python3-apt sudo
      SHELL
    end
  end
end
```

### create the private network

the configuration file specify a "private_network" but we need to declare it before launching ou VMs

```xml
<network>
  <name>vagrant-private-dhcp</name>
  <bridge name="virbr1" />
  <forward mode="nat"/>
  <ip address="192.168.121.1" netmask="255.255.255.0">
    <dhcp>
      <range start="192.168.121.2" end="192.168.121.254" />
    </dhcp>
  </ip>
</network>
```
This forces the use of the network 192.168.121.0 so make sure it's available also for you.

Once this is done, we can create the network and start it :

```bash
sudo virsh net-define vagrant-libvirt.xml
sudo virsh net-autostart vagrant-private-dhcp
sudo virsh net-start vagrant-private-dhcp

```
### launch the vm

Launching the VMs through vagrant shouldn't cause too much issues, this command should bring everything up

```bash
vagrant up --privder=libvirt
```
### ssh_config

now to connect via ssh, we can ask vagrant to generate the ssh config file with this simple command :

```bash
vagrant ssh-config > ssh_config
```

### generate an inventory file

Because ansible usually needs an *inventory* file, based on what we created above we can pretty much hard code the file as such :

```ini
[debian]
debian1
debian2
debian2

[debian:vars]
ansible_ssh_common_args=-F ssh_config

```

What we're doing is that we specify the hostname of our 3 servers under the *debian* group.
We then specify that for this group, always use the variable *ansilbe_ssh_common_args* so that the correct IdentityFile will be used (and thus use the correct ssh key).

#### test connection

you can now test if ansible works correctly :

```bash
ansible all -i inventory -m ping
```

all the tests should pass on all 3 debians

### (optional) extra commands - destroy all VM

when you're done with you VMs and want to destroy all of them you can do :

```bash
vagrant destroy -f
```