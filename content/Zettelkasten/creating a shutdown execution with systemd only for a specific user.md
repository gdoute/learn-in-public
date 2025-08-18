---
title: creating a shutdown execution with systemd only for a specific user
draft: false
tags:
  - systemd
---
 
A proper way to execute particular scripts during shutdown for a specific user is to have it done by systemd and using the `systemctl --user` command.


### example unit service

in the `~/.config/systemd/user` directory, add your service. Here is an example of the *quartz-logout.service* implemented :

```ini
[Unit]
Description=Run Quartz Sync on session exit
After=graphical-session.target

[Service]
Type=oneshot
ExecStart=/bin/bash -lc 'cd /home/gdo/path/to/quartz && npx quartz sync'

[Install]
WantedBy=exit.target
```

next we reload the systemd daemon for the user and enable the service :

```bash
systemctl --user daemon-reexec
systemctl --user daemon-reload
systemctl --user enable quartz-logout.service
```

After the enable command, this should create a directory in ~/.config/systemd/user called *exit.target.wants* and should contain an symlink to the quartz-logout.service file 
### testing

We can test by restarting the service and then execute the stop instruction for systemd and check in the logs with journalctl :

```bash
systemctl --user restart quartz-logout.service
systemctl --user stop quartz-logout.service
journactl --user -u quartz-logout.service
```

