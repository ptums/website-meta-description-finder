# import libraries
import sys

# site name
sitename = sys.argv[1];

# iterate over site DOM and find meta descriptions
def findmeta(site, flag):
    # request library
    import urllib.request
    # python scrape library
    from bs4 import BeautifulSoup

    # iterate over DOM elements found after scraping
    with urllib.request.urlopen(site) as response:
        # read html
        html = response.read()
        soup3 = BeautifulSoup(html, "html.parser");

        # storing meta description and title information
        title = soup3.find("title").get_text()
        descog = soup3.find("meta", property="og:description")
        descname = soup3.find("meta", attrs={'name':'description'})

        #  determine if meta description is open graph or standard
        if(descog):
            print(flag + "\n")
            print (title + "\n" + descog["content"])
        elif(descname):
            print(flag + "\n")
            print (title + "\n" + descname["content"])
        else:
            print ("No meta description found.")



# launch findmeta()
def main():
    # iterate over urls from the user
    for links in sys.argv[2:]:
        findmeta(links, sitename)

if __name__ == "__main__": main()
