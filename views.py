# from django.http import HttpResponse
# from django.http import HttpResponseForbidden, HttpResponseBadRequest
# from django.http import JsonResponse
# from django.core.serializers.json import DjangoJSONEncoder
# from django.shortcuts import render
# from django.template.response import TemplateResponse

# def index(request):
#     return HttpResponse("<h2>Главная</h2>")

# def user(request):
#     age = request.GET.get("age")
#     name = request.GET.get("name")
#     return HttpResponse(f"<h2>Имя: {name} Возраст: {age}</h2>")

# 33
# def user(request):
#     age = request.GET.get("age", 0)
#     name = request.GET.get("name", "Undefined")
#     return HttpResponse(f"<h2>Имя: {name} Возраст: {age}</h2>")

# 34
# def index(request):
#     return HttpResponse("Index")

# def about(request):
#     return HttpResponse("About")

# def contact(request):
#     return HttpResponseRedirect("/about")

# def details(request):
#     return HttpResponsePermanentRedirect("/")

# 36
# def index(request, id):
#     people = ["Tom", "Bob", "Sam"]
#     if id in range(0, len(people)):
#         return HttpResponse(people[id])
#     else:
#         return HttpResponseNotFound("Not Found")
    
# def access(request, age):
#     if age not in range(1, 111):
#         return HttpResponseBadRequest("Некорректные данные")
#     if (age > 17):
#         return HttpResponse("Доступ разрешен")
#     else:
#         return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")

# 38
# def index(request):
#     return JsonResponse({"name" : "Tom", "age":38})

# 39
# def index(request):
#     bob = Person("Bob", 41)
#     return JsonResponse(bob, safe = False, encoder = PersonEncoder)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class PersonEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Person):
#             return {"name": obj.name, "age": obj.age}
#         return super().default(obj)

# 42
# def set(request):
#     username = request.GET.get("username", "Underfined")
#     response = HttpResponse(f"Hello {username}")
#     response.set_cookie("username", username)
#     return response

# 43
# def set(request):
#     username = request.GET.get("username", "Underfined")
#     response = HttpResponse(f"Hello {username}")
#     response.set_cookie("username", username)
#     return response

# def get(request):
#     username = request.COOKIES["username"]
#     return HttpResponse(f"Hello {username}")

# 46
# def index(request):
#     return render(request, "index.html")

# 47
# def index(request):
#     return TemplateResponse(request, "index.html")

# def about(request):
#     return render(request, "about.html")

# def contact(request):
#     return render(request, "contact.html")

# 49
# def index(request):
#     data = {"header" : "Hello Django", "message" : "Welcome to Python"}
#     return render(request, "index.html", context=data)

# 51
# def index(request):
#     header = "Данные пользователя"
#     langs = ["Python", "Java", "C#"]
#     user = {"name" : "Tom", "age" : 23}
#     address = ("Абрикосовая", 23, 45)

#     data = {"header" : header, "langs" : langs, "user" : user, "address" : address}
#     return render(request, "index.html", context=data)

# 52
# from django.template.response import TemplateResponse
# def index(request):
#     header = "Данные пользователя"
#     langs = ["Python", "Java", "C#"]
#     user = {"name" : "Tom", "age" : 23}
#     address = ("Абрикосовая", 23, 45)

#     data = {"header" : header, "langs" : langs, "user" : user, "address" : address}
#     return TemplateResponse(request, "index.html", context=data)

# 52.2
# from django.shortcuts import render
# def index(request):
#     return render(request, "index.html", context = {"person": Person("Tom")})

# class Person:
#     def __init__(self, name):
#         self.name = name 

# 54
# from django.shortcuts import render
# def index(request):
#     return render(request, "index.html", context = {"boby": "<h1> Hello World! </h1>"})

# 55
# from django.shortcuts import render
# def index(request):
#     data = {"n" : 5}
#     return render(request, "index.html", context = data)

# 57
# from django.shortcuts import render
# def index(request):
#     langs = ["Python", "JavaScript", "Java", "C#", "C++"]
#     return render(request, "index.html", context = {"langs": langs})

# 58
# from django.shortcuts import render
# def index(request):
#     data = ["red": "красный", "green": "зеленый", "blue":"синий"]
#     return render(request, "index.html", context = {"data": data})

# 65
# from datetime import datetime
# from django.shortcuts import render
# def index(request):
#     return render(request, "index.html", context = {"my_date": datetime.now()})

# 66
# from datetime import datetime
# from django.shortcuts import render
# def index(request):
#     users = ["Tom", "Sam", "Bob", "Mike"]
#     return render(request, "index.html", context = {"users": users})

# 
