---
tags:
  - systemd
---
systemd can be used for a user session and many scripts can be leveraged this way. Typically, it's possible to replace CRON with systemd when setting timers.
But the point here is to know a few commands that can be helpful when managing systemctl and journalctl to view how the unit services are behaving

In the examples below, I'm setting *restic-backup.service* but it can be any unit service file.
### basic stop/start and enablers

```bash
systemctl --user start restic-backup.service
```

this will execute the *ExecStart* part of the restic-backup service

```bash
systemctl --user stop restic-backup.service
```

same thing but for halting.

To make sure it's executed on user session start, you can enable the service :

```bash
systemctl --user enable restic-backup.service
systemctl --user disable restice-backup.service # to not have it no longer executed at start
```

To verify if a service that are currently enabled :

```bash
systemctl --user is-enabled restic-backup.service
```

### logs of a service

to view the logs of systemctl execution for a particular service

```bash
journalctl --user -u restic-backup.service
```

to get a more detailed output and add colors you can add the `-x` (also known as `--catalog`) :

```bash
journalctl --user -xu restic-backup.service
```