from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import sys
import traceback
from business import Sudoku
import time

def index(request):
    context = []
    return render(request, 'sudoku/index.html', context)


def map_json_to_sudoku(in_json):
    dimension2 = len(in_json['sudoku'])
    sudoku = Sudoku(dimension2)
    for i in range(dimension2):
        for j in range(dimension2):
            sudoku.set(i, j, str(in_json['sudoku'][i]['cells'][j]['symbol']))
    return sudoku


def map_sudoku_to_json(sudoku):
    return [{'cells': [{'symbol': sudoku.get(i, j), 'valid': sudoku.validate(i, j)} for j in range(sudoku.dimension2)]} for i in range(sudoku.dimension2)]


def verify(request):
        jsonsudoku = json.loads(request.body)
        sudoku = map_json_to_sudoku(jsonsudoku)
        jsonsudoku['sudoku'] = map_sudoku_to_json(sudoku)
        return JsonResponse(jsonsudoku)
 
def generate(request):
    try:
        jsonsudoku = json.loads(request.body)
	dimension2 = len(jsonsudoku['sudoku'])
	sudoku = Sudoku(dimension2)
	start=time.time()
	sudoku.solve()
        jsonsudoku['sudoku'] = map_sudoku_to_json(sudoku)
        print 'time',time.time()-start 
        return JsonResponse(jsonsudoku)
    except:
        traceback.print_exc(file=sys.stdout)
        raise
