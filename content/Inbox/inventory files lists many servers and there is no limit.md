---
title: inventory files lists many servers and there is no limit
draft: false
tags:
  - ansible
---
 
We can group servers through the ini syntax like so :

```ini
[app]
192.168.1.1

[bdd]
192.168.2.1
```

we can then group both of them by mentioning only the group names

```ini
[multi:children]
app
bdd
```

It's also important to know that we can specify particular variables for the groups. So if we want to set variables for the *multi* group we would do this :

```ini
[multi:vars]
ansible_user=gdo
ansible_ssh_private_key_file=~/.ssh/id_rsa_specific
```


