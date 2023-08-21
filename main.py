print("""
▄▄▄▄·  ▄▄▄·  ▐ ▄ ·▄▄▄▄       ▐ ▄  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .     ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
▐█ ▀█▪▐█ ▀█ •█▌▐███▪ ██     •█▌▐█▐█ ▀█ ·██ ▐███▪▀▄.▀·    ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
▐█▀▀█▄▄█▀▀█ ▐█▐▐▌▐█· ▐█▌    ▐█▐▐▌▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
██▄▪▐█▐█ ▪▐▌██▐█▌██. ██     ██▐█▌▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌    ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
·▀▀▀▀  ▀  ▀ ▀▀ █▪▀▀▀▀▀•     ▀▀ █▪ ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀     ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
""")

user_name = input("Please enter your name : ")

print(f"\nWelcome to The Band Name Generator, {user_name}.\nWe see you're here because you're having difficulty"
      " selecting a name for your music band.\n\nWell, worry no more! The Band Name Generator is here to"
      " help you.")

city_name = input("\nWhat's the name of the city you grew up in? : ")

pet_name = input("\nWhat's the name of your pet you have or had? : ")

print(f"""
----------------------------------------------------
Your band name could be: {city_name} {pet_name}
----------------------------------------------------""")
