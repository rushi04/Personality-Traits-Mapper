from django.shortcuts import render
from watson_developer_cloud import PersonalityInsightsV3
from django.http import JsonResponse
import json
import pandas as pd

from matplotlib import pyplot as plt


# Create your views here one moment at a time one breath at a time one thought at a time my boyy.


def rush(request):
    url='https://gateway-lon.watsonplatform.net/personality-insights/api'
    apikey='gbRDQN-e61tQ_bB6cAFf_gTsFY-Zp6uRQfvihM58Wn51'
    service=PersonalityInsightsV3(url=url, iam_apikey=apikey,version='2019-30-06')
    text='''r Brock It is with a heavy heart that I return the Eagle Scout pin and badge I was awarded in August of 1980 while I was a member of Holy Cross Troop 31, Bay Lakes Council. I do this in protest of the Boy Scouts of America’s policy to deny leadership positions to gay and lesbian adults and membership to young adults who identify as gay.
    How sad that an organization that teaches leadership has chosen to relinquish the lead in one of the most important civil rights issues of our time.
    I pray that one day you will see the error of your ways and realize that the principles and ideals of scouting can be taught by men or women, gay or straight. And the knowledge, wisdom and benefits of Scouting should be available to all young men regardless of their sexual identity.
    With regret Jonathan Johns'''
    profile=service.profile(text, content_type='text/plain').get_result()
    # len(profile['warnings'])
    profile1 = json.dumps(profile,indent=2)
    print(type(profile))
    needs = profile.get('needs')
    results = {}
    j=0
    for need in needs:
        result={need['name']:need['percentile']}
        results.update(result)
    print(results)
    return JsonResponse({'result':results,'profile':profile})

def analyse(request):
    if request.method == 'POST':
        text = request.POST['text']
        print(text)
    return render(request,'Traits/home.html')
    