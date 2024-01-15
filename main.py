import tls_client, string, random, colorama, threading
session = tls_client.Session(
                    client_identifier="okhttp4_android_9",
                    random_tls_extension_order=True
                )
def check() -> None:
    try:
        username = "".join(random.choices(string.ascii_letters + string.digits, k=4))
        proxy = random.choice(open('proxies.txt', 'r').read().splitlines())
        json_data = {
            'username': username,
        }

        session = nigga.post(
            'https://discord.com/api/v9/unique-username/username-attempt-unauthed',
            json=json_data,
            proxy=f"http://{proxy}"
        )
        if response.json()['taken'] == False:
            with open("usernames.txt", "a+") as f:
                f.write(username + "\n")
            print(f"{colorama.Fore.GREEN}Free:{colorama.Fore.RESET} {username}")
        else:
            print(f"{colorama.Fore.RED}Taken:{colorama.Fore.RESET} {username}")
    except Exception as e:
        pass
for i in range(100):
    threading.Thread(target=check).start()
