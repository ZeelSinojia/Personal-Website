from django.contrib import admin
from .models import (
	Project,
	Education,
	TechnicalSkill,
	PersonalWebsite,
	Activity,
)


admin.site.register(Project)
admin.site.register(Education)
admin.site.register(TechnicalSkill)
admin.site.register(PersonalWebsite)
admin.site.register(Activity)
