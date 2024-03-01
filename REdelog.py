import requests
import time

# Credentials
username = "yourusername"
password = "yourpassword"

# Dictionary mapping character IDs to classes
character_ids = {
    784: "Priest",
    782: "Wizard",
    # List of character IDs:
    # 768: "Rogue",
    # 775: "Archer",
    # 782: "Wizard",
    # 784: "Priest",
    # 785: "Samurai",
    # 796: "Bard",
    # 797: "Warrior",
    # 798: "Knight",
    # 799: "Paladin",
    # 800: "Assassin",
    # 801: "Necromancer",
    # 802: "Huntress",
    # 803: "Mystic",
    # 804: "Trickster",
    # 805: "Sorcerer",
    # 806: "Ninja",
    # 817: "Summoner",
    # 818: "Kensei",
}

def login():
    # Login to Realmeye
    url = "https://www.realmeye.com/login"
    payload = f"password={password}&username={username}&bindToIp=f"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    # Extract the value of the "Set-Cookie" header
    set_cookie = response.headers.get('Set-Cookie')

    # If "Set-Cookie" header exists, return the session cookie
    if set_cookie:
        print(f"Logged in as {username}")
        print(f"Session Cookie: {set_cookie}")
        return set_cookie.split(";")[0].split("=")[1]
    else:
        print("Set-Cookie header not found in response.")
        return None

def delete_characters(session_cookie):
    # Remove characters with specified IDs
    for character_id, character_class in character_ids.items():
        # Create the payload and headers
        url = "https://www.realmeye.com/dead-character"
        payload = f"class={character_id}&session=" + session_cookie
        headers = {
            "cookie": f"session={session_cookie}",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }

        # Send the delete request
        response = requests.request("POST", url, data=payload, headers=headers)

        # Output character removal message
        print(f"{character_class} ({character_id}) has been removed from your RealmEye")

def logout(session_cookie):
    # Logout from Realmeye
    url = "https://www.realmeye.com/logout"
    payload = f"session={session_cookie}"
    headers = {
        "cookie": f"session={session_cookie}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    response = requests.post(url, data=payload, headers=headers)

    # Output logout message
    print(f"Logged out as {username}")

if __name__ == "__main__":
    while True:
        # Login to Realmeye and get the session cookie
        session_cookie = login()

        if session_cookie:
            # Delete characters every minute for an hour
            for _ in range(60):  # 60 iterations (how many times to loop). currently set at every hour
                delete_characters(session_cookie)
                time.sleep(60)  # Sleep for 60 seconds

            # Logout of Realmeye
            logout(session_cookie)
