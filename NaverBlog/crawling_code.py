searchList = []
# 검색할 키워드와 페이지 수 지정
def NaverBlog(keyword, page_num):
    for i in range(1,page_num):

        keyword_decode = urllib.parse.quote(keyword)

        url = "https://section.blog.naver.com/Search/Post.naver?pageNo={}&rangeType=PERIOD&orderBy=sim&startDate=2021-01-01&endDate=2021-03-31&keyword={}"
        url = url.format(i, keyword_decode)
        print(url)

        driver= wd.Chrome( r"chromedriver_win32\chromedriver.exe")
        driver.get(url)
        time.sleep(rand.randrange(2,4,1)) 

        res = driver.page_source
        obj = bs(res, 'html.parser')

        for j in range(0,len(obj.findAll('a',attrs={'class':'desc_inner'}))):

            content_url = obj.findAll('a',attrs={'class':'desc_inner'})[j].attrs['href']

            URL = "https://blog.naver.com/PostView.naver?blogId={}&logNo={}&redirect=Dlog&widgetTypeCall=true&from=section&topReferer=https%3A%2F%2Fsection.blog.naver.com%2FSearch%2FPost.naver%3FpageNo%3D1%26rangeType%3DPERIOD%26orderBy%3Dsim%26startDate%3D2021-01-01%26endDate%3D2021-06-30%26keyword%3D%25EC%2583%2589%25EC%25A1%25B0%25EB%25A9%2594%25EC%259D%25B4%25ED%2581%25AC%25EC%2597%2585&directAccess=false"
                       
            bolgid = content_url.split('/')[3]
            logno = content_url.split('/')[4]
            result_url = URL.format(bolgid, logno)
            print(result_url)
            
            r = requests.get(result_url)
            time.sleep(rand.randrange(2,4,1)) 
            
            soup = BeautifulSoup(r.text, 'html.parser')
            for q in range(0, len(soup.findAll('div',attrs={'class':'se-main-container'}))):
                temp = []
                
                try:
                    # 작성일
                    Date = soup.findAll('span',attrs={'class':'se_publishDate pcol2'})[0].get_text().strip()
                    print(Date)
                    temp.append(Date)

                    # 내용
                    content = soup.findAll('div',attrs={'class':'se-main-container'})[q].get_text().strip()
                    # 본문 내용이 길어서 생략
                    #print(content)
                    temp.append(content)
                except:
                    pass

                searchList.append(temp)
        
        driver.close()
        driver.quit()
        
    return searchList
        
