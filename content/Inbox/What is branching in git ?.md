---
tags:
  - git
---


Branches must be understood as simple bookmarks in  the timeline of commit. Contrary to other tools like Subversion, where a branch is a fork of the main timeline, here they are just pointers.

So considering this timeline of commit in a *main* branch

```css
A -- B -- C (main)
```

Considering that HEAD is on C, then doing the following command to create a branch will simply create a "pointer" to C named *feature-x*

```bash
git branch feature-x
```

it creates this :

```css
A -- B -- C
			\
			(main)
			(feature-x)
```


[[What is HEAD ?]]

[[How do I change from one branch to another ?]]

[[What is the difference between a local and remote branch ?]]
