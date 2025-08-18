---
tags:
  - RoR
---

## some files

### README.md

This is a readme file that is created by rails but is meant to be updated during development. explains how to setup the applicaition, etc.

### .ruby_version
simply hols the expected ruby version. this is used by tools, such as asdf, rvm, etc.

### config.ru
a file used by rack, ruby's web framework, that can be used to configure it

### gemfile
list you gems and library dependencies.
see [[Gemfile and Gemfile.lock]]

### gemfile.lock

lists all the current versions that were installed through bundle after going through the Gemfile.
the gemfile.lock is read later for production deployment to assure that no newer versions are installed ; which can happen if we specify in the gemfile that we want a particular gem to be "any versions above 2.0" for example. In this situation, the time gap between what was deployed in dev and by the time it's deployed in production, there can be a newer version installed.

### Rakefile

this is the Rakefile that defines oneoff commands, think of `rails new`. Rakefile is like Makefile for ruby.
## app


This is where we will spend most of our time writing code, this folder holds the subfolder for the **views**, **controller** and **model**.
But it also contains others like : 

- **assets** : it holds any images and stylesheets that will be used for the application.
- **channels** : this is to be used with ActionCables for setting up WebSockets.
- **helpers** : holds the methods to help with development of views especially anything regarding the formating of dates, sanitazing content, creating forms (with *form_with*) and others. anything related to HTML rendering in short.
- **javascript** : any javascript libraries that will be loaded, used with Turbo and Stimulus.
- **jobs** : for setting anything that needs to be executed asynchronously, like import of csv files
- **mailers** : all the configuration of setting up emails.

## bin

executables to load bundle, rails, rake, etc. as expected

## config


### Environment folder and application.rb

Application.rb holds general information on the configuration of the application; like the timezone. the environment folder holds information for different environments that can override the settings that were set in application.rb ; for example if you want to override the email settings so as to make sure it's not really sending anything in a dev/test environment unlike production.

### boot.rb

specifies what will be executed when rails is launched. You usually see the bundler execution and setup.

### database.yml

This holds any information regarding database connection. in there you specify the environments


### puma.rb

tweak the behavior of the puma server ; puma is a http server that is multi-threaded and optimized for parallelism.
this file is mostly to be modified in production

### routes.rb

specify the URLs that are available for the application and that will call the controller

### storage.yml

specifies where we would store files if on disk or amazon S3, etc. it's looked by the environments

## db

Where the database is stored for sqlilet for example but mostly holds migration files that specifies what changes in the database schema must be done or has not been done there yet.
### seeds.rd

adds default data when creating the application and sets data in the database.

## logs

Simply where the logs of the application are stored per 

## public

any static files for example the robot.txt, the favicon.ico or any http error pages like 404.html.

## storage
file upload storage. meant to stay empty in dev, but in prod it will contain more files.

## Test

holds all the unit tests
## vendor

This is where we store any 3rd party vendor code and library like any Javascript packages (think react)