from django.shortcuts import render

def visitCount(request):
    num_visit = request.session.get('count',0)
    num_visit=num_visit+1
    request.session['count'] = num_visit
    return render(request,'show.html', {'num_visits':num_visit})
