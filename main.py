import requests

print("=" * 40)
print("      GitHub Public API Caller")
print("=" * 40)

url = "https://api.github.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\nAPI Connected Successfully!\n")

        print("Current User URL:")
        print(data["current_user_url"])

        print("\nRepository URL:")
        print(data["repository_url"])

        print("\nRate Limit URL:")
        print(data["rate_limit_url"])

    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request Failed!")
    print(e)