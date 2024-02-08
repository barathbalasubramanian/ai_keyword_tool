from django.shortcuts import render
from django.http import HttpResponse
import datetime
from Keyword_Bomber_Tool_Backend.app import keyword_analysis_function
import json
from django.http import HttpResponse, HttpResponseNotFound , JsonResponse


def my_view(request):

    print("Running")
    input_keyword = "Marketing Automation"
    input_country = "us"
    return render(request , "home.html")


# def generate(input_keyword,input_country) :
#     print(input_keyword,input_country)
#     result = keyword_analysis_function(input_keyword,input_country)
#     file_path = 'output.json'
#     with open(file_path, 'w') as json_file:
#         json.dump(result, json_file, indent=2) 
#     print("Result : " ,result)


def generate(request):
    if request.method == 'POST':
        input_keyword = request.POST.get('key', '')
        input_country = request.POST.get('con', '')
        
        result = keyword_analysis_function(input_keyword, input_country)
        file_path = 'output.json'
        with open(file_path, 'w') as json_file:
            json.dump(result, json_file, indent=2) 
        print(result)
        # Assuming keyword_analysis_function returns a dictionary
        return JsonResponse({'result': result})
    
    return JsonResponse({'error': 'Invalid request method'})