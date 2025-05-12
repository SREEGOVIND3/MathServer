from django.shortcuts import render

def lamp_power(request):
    area = ''
    l = ''
    b = ''
    
    if request.method == 'POST':
        try:
            l = float(request.POST.get('length', 0))
            b = float(request.POST.get('breadth', 0))
            area = l * b
        except (TypeError, ValueError):
            area = 'Invalid input'

    return render(request, 'mathapp/math.html', {'l': l, 'b': b, 'area': area})
