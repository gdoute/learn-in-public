Ansible is configuration tool that helps maintaining the configuration of your host in one place, but it's more than that.

It's also a way to create scripts that help you manage servers that can run across multiple servers and multiple OS.

Ansible's benefit is to be reuseable.

Ansible aims Idempotency, meaning that an ansible commands should return the same result if executed multiple times. If a configuration is different, from what the playbook specifies, it'll make the correction, otherwise it will leave it as is.