from django.shortcuts import render
from urllib.parse import parse_qs
import random

class Check:
    def __init__(self, secret, actual):
        self.secret = secret
        self.actual = actual

    def guess_numbers(self):
        bulls = 0
        cows = 0
        if len(set(self.actual)) == 4:
            for i in range(len(self.secret)):
                if 0 >= self.actual[i] or self.actual[i] >= 11:
                    return 'Введенные чиcла не должны быть меньше (0) и не больше 10!'
                if self.secret[i] == self.actual[i]:
                    bulls = bulls + 1
                elif self.actual[i] in self.secret:
                    cows = cows + 1
            if bulls == 4:
                return 'ВЫ ПОБЕДИЛИ!'
            else:
                return f'bulss = {bulls}, cows = {cows}'
        elif len(self.actual) != 4:
            return 'Вводите ровно 4 числа! не меньше и не больше!'
        else:
            return 'Введены похожие числа!'


l = list(range(1, 10))
secret = random.sample(l, 4)


def check_view(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        request_body = parse_qs(request.body.decode())
        try:
            data = list(map(int, request_body['numbers'][0].split(' ')))
            global secret
            check = Check(secret, data)
            guessed_num = check.guess_numbers()
            if guessed_num == 'ВЫ ПОБЕДИЛИ!':
                message = f'{guessed_num}'
                secret = random.sample(l, 4)
            else:
                message = f'{guessed_num}'
        except ValueError:
            message = f'Введены не числа!'
        except KeyError:
            message = f'Введите данные!'
    return render(request, 'home.html', {'message': message})
