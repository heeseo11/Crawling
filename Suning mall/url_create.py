# good
good_url = "https://review.suning.com/cluster_cmmdty_review/general-35279546-000000010740759469-0000000000-{}-good.htm?originalCmmdtyType=general&safp=d488778a.10004.loverRight.131&curCheckFlag=true"
all_good_url = []
for i in range(1, 51):
    URL = good_url.format(i)
    all_good_url.append(URL)
    
# normal
normal_url = "https://review.suning.com/cluster_cmmdty_review/general-35279546-000000010740759469-0000000000-{}-normal.htm?originalCmmdtyType=general&safp=d488778a.10004.loverRight.131&curCheckFlag=true"
all_normal_url = []
for i in range(1, 4):
    URL = normal_url.format(i)
    all_normal_url.append(URL)

# bad
bad_url = "https://review.suning.com/cluster_cmmdty_review/general-35279546-000000010740759469-0000000000-{}-bad.htm?originalCmmdtyType=general&safp=d488778a.10004.loverRight.131&curCheckFlag=true"
all_bad_url = []
for i in range(1, 5):
    URL = bad_url.format(i)
    all_bad_url.append(URL)
# all
all_url = all_good_url + all_normal_url + all_bad_url
len(all_url)
