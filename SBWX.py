import os
f = open("SBWX.txt", "a")
f.write("""
یا ارزش پوزش این ابزار به طور کامل از دسترس خارج شده و کار نمیکند برای اطلاع از نسخه های جدید و یا نسخه های بهینه شده
به تلگرام ما بپیوندید t.me/SaDWX_CH_TM
برای ارتباط با من  t.me/SaDWX_Nope

اگر نمیتوانید در تلگرام با ما در ارتباط باشید
ایمیل ما 
www.sadwx01@gmail.com """)
f.close()
while True:
  os.system("xdg-open SBWX.txt")
  print("pls open SBWX.txt")
p=input("open gmail?for speak with me? (y)")
if p=="y" or p=="Y":
  os.system("xdg-open www.sadwx01@gmail.com")
else:
  print("pls enter Y or y")
  os.system("python3 SBWX.py")
