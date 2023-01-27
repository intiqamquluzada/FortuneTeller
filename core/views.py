from random import random

from django.shortcuts import render


def first(request):
    listt = [
        'Siz cetinlikle ugur qazanacaqsiniz, el cekmeyin',
        'Siz bedbextsiniz',
        'Heyatiniz cox qaydasindadir',
        'Etrafinizda size deyer veren insanlara deyer verin',
        'Herseyden onemli ozunuz oldugunu unutmayin',
        'Insanlarin fikirlerini onemsemeyin,yolunuza baxin',
        'Cetin veziyyetlerde qacmagi tercih etmeyin, ustune dogru gedin',
        'Gordun alinmir coxda sey eleme',
        'Backend-in basini burax seninki frontdu',
        'Backend senin ucun yaradilib :)',
        'Elsene benzemeye calis'
    ]
    fr = listt
    context = {
        'fr': fr
    }
    return render(request, 'index.html', context)
