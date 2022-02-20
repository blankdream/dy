import requests
from urllib import request
import re,winreg
while True:
    #检查视频链接
    while True:
        print('请输入视频链接！')
        url = input()  # 链接地址
        try:
            real_address = request.urlopen(url).geturl()#获取跳转url
            number = re.findall(r'(\w*[0-9]+)\w*',real_address)#提取视频id
            break
        except:
            print('链接有误，请重新输入链接！')
    #伪装浏览器
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'
    }
    addresss = 'https://www.douyin.com/web/api/v2/aweme/iteminfo/?item_ids={}'.format(''.join(number))#拼接网址
    res = requests.get(addresss, headers=headers)#请求拼接网址
    video_info = res.json()#解析内容
    video_url = video_info['item_list'][0]['video']['play_addr']['url_list'][0]#获取无水印链接地址
    video_name = video_info['item_list'][0]['desc']#获取视频标题
    video = requests.get(video_url, headers=headers)#抓取视频
    # 获取桌面路径
    def get_desktop():
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
        return winreg.QueryValueEx(key, "Desktop")[0]# 获取桌面的路径
    Desktop_path = str(get_desktop())# 转化成字符串类型
    path = Desktop_path + '/'
    #下载无水印视频
    with open(r'{0}\{1}.mp4'.format(path, video_name), 'wb') as sp:
        sp.write(video.content)
        print(sp.name + '》》》下载成功！')