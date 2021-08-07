def Rakuten(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # 총 리뷰수
    review_count = soup.findAll('span',{'class':'revEvaCount'})[0].get_text()
    review_count = int(re.sub('[()件]', ' ', review_count))
    print(review_count)
    
    # 제품명
    product_name = soup.findAll('a',{'sid_linkname':'item_01'})[0].get_text().strip()
    print(product_name)
    
    # 리뷰 작성자
    for i in soup.findAll('ul',{'class' :'revUserRvwer'}):
        member_ID = i.get_text().split('さん')[0].strip()
        mask_name = member_ID.replace(member_ID[math.floor(len(member_ID)/2):],"*****")
        print(mask_name)

    # 리뷰
    for i in soup.findAll('dd',{'class':'revRvwUserEntryCmt description'}):
        print("--------------------------------------------------")
        review = i.get_text()
        print(review)
