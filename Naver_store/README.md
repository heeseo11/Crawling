# Naver_store 상품 리뷰 데이터 수집

- 상품 정보 URL

  - example : https://smartstore.naver.com/beautylook/products/4946239777


   <img src = "https://user-images.githubusercontent.com/61724682/126807889-8a8cedad-57ad-4644-9d4b-b2e079a78a28.png" width="70%" height="70%">


- 상품 리뷰 json파일
  
      네이버 스토어의 경우 단순한 url 파싱으로 정보 수집이 안됨
      따라서  network 탭에서 상품 리뷰 정보를 담은 json파일을 찾아서 해당 Request URL을 받아서 크롤링을 진행해야 함

  - example : https://smartstore.naver.com/i/v1/reviews/paged-reviews?page=1&pageSize=20&merchantNo=500122169&originProductNo=4929853516&sortType=REVIEW_RANKING


  <img src = "https://user-images.githubusercontent.com/61724682/126808537-ca863ab8-6ed8-41ee-bf63-e17390fde108.png" width="90%" height="90%">


