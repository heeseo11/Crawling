csvfile = open('./해먹.csv', 'a', encoding='utf-8-sig', newline= '')
csvwriter = csv.writer(csvfile)
for i in all_url:
    r = requests.get(i)
    soup = BeautifulSoup(r.text, 'html.parser')
    temp = []
    print(i)
    
    try:
        
        # 레시피명
        name = soup.findAll('strong')[1].get_text()
        #print(name)
        temp.append(name)
        
        #스크랩수
        count = soup.findAll('dd',attrs={'id':'scrap-cnt'})[0].get_text()
        #print(count)
        temp.append(count)
        
        # 레시피 순서
        rec_order = soup.findAll('ol', attrs = {'class':'lst_step'})[0].get_text().replace("\n","")
        #print(rec_order)
        temp.append(rec_order)
        
        # 영양정보
        info_list = []
        for i in range(len(soup.findAll('p',attrs={'style':'display:none;'}))):
            info = soup.findAll('p',attrs={'style':'display:none;'})[i].get_text()
            #print(info)
            info_list.append(info)
        temp.append(info_list)
        
        # 재료리스트
        con_list = []
        for i in range(len(soup.findAll('div',attrs={'class':'btm'})[0].findAll('span'))):
            con = soup.findAll('div',attrs={'class':'btm'})[0].findAll('span')[i].get_text()
            #print(con)
            con_list.append(con)
            
        temp.append(con_list)
        
        print(temp)
        csvwriter.writerow(temp)
        print("------------------------------------------------------------------")
            
    except:
        print("존재하지 않는 레시피")
        pass
        
    
