---
tags:
  - RoR
---


### To create a new application

```bash
rails new newap
```

This will create the app with all the structure of ruby on rails

[[How a ruby application is structured]]

### to generate a model entry

```bash
rails generate model User
```

This creates a Class name **User** but also a table *users* (note the **s**) and create a new file under `/app/models/user.rb` which will contain