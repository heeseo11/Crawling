def Olive_Young(URL):
    searchList = []
    
    r = requests.get(URL)
    time.sleep(rand.randrange(2,4,1)) 
    
    soup = BeautifulSoup(r.text, 'html.parser')
    conduct = soup.findAll('a',attrs={'class':'prd_thumb goodsList'})
        
    for i in range(0,len(conduct)):
        
        conduct_code = conduct[i].attrs['data-ref-goodsno']
        url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo={}".format(conduct_code)
        print(url)
        
        driver= wd.Chrome( r"chromedriver.exe")
        driver.get(url)
        time.sleep(rand.randrange(2,4,1)) 
        
        X_PATH = '//*[@id="buyInfo"]/a'
        driver.find_element_by_xpath(X_PATH).click()
        
        WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="artcInfo"]/dl[1]/dd'))
            )

        res = driver.page_source
        obj = bs(res, 'html.parser')
        
        temp = []
        
        # 제품명
        product_name = obj.findAll('p',attrs={'class':'prd_name'})[0].get_text().strip()
        print(product_name)
        temp.append(product_name)
        
        # 가격
        try:
            price_1 = obj.findAll('span',attrs={'class':'price-1'})[0].get_text().strip()
            price_1 = price_1.replace("\n","")
            price_1 = price_1.replace("원","")
            print(price_1)
            temp.append(price_1)
        except:
            price_2 = obj.findAll('span',attrs={'class':'price-2'})[0].get_text().strip()
            price_2 = price_2.replace("\n","")
            price_2 = price_2.replace("원","")
            print(price_2)
            temp.append(price_2)
            
        # 용량
        try:
            capa = obj.findAll('dl',attrs={'class':'detail_info_list'})[0].get_text().strip()
            capa = capa.split('\n')[1].replace("■ ","")
            print(capa)
            temp.append(capa)
        except:
            capa = obj.findAll('dl',attrs={'class':'detail_info_list'})[0].get_text().strip()
            print(capa)
            temp.append(capa)
        
        # 성분
        try:
            inge = obj.findAll('dl',attrs={'class':'detail_info_list'})[6].get_text().strip()
            inge = inge.split('\n')[1].replace("■ ","")
            print(inge)
            temp.append(inge)
            
            driver.close()
            driver.quit()
            
        except:
            inge = obj.findAll('dl',attrs={'class':'detail_info_list'})[6].get_text().strip()
            print(inge)
            temp.append(inge)
            
            driver.close()
            driver.quit()

        searchList.append(temp)
        print("-----------------------------------------------------")
        #print(product_Name + ':' + member_ID + ':' + review)

    return searchList   
