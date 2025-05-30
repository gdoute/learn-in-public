---
tags:
  - RoR
---


## app


This is where we will spend most of our time writing code, this folder holds the subfolder for the **views**, **controller** and **model**.
But it also contains others like : 

- **assets** : it holds any images and stylesheets that will be used for the application.
- **channels** : this is to be used with ActionCables for setting up WebSocets
- **helpers** : holds the methods to help with development of views especially anything regarding the formating of dates, sanitazing content, creating forms (with *form_with*) and others
- **jobs** : for setting anything that needs to be executed asynchronously, like import of csv files
- **mailers** : all the configuration of setting up emails