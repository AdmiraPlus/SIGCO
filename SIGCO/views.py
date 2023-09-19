from django.shortcuts import render, redirect

import os
from SIGCO.settings import BASE_DIR

def home(request):
	
	print(os.path.join(BASE_DIR, 'templates'))
	
	
	return render(request, 'home.html')