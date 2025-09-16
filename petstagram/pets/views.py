from django.shortcuts import render

# Create your views here.
def add_pet(request):
    from django.http import HttpResponse
    return HttpResponse("Add pet page")

def pet_details(request, username, pet_slug):
    from django.http import HttpResponse
    return HttpResponse("Pet details page")

def edit_pet(request, username, pet_slug):
    from django.http import HttpResponse
    return HttpResponse("Edit pet page")

def delete_pet(request, username, pet_slug):
    from django.http import HttpResponse
    return HttpResponse("Delete pet page")