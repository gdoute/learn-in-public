---
tags:
  - git
---


Going from one branch to another consists of using the `checkout` command ; alternatively you can use the `switch` command.

Considering this timeline and that you are on *main* branch :

```css
A -- B -- C -- D (feature-X)
		    \
		    (main)HEAD
```

doing :

```bash
git checkout feature-X
```

does the following :

```css
A -- B -- C -- D (feature-X)HEAD
		    \
		    (main)
```

[[What is the difference between checkout and switch ?]]