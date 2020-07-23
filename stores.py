from collections import OrderedDict

search_links = OrderedDict([
    ("itch.io", "https://itch.io/search?q={{ query }}"),
    ("GOG.com", "https://www.gog.com/games?search={{ query }}"),
    ("Humble Store","https://www.humblebundle.com/store/search?search={{ query }}"),
    ("Steam", "https://store.steampowered.com/search/?term={{ query }}"),
    ("Google Play", "https://play.google.com/store/search?q={{ query }}&c=apps"),
    ("Kartridge", "https://www.kartridge.com/search/{{ query }}"),
    ("iTunes", "https://www.google.com/search?q=site%3Aitunes.apple.com+{{ query }}"),
    ("Epic Games Store", "https://www.epicgames.com/store/browse?q={{ query }}"),
    ("Origin", "https://www.origin.com/search?searchString={{ query }}"),
    ("Ubisoft Store", "https://store.ubi.com/search?q={{ query }}"),
    ("Nintendo Switch", "https://www.nintendo.com/search/#category=game&query={{ query }}"),
    ("PlayStation Store", "https://store.playstation.com/en-us/grid/search-game/1?query={{ query }}"),
    ("Microsoft Store", "https://www.microsoft.com/en-us/search/shop/games?q={{ query }}"),
    ("Bethesda.net", "https://bethesda.net/search?q={{ query }}&scope=games")
    ])
# you can comment out the stores you don't want to query