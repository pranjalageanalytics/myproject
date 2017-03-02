from django.contrib import admin
from .models import ChallengeType

# Register your models here.
"""class ChallengeAdmin(admin.ModelAdmin):
    model = UserChallengeCategoryLocation
    list_display = ['user', 'start_date_time', 'end_date_time']"""

admin.site.register(ChallengeType)