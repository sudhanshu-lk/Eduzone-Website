from django.contrib import admin
from .models import Course, PageCourse, TeamMember, Quiz, Question, Result

admin.site.register(Course)
admin.site.register(PageCourse)
admin.site.register(TeamMember)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 4

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ('course',)
    inlines = [QuestionInline]

admin.site.register(Question)
admin.site.register(Result)
