---
tags:
  - git
---


`checkout` is the historic command and `switch` was introduced later.
With time, `checkout` introduced many features that ended up confusing people. As a result `switch` was introduced to improve user experience.

`switch` has less features than `checkout` but it's by design. It's considered to be the safer command to use if all you want is to change from one branch to another.

An example of confusing feature is the restoring of file.
If you made modifications to a file but decide it's not worth it and you want to restore it to the last commit state, you can do so with `checkout` by doing :

```bash
git checkout -- myfile.md
```

however, `switch` doesn't do that, it's main purpose is to go from one branch to another. You would need to use `restore` :

```bash
git restore myfile.md
```

In the process we can say that it's much cleaner as we're avoiding a strange `--` flag that was present for `checkout`