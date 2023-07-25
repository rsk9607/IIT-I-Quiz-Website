from django.contrib import admin
from quizocrats.models import quizzes,questionare,result,help
# Register your models here.
admin.site.register(quizzes)
admin.site.register(questionare)
admin.site.register(result)
admin.site.register(help)
