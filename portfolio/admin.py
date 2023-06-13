from django.contrib import admin

from portfolio.models import Programmer, Project, Lab, News, Technologies

admin.site.register(Programmer)
admin.site.register(Project)
admin.site.register(Lab)
admin.site.register(News)
admin.site.register(Technologies)