# KeepItRunnin-DJANGO

Reqs: Django 2.1.5 | pillow | django-widget-tweaks | django-crispy-forms |

To Run Application: Navigate to Manage.py directory and run "Python manage.py runserver"

A personal project designed to help organize vehicle maintenance and scheduling.

A user can create several vehicle profiles allowing for a unique vehicle maintenance schedule for each vehicle. (Older vehicles will require different maintenance than a brand new vehicle)

After creating a vehicle profile, the user may begin creating maintenance tasks for that vehicle and can begin setting up maintenance intervals and due dates for that task.

Once a maintenance task has been created, the user will begin to see a list of pending due maintenance tasks in the home page (and may begin to receive email and text reminders depending on the user preferences [ TO BE SET UP ])

A critical part of vehicle maintenance is replacing parts for the vehicle. The user may also keep track of equipment, consumables, and parts that need replacing or purchasing. The user may submit an item to the Parts Needed list and can set Due dates for each request in order to receive reminders and see urgent parts on the home page.

In order to better automate the maintenance process, parts can be associated to maintenance tasks and when a maintenance task to due, its associated part will automatically be added to the parts needed list.

Once a part has been purchased, the user may log that purchase including the purchase price and location to keep track of cost and item usage.
