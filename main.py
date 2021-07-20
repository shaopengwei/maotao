"""
Copyright (c) 2021 Shaopengwei, Inc. All Rights Reserved
@author shaopengwei (shaopengwei@hotmail.com)
@date 2021/7/20
@brief
"""

import requests
from bs4 import BeautifulSoup
import json

if __name__ == "__main__":
    maotai_paimai_url = "https://paimai.taobao.com/pmp_seller/2209328166496.htm?history=0&sort_price=0&filter_status" \
                        "=0&page=1"
    my_header = {
        "cookie": "t=cede4713537a6016ff37ee21b3443cf7; cna=MKjMGNW3BycCAXTVqLf6CEBu; "
                  "tracknick=%5Cu4E0D%5Cu91CD%5Cu8981%5Cu7684%5Cu5175%5Cu4E01; thw=cn; "
                  "enc=mf6irv71FFW6jk12w%2BsvM3cWV%2BLEq4otX7dkwAd1tzS3b4iZxTEnvwzFZcxDAZIQOSn0or2ZjCe1lqJsIvFvQg%3D"
                  "%3D; hng=CN%7Czh-CN%7CCNY%7C156; _samesite_flag_=true; cookie2=1c933df399f38b0cbc26a352cdaaff52; "
                  "_tb_token_=331ee3bf1579e; miid=2350943192024443125; xlly_s=1; "
                  "lgc=%5Cu4E0D%5Cu91CD%5Cu8981%5Cu7684%5Cu5175%5Cu4E01; cancelledSubSites=empty; "
                  "dnk=%5Cu4E0D%5Cu91CD%5Cu8981%5Cu7684%5Cu5175%5Cu4E01; mt=ci=34_1; "
                  "UM_distinctid=17abe35cebeecb-0cfeab619ee3e7-34647600-1aeaa0-17abe35cebff26; "
                  "JSESSIONID=31D28A97B617859A06CF18A0CB6EE093; "
                  "_m_h5_tk=b8e262f9f715a43e5fa1365176f5da22_1626764370741; "
                  "_m_h5_tk_enc=2376c86678b7a2bcb345f22d82056165; "
                  "CNZZDATA1253345903=492899278-1626686267-https%253A%252F%252Fwww.taobao.com%252F%7C1626755420; "
                  "sgcookie=E100h8XGhZ2%2BpBa2yP3Ol%2BOG"
                  "%2BhBz6uRRVy3fsQVeQ2r9YHNYLpKrZ584Fi9E9P033y7ulqGD1H88eczINwNcTOZSIw%3D%3D; unb=502013273; "
                  "uc3=vt3=F8dCuwJH4okADIgx0LY%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&id2=Vv7LhvAdMv5c&nk2=0XnihoudgBg%2B%2F7QH; "
                  "csg=1db9843c; cookie17=Vv7LhvAdMv5c; skt=21a80a1307a6a5a8; existShop=MTYyNjc1NzcyMw%3D%3D; "
                  "uc4=nk4=0%4000HJyKMN407LHV2HgkDsesXWJfouvoA%3D&id4=0%40VHj3C48gk7OlTTIen%2BTiDvOUSLg%3D; "
                  "_cc_=WqG3DMC9EA%3D%3D; _l_g_=Ug%3D%3D; sg=%E4%B8%8135; "
                  "_nk_=%5Cu4E0D%5Cu91CD%5Cu8981%5Cu7684%5Cu5175%5Cu4E01; "
                  "cookie1=V3oZLs7DvTTFUil1mr8xgORnMUGdRKTuXn8KGoUmx8E%3D; "
                  "uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&cookie14"
                  "=Uoe2yzgpoJWNPg%3D%3D&cookie21=VT5L2FSpdet1EftGlDX54Q%3D%3D&existShop=false&pas=0; "
                  "tfstk=cYjGBImHnBGSVILhPlt1ImnOxpadwuhvZZ7hYig1PAMaxk50X2urKaPH1kUZl; "
                  "l=eBMZdmSHjcEppBkNKOfanurza77OSIRYYuPzaNbMiOCPOp1B5"
                  "-ZAW6TPFNT6C3GVhs_MR3k0kl4WBeYBcQAonxvtOTLLGSMmn; "
                  "isg=BF5e5Dagsn-HZ-YRx5Qt5v9Ir_KgHyKZ2oCeHwjnyqGcK_4FcK9yqYTNIzcnExqx"
    }
    ret = requests.get(maotai_paimai_url, headers=my_header)
    soup = BeautifulSoup(ret.text, features="html.parser")
    item_string = '[' + \
                  str(soup.find_all(name='script', attrs={"class": "J_pmp_item_list_params"})[0]).strip().split('[')[
                      1].split(']')[0].strip().replace(" ", "").replace("\n", "").replace("\r", "") + ']'
    for item in json.loads(item_string):
        print(item['title'])
