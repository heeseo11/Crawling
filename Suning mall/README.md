# suning mall 상품 리뷰데이터 크롤링

- 상품 정보 URL

  - example : https://product.suning.com/0000000000/10740759469.html?safp=d488778a.review.5.2&safc=prd.0.0&safpn=10009
  
  <img src = "https://user-images.githubusercontent.com/61724682/126667303-799acd86-9728-4d57-9280-f1197ac4342a.png" width="70%" height="70%">


- 상품 리뷰 URL (실제 리뷰데이터 수집 사이트)

         설명 : 긍정, 중립, 부정을 나눠서 수집을 진행 
         해당 URL의 good, normal, bad로 구분되어 있음
      
      
  - example
  - https://review.suning.com/cluster_cmmdty_review/general-35279546-000000010740759469-0000000000-{}-good.htm?originalCmmdtyType=general&safp=d488778a.10004.loverRight.131&curCheckFlag=true
  - https://review.suning.com/cluster_cmmdty_review/general-35279546-000000010740759469-0000000000-{}-normal.htm?originalCmmdtyType=general&safp=d488778a.10004.loverRight.131&curCheckFlag=true
  - https://review.suning.com/cluster_cmmdty_review/general-35279546-000000010740759469-0000000000-{}-bad.htm?originalCmmdtyType=general&safp=d488778a.10004.loverRight.131&curCheckFlag=true
  
  <img src = "https://user-images.githubusercontent.com/61724682/126667774-bf227ebd-41e5-4b36-9749-af92bf5afc79.png" width="80%" height="80%">


- 결과 DataFrame

  - suning mall의 경우 리뷰를 총 500개까지 제공
  
  <img src = "https://user-images.githubusercontent.com/61724682/126669910-d1540b23-39a1-4959-8f39-5b9820a7cd55.png" width="70%" height="70%">




