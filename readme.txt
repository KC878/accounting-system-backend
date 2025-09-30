from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('accountant', 'Accountant'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='accountant')
    date_updated = models.DateTimeField(auto_now=True)  # auto-update timestamp

AUTH_USER_MODEL = 'accounting.Users''
 

## adding a custom auth_user


## Creating a SuperUser 
python manage.py createsuperuser




## Filter repo 
Here’s a clean approach using git filter-repo:

Install git-filter-repo (if you haven’t):

Here’s a safe local approach using git filter-repo:

Install git-filter-repo (if not yet installed):

pip install git-filter-repo


Backup your repo folder—just in case.

Remove settings.py from the entire history:

git filter-repo --path accountingfront/settings.py --invert-paths


This rewrites all commits, removing the file completely.

Verify:

git log --stat


You should see that settings.py is gone from all previous commits.

Optional: If you want to keep it in your working directory for local use, just copy it back after the filter and add it to .gitignore so it’s never tracked again:

accountingfront/settings.py



## Installing Django restframework

pip install djangorestframework



# About Serializer --
- its basically converting complex query set to dictionary and to JSON 

-> From Database = querysets 
-> From serializer(queryset) = Python dictionary
-> Dictionary can be converted to JSON format to communicate with the web app 


# All About HTTP Status Codes 
1xx is informational 
2xx is sucerss 
3xx is forwaring 
4xx error response 
5xx backend type of error 