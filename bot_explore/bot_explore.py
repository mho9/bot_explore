import requests,json,re
import time as ti
from urllib.parse import urlencode
from random import choice

# Demo bot_explore app :)
# instagram : https://www.instagram.com/pyby0
# Login Cookies 

usera_list  = []
file = json.load(open('use.json'))# json file
usera_list = file['User_agent']
us =choice( usera_list)



s = requests.Session()

class app:
   
    def __init__(self,sessionid,time,cmt):
        self.time = time
        self.cmnt = cmt
        self.contCom = 0
        self.contLike = 0
        self.login(sessionid)

    def login(self,ses):
        if ses !='' or ses!=None:
           
                s.cookies.update({
                    'sessionid' : ses,
                })
              

                a = s.get('https://www.instagram.com/')
                csrf =a.cookies['csrftoken']
                rollout_hash = re.search('(?<="rollout_hash":")\w+', a.text).group(0)
                s.headers ={# headers
                    
                    'accept': '*/*',
                    'origin':'https://www.instagram.com/',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                    'X-CSRFToken':csrf,
                    'user-agent':us,
                    "X-Instagram-AJAX": rollout_hash,

                }
                
                
                finder = a.text.find("full_name")
    
                 # find  full_name 
                if finder !=-1:
                    print('Done')
                    self.explore()
            
                else:
                    pass
        else:
            print('Sessionid is Empty ')
     
    def explore(self):
            while True:
                ti.sleep(1)
                url_exp = 'https://www.instagram.com/explore/grid/?'+ urlencode({
                    'is_prefetch':'false',
                    'omit_cover_media': 'false',
                    'module': 'explore_popular',
                    'use_sectional_payload': 'true',
                    'cluster_id':' explore_all',
                    'include_fixed_destinations': 'true'
                })
                get_explore = s.get(url_exp)

                if get_explore.status_code ==200:

                    get_explore = get_explore.json()# json 

                    seitems = get_explore['sectional_items']
                    ##
                    for i in seitems:
                      
                        if i['layout_type'] =="media_grid":
                        

                            posts_info = i['layout_content']['medias'] # get Posts 
                                
                            for i in posts_info:

                                if self.time !=None and self.time >=38 :
                                    ti.sleep(int(self.time))
                                else:
                                    ti.sleep(60)

                                
                            
                                
                
                                i_d = i['media']['id']# id the post
                                i_d = i_d.split('_')[0]
                                
                                self.like(i_d)
                                self.comment(i_d)
                                
                                
                    
                    
    def like(self,i_d):
        urlLik  =f'https://www.instagram.com/web/likes/{i_d}/like/'
        doLike =s.post(urlLik,verify=False)
        if doLike.status_code ==200:
            print('\b'+'Like Done :'+str(self.contLike),end="\r")
            self.contLike +=1
        else:
            if doLike.status_code == 400:
                    ti.sleep(60 * 5)
                    doLike =s.post(urlLik)
            print(doLike)


    def comment(self,i_d):
        urlcom = f'https://www.instagram.com/web/comments/{i_d}/add/'

        data = {
                'comment_text':f'''{self.cmnt}''',
                'replied_to_comment_id':'' 
            }
                
        doComment =s.post(urlcom,data=data,verify=False)

        if doComment.status_code ==200:

            print('\b'+'Comment Done :'+str(self.contCom),end="\r")
            self.contCom+=1
          
        else:
            if doComment.status_code == 400:
                    ti.sleep(60 * 5)
                    doComment =s.post(urlcom)
                    if doComment.status_code ==200:
                            self.contCom+=1
            print(doComment)






'33715125622:zqGnWh73xvUhCF:12'
ses = input('Enter Sessionid : ')
time = int(input('Enter sleep (biggest then 38) : '))
com = input('Enter Comment : ')#
#ذا شفت الرسالة ذي رد بنقطه :>
app(ses,time,com)

'32288547846%3AjTj4GzMgmFARnh%3A25'