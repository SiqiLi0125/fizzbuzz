# import create-ticket

# def getnetworkdevicecount():


"""
This script prints out IOS config by deviceId:
User select a device from the list and script retrieve device ID according to user's selection
then calls - GET /network-device/{id}/config - to print out IOS configuration
"""
from apicem import * # APIC-EM IP is assigned in apicem_config.py

# Print out device list for user to select
device = []

    resp= get(api="network-device") # The response (result) from "GET /network-device" request
    status = resp.status_code
    response_json = resp.json() # Get the json-encoded content from response
    device = response_json["response"] # Network-device



device_list = []

i=0
for item in device:
    i+=1
    device_list.append([i,item["hostname"],item["managementIpAddress"],item["type"],item["instanceUuid"]])

print (tabulate(device_list, headers=['number','hostname','ip','type'],tablefmt="rst"),'\n')

print ("*** Please note that some devices may not be able to show configuration for various reasons. ***\n")


id = ""
device_id_idx = 4
while True:
    user_input = input('=> Select a number for the device from above to show IOS config: ')
    user_input= user_input.lstrip() # Ignore leading space
    if user_input.lower() == 'exit':
        sys.exit()
    if user_input.isdigit():
        if int(user_input) in range(1,len(device_list)+1):
            id = device_list[int(user_input)-1][device_id_idx]
            break
        else:
            print ("Oops! number is out of range, please try again or enter 'exit'")
    else:
        print ("Oops! input is not a digit, please try again or enter 'exit'")
# End of while loop

# Get IOS configuration API

try:
    response_json = resp.json()
    # Replace "\r\n" to "\n" to remove extra space line (Carriage Return)
    print (response_json["response"].replace("\r\n","\n\"))
