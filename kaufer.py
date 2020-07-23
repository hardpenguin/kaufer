import os

class Kaufer(object):

    def Search(query, search_links):
        print("Searching on:")
        for store, link in search_links.items():
            print("%s" % store, end=" | ")
            l = link.replace("{{ query }}", query)
            os.system("xdg-open \"%s\" " % l)
        print("")