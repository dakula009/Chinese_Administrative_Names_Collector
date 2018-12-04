# Chinese_Administrative_Names_Collector
A python web crawler collecting administrative names ( from Admin1  to Admn4) from governmental website
Mine Chinese admin s using a python web-crawler

The data is farmed from a Chinese governmental webpage: http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/, 

The website updates Chinese administrative info annually. The most updated vintage is 2017.

Admin-1:  Provinces  省

Admin-2:  Prefectures 地级行政区

Admin-3:  Counties 县级行政区 （县/市/区）

Aadmin-4: Townships 乡级行政区 （乡镇/街道）

### Prerequisites

This tool was written in Python 2.7 

You need to install the following Python libraries before using the tool:

BeautifulSoup4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Requests: http://docs.python-requests.org/en/master/

Fake-UserAgent: https://pypi.org/project/fake-useragent/

### Running

Feel free to change the work directory. The default one is "C:\Temps"

Run the script "Get_Admins_1.0.py"

There major output will be a txt file containing collected informaiton

In the output file "Chinese_Admins_1to4_unique.txt", each row is composed by Admin1 + Admin2 + Admin3 + Admin4


## Contributing

Please folk the project if needed

## License

This repo is released under the WTFPL 
