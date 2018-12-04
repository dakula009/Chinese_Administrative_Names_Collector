# -*- coding: UTF-8 -*-
import requests
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def get_base(url):
    """Extract the parent directory of a URL.
    """
    return url[:url.rindex('/')+1]

def get_done(dir):

    with open(dir, 'a+') as logfile:
        log_set= logfile.readlines()

    return log_set

def write_error(data):

    with open('C:\Temp\Chinese_Admins_1to4_error.txt', 'a+') as logfile:
        logfile.write(data + '\n')

def get_admin1(url):

    provin_dict = {}

    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}

        # Must set correct encoding for r, according to the head of html: "charset=gb2312"
        r = requests.get(url, headers=headers, timeout=100)
        #time.sleep(1)
        r.encoding = 'GBK'
        text = r.text
        # soup text instead of content to avoid encoding issues
        soup = BeautifulSoup(text, "lxml")

        provin_tab = soup.find('table', class_ = 'provincetable').find_all('tr',class_ = "provincetr")
        for row in provin_tab:
            for p in row.find_all('a'):
                province= p.contents[0]
                link= p.get('href')
                provin_dict.update({province.encode('utf-8'): link})

    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        import sys
        tb = sys.exc_info()[2]
        print "An error occured on line %i" % tb.tb_lineno
        print(e)

    except Exception as e:
        import sys
        tb = sys.exc_info()[2]
        print "An error occured on line %i" % tb.tb_lineno
        print(e)
        write_error(url)

    return provin_dict

def get_admin2(url):

    city_dict = {}

    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}

        r = requests.get(url, headers=headers, timeout=100)
        r.encoding = 'GBK'
        text = r.text
        soup = BeautifulSoup(text, "lxml")

        city_tab = soup.find('table', class_ = 'citytable').find_all('tr',class_ = "citytr")
        for row in city_tab:
            #print row.contents
            c=  row.find_all('td')
            code = c[0].contents[0].string
            city = c[1].contents[0].string
            link = c[1].contents[0].get('href')
            city_dict.update({city.encode('utf-8'): [code,link]})

    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        import sys
        tb = sys.exc_info()[2]
        print "An error occured on line %i" % tb.tb_lineno
        print(e)

    except Exception as e:
        import sys
        tb = sys.exc_info()[2]
        print "An error occured on line %i" % tb.tb_lineno
        print(e)
        write_error(url)

    return city_dict

def get_admin3(url):

    a3_dict = {}

    try:

        ua = UserAgent()
        headers = {'User-Agent': ua.random}

        r = requests.get(url, headers=headers, timeout=100)
        r.encoding = 'GBK'
        text = r.text
        soup = BeautifulSoup(text, "lxml")

        a3_tab = soup.find('table', class_ = 'countytable').find_all('tr',class_ = "countytr")
        for row in a3_tab:
            #print row.contents
            c=  row.find_all('td')
            code = c[0].contents[0].string
            a3 = c[1].contents[0].string
            #print code
            #print a3
            if a3.encode('utf-8') == '市辖区':
                pass
            else:
                link = c[1].contents[0].get('href')
                a3_dict.update({a3.encode('utf-8'): [code,link]})

    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        import sys
        tb = sys.exc_info()[2]
        print "An error occured on line %i" % tb.tb_lineno
        print(e)

    except Exception as e:
        import sys
        tb = sys.exc_info()[2]
        print "An error occured on line %i" % tb.tb_lineno
        print(e)
        write_error(url)

    return a3_dict

def get_admin4(url):

    a4_dict = {}

    try:

        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        r = requests.get(url, headers=headers, timeout=100)
        time.sleep(1)
        # Must set correct encoding for r, according to the head of html: "charset=gb2312"
        r.encoding = 'GBK'
        text = r.text

        #with open('C:/Temp/admin4.html', 'w') as file:
            #file.write(r.content)

        soup = BeautifulSoup(text, "lxml")

        a4_tab = soup.find('table', class_ = 'towntable').find_all('tr',class_ = "towntr")
        for row in a4_tab:
            #print row
            c=  row.find_all('td')
            code = c[0].contents[0].string
            a4 = c[1].contents[0].string
            #print code
            #print a4
            link = c[1].contents[0].get('href')
            #print link

            a4_dict.update({a4.encode('utf-8'): [code,link]})

    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        import sys
        tb = sys.exc_info()[2]
        print "An error occured on line %i" % tb.tb_lineno
        print(e)


    except Exception as e:
        import sys
        tb = sys.exc_info()[2]
        print "An error occured on line %i" % tb.tb_lineno
        print(e)
        write_error(url)

    return a4_dict

def get_admin5(url):

    a5_dict = {}

    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        r = requests.get(url, headers=headers, timeout=100)
        r.encoding = 'GBK'
        text = r.text
        soup = BeautifulSoup(text, "lxml")

        a5_tab = soup.find('table', class_ = 'villagetable').find_all('tr',class_ = "villagetr")
        for row in a5_tab:
            #print row.contents
            c= row.find_all('td')
            code1 = c[0].contents[0].string
            code2 = c[1].contents[0].string
            a5 = c[2].contents[0].string
            print a5
            print code1
            print code2
            a5_dict.update({a5.encode('utf-8'): [code1,code2]})

    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        import sys
        tb = sys.exc_info()[2]
        print "An error occured on line %i" % tb.tb_lineno
        print(e)

    except Exception as e:
        import sys
        tb = sys.exc_info()[2]
        print "An error occured on line %i" % tb.tb_lineno
        print(e)
        write_error(url)

    return a5_dict

baseurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html'

admin1s = get_admin1(baseurl)

df_list = []

doneset= get_done('C:\Temp\Chinese_Admins_1to4_log.txt')

for a1 in admin1s.keys():

    #print a1
    sublink = admin1s[a1]
    a1_link= get_base(baseurl) + sublink
    #print a1_link
    provlink = a1_link.replace('.html','/')
    admin2s = get_admin2(a1_link)

    for a2 in admin2s:

        log_string = a1 + ',' + a2 + '\n'

        if log_string in doneset:
            # print "a2 was already done"
            continue

        else:

            sublink = admin2s[a2][1]
            a2_link = baseurl.replace('index.html', '') + sublink
            admin3s = get_admin3(a2_link)

            for a3 in admin3s:
                sublink = admin3s[a3][1]
                a3_link = provlink + sublink
                admin4s = get_admin4(a3_link)
                ctylink = get_base(a3_link)
                #log_string = a1 + ',' + a2 + ',' + a3 + '\n'

                #print "a3 was not done"
                for a4 in admin4s:

                    string = a1 + ',' + a2 + ',' + a3 + ',' + a4

                    print string

                    with open('C:\Temp\Chinese_Admins_1to4.txt', 'a+') as output:
                        output.write(string + "\n")

            with open('C:\Temp\Chinese_Admins_1to4_log.txt', 'a+') as output:
                output.write(log_string)

                '''
                sublink = admin4s[a4][1]
                a4_link = ctylink + sublink
                print a4_link
                admin5s = get_admin5(a4_link)
                '''


lines_seen = set() # holds lines already seen
outfile = open("C:\Temp\Chinese_Admins_1to4_unique.txt", "w")
for line in open("C:\Temp\Chinese_Admins_1to4.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()