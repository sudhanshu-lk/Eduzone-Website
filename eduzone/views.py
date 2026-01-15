from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Course, PageCourse, TeamMember
from .models import Quiz, Question, Result
from django.contrib.auth.decorators import login_required

def home_view(request):
    course = Course.objects.all()
    return render(request, 'home.html', {'course': course})

def about(request):
    members = TeamMember.objects.all()
    return render(request, 'about.html', {'members': members})

def course_detail_view(request, slug):
    course = get_object_or_404(PageCourse, slug=slug)
    return render(request, 'course_detail.html', {'course': course})

def course_view(request):
    courses = PageCourse.objects.all()
    return render(request, 'course.html', {'courses': courses})

# @login_required
def quiz_list(request):
    query = request.GET.get('q')
    if query:
        #Searches for quiz title or course name
        quizzes = Quiz.objects.filter(course__title__icontains=query) | Quiz.objects.filter(title__icontains=query)
    else:
        quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

# @login_required
def take_quiz(request, quiz_id):
    quiz_obj = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz_obj.questions.all()

    if request.method == 'POST':
        score = 0
        total = questions.count()

        for q in questions:
            # Matches the radio button 'name' attribue in HTML
            selected_ans = request.POST.get(f'question_{q.id}')
            if selected_ans == q.answer:
                score += 1
            
        percent = (score / total) * 100 if total > 0 else 0
        Result.objects.create(quiz=quiz_obj, user=request.user, score=score, total=total, percent=percent)

        return render(request, 'quiz_result.html',{
            'score': score, 'total': total, 'percent': percent, 'quiz': quiz_obj
        })
    
    return render(request, 'take_quiz.html', {'quiz': quiz_obj, 'questions': questions})