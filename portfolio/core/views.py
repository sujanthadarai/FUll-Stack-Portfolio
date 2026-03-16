from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

'''

GIT & GITHUB
GIT : version control system 
it helps developer :
- track code changes
- work with team
- restore with old version 
-code histroy (save ,edit ,resave)



Example : suppose you are making django project 
day 1 : login system #version 1(login solve)
day 2 : register system #version 2
day 3 : login & register , dashboard #version 3

Github : it is website where the project are store online usin git


computer folder(local folder)
git add  --> stage area
git commit -m "first changes" # local repo 
git push -->remote repo
--> github(remote(repo))

'''
