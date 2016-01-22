import wget
import calendar

# In[47]:

download_urls = []
BASE = 'http://data.githubarchive.org/'
year = 2015
archive_2015 = []
for mon in range(6, 13):
    days = calendar.monthrange(year,mon)[1]
    month = str(mon) if mon > 9 else "0" + str(mon)
    for day in range(1, days+1):
        day_str = str(day) if day > 9 else "0" + str(day)
        for hour in range(1, 24):
            download_urls.append(str(BASE) + str(year) + "-" + month + "-" + day_str + "-" + str(hour) + ".json.gz")
 
mon = 1
year = 2016
days = 20
month = str(mon) if mon > 9 else "0" + str(mon)
for day in range(1, days+1):
    day_str = str(day) if day > 9 else "0" + str(day)
    for hour in range(1, 24):
        dl_url = str(BASE) + str(year) + "-" + str(month) + "-" + day_str + "-" + str(hour) + ".json.gz"
        download_urls.append(dl_url)      



# In[48]:
def wget_github(url):
    try:
        filename = wget.download(url)
    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        with open("wget_log.txt", "a") as log:
            log.write("ERROR IN: " + url + " with message: \n")
            log.write(message)
            log.write("\n")
            log.close()
        




# In[53]:
print('beginning dl')
for i, url in enumerate(download_urls):
    if (i % 168 == 0):
        print('starting:' + url)
    wget_github(url)
print('finished')




