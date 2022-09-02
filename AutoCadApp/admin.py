from django.contrib import admin
from .models import Tutorial, TutorialTest, Test, AppUser, Certificate
# Register your models here.


admin.site.register(Tutorial)
admin.site.register(TutorialTest)
admin.site.register(Test)
admin.site.register(AppUser)
admin.site.register(Certificate)
