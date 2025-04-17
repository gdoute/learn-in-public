HEAD is basically where *you* are located in the commit timeline in git. Or more precisely, it's the pointer to the current branch.

Any time that you use the `checkout` (or `switch`) command to go from one branch to another, you're basically changing the location of HEAD.

Normally HEAD points to a branch, such that the links between HEAD, branch and commit is as follow :

```CSS
HEAD -> main -> commit ABC
```

HEAD can be what is called *detached*, which means it's not pointing to a branch :

```css
HEAD -> commit ABC
```

This can be interesting if you want to create a new branch in time after many commits were done, but you generally don't want to stay in a *detached* state.