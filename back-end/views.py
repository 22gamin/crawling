from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create your views here.
def dust(request):
    # 지역 받아오기
    area=request.GET.get('area')
    # 지역이 공백이면 None
    if area==None:
        contents={'result':None}
    else:
        # 네이버 미세먼지 크롤링
        url='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&tqi=iuRlblp0JywsslVHc8VssssstnN-001056'
        html=urlopen(url)
        bs=BeautifulSoup(html.read(),'html.parser')

        # 지역,미세먼지농도,오전,오후 상황 받아오기
        data=bs.find_all('table')[1].find_all('tbody')[0].text.split(' ')
        
        # 중간에 공백 지우고 리스트에 넣기
        li=[]
        for i in data:
            if i!='':
                li.append(i)
            else:
                continue
                
        # 지역, 미세먼지농도, 오전상태, 오후상태 배열안에 저장     
        area_dust=[]
        for i in range(0,4):
            result=[]
            for j in range(i,68,4):
                result.append(li[j])
            area_dust.append(result)
        
        # 배열안에 지역이 있으면 idx에 넣기
        if area in area_dust[0]:
            idx=area_dust[0].index(area)
            con=area_dust[1][idx]
            morning=area_dust[2][idx]
            noon=area_dust[3][idx]

            contents={
            'result':f'{area}의 미세먼지 농도는 {con}이고, 오전예보는 {morning}, 오후예보는 {noon} 입니다'
        }




        # 없으면 선택지를 출력
        else:
            contents={
                'result' : f'{area}는 없습니다.' 
            }
            
        
    return render(request,'dust.html',contents)


def ultrafine_dust(request):
    # 지역 받아오기
    area = request.GET.get('area')

    # 지역이 공백이면 None
    if area==None:
        contents={'result':None}
    else:
        # 네이버 초미세먼지 크롤링
        url='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&tqi=iuh2hdprvTossNDiJPlssssstiC-452548'
        html=urlopen(url)
        bs=BeautifulSoup(html.read(),'html.parser')

        # 지역,초미세먼지농도,오전,오후 상황 받아오기
        data=bs.find_all('table')[1].find_all('tbody')[0].text.split(' ')
        
        # 중간에 공백 지우고 리스트에 넣기
        li=[]
        for i in data:
            if i!='':
                li.append(i)
            else:
                continue
                
        # 지역, 초미세먼지농도, 오전상태, 오후상태 배열안에 저장     
        area_dust=[]
        for i in range(0,4):
            result=[]
            for j in range(i,68,4):
                result.append(li[j])
            area_dust.append(result)
        
        # 배열안에 지역이 있으면 idx에 넣기
        if area in area_dust[0]:
            idx=area_dust[0].index(area)
            con=area_dust[1][idx]
            morning=area_dust[2][idx]
            noon=area_dust[3][idx]

            contents={
            'result':f'{area}의 초미세먼지 농도는 {con}이고, 오전예보는 {morning}, 오후예보는 {noon} 입니다'
        }




        # 없으면 선택지를 출력
        else:
            contents={
                'result' : f'{area}는 없습니다.' 
            }
            
        
        

    return render(request,'u_dust.html',contents)

def main(request):
    return render(request,'main.html')
