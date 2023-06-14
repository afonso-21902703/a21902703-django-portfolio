from django.contrib import admin

from portfolio.models import Programmer, Project, Lab, News, Technologies, Patterns

admin.site.register(Programmer)
admin.site.register(Project)
admin.site.register(Lab)
admin.site.register(News)
admin.site.register(Technologies)
admin.site.register(Patterns)
