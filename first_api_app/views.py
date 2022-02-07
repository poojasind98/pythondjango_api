from django.shortcuts import render
from django.http import HttpResponse
from first_api_app.models import IndexModel
import requests

def index(request):
    # my_dict={'insert_me': "NOW IT IS FROM FIRST APP  index"}
    # return render(request,'first_api_app/index.html',context=my_dict)
    all_memes={}
    response=requests.get('https://api.imgflip.com/get_memes')
    data=response.json()
    x=data['data']
    memes=x['memes']
    # print(memes)
    for i in memes:
        memes_data = IndexModel(
        # print(i)
        id=i['id'],
        name=i['name'],
        url=i['url'],
        width=i['width'],
        height=i['height'],
        box_count=i['box_count']
        # id=i[0],
        # name=i[0],
        # url=i[1],
        # width=i[2],
        # height=i[3],
        # box_count=i[4]
        )
        memes_data.save()
        all_memes=IndexModel.objects.all()
    print(all_memes)
    return render(request,'first_api_app/index.html',{'all_memes':all_memes} )
# Create your views here.
