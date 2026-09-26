from RegisterRewards import SteamDeckRegister
from urllib.parse import unquote

def formatToken(steamLoginSecure):
    decoded = unquote(steamLoginSecure)

    steam_id, access_token = decoded.split("||", 1)
    return steam_id, access_token

def run():
    SDR = SteamDeckRegister()

    print(
        "* How to use\n",
        "* - Login to steam\n",
        "* -- Enter Your Serial Code from Steam Deck\n",
        "* --- Enter Your Controller Code from Steam Deck\n",
        "* ---- Result\n",
    )
        
    Username = input('* Username: ')
    Password = input('* Password: ')

    session = SDR.SteamLogin(username=Username, password=Password)
    
    steam_login_secure = session.cookies.get("steamLoginSecure")
    steam_id, access_token = formatToken(steam_login_secure)

    print(f'\n* Applying to [{steam_id}]')

    Serial  = input('* Device Serial Code: ')
    CCode   = input('* Controller Code: ')

    SDR.RegisterForSteamDeckRewards(serial_id=Serial, controller_code=CCode, access_token=access_token)

run()
