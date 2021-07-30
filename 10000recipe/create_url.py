조리법_code = [6,1,7,36,41,42,8,10,9,38,67]
code_url = []
for i in 조리법_code:
    url = "https://www.10000recipe.com/recipe/list.html?cat1={}&order=reco&page={}".format(i,"{}")
    code_url.append(url)
    print(url)
    
# 조리법 code별 레시피 페이지 만들기
all_url = []
def page_url(code, page_count):
    url = "https://www.10000recipe.com/recipe/list.html?cat1={}&order=reco&page={}".format(code,"{}")
    code_url.append(url)
    print(url)
    for i in range(1,page_count):
        URL = url.format(i)
        all_url.append(URL)
        
# 모든 레시피의 url 생성
all_receipe = []
def make_url(URL_list):
    for i in URL_list:
        r = requests.get(i)
        soup = BeautifulSoup(r.text, 'html.parser')

        for j in range(0, len(soup.findAll('a',attrs={'class':'common_sp_link'}))):
            recipe_url = soup.findAll('a',attrs={'class':'common_sp_link'})[j].attrs['href']
            recipe_url = "https://www.10000recipe.com{}".format(recipe_url)
            all_receipe.append(recipe_url)
            
            
