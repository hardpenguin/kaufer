from collections import OrderedDict

search_links = OrderedDict([
    ("itch.io", "https://itch.io/search?q={{ query }}"),
    ("GOG.com", "https://www.gog.com/games?search={{ query }}"),
    ("Humble Store","https://www.humblebundle.com/store/search?search={{ query }}"),
    ("Steam", "https://store.steampowered.com/search/?term={{ query }}"),
    ("Google Play", "https://play.google.com/store/search?q={{ query }}&c=apps"),
    ("Discord", "https://discordapp.com/store/browse?q={{ query }}"),
    ("Kartridge", "https://www.kartridge.com/search/{{ query }}"),
    ("iTunes", "https://www.google.com/search?q=site%3Aitunes.apple.com+{{ query }}"),
    ])
# you can comment out the stores you don't want to query