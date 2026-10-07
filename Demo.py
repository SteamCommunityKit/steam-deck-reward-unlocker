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
    
    if not steam_login_secure:
        print("* Login failed or could not retrieve steamLoginSecure cookie.")
        return
        
    steam_id, access_token = formatToken(steam_login_secure)

    print(f'\n* Applying to [{steam_id}]')

    max_attempts = 5
    
    for attempt in range(1, max_attempts + 1):
        print(f"\n--- Attempt {attempt} of {max_attempts} ---")
        Serial  = input('* Device Serial Code: ')
        CCode   = input('* Controller Code: ')


        is_success = SDR.RegisterForSteamDeckRewards(serial_id=Serial, controller_code=CCode, access_token=access_token)
        
        if is_success:
            print("* Rewards registered successfully! Exiting.")
            break 
        else:
            tries_remaining = max_attempts - attempt
            if tries_remaining > 0:
                print(f"* Registration failed. You have {tries_remaining} tries remaining on this login.")
            else:
                print("* Maximum attempts reached. Exiting.")

if __name__ == "__main__":
    run()
