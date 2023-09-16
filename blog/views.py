from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("""<html>
                        <title>Блог Вероники Рыжковой</title>
                        <h1>Вероника Рыжкова</h1>
                        </html>""")
