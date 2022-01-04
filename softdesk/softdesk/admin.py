from django.contrib import admin
from core.models import Users, Projects
from contributor.models import Contributors
from issue.models import Issues, Comments


admin.site.register(Users)
admin.site.register(Projects)
admin.site.register(Contributors)
admin.site.register(Issues)
admin.site.register(Comments)
