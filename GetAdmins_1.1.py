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

        index_set= logfile.readline()

        if len(index_set) == 0:

            index_set = [0,0,0,0]

        else:

            index_set = index_set.split(',')
            index_set = [int(i) for i in index_set]

    return index_set

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

doneset= get_done('C:\Temp\Chinese_Admins_1to4_index.txt')

print doneset

a1_done = doneset[0]
a2_done= doneset[1]
a3_done= doneset[2]
a4_done = doneset[3]

a1_list = admin1s.keys()

for a1 in a1_list[a1_done:]:

    #print a1
    index_a1 = a1_list.index(a1)
    sublink = admin1s[a1]
    a1_link= get_base(baseurl) + sublink
    #print a1_link
    provlink = a1_link.replace('.html','/')
    admin2s = get_admin2(a1_link)
    a2_list = admin2s.keys()

    #print a2_list.index('菏泽市')

    for a2 in a2_list[a2_done:]:

        #print ' ' + a2
        index_a2 = a2_list.index(a2)
        a2_done= index_a2
        sublink = admin2s[a2][1]
        a2_link = baseurl.replace('index.html', '') + sublink
        admin3s = get_admin3(a2_link)
        a3_list = admin3s.keys()

        #print a3_list

        for a3 in a3_list[a3_done:]:
            #print '  ' + a3
            index_a3 = a3_list.index(a3)
            a3_done = index_a3
            sublink = admin3s[a3][1]
            a3_link = provlink + sublink
            admin4s = get_admin4(a3_link)
            ctylink = get_base(a3_link)
            a4_list = admin4s.keys()
            #log_string = a1 + ',' + a2 + ',' + a3 + '\n'

            #print "a3 was not done"
            for a4 in a4_list[a4_done:]:
                #print '   ' + a4

                index_a4= a4_list.index(a4)


                string = a1 + ',' + a2 + ',' + a3 + ',' + a4

                index = '{0},{1},{2},{3}'.format(index_a1,index_a2,index_a3,index_a4)

                print string

                with open('C:\Temp\Chinese_Admins_1to4.txt', 'a+') as output:
                    output.write(string + "\n")

                # Record the last mined admin4's indices
                with open('C:\Temp\Chinese_Admins_1to4_index.txt', 'w') as output:
                    output.write(index + "\n")

            a4_done = 0

        a3_done = 0

    a2_done = 0





lines_seen = set() # holds lines already seen
outfile = open("C:\Temp\Chinese_Admins_1to4_unique.txt", "w")
for line in open("C:\Temp\Chinese_Admins_1to4.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()