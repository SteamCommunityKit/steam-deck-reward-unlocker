import requests
from steamcommunitykit import SteamClient

class SteamDeckRegister:
    def __init__(self):
        self.client = SteamClient()

    def SteamLogin(self, username, password):
        self.client.login_to_community(username, password)
        session = self.client.build_community_requests_session()
        print(f"* Logged into {username}")
        return session

    def RegisterForSteamDeckRewards(self, serial_id, controller_code, access_token):
        try:
            response = requests.post(
                "https://api.steampowered.com/ILoyaltyRewardsService/RegisterForSteamDeckRewards/v1/",
                params={
                    "access_token": access_token,
                    "serial_number": serial_id,
                    "controller_code": controller_code
                }
            )

            status_code = response.status_code
            body = response.text
            
            try:
                data = response.json()
            except ValueError:
                data = {}

            if status_code == 200:
                if data.get("response", {}).get("granted_profile_modifier") == True:
                    print("* Register | Success")
                    print(f"\n* Response: {body}")
                    return True
                else:
                    print("* Register | False")
                    print(f"\n* Response: {body}")
                    return False

            elif status_code == 429:
                print("* Too many requests, Try again later")
                print(f"\n* Response: {body}")
                return False

            else:
                print(f"* Unknown error | Status: {status_code}")
                print(f"\n* Response: {body}")
                return False

        except Exception as Error:
            print(f"* Unknown Error | {Error}")
            return False
