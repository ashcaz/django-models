# Lab 27: Django Models

## Overview

Django has a powerful Object Relational Mapper that allows us to persist data using Python instead of SQL.

Today you’ll build out a project with one model and wire up that model using Django Views.

## Implementation Notes

- The instructions are becoming more conceptual.
- All the concepts listed relate to key Django steps covered in the demo.
- If there is confusion about what, exactly, is required then ask the client (aka the instructors.)
- TLDR - make your lab project like the demo project.

## Feature Tasks and Requirements

### Models

- create snack_tracker_project project
  - This will involve some preliminary steps.
  - Review previous class lab for details.
- create snacks app
- Add snacks app to project
- create Snack model

  - make sure it extends from proper base class
  - add name as a CharField with maximum length of 64 characters.
  - add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
    - from django.contrib.auth import get_user_model
  - add description TextField

- add model to admin
- modify Snack model have user friendly display in admin
- create migrations and migrate data
- create a super user
- run development server
- Add a few snacks via Admin panel
- create another user and more snacks via Admin panel
- confirm that snacks behave as expected with proper name, purchaser and description.
- Looks like your model in good shape. Congrats!
