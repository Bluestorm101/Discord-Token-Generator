import tls_client,websocket,json,requests,random,binascii,base64,time,os,urllib,threading,colorama,httpx,time,pystyle,ctypes
import datetime as dt
from datetime import datetime
from colorama import Fore
from os.path import isfile, join



class console:

    def info(message):
        print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{dt.datetime.fromtimestamp(time.time()).strftime(f"%H{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%M{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%S")}{Fore.RESET}] [{Fore.CYAN}INFO{Fore.RESET}] {Fore.LIGHTMAGENTA_EX}{message}{Fore.RESET}')
    def solver(message):
        print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{dt.datetime.fromtimestamp(time.time()).strftime(f"%H{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%M{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%S")}{Fore.RESET}] [{Fore.LIGHTCYAN_EX}SOLVER{Fore.RESET}] {Fore.LIGHTWHITE_EX}{message}{Fore.RESET}')
    def websocket(message):
        print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{dt.datetime.fromtimestamp(time.time()).strftime(f"%H{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%M{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%S")}{Fore.RESET}] [{Fore.MAGENTA}WEBSOCKET{Fore.RESET}] {Fore.BLUE}{message}{Fore.RESET}')
    def error(message):
        print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{dt.datetime.fromtimestamp(time.time()).strftime(f"%H{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%M{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%S")}{Fore.RESET}] [{Fore.RED}ERROR{Fore.RESET}] {Fore.RESET}{message}{Fore.RESET}')
    def Unlocked(message):
        print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{dt.datetime.fromtimestamp(time.time()).strftime(f"%H{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%M{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%S")}{Fore.RESET}] [{Fore.LIGHTGREEN_EX}UNLOCKED{Fore.RESET}]{Fore.BLUE}{message}{Fore.RESET}')
    def locked(message):
        print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{dt.datetime.fromtimestamp(time.time()).strftime(f"%H{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%M{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%S")}{Fore.RESET}] [{Fore.RED}LOCKED{Fore.RESET}] {Fore.RED}{message}{Fore.RESET}')




class gen:
    def __init__(self):
        self.config = json.load(open('config.json', 'r', encoding='utf-8'))
        self.setting = self.config['config']
        self.threads = self.setting['threads']
        self.captchakey = self.setting['capsolverkey']
        self.kopechekka = self.setting['kopechekkakey']



    def gentoken(self):
        while True:
            useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
            session = tls_client.Session(client_identifier="chrome_110",random_tls_extension_order=True )
            chooseproxy = random.choice(open("proxies.txt", "r").read().splitlines())
            proxy = {
                'http':f"http://{chooseproxy}"
            }
            try:
                taskid = requests.post('https://api.capsolver.com/createTask' ,json={
                        "clientKey": f"{self.captchakey}",
                        "task": {
                            "type": "HCaptchaEnterpriseTask",
                            "websiteURL": "https://discord.com/",
                            "websiteKey": "4c672d35-0701-42b2-88c3-78380b0db560",
                            "proxy": f'http://{chooseproxy}',
                            "useragent": useragent
                        }})
                tid = taskid.json() ['taskId']
                data = {
                                        "clientKey": f"{self.captchakey}",
                                        "taskId": tid
                        }
                        
                
                while True:
                    get_result = requests.post(f"https://api.capsolver.com/getTaskResult", json=data)
                    process = get_result.json() ["status"]
                    if process == "processing":
                        continue
                    elif process == "ready":
                        answer = get_result.json() ["solution"]["gRecaptchaResponse"]
                        console.solver(f"Solved Captcha > {answer[:50]}")
                        break
            except:
                    console.error(f"Failed to Solve Captcha {taskid.json()} ")
                    continue
            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-SE",
                "Alt-Used": "discord.com",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "Host": "discord.com",
                "Origin": "https://discord.com",
                "Referer": "https://discord.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
                "User-Agent": useragent,
                "X-Track": " eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3NTU3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=="
            }
            cookies = session.get("https://discord.com/" ,headers=headers, proxy=proxy).cookies

            cfruid = cookies['__cfruid']
            dcfduid = str(binascii.b2a_hex(os.urandom(16)).decode('utf-8'))
            sdcfduid = str(binascii.b2a_hex(os.urandom(42)).decode('utf-8'))
            x = session.get("https://discord.com/register", proxy=proxy).text
            cfbm =  session.post("https://discord.com/cdn-cgi/bm/cv/result?req_id=" + x.split("r:'")[1].split("',s")[0], json={
                    "m": x.split(",m:'")[1].split("',s:")[0],
                    "results": [
                        str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
                        str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
                    ],
                    "timing": random.randint(40, 180),  # Execution time
                    "fp": {
                        "id": 3,
                        "e": {
                            "r": [
                                1920,  # Height
                                1080   # Width
                            ],
                            "ar": [
                                1054,  # availHeight
                                1920   # availWidth
                            ],
                            "pr": 1,   # Pixel Ratio
                            "cd": 24,     # Color Depth
                            "wb": False,  # Web-driver
                            "wp": False,  # PhantomCall
                            "wn": False,  # NightMare
                            "ch": True,   # Chrome
                            "ws": False,  # Selenium
                            "wd": False   # domAutomation
                        }
                    }
                }, proxy=proxy).cookies.get("__cf_bm") 
            
            timetoday = datetime.today().strftime("%a+%b+%d+%Y")
            clockatm = urllib.parse.quote(datetime.today().strftime("%H:%M:%S"))
            optanconsent = f"isIABGlobal=false&datestamp={timetoday}+{clockatm}+GMT%2B0200+(Central+European+Summer+Time)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0&AwaitingReconsent=false"
            x = session.get("https://discord.com/api/v9/experiments", proxy=proxy).json()
            fingerprint = x['fingerprint']
            headers = {
                'authority': 'discord.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'cookie': f'__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; __cfruid={cfruid}; OptanonConsent={optanconsent}; locale=en-US; __cf_bm={cfbm}',
                'origin': 'https://discord.com',
                'referer': 'https://discord.com/register',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'x-debug-options': 'bugReporterEnabled',
                'x-discord-locale': 'en-US',
                'x-fingerprint': f'{fingerprint}',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3NTU3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
            }
            username = random.choice(open("data/usernames.txt",encoding = "utf-8").read().splitlines())
            register = session.post("https://discord.com/api/v9/auth/register", json={
                "consent": True,
                "fingerprint": fingerprint,
                "username": username,
                "captcha_key": answer
                }, headers = headers, proxy=proxy)
            
            if register.status_code == 201:
                token  = register.json()['token']
                headers = {
                'authority': 'discord.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'cookie': f'__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; __cfruid={cfruid}; OptanonConsent={optanconsent}; locale=en-US; __cf_bm={cfbm}',
                'authorization': token,
                'origin': 'https://discord.com',
                'referer': 'https://discord.com/@me',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'x-debug-options': 'bugReporterEnabled',
                'x-discord-locale': 'en-US',
                'x-fingerprint': f'{fingerprint}',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3NTU3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
            }
                r = session.get("https://discord.com/api/v9/users/@me/settings", headers=headers,proxy=proxy)
                if r.status_code == 200:
                        console.Unlocked(message=token)
                        try:
                            proxytest = f"http://{chooseproxy}"
                            proxyweb = str(proxytest.split("http://")[1]).split("@")
                            username, password, host, port = proxyweb[0].split(":")[0], proxyweb[0].split(":")[1], proxyweb[1].split(":")[0], proxyweb[1].split(":")[1]

                            ws = websocket.WebSocket()
                            ws.connect('wss://gateway.discord.gg/?v=6&encoding=json',
                                http_proxy_host=host,
                                http_proxy_port=str(port),
                                proxy_type="http",
                                http_proxy_auth=(
                                    username,
                                    password
                                )
                            )

                            hello = json.loads(ws.recv())

                            versionb = useragent.split("Chrome/")[1].split(" ")[0]

                            auth = {
                                "op": 2,
                                "d": {
                                    "token": token,
                                    "capabilities": 125,
                                    "properties":{
                                        "os":"Windows",
                                        "browser":"Chrome",
                                        "device":"",
                                        "system_locale":"en-SE",
                                        "browser_user_agent":useragent,
                                        "browser_version":versionb,
                                        "os_version":"10",
                                        "referrer":"",
                                        "referring_domain":"",
                                        "referrer_current":"",
                                        "referring_domain_current":"",
                                        "release_channel":"stable",
                                        "client_build_number":"175627",
                                        "client_event_source":None
                                    },
                                    "presence": {
                                        "status": "online",
                                        "since": 0,
                                        "activities": [
                                            {
                                            "name": "Custom Status",
                                            "type": 4,
                                            "state": "cool",
                                            "emoji": None
                                            }
                                        ],
                                        "afk": False
                                    },
                                    "compress": False,
                                    "client_state": {
                                        "guild_hashes": {},
                                        "highest_last_message_id": "0",
                                        "read_state_version": 0,
                                        "user_guild_settings_version": -1,
                                        "user_settings_version": -1
                                    }
                                }
                            }

                            ws.send(json.dumps(auth))
        

                        except Exception as e:
                            print(str(e))
                        
                        console.websocket(message="OPEN")
                        birth = f"{str(random.randint(1985,2005))}-{str(random.randint(1,12)).zfill(2)}-{str(random.randint(1,23)).zfill(2)}"

                        addbirth = session.patch("https://discord.com/api/v9/users/@me",json= {"date_of_birth": birth},headers=headers,proxy=proxy)
                        if addbirth.status_code == 200:
                                console.info("Added Birth")
                        else:
                                console.error("Failed to Add Birth")
                        picture = [f for f in os.listdir("data/avatars/") if isfile(join("data/avatars/", f))]
                        random_picture = random.choice(picture)

                        with open(f'data/avatars/{random_picture}', "rb") as image_file:
                                encoded_string = base64.b64encode(image_file.read())
                            
                        addpfp = session.patch('https://discord.com/api/v9/users/@me',headers=headers,json = {'avatar': f"data:image/png;base64,{(encoded_string.decode('utf-8'))}",},proxy=proxy)
                                
                        if addpfp.status_code == 200:
                            console.info("Added PFP")
                        else:
                            console.error("Failed to Add Pfp")
                                    
                        banner_color = random.randrange(0, 16**6)

                        addbio = session.patch("https://discord.com/api/v9/users/%40me/profile",json= { "bio": random.choice(open("data/bios.txt","r", encoding="utf8").read().splitlines()),"accent_color": banner_color},headers=headers, proxy=proxy)

                        if addbio.status_code == 200:
                            console.info("Added Bio")
            

                        else:
                            console.error("Failed to Add BIO")
                        houseid = random.randint(1,3)

                        hypesquad = session.post("https://discord.com/api/v9/hypesquad/online",json= {"house_id": houseid},headers=headers,proxy=proxy)

                        if hypesquad.status_code == 204:
                            console.info("Joined a Hype Squad")
                        else:
                            console.error("Failed to Join a Hype Squad")
                        devmode = session.patch("https://discord.com/api/v9/users/@me/settings-proto/1", json = {"settings": "YhYKBwoFZW4tVVMSCwiI//////////8BagIQAQ=="},headers=headers,proxy=proxy)
                        if devmode.status_code == 200:
                            console.info("Enabeled Dev mode")
                        else:
                            console.error("Failed to Enable Dev Mode")
                        
                        buy = requests.get(f'https://api.kopeechka.store/mailbox-get-email?api=2.0&spa=1&site=discord.com&sender=discord&regex=&mail_type=outlook.com&token={self.kopechekka}') 
                        status = buy.json()['status']      
                        if status == 'OK':
                            id = buy.json() ['id']
                            email = buy.json()['mail']
                            stuff = "ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghijklmnopqrstuvwxyz0123456789"
                            password = ''.join((random.choice(stuff) for i in range(12)))
                                    #console.info(f"Email:{email} Password:{password}")
                        else:
                            print(buy.json())
                        
                        claim = session.patch("https://discord.com/api/v9/users/@me",json = {"email": email,"password": password}, headers=headers,proxy=proxy)
                        if claim.status_code == 200:
                                new_token = claim.json()['token']
                                console.info(f"{Fore.LIGHTBLUE_EX}Email: {Fore.LIGHTWHITE_EX}{email}{Fore.LIGHTBLUE_EX} Password: {Fore.LIGHTWHITE_EX}{password}")
                                console.info(f"Claimed account > {Fore.LIGHTWHITE_EX} {new_token}")
                        else:
                            console.error("Failed to claim token")
                        while True:
                                x =  requests.get(f'http://api.kopeechka.store/mailbox-get-message?full=0&id={id}&token={self.kopechekka}&type=json')
                                value = x.json() ['value']
                                if value == "WAIT_LINK":
                                    continue
                                elif value != "WAIT_LINK":
                                    link = x.json()['value']
                                    email_url = httpx.get(link, follow_redirects=True).url
                                    x,emailtoken = str(email_url).split("https://discord.com/verify#token=",1)
                                    verify = session.post("https://discord.com/api/v9/auth/verify",json = {"captcha_key": None,"token": emailtoken}, headers = headers, proxy=proxy)
                                    if verify.status_code == 200:
                                        console.info("Verified Email")
                                        with open("data/tokens.txt", "a", encoding="utf-8") as file:
                                            file.write(f"{email}:{password}:{new_token}\n")
                                    else:
                                        console.info(f"failed to verify > {verify.json()}")
                                    break
                                else:
                                    print("error")

                elif r.status_code == 403:
                        console.locked(f"{token}")


                     
            elif register == 429:
                print("ratelimited by discord")
            else:
                 print(register.json())




  
    def start(self):
        while threading.active_count() < self.threads['threads'] + 1:
            threading.Thread(target=self.gentoken).start()
     

if __name__ == '__main__':
    token = gen()
    token.start()



                    