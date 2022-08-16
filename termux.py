print("\n\033[1;33;40m MYANMAR IP-TRACKER\n")
print("\n \033[1;33;40m  ██████   ██████ █████ █████   █████████   ██████   █████ ██████   ██████   █████████   ███████████\n")
print("\n \033[1;33;40m ░░██████ ██████ ░░███ ░░███   ███░░░░░███ ░░██████ ░░███ ░░██████ ██████   ███░░░░░███ ░░███░░░░░███\n")
print("\n \033[1;33;40m  ░███░█████░███  ░░███ ███   ░███    ░███  ░███░███ ░███  ░███░█████░███  ░███    ░███  ░███    ░███\n")
print("\n \033[1;32;40m  ░███░░███ ░███   ░░█████    ░███████████  ░███░░███░███  ░███░░███ ░███  ░███████████  ░██████████\n")
print("\n \033[1;32;40m  ░███ ░░░  ░███    ░░███     ░███░░░░░███  ░███ ░░██████  ░███ ░░░  ░███  ░███░░░░░███  ░███░░░░░███\n")
print("\n \033[1;31;40m  ░███      ░███     ░███     ░███    ░███  ░███  ░░█████  ░███      ░███  ░███    ░███  ░███    ░███\n")
print("\n \033[1;31;40m  █████     █████    █████    █████   █████ █████  ░░█████ █████     █████ █████   █████ █████   █████\n")
print("\n \033[1;31;40m ░░░░░     ░░░░░    ░░░░░    ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░     ░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░░\n")

print("\n \033[1;33;40m IP-TRACK\n")
url = "http://ip-api.com/json/"
ip = input("Input the IP Address : ")
print("\n \033[1;33;40m Please wait....\n")
request = request.urlopen(url + ip)
data_json = json.loads(request.read())

if data_json['status'] == "success":
        print(f"IP : {data_json['query']}")
        print(f"Country : {data_json['country']}")
        print(f"Region : {data_json['regionName']}")
        print(f"City : {data_json['city']}")
        print(f"Latitude : {data_json['lat']}")
        print(f"Longitude : {data_json['lon']}")
        print(f"ISP : {data_json['isp']}")
        print(f"Zip : {data_json['zip']}")
        print(f"AS : {data_json['as']}")
else:
        print("Failed to find the IP informations.")
