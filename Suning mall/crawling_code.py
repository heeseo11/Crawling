def sunmall(URL):
    searchList = []

    print(URL)
    driver= wd.Chrome( r"\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get(URL)
    time.sleep(2)
    
    res = driver.page_source
    soup = bs(res, 'html.parser')

    # 제품명
    for i in range(0, len(soup.findAll('div',attrs={'class':'username'}))):
        temp = []
        conduct_name = soup.findAll('div',attrs={'class':'the-pro-info'})[0].get_text().strip()
        print(conduct_name)
        print("------------------------------------------------------------------")
        temp.append(conduct_name)
            
        #작성자
        try: 
            Name = soup.findAll('div',attrs={'class':'username'})[i].get_text().strip()
            print(Name)
            print("------------------------------------------------------------------")
            temp.append(Name)
        except:
            pass
            
        try:
        # 리뷰내용
            review = soup.findAll('p',attrs={'class':'body-content'})[i].get_text().strip()
            print(review)
            print("------------------------------------------------------------------")
            temp.append(review)
        except:
            pass
    
        searchList.append(temp)
        
    driver.close()
    driver.quit()
        
    return searchList    
