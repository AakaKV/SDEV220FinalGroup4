from django.apps import AppConfig
#We want to track time at least a little in this
from django.utils import timezone
#We want this to redirect to the repair page when a mechanic confirms repair
from django.shortcuts import redirect
#Importing security features from django to help us verify mechanics
from django.contrib.auth.decorators import login_required

class MechsystConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MechSyst'
