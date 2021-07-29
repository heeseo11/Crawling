def coupang_store(URL):
    searchList = []
    # 총 리뷰 수와 리뷰 페이지 수 추출
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    sum = 0
    for i in range(0, 5):
        a = int(soup.findAll('div',attrs={'class':'js_reviewArticleHiddenValue'})[i]['data-count'])
        sum = sum + a

    print("review_count : {}".format(sum))    
    review_url_count = math.floor(sum/5)
    print("review_url_count : {}".format(review_url_count))
    # 리뷰 데이터 크롤링
    review_urls = []
    
    for i in range(1,review_url_count):
        review_url = URL.format(i)
        review_urls.append(review_url)
        
    for j in range(0,len(review_urls)):
        print(j)
        review_url = review_urls[j]
        r = requests.get(review_url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        page_review = soup.findAll('div',attrs={'class':'sdp-review__article__list__review__content js_reviewArticleContent'})

        for q in range(0,len(page_review)):
            temp = []
            
            # 제품명
            product_Name = soup.findAll('div',attrs={'class':'sdp-review__article__list__info__product-info__name'})[q].get_text()
            temp.append(product_Name)
            
            # 작성자
            member_ID = soup.findAll('span',attrs={'class':'sdp-review__article__list__info__user__name js_reviewUserProfileImage'})[1].get_text()
            member_ID = member_ID.replace('\xa0','')
            temp.append(member_ID)
            
            # 리뷰
            review = page_review[q].get_text()
            temp.append(review)

            searchList.append(temp)
            print("-----------------------------------------------------")
            print(product_Name + ':' + member_ID + ':' + review)

    return searchList
