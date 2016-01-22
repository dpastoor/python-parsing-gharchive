import wget
import calendar

# In[47]:

download_urls = []
BASE = 'http://data.githubarchive.org/'
year = 2015
archive_2015 = []
for mon in range(1, 13):
    days = calendar.monthrange(year,mon)[1]
    month = str(mon) if mon > 9 else "0" + str(mon)
    for day in range(1, days+1):
        day_str = str(day) if day > 9 else "0" + str(day)
        for hour in range(1, 24):
            download_urls.append(str(BASE) + str(year) + "-" + month + "-" + day_str + "-" + str(hour) + ".json.gz")
        


# In[48]:

def wget_github(url):
    try:
        filename = wget.download(url)
    except:
        with open("wget_log.txt", "a") as log:
            log.write("ERROR IN: " + url + "\n")
            log.close()
        


# In[49]:

wget_github(download_urls[0])


# In[53]:
print('beginning dl')
for i, url in enumerate(download_urls):
    if (i % 168 == 0):
        print('starting:' + url)
    wget_github(url)
print('finished')




