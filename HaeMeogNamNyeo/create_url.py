URL = "https://haemukja.com/recipes?cooking_time=&difficulty=&healthy=&name=%EB%96%A1&page={}&sort="

all_url = []
for i in range(1,22):
    url = URL.format(i)
    print(url)
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    for i in range(len(soup.findAll('a',attrs={'class':'call_recipe thmb'}))):
        href = soup.findAll('a',attrs={'class':'call_recipe thmb'})[i]['href']
        rec_url = "https://haemukja.com{}".format(href)
        #print(rec_url)
        all_url.append(rec_url)
