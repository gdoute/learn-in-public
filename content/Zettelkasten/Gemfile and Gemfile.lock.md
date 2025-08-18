---
tags:
  - ruby
  - RoR
---


The *Gemfile* for any ruby program is where you specify all the dependencies of other ruby libraries (i.e : gems) are required.

Here is an example of what contains an gemfile

```bash
source "https://rubygems.org"

# Bundle edge Rails instead: gem "rails", github: "rails/rails", branch: "main"
gem "rails", "~> 8.0.2"
# The modern asset pipeline for Rails [https://github.com/rails/propshaft]
gem "propshaft"
# Use sqlite3 as the database for Active Record
gem "sqlite3", ">= 2.1"
# Use the Puma web server [https://github.com/puma/puma]
gem "puma", ">= 5.0"
```

a *gemfile.lock* is a file that holds all the versions of gems that were currently installed. This is allows to execute the import gems reading the gemfile with only downloading the versions that can be updated (for example when setting a particular version)

This is what a gemfile.lock looks like after creating an application with rails 8.0.2 : 

```bash
GEM
  remote: https://rubygems.org/
  specs:
    actioncable (8.0.2)
      actionpack (= 8.0.2)
      activesupport (= 8.0.2)
      nio4r (~> 2.0)
      websocket-driver (>= 0.6.1)
      zeitwerk (~> 2.6)
    actionmailbox (8.0.2)
      actionpack (= 8.0.2)
      activejob (= 8.0.2)
      activerecord (= 8.0.2)
      activestorage (= 8.0.2)
      activesupport (= 8.0.2)
      mail (>= 2.8.0)
    actionmailer (8.0.2)
      actionpack (= 8.0.2)
      actionview (= 8.0.2)
      activejob (= 8.0.2)
      activesupport (= 8.0.2)
      mail (>= 2.8.0)
      rails-dom-testing (~> 2.2)
    actionpack (8.0.2)
      actionview (= 8.0.2)
      activesupport (= 8.0.2)
      nokogiri (>= 1.8.5)
      rack (>= 2.2.4)
      rack-session (>= 1.0.1)
      rack-test (>= 0.6.3)
      rails-dom-testing (~> 2.2)
      rails-html-sanitizer (~> 1.6)
      useragent (~> 0.16)
```

Those files are used by *bundler* when deploying later in production

[[Bundler is the ruby gem manager]]
