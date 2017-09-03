# 在真实网页中获取信息：
# 每次点击页面就是一次request，然后接受response:http协议
# request: get/post
from bs4 import BeautifulSoup
import requests
import time

url_saves = 'https://www.tripadvisor.cn/Saves/833113'
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
#url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-oa30-New_York_City_New_York.html#ATTRACTION_LIST'
urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'\
        .format(str(i)) for i in range(30, 1111,30)]
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Cookie': 'TATravelInfo=V2*AY.2017*AM.9*AD.10*DY.2017*DM.9*DD.11*A.2*MG.-1*HP.2*FL.3*RVL.105127_243l60763_243l1687489_243*DSM.1504230903564*RS.1; TAUD=LA-1504230824269-1*RDD-1-2017_08_31*LD-79277-2017.9.10.2017.9.11*LG-79279-2.1.F.; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1504784376121; TAUnique=%1%enc%3AILkYE3gURan%2BQA5HEqavGiGBGM9M%2BTdSlAMiVzQSqSQ%3D; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C4%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TASSK=enc%3AAAykDEmOqIqQtQ4EKUDlqaJpnMzufIYF1R1ByAF%2B%2BG3f5SxCMbHdaxXCBpBkBaIy5zcrKhdphsxMtX%2BT6cGmzkzZP0SVIxVdLOAUK1sl0OqY9Lmb%2Fy0AZJgPrUgZNui0sA%3D%3D; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1504172166,1504179777; _smt_uid=59a7d886.3a63dbc5; _jzqa=1.4539076001434692600.1504172167.1504179777.1504184085.3; _jzqy=1.1504172167.1504172167.1.jzqsr=baidu|jzqct=tripadvisor.-; _jzqckmp=1; ki_t=1504172168606%3B1504172168606%3B1504184087245%3B1%3B7; ki_r=; CommercePopunder=SuppressAll*1504173033691; _qzja=1.953871917.1504172167086.1504179776885.1504184085283.1504180505365.1504184085283..0.0.7.3; TASession=%1%V2ID.D1942965A3BEFB29847EEE4E4C87129C*SQ.45*LP.%2F*PR.427%7C*LS.DemandLoadAjax*GR.95*TCPAR.39*TBR.7*EXEX.86*ABTR.62*PHTB.36*FS.80*CPU.15*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.E1B95FB654F9D69FF0E1095E2168FAB1*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.1687489; ServerPool=A; TAReturnTo=%1%%2FAttraction_Review-g60763-d1687489-Reviews-The_National_9_11_Memorial_Museum-New_York_City_New_York.html; SecureLogin2=3.4%3AALpNj13MjkIGWJu8M20SiolYlBnqspABwDhrUnEVLapyPz7udxoxxKQovEEdPkxBtRLsrc72rgCn%2FVZA8iy9t7g9yq3%2BcqhWkUksBHttl3uzehtXsm1J4mUI2mb3SF8CPuApvP3%2BA8NwIWoyvVDn9MNLR0yi3ASusRkL%2BvrsAXn61Zzlz3KeA6LxXybZP9wW31HlTBLjIiflaH4C4Coojm4%3D; TAAuth3=3%3A4292a169723f4493cf8f0c51ba09adda%3AAGV1He7dWvq9IsUk3KKq4x6CjG7JzrDq7erIHcBXX4B2lFTVskZZKvstHF4SatcP1pUrA7%2BbXkwI7OZbsdOKXuLZIockEfHoltZItyIJooBLaz4k0cfOV5eyO1ygR2jEY6m1ZV4lTpmYg2ZJy6orkaLeB6b4y%2BOPth26YV78fp5Gb1yaO99jaeBypwTjOnp4Jw%3D%3D; roybatty=TNI1625!AEJgnpC2TPKkHriZyARwLUQ6Xe9IorullRlV5yud0CnnQSoApOV81MmItwwBptPU2%2B4MM7aA%2Bc1aM9czSB2iaOf7J3aPZkR3oaRuCgwQUEaFOtEWBur4umZcjqJKsJzQQkXRYFkr%2BdzNAu%2BM6JogoAUUrCmUxc7N3Gy8YCxv2Z0N%2C1'
}


def get_attraction(url, data = None):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('div.listing_title > a[target="_blank"]')
    imgs = soup.select('img[width="180"]')
    cates = soup.select('div.p13n_reasoning_v2')
    for title, img, cate in zip(titles, imgs, cates):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'cate': list(cate.stripped_strings)
        }
        print(data)

#使用Cookie模拟登录
def get_favs(url, data=None):
    web_data = requests.get(url_saves, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('a.location-name')
    imgs = soup.select('img.photo_image')
    cates = soup.select('spn.format_address')
    for title, img, cate in zip(titles, imgs, cates):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'cate': list(cate.stripped_strings),
        }
        print(data)

#get_attraction(url)
#get_favs(url_saves)

#爬去每个页面：链接：
#反爬取措施，每次请求暂停两秒：
for single_url in urls:
    print(single_url)
    get_attraction(single_url)
    time.sleep(2)
#解决图片显示错误的问题：
#通过模拟移动端来解决：
