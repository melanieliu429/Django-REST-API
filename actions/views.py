from rest_framework import generics
from .models import SustainabilityAction
from .serializers import SustainabilityActionSerializer

class ActionListCreateView(generics.ListCreateAPIView):
    queryset = SustainabilityAction.objects.all()
    serializer_class = SustainabilityActionSerializer

class ActionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SustainabilityAction.objects.all()
    serializer_class = SustainabilityActionSerializer

import json
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import SustainabilityAction
from .serializers import SustainabilityActionSerializer

JSON_FILE = settings.BASE_DIR / "actions_data.json"

def save_to_json():
    actions = SustainabilityAction.objects.all()
    data = [SustainabilityActionSerializer(action).data for action in actions]
    with open(JSON_FILE, "w") as file:
        json.dump(data, file)

@csrf_exempt
def save_and_return_actions(request):
    if request.method == "GET":
        try:
            with open(JSON_FILE, "r") as file:
                data = json.load(file)
            return JsonResponse(data, safe=False)
        except FileNotFoundError:
            return JsonResponse([], safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = SustainabilityActionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            save_to_json()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)