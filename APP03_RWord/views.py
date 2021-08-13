from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def rword(request):
    if 'contador' not in request.session:
        request.session['contador'] = 0
    request.session['contador'] += 1
    randomword = get_random_string(length=14)
    context = {
        'rand_word': randomword,
        'count': request.session['contador']
    }
    return render(request, 'index.html', context)


def accion(request):
    selector = request.POST['presionado']
    print(selector)
    if selector == '0':
        return redirect("/")
    if selector == '1':
        request.session['contador'] = 0
    return redirect("/")