
DNS_dictionary = {}
newValues = {}
ips = ["209.244.0.3", "64.6.64.6", "8.8.8.8", "9.9.9.9", "84.200.69.80",
       "8.26.56.26", "208.67.222.222", "199.85.126.10", "81.218.119.11",
       "195.46.39.39", "69.195.152.204", "208.76.50.50", "216.146.35.35",
       "37.235.1.174", "198.101.242.72", "77.88.8.8", "91.239.100.100",
       "74.82.42.42", "109.69.8.51", "156.154.70.1", "1.1.1.1", "45.77.165.194"]


providers = ["Level3", "Verisign", "Google", "Quad9", "DNS.WATCH",
             "Comodo Secure DNS", "OpenDNS Home", "Norton ConnectSafe",
             "GreenTeamDNS", "SafeDNS", "OpenNIC", "SmartViper", "Dyn",
             "FreeDNS", "Alternate DNS", "Yandex.DNS", "UncensoredDNS",
             "Hurricane Electric", "puntCAT", "Neustar", "Cloudflare",
             "Fourth Estate"]


# create and print dictionary and its data


def create():

    # create database dictionary and match
    global DNS_dictionary

    for provider in (providers):
        data = dict(zip(providers, ips))
        # print(data)

        for company in data.keys():

            company + " : " + data[company]

        # Creating separation between each new item prompt
        DNS_dictionary = data

        break

    # print(DNS_dictionary.keys())
    # print(DNS_dictionary.values())
    # print(DNS_dictionary.items())


create()


print(DNS_dictionary)
# print(DNS_dictionary.keys())
# print(DNS_dictionary.values())
# print(DNS_dictionary.items())


# printing a key value pair by specifics
def printingSpecificValues(key):

    dictionary = DNS_dictionary

    for value in dictionary.values():
        # Print out the current value and let the user know it is a SSN
        if key == key:
            print("This company's ip is: " + dictionary[key])
        break


printingSpecificValues("Hurricane Electric")

# making associated dictionary


def associatedDictionaries():
    associatedDictionary = DNS_dictionary
    provider_names = associatedDictionary.keys()
    primary_servers = associatedDictionary.values()
    print(provider_names)
    print(primary_servers)

    for provider, server in associatedDictionary.items():

        print("Name: " + provider + " || IP: " + server)


associatedDictionaries()


# adding providers

def addingProviders():
    d = DNS_dictionary
    len(d)
    print("There are exactly " + str(len(d.keys())) + " providers.")


addingProviders()


# bonus 1 adding values to keys
# step one make new dict

# step two : pass into global dict


def update(existingKey, passedIP):
    c = DNS_dictionary
    global ips
    global providers
    y = [passedIP]
    z = []
    o = [y] + [z]
    count = 0

    for p in providers:
        if p == existingKey:
            z.append((c[p]))
            ips.append(passedIP)
            for x in ips:
                if x == passedIP:
                    print(passedIP)
                    print(existingKey)
                    c[p] = o
                    count += 1
                    print("true")
                    print(c)
                    c = DNS_dictionary

            break


update("Level3", "209.244.0.4")
update("Verisign", "64.6.65.6")
print(DNS_dictionary)


def addNewValues(key, newValue):

    a = newValues
    key = "Level3"
    a.setdefault(key, [])
    a[key].append(newValue)

    print(a)
    a = newValues


addNewValues("Level3", "209.244.0.4")
