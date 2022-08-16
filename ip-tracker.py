import json                                           
from urllib import request

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
        print(f"\n \033[1;33;40m  IP\n \n \033[1;32;40m {data_json['query']}\n")     
        print(f"\n \033[1;33;40m Country\n \n \033[1;32;40m {data_json['country']}\n")
        print(f"\n \033[1;33;40m Region\n \n \033[1;32;40m {data_json['regionName']}\n") 
        print(f"\n \033[1;33;40m City\n \n \033[1;32;40m {data_json['city']}\n")
        print(f"\n \033[1;33;40m Latitude\n \n \033[1;32;40m {data_json['lat']}\n") 
        print(f"\n \033[1;33;40m Longitude\n \n \033[1;32;40m {data_json['lon']}\n")
        print(f"\n \033[1;33;40m ISP\n \n \033[1;32;40m {data_json['isp']}\n") 
        print(f"\n \033[1;33;40m Zip\n \n \033[1;32;40m {data_json['zip']}\n")
        print(f"\n \033[1;33;40m AS\n \n \033[1;32;40m {data_json['as']}\n")
else:
        print("\n \033[1;31;40m Failed to find the IP informations.\n")
