---
tags:
  - portainer
---


Because there is no update mechanism included in the community edition of portainer, it has to be done manually.

The steps required are
1. stop the container of portainer
2. Pull the new image
3. start docker with the image without forgetting to set the volume

## Commands


```bash
docker stop portainer
docker rm portainer
docker pull portainer/portainer-ce:latest
docker run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```

## Reference

- https://docs.portainer.io/start/upgrade/docker