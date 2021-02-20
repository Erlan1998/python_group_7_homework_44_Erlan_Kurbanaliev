from django.shortcuts import render
from urllib.parse import parse_qs


def check_view(request):
    secret = [1, 2, 3, 4]
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        request_body = parse_qs(request.body.decode())
        try:
            data = list(map(int, request_body['numbers'][0].split(' ')))

            if data == secret:
                message = f'ВЫ ПОБЕДИЛИ!'
            else:
                message = f'попробуйте еще раз'
        except ValueError:
            message = f'Введены не числа!'
        except KeyError:
            message = f'Введите данные!'
    return render(request, 'home.html', {'message': message})
