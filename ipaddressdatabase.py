
DNS_dictionary = {}


def create():

    providers = ["Level3", "Verisign", "Google", "Quad9", "DNS.WATCH",
                 "Comodo Secure DNS", "OpenDNS Home", "Norton ConnectSafe",
                 "GreenTeamDNS", "SafeDNS", "OpenNIC", "SmartViper", "Dyn",
                 "FreeDNS", "Alternate DNS", "Yandex.DNS", "UncensoredDNS",
                 "Hurricane Electric", "puntCAT", "Neustar", "Cloudflare",
                 "Fourth Estate"]

    ips = ["209.244.0.3", "64.6.64.6", "8.8.8.8", "9.9.9.9", "84.200.69.80",
           "8.26.56.26", "208.67.222.222", "199.85.126.10", "81.218.119.11",
           "195.46.39.39", "69.195.152.204", "208.76.50.50", "216.146.35.35",
           "37.235.1.174", "198.101.242.72", "77.88.8.8", "91.239.100.100",
           "74.82.42.42", "109.69.8.51", "156.154.70.1", "1.1.1.1", "45.77.165.194"]

    # create database dictionary and match
    global DNS_dictionary

    for provider in (providers):
        data = dict(zip(providers, ips))
        # print(data)

        for company in data.keys():

            print(company + " => " + data[company])

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


def printingSpecificValues(key):

    dictionary = DNS_dictionary

    for value in dictionary.values():
        # Print out the current value and let the user know it is a SSN
        if key == "Hurricane Electric":

            print("This company's ip is: " + dictionary["Hurricane Electric"])
        break


printingSpecificValues("Hurricane Electric")
