#  각 제품 정보에 대한 url
#url = [
#        "https://www.amazon.com/Bio-Oil-200ml-Multiuse-Skincare-6-7oz/dp/B00AREGVUM/ref=sr_1_1?dchild=1&keywords=Bio-Oil+Skincare+Oil%2C+Body+Oil+for+Scars+and+Stretchmarks%2C+Serum+Hydrates+Skin%2C+Non-Greasy%2C%E2%80%A6&qid=1624412876&sr=8-1",
#        "https://www.amazon.com/Softsoap-Liquid-Hand-Soap-Aloe/dp/B079FV8QB9/ref=sr_1_1?dchild=1&keywords=Softsoap+Moisturizing+Liquid+Hand+Soap%2C+Soothing+Clean+Aloe+Vera+-+7.5+Fluid+Ounces+%286+Pack%29&qid=1624412973&sr=8-1",
#        "https://www.amazon.com/Dove-Purely-Pampering-Coconut-Sulfate/dp/B0846GC23D/ref=sr_1_1?dchild=1&keywords=Dove+Purely+Pampering+Body+Wash+for+Dry+Skin+Coconut+Butter+and+Cocoa+Butter+Effectively%E2%80%A6&qid=1624413010&sr=8-1",
#        "https://www.amazon.com/Dr-Squatch-Pine-Tar-Soap/dp/B00TXRDA9O/ref=sr_1_1?dchild=1&keywords=Dr.+Squatch+Pine+Tar+Soap+%E2%80%93+Mens+Soap+with+Natural+Woodsy+Scent+and+Skin+Scrub+Exfoliation%E2%80%A6&qid=1624413030&sr=8-1",
#      ... ]

# 제품 정보 url의 /dp/를 기준으로 상품의 code를 리스트로 저장
code = []
for u in url:
    code = u.split("/dp/")[1]
    code.append(code[:10])

# code 리스트에 저장된 상품의 코드로 상품 리뷰 url 생성
url = []
for i in code:
    url = 'https://www.amazon.com/product-reviews/{}/ref=cm_cr_arp_d_viewopt_sr?pageNumber=1'.format(i)
    print(url)
    url.append(url)
    
