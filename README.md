# Read Under Images!

<img width="714" height="239" alt="image" src="https://github.com/user-attachments/assets/4f85b064-a658-4ffb-808b-5e2f33dd7c85" />


<img width="1148" height="819" alt="image" src="https://github.com/user-attachments/assets/38fa7445-b504-4d30-859d-9773a5eb20ed" />

# Steam Deck Rewards CLI

A simple Python command-line utility to register and claim Steam Deck profile rewards directly through the Steam API using `ILoyaltyRewardsService#RegisterForSteamDeckRewards`.

Built using [`steamcommunitykit`](https://github.com/steamcommunitykit) for Steam authentication and authenticated Steam Community sessions.

## Prerequisites

- Python 3.8+
- A Steam account
- A Steam Deck eligible for profile rewards
- The Steam Deck serial number
- The Steam Deck controller code

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Steam-Deck-Rewards-CLI.git
cd Steam-Deck-Rewards-CLI
```

Install the required dependencies:

```bash
pip install requests steamcommunitykit
```

Alternatively:

```bash
python -m pip install requests steamcommunitykit
```

## Usage

Run the CLI:

```bash
python Demo.py
```

You will be prompted for your Steam account credentials:

```text
* Username:
* Password:
```

After successfully authenticating:

```text
* Logged into example_account

* Applying to [7656119XXXXXXXXXX]
```

Enter your Steam Deck information:

```text
* Device Serial Code:
* Controller Code:
```

Example:

```text
* How to use
 * - Login to steam
 * -- Enter Your Serial Code from Steam Deck
 * --- Enter Your Controller Code from Steam Deck
 * ---- Result

* Username: example_account
* Password: ********

* Logged into example_account

* Applying to [7656119XXXXXXXXXX]

* Device Serial Code: XXXXXXXXXXXXX
* Controller Code: XXXXXXXXX

* Register | Success
```

## How It Works

### 1. Steam Login

The program authenticates using `SteamClient` from `steamcommunitykit`:

```python
self.client.login_to_community(username, password)
```

An authenticated Steam Community session is then created:

```python
session = self.client.build_community_requests_session()
```

### 2. Authentication Token

The authenticated session contains the `steamLoginSecure` cookie:

```python
steam_login_secure = session.cookies.get("steamLoginSecure")
```

The value is URL-decoded and separated into the SteamID64 and access token:

```python
decoded = unquote(steamLoginSecure)

steam_id, access_token = decoded.split("||", 1)
```

The access token is then used to authenticate the Steam Web API request.

### 3. Steam Deck Rewards Request

The CLI submits a request to:

```text
https://api.steampowered.com/ILoyaltyRewardsService/RegisterForSteamDeckRewards/v1/
```

with:

```text
access_token
serial_number
controller_code
```

The request:

```python
requests.post(
    "https://api.steampowered.com/ILoyaltyRewardsService/RegisterForSteamDeckRewards/v1/",
    params={
        "access_token": access_token,
        "serial_number": serial_id,
        "controller_code": controller_code
    }
)
```

## Project Structure

```text
Steam-Deck-Rewards-CLI/
│
├── RegisterRewards.py
├── Demo.py
└── README.md
```

### `RegisterRewards.py`

Contains the `SteamDeckRegister` class for Steam authentication and sending the Steam Deck rewards request.

### `Demo.py`

Provides the CLI and passes the account and device information to `SteamDeckRegister`.

## Important Notes

- Only use this tool with Steam accounts and Steam Deck devices that you own or are authorized to use.
- A Steam Deck must be eligible for the relevant rewards.
- Steam may reject a registration if the device or rewards have already been registered.
- Steam API behavior may change without notice.
- Excessive requests may result in temporary rate limiting.
- This project is not affiliated with, endorsed by, or supported by Valve Corporation.

## Disclaimer

This is an unofficial Steam utility and is not affiliated with Valve Corporation. Use it at your own risk.
