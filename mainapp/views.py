import json
from asgiref.sync import sync_to_async
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .rto import fetch_carinfo

class Index(View):
     def get(self, request):
        carinfo = fetch_carinfo("JH10BK5078")
        print(carinfo)
        return render(request, "index.html")

class RC_info(View):
    def post(self, request, *args, **kwargs):
        # 1) Read and parse the JSON body (no await)
        data = json.loads(request.body)
        text = data.get('text', '')
        
        # 2) Call the blocking fetch_carinfo in a threadpool
        carinfo = fetch_carinfo(text)
        print(carinfo)
        # 3) Return the result
        return JsonResponse({
            "msg": "we got it",
            "carinfo": carinfo
        })
