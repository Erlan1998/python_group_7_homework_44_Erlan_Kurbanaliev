from django.shortcuts import render
from urllib.parse import parse_qs
import random

# Create your views here.
l = list(range(1,10))
secret = random.sample(l, 4)
def check_view(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        request_body = parse_qs(request.body.decode())
        try:
            data = list(map(int, request_body['numbers'][0].split(' ')))




