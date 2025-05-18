This lab had the following requirements :


## challenge
#### Tasks:

- Create users: `admin`, disable `root` SSH login.
- Setup `sudo` access with no password prompt.
- Set timezone and locale.
- Disable unnecessary services (like `bluetooth`, `cups`, etc.).
- Ensure `ufw` is installed and configured (basic firewall).
- Set the hostname of each server via inventory variables.
    

#### Concepts:

- `user`, `lineinfile`, `copy`, `service`, `ufw`, `hostname`
- Inventory variables (`host_vars/`, `group_vars/`)
- Idempotency checks


## My playbook result

Here is what I ended up doing :

```yaml
---

- name: ansible test lab 1
  become: true
  become_method: sudo
  become_user: root
  hosts: all
  tasks:

    - name: set hostname
      hostname:
        name: "{{ hostname }}"

    - name: set /etc/hosts entry
      lineinfile:
        path: /etc/hosts
        regexp: '^127\.0\.1\.1\s+'
        line: "127.0.1.1 {{ hostname }} "
        state: present

    - name: install sudo
      ansible.builtin.apt:
        name: sudo
        state: present

    - name: install ufw
      ansible.builtin.apt:
        name: ufw
        state: present

    - name: set timezone
      timezone:
        name: Europe/Paris


    - name: get list of installed packages
      package_facts:
        manager: auto

    - name: deactivate cups if present
      service:
        name: cups
        state: stopped
      when: "'cups' in ansible_facts.packages"

    - name: check ufw is up
      ufw:
        state: enabled
        policy: allow


    - name: create user
      ansible.builtin.user:
        name: admin
        comment: admin user
        group: sudo
        shell: /bin/bash
        password: "{{ 'changeit' | password_hash('sha512')}}"
```

### thoughts on the playbook

#### hostname and sudo 

There where issues right after the change of the hostname where doing sudo actually took too much time and ended in a timeout. At first I increased the timeout variable when calling ansible-playbook like so :

```bash
ansible-playbook -i inventory.ini ../playbooks/main.yml --timeout 60
```

this worked around the problem.
The real solution whas to add the second task in the playbook : modifying the /etc/hosts file

#### check service present

checking if a service is present is necessary if you intend to add the task to stop a service. In this regard, it doesn't check for you this before hand. This is why I had to add the *het list of installed packages* first and user the *when* statement in the next task

#### improvements

There are many way this can be improved, like the creation of the user, we can set a ssh key instead of a hardcoded password. We can also do the install of sudo and ufw in one task instead of two