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

            if status_code == 200:
                if '{"response":{}}' in body:
                    print("* Register | False")
                    
                else:
                    print("* Register | Success")

            elif status_code == 429:
                print("* Too many requests, Try again later")

            else:
                print("* Unknown error")

            print(f"\n* Response: {body}")

        except Exception as Error:
            print(f"* Unknown Error | {Error}")
