---
title: Ansible inventories are text files listing servers and options
draft: false
tags:
  - ansible
---
 
Inventory files are simple files listing the servers that are present.
It's not much different from an .ini file where one line holds the information for one server.

## Example inventory file

```ini
[example]
www1.example.com
www2.example.com
```

In this example, the *example* is a group of servers. When called by ansible, the command will execute on all the servers specified below. In this case *www1* and *www2*

This file can be in any directories as long as it's being called by ansible from the current location the user is situated ; So we can create a *inventory* directory and set our *hosts.ini* file there.

**important** : the *.ini* extension is actually useless for ansible. Here this gives only the visual aid that the file is in an ini format

## Related
- [[inventory files lists many servers and there is no limit]]
- [[Related Note 2]]
