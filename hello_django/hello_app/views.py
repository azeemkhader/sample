from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def print_hello(request):
    movie_data={
        'movies': [ 
         {
        'title': 'Wolf of Wall Street',
        'year':'2007',
        'summary': 'Great MOvie!!!! BUt Not TO Adapt ',
        'success': True
        },

         {
        'title': 'Leo',
        'year':'2023',
        'summary': ' SuperBB Film to watch  ',
        'success': True
        },

         {
        'title': ' Jacobintint Swargarajyam',
        'year':'2015',
        'summary': 'Great Great !!!! Movie For That Motivation  ',
        'success': True
        },

         {
        'title': ' Margin Call',
        'year':'2010',
        'summary': ' Film Mainly MAde To Understand How Bussiness Works!!!',
        'success': False
        },

         {
        'title': ' RDX',
        'year':'2023',
        'summary': 'Great Fighting Movie!!! and abt The value of Friendship ',
        'success': True
        },

        
        

    ]}
    return render(request,'hello.html',movie_data)
