from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import sys
import traceback
from business import Sudoku


def index(request):
    context = []
    return render(request, 'sudoku/index.html', context)


def verify(request):
    try:
        jsonsudoku = json.loads(request.body)
        sudoku = Sudoku()
        jsonsudoku['sudoku'][0]['cells'][0]['symbol'] = 3
        return JsonResponse(jsonsudoku)
    except:
        traceback.print_exc(file=sys.stdout)
        raise
