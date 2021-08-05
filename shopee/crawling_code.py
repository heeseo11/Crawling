def shope_result(URL):    
    searchList = []

    r = requests.get(URL)
    json_data = r.json()
    try:
        for i in range(0,len(json_data['data']['ratings'])):

            temp = []
            #제품명
            product_name = json_data['data']['ratings'][0]['product_items'][0]['name']
            temp.append(product_name)

            # 작성자
            member_ID = json_data['data']['ratings'][i]['author_username']
            temp.append(member_ID)

            # 리뷰
            review = json_data['data']['ratings'][i]['comment']
            temp.append(review)

            try:
                searchList.append(temp)
                print("-----------------------------------------------------")
                print(product_name + ':' + member_ID + ':' + review)

            except:
                print("data가 없음")
    except:
        print('review가 없음 ')
            
    return searchList   
