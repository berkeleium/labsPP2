import json

with open("labka 4\json\sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("DN", " " * 47, "Description", " " * 9, "Speed", "  ", "MTU")
print("-" * 50, "-" * 20, "", "-" * 6, "", "-" * 6)
for item in data["imdata"]:
    temp = item["l1PhysIf"]["attributes"]
    dn = temp["dn"]
    descr = temp["descr"]
    sp = temp["speed"]
    mtu = temp["mtu"]
    print(dn, "\t\t", descr, "\t\t", sp, "", mtu)