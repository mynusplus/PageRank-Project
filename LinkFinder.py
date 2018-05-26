import os
from bs4 import BeautifulSoup as BS


def findLinks():
    # This code assumes that all html pages it will be evaluating are in this directory.
    location = r'\\southw-sfps-01.business.mpls.k12.mn.us\Students_A-L\tlin2001\Desktop\PageRank_Pages'

    # Finds the names of the html pages in the location folder, stores in htmlPageNames.
    htmlPageNames = []
    for file in os.listdir(location):
        if file.endswith('.html'):
            htmlPageNames.append(file)

    # Finds the paths to the html pages, stores in htmlPagePaths.
    htmlPagePaths = []
    for name in htmlPageNames:
        htmlPagePaths.append(os.path.join(location, name))

    # Uses Beautiful Soup 4 to look through the pages and find what values their elements with href have, aka what pages
    # they have outgoing links to. Stores in links dictionary.
    links = {}
    assert(len(htmlPageNames) == len(htmlPagePaths))
    for item in range(len(htmlPageNames)):
        name = htmlPageNames[item]
        file = htmlPagePaths[item]
        links[name] = []
        page = open(file, 'r')
        data = page.read()
        page.close()
        soup = BS(data, "html.parser")
        hrefTags = soup.find_all(href=True)
        for thing in hrefTags:
            
            links[name].append(thing['href'])

    # Changes outgoing links into numbers so that the PageRank algorithm can use them as a matrix.
    linkNums = {}
    for key in links:
        linkNums[htmlPageNames.index(key)] = []
        for item in links[key]:
            linkNums[htmlPageNames.index(key)].append(htmlPageNames.index(item))

    return linkNums
