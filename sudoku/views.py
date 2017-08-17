from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import sys
import traceback
from .business import Sudoku
import time

# Helpers to convert to and from json format


def map_json_to_sudoku(in_json):
    dimension2 = len(in_json['sudoku'])
    sudoku = Sudoku(dimension2)
    for i in range(dimension2):
        for j in range(dimension2):
            sudoku.set(i, j, str(in_json['sudoku'][i]['cells'][j]['symbol']))
    return sudoku


def map_sudoku_to_json(sudoku):
    return [{'cells': [{'symbol': sudoku.get(i, j), 'valid': sudoku.validate(i, j)} for j in range(sudoku.dimension2)]} for i in range(sudoku.dimension2)]

# The actual views


def index(request):
    context = {}
    return render(request, 'sudoku/index.html', context)


def verify(request):
    jsonsudoku = json.loads(request.body.decode('UTF-8'))
    sudoku = map_json_to_sudoku(jsonsudoku)
    jsonsudoku['sudoku'] = map_sudoku_to_json(sudoku)
    return JsonResponse(jsonsudoku)


def generate(request):
    jsonsudoku = json.loads(request.body.decode('UTF-8'))
    dimension2 = len(jsonsudoku['sudoku'])
    sudoku = Sudoku(dimension2)
    sudoku.solve()
    sudoku.add_whitespace()
    jsonsudoku['sudoku'] = map_sudoku_to_json(sudoku)
    return JsonResponse(jsonsudoku)


def solve(request):
    jsonsudoku = json.loads(request.body.decode('UTF-8'))
    sudoku = map_json_to_sudoku(jsonsudoku)
    sudoku.solve()
    jsonsudoku['sudoku'] = map_sudoku_to_json(sudoku)
    return JsonResponse(jsonsudoku)
