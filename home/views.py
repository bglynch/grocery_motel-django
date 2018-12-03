from django.shortcuts import render


# View to show the home page
def get_home(request):
    return render(request, 'home/home.html')
