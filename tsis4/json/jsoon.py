import json
with open("sample-data.json", "r") as read_file:
    data = json.load(read_file)
print(data)
print("""Interface Status
================================================================================""")
print("""DN                                                 Description           Speed    MTU """)
print("""-------------------------------------------------- --------------------  ------  ------""")
z = 0
while(z < 18):
    for i, k in data["imdata"][z]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            if z < 13 and z > 3:
                print(k, end="                               ")
            else:
                print(k, end="                              ")
        if i == "mtu":
            p = k
        if i == "speed":
            print(k," ", p)
    z += 1
