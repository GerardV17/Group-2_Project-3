import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "pYfLTQP5KzKmegx03IaUQPbMPTnGnZcy"

while True:
 orig = input("Starting Location: ")
 if orig == "quit" or orig == "q":
    break
 dest = input("Destination: ")
 if dest == "quit" or dest == "q":
    break
 url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
 print("URL: " + (url))
 
 json_data = requests.get(url).json()
 json_status = json_data["info"]["statuscode"]
 
 if json_status == 0:
    print("\033[1;32mAPI Status: " + str(json_status) + " = A successful route call.\n\033[0m")
    print("=============================================")
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration: " + "\033[1;31m" + (json_data["route"]["formattedTime"] + "\033[0m"))
    print("Kilometers: " + "\033[1;31m" +
    str("{:.2f}".format((json_data["route"]["distance"])*1.61) + "\033[0m"))
    print("Fuel Used (Ltr): " + "\033[1;31m" +
    str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78) + "\033[0m"))
    print("=============================================\n")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print(("\033[0;34m" + each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)\033[0m"))
        print("=============================================\n")
    
 elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
 elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
 else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
