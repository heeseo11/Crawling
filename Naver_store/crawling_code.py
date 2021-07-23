# NAVER_store 함수 
def NAVER_store(URL):
    try:
        searchList = []
        # 해당 리뷰 URL의 제품 정보 URL 추출
        review_url = URL.format(1)
        r = requests.get(review_url)
        json_data = r.json()
        for j in range(0,1):    
            info_url = json_data['contents'][j]['productUrl']
            print(info_url)
            
            # 리뷰 수와 리뷰 수에 따른 리뷰 URL 수
            review_url = info_url
            r = requests.get(review_url)
            soup = BeautifulSoup(r.text, 'html.parser')
            review = soup.findAll('strong',attrs={'class':'_2pgHN-ntx6'})[0].get_text()
            review_count = int(review.replace(",",""))
            review_url_count = math.floor(int(review.replace(",",""))/20)
            print( "review_count : {}".format(review_count))
            print("review_url_count",format(review_url_count))
            
            # 리뷰 데이터 크롤링
            review_urls = []
            for i in range(1,review_url_count):
                review_url = URL.format(i)
                review_urls.append(review_url)
                
            for q in range(0,len(review_urls)):
                print(q)
                review_url = review_urls[q]
                r = requests.get(review_url)
                json_data = r.json()
                
                reviews = json_data['contents']
                for j in range(0,len(reviews)):        
                    temp = []
                    # 상품명
                    product_Name = reviews[j]['productName']
                    temp.append(product_Name)
                    
                    # 작성자
                    writememberID = reviews[j]['writerMemberId']
                    temp.append(writememberID)
                    
                    # 리뷰 
                    review = reviews[j]['reviewContent']
                    temp.append(review)
                    
                    searchList.append(temp)
                    print("-----------------------------------------------------")
                    print(product_Name + " : "+  writememberID + ":" + review)
        
        return searchList
                
    except:
        print("리뷰가 없음")
