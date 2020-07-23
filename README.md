## Description

**Käufer** is a tool for triggering web browser searches for games availability in the most popular digital distribution stores.

The idea of creating it came to me as I realized that less popular stores do not have any kind of useful web API that could be used for querying their offer. Therefore, it is significantly easier to just trigger a regular search in web browser.

Käufer is written in Python 3 and currently Linux-only compatible.

Some of the supported stores include:

- itch.io
- GOG.com
- Humble Store
- Steam
- Google Play
- Kartridge
- iTunes (App Store) via Google Search
- Epic Games Store
- Origin (EA)
- Ubisoft Store (UPlay)
- Nintendo Switch
- PlayStation Store
- Microsoft Store (Xbox One and Windows 10)
- Bethesda.net

## Dependencies

- Python 3
- PyQt5

They can be installed on Debian/Ubuntu by running:

    sudo apt-get install python3 python3-pyqt5

## Usage

Start the GUI
    
    ./gui.py

or in the CLI

    ./kaufer.py "Fallout 3"
    ./kaufer.py "Minit"

## Screenshot
![Screenshot of Käufer window](https://github.com/hardpenguin/kaufer/raw/master/screenshot.png)

## Todo

- support for Windows and macOS
- platform and feature filtering (?)