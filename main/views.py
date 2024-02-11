from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
def json_response(request):
    return HttpResponse('Hello, World! Welcome to main')

def http_response(request):
    return HttpResponse("<h1>Hello, World! Welcome to main</h1>")

def say_hello(request):
    return HttpResponse("<h1>Hello, World! Welcome to main</h1>")


user  = {"name": "Obehi", "email": "Nigeria", "phoneNumber": "coding"}

def user_profile(request):
    return JsonResponse(user)

data = [
    {
    "id" : 1,
    "name": "Obehi",
    "title": "Python",
    "description": "Python is a programming language",
    "submitted by": "Obehi"
},
{
    "id" : 2,
    "name": "Oyinlade",
    "title": "React",
    "description": "React is a programming language",
    "submitted by": "Oyin"
},
{
    "id" : 3,
    "name": "Suad",
    "title": "Angular",
    "description": "Angular is a programming language",
    "submitted by": "Suad"
},

]

# def user_query(request, query_id):
#     if query_id == 1:
#         return JsonResponse(data[0])
#     elif query_id == 2:
#         return JsonResponse(data[1])
#     elif query_id == 3:
#         return JsonResponse(data[2])
#     else:
#         return JsonResponse({"error": "Query not found"}, status=404)
    
def all_queries(request):
    return JsonResponse(data, safe=False)   

def user_query(request, query_id):
    for query in data:
        if query['id'] == query_id:
            return JsonResponse(query)
        

class QueryView(View):
    queries = [
        {"id": 1, "name": "Obehi", "title": "Python", "description": "Python is a programming language", "submitted by": "Obehi"},
        {"id": 2, "name": "Oyinlade", "title": "React", "description": "React is a programming language", "submitted by": "Oyin"},  
    ]
    def get(self, request):
        return JsonResponse({"results": self.queries})
    
    def post(self, request):
        return JsonResponse({"message": "Query submitted successfully"})