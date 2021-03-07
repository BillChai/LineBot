#分享鐵人幫
import requests
from bs4 import BeautifulSoup as bs 

def lineNotifyMessage(token, msg, img):

    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {
        'message': msg,
        'imageThumbnail' : img, #imageThumbnail、imageFullsize為成對的圖片，各有尺寸大小
        'imageFullsize' : img,
        'stickerPackageId' : 2, #stickerPackageId、stickerId為貼圖成對的編號，參閱Line Sticker List
        'stickerId' : 520
    }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code



if __name__ == "__main__":
  token = '27ovjZjEm7AzC2vDS7Ju7yYpAivoacrl8kxml53rk7z'
  message = '大賢者【告】今日網友梗圖Top1'
  url = 'https://memes.tw/wtf' # 爬取https://memes.tw/wtf中網友創作的第一張梗圖
  img = bs(requests.get(url).text ,"lxml").find_all("", {'class': 'img-fluid'})[0]['data-src']
  
  lineNotifyMessage(token, message, img)