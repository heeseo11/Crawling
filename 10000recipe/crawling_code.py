csvfile = open('./볶음.csv', 'a', encoding='utf-8-sig', newline= '')
csvwriter = csv.writer(csvfile)
# 10개의 레시피만 크롤링 
for i in all_receipe[:10]:
    print(i)
    r = requests.get(i)
    soup = BeautifulSoup(r.text, 'html.parser')
    temp = []
    
    # 레시피 명
    try:
        A = soup.findAll('div',attrs={'class':'view2_summary st3'})[0].get_text().strip().split('\n')[0]
        #print(A)
        #print("------------------------------------------------------------------")
        temp.append(A)
    except:
        pass
        print("레시피가 없음")
        
    
    # 레시피 등록 날짜
    try:
        date = soup.findAll('p',attrs={'class':'view_notice_date'})[0].get_text().strip().split(" ")[2]
    except:
        print('날짜 없음')
        pass

        
    
    # 조회수
    try:
        count = soup.findAll('span',attrs={'class':'hit font_num'})[0].get_text()
        temp.append(date)
    except:
        pass
    
    # 재료
    try:
        A_list = soup.findAll('div',attrs={'class':'ready_ingre3'})[0].get_text().split()
        mate = " ".join(A_list)
        temp.append(mate)
    except:
        print('재료없음')
        pass
     
    try:
        soup_1 = soup.findAll('div',attrs={'class':'view_step'})[0]
    except:
        #print("레시피 정보가 없음")
        pass
        
    # 요리 순서
    try:
        for j in range(0, len(soup.findAll('div',attrs={'class':'media-body'}))):
            A = soup_1.findAll('div',attrs={'class':'media-body'})[j].get_text()
            temp.append(A)

    except:
        pass
    
    print(temp)
    csvwriter.writerow(temp)
    print("------------------------------------------------------------------")
