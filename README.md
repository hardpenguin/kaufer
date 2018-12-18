## Description

**Käufer** is a tool for triggering web browser searches for games availability in the most popular digital distribution stores.

The idea of creating it came to me as I realized that less popular stores do not have any kind of useful web API that could be used for querying their offer. Therefore, it is significantly easier to just trigger a regular search in web browser.

Käufer is written in Python 3 and currently Linux-only compatible.

Supported stores:
- itch.io
- GOG.com
- Humble Store
- Steam
- Google Play
- Discord
- Kartridge
- iTunes (App Store) via Google Search

## Usage
	./kaufer.py "Fallout 3"
	./kaufer.py "Minit"

## Todo

- some nice GUI
- support for Windows and macOS
- platform filtering
- feature filtering