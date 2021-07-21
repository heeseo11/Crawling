def Amazon(URL):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size = 1920x1080")
    options.add_argument("disable-gpu")
    
    driver= wd.Chrome( r".\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get(URL)

    res = driver.page_source
    obj = bs(res, 'html.parser')

    #총 리뷰수 
    rev = obj.select('#filter-info-section > div > span')[0].get_text().strip()
    rev = int(rev.split(" | ")[1].split(" ")[0].replace(",", ""))
    print("리뷰수 : {}".format(rev))

    member_ID = []
    review_title = []
    reviews = []
     
    df = pd.DataFrame()

    while True :
        time.sleep(3)
        source = driver.page_source
        bs_obj = bs(source,"html.parser")

        #제품명
        product_Name = bs_obj.findAll('a',{'data-hook':'product-link'})[0].get_text()
        product_Name = re.sub('[/\?<>:|"]', '', product_Name)
        print(product_Name)
        
        #작성자 이름
        try : 
            for u in  bs_obj.findAll('span',{'class':'a-profile-name'})[2:]:
                pro_name = u.get_text().strip()
                mask_name = pro_name.replace(pro_name[math.floor(len(pro_name)/2):],"*****")
                member_ID.append(mask_name)
                print(mask_name)
        except:
            mask_name = 0
            member_ID.append(mask_name)
            print(mask_name)
            
        #리뷰 타이틀
        try : 
            for u in bs_obj.findAll('a',{'data-hook':'review-title'}):
                content_title = u.get_text()
                review_title.append(content_title)
                print(content_title)
                
        except:
            content_title = 0
            review_title.append(content_title)
            print(content_title)
            
            
        #리뷰 내용
        try : 
            for u in bs_obj.findAll('span',{'data-hook':'review-body'}):
                review = u.get_text().strip()
                reviews.append(review)
                print(review)
        except:
            review = 0
            reviews.append(review)
            print(review)
            
        try : 
            df = pd.DataFrame({'product_Name' : product_Name,'member_ID' : member_ID, 'review_title' : review_title, 'reviews' : reviews})
            
            # 다음 리뷰 페이지로 넘어가기 위해서 next button 클릭
            driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()

            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="a-autoid-3"]/span/input'))
            )
        
        except:
            
            try : 
                driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()

                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="a-autoid-3"]/span/input'))
                )

            except:
                print("next button이 없습니다")
                driver.close()
                driver.quit()
                df.to_excel("Amazon_{}.xlsx".format(product_Name))
                return df
