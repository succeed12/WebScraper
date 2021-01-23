import pandas as pd
import csv

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs



base_url = ""
request = ""
min_max = ""
url_seperator = "" 
page_num = ""

def get_page_count(site, item, low="", high=""):
    """[Gets the number of pages for query]
    
    Arguments:
        site {str} -- User choice of site
        item {str} -- Users choice of product
    
    Keyword Arguments:
        low {str} -- Lowest cost range (default: {""})
        high {str} -- Highest cost range (default: {""})
    
    Returns:
        [type] -- html content, page count and True
    """

    global base_url 
    global request
    global min_max 
    global url_seperator
    global page_num

    if site == "0":
        base_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="
    else:
        return "INVALID"

    request = item.replace(" ", "+")
    print(request)

    min_max = f"&_udlo={low}&_udhi={high}"

    url_seperator = "&_sacat=0&_pgn="
    page_num = "1"

    url = f"{base_url}{request}{min_max}{url_seperator}{page_num}"
    html = urlopen(url).read()
    soup = bs(html, "html.parser")

    results = soup.findAll("h1", {"class" : "srp-controls__count-heading"})[0]  
    page_counts = results.findAll("span", {"class" : "BOLD"})[0].text
    page_counts = page_counts.replace(",", "")

    return soup, int(page_counts), True


def make_csv(content):
    """[Creates the csv dataset]
    
    Arguments:
        content {[dict]} -- [Table of product listings]
    """

    file_name = "scrape_data_set.csv"
    df = pd.DataFrame(content)
    print(f"Shape >>> {df.shape}")
    df.to_csv(file_name)


def scrape(soup, start_page, end_page):
    """[Scrapes all the pages within given page range]
    
    Arguments:
        soup {[type]} -- [description]
        start_page {[type]} -- [description]
        end_page {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    titles, prices, links, pages = [], [], [], []

    for page in range(start_page, end_page+1):
        for post in soup.findAll("li", {"class" : "s-item"}):
            if len(str(post)) > 1002:
                title = post.findAll("h3", {"class" : "s-item__title"})[0].text
                price = post.findAll("span", {"class" : "s-item__price"})[0].text
                link = post.findAll("a", {"class" : "s-item__link"})[0]['href']

                # Append to lists 
                pages.append(page)
                titles.append(title)
                prices.append(price)
                links.append(link)

        # Updating soup to next page
        page_num = str(page)
        print(f"Page # {page_num}")
        url = f"{base_url}{request}{min_max}{url_seperator}{page_num}"
        html = urlopen(url).read()
        soup = bs(html, "html.parser")

    # print("Lengths >>> ", len(titles), len(prices), len(links))
    content = { "Title" : titles, "Price" : prices, "Link"  : links, "Page Number"  : pages }
    return content


def main():
    """Main functionality of program.
    """
    print("*"*50)
    print(f"*\t\tWelcome to Price Check\t\t *")
    print("*"*50)

    print() 

    site = ""
    while True:
        print("Choose between Available sites")
        print("[0] - Ebay")
        print("[1] - Amazon  (Coming Soon!)")
        site = input(" > ")
        if site != str(0):
            print("This site is currently not available\n")
        else:
            break

    item = input("\nEnter an item to look for\n > ")

    is_valid = False
    while True:
        print("Enter a price range you're interested in\n  (ex: '100 350' => between 100-350 AND 0' => All Range)")
        price_range = input(" > ")
        if price_range == "0":
            soup, page_count, is_valid = get_page_count(site, item)
            break
        if len(price_range.split()) == 2:
            low, high = price_range.split()
            if low.isdigit() and high.isdigit():
                soup, page_count, is_valid = get_page_count(site, item, low, high)
                break
            else:
                print("Invalid price range!")
        else:
            print("Invalid price range!")

    if is_valid:
        print(f"There are {page_count} total pages\n")
        while True:
            page_range = input("Enter a page range (ex: '1 100')\n > ")
            if len(page_range.split()) == 2:
                start, end = page_range.split()
                if start.isdigit() and end.isdigit() and start < end:
                    content = scrape(soup, int(start), int(end))            # Scrape if all above condition is met
                    break
                else:
                    print("Invalid range for pages")
        make_csv(content)                             # Export data to csv  
        print("Sucessfully created dataset!")
    else:
        print("Failed to make dataset!")


def read_csv():
    file_name = "scrape_data_set.csv"
    titles, prices, links = [], [], []

    with open(file_name) as f:
        content = csv.reader(f)
        for row in content:
            titles.append(row[1])
            prices.append(row[2]) 
            links.append(row[3])
    # Remove $ and only account for "207.00" in "$207.00 to $329.00"
    tmp_prices = [float(price.partition(" to ")[0].replace("$", "")) for price in prices[1:]]
    
    #sort all tree list simultaniously
    zipped = zip(tmp_prices, titles[1:], links[1:])

    sorted_zipped = sorted(zipped)

    new_prices, new_titles, new_links = [], [], []
    for value in sorted_zipped:
        new_prices.append(value[0])
        new_titles.append(value[1])
        new_links.append(value[2])
    #Get n (5) smaller values
    N = 5
    print("Top 5 cheapest are:")
    for i in range(N):
        print(f'NUmber #{i}')
        print(f'{new_titles[i]}\t {new_prices[i]}\t {new_links[i]}')    

if __name__ == "__main__":
    # read_csv()

    try:
        main()
        # At this point the dataset is created. It can now be used to check compare prices
        read_csv()
    except:
        print("An error Occured!")
