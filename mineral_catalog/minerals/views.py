from django.shortcuts import render
from django.http import HttpResponse
from .models import Minerals
from django.db import IntegrityError

import json

# Create your views here.

def minerals_create(request):
    """ get the minerals from json to database """
    with open('minerals/minerals.json') as minefile:
        all_mine = json.load(minefile)
        for mine in all_mine:
            try:
                Minerals(name=mine['name']).save()
            except IntegrityError:
                pass
        for mine in all_mine:
            obj = Minerals.objects.get(name=mine['name'])
            obj.image_filename = mine['image_filename']
            obj.image_caption = mine['image_caption']
            obj.category = mine['category']
            try:
                obj.formula = mine['formula']
            except KeyError:
                pass
            try:
                obj.strunz_classification = mine['strunz_classification']
            except KeyError:
                pass
            try:
                obj.crystal_system = mine['crystal_system']
            except KeyError:
                pass
            try:
                obj.unit_cell = mine['unit_cell']
            except KeyError:
                pass
            try:
                obj.color = mine['color']
            except KeyError:
                pass
            try:
                obj.crystal_symmetry = mine['crystal_symmetry']
            except KeyError:
                pass
            try:
                obj.cleavage =  mine['cleavage']
            except KeyError:
                pass
            try:
                obj.mohs_scale_hardness = mine['mohs_scale_hardness']
            except KeyError:
                pass
            try:
                obj.luster = mine['luster']
            except KeyError:
                pass
            try:
                obj.streak = mine['streak']
            except KeyError:
                pass
            try:
                obj.diaphaneity = mine['diaphaneity']
            except KeyError:
                pass
            try:
                obj.optical_properties = mine['optical_properties']
            except KeyError:
                pass
            obj.group = mine['group']
            try:
                obj.refractive_index = mine['refractive_index']
            except KeyError:
                pass
            try:
                obj.crystal_habit = mine['crystal_habit']
            except KeyError:
                pass
            try:
                obj.specific_gravity = mine['specific_gravity']
            except KeyError:
                pass
            obj.save()

    return HttpResponse("get the minerals data from json")



def mineral_list(request):
    minerals = Minerals.objects.all()
    return render(request, 'minerals/list.html', {'minerals':minerals})
