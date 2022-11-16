import requests
from bs4 import BeautifulSoup
import json

def GE_A_scraper(A_list):
    GE_A_1(A_list)

def GE_B_scraper(B_list):
    GE_B_1(B_list)
    GE_B_2(B_list)
    GE_B_3(B_list)
    GE_B_4(B_list)

def GE_C_scraper(C_list):
    GE_C_1(C_list)
    GE_C_2(C_list)
    GE_C_3(C_list)
def GE_D_scraper(D_list):
    GE_D_1(D_list)
    GE_D_2(D_list)
    GE_D_3(D_list)

def GE_E_scraper(E_list):
    GE_E_1(E_list)
    GE_E_2(E_list)

def GE_F_scraper(F_list):
    GE_F_1(F_list)
    GE_F_2(F_list)


def GE_G_scraper(G_list):
    GE_G_1(G_list)
    GE_G_2(G_list)
def GE_H_scraper(H_list):
    GE_H_1(H_list)
    GE_H_2(H_list)


def GE_A_1 (A_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
        'uscsso-my': 'EPM%2F4eR3os0PV%2BbKNV8E0rffhmehzNfaXAv1n5E9lNePi0a%2F0hSYks%2B2ieEM3eogYxaR%2Fb258DVn00zDUR7j%2BoSbS0JKsrMfHWGEsiYtJ3gFeeUKvryDHM2Khj7sCy6k',
        '_gat': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553; uscsso-my=EPM%2F4eR3os0PV%2BbKNV8E0rffhmehzNfaXAv1n5E9lNePi0a%2F0hSYks%2B2ieEM3eogYxaR%2Fb258DVn00zDUR7j%2BoSbS0JKsrMfHWGEsiYtJ3gFeeUKvryDHM2Khj7sCy6k; _gat=1',
        'Referer': 'https://webreg.usc.edu/Departments',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'ARTS',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div', class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ","")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)


    for i in range(len(courseID_list)):
        A_list.append({"ClssID": courseID_list[i], "Professor":professor_list[i], "Category": "A"})
def GE_B_1(B_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553',
        'Referer': 'https://webreg.usc.edu/Departments',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'HINQ',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div',
                                    class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ", "")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)

    for i in range(len(courseID_list)):
        B_list.append({"ClssID": courseID_list[i], "Professor": professor_list[i], "Category": "B"})
def GE_B_2(B_list):


    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
        '_gat': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553; _gat=1',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=HINQ',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'HINQ',
        'page': '2',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div',
                                    class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ", "")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)

    for i in range(len(courseID_list)):
        B_list.append({"ClssID": courseID_list[i], "Professor": professor_list[i], "Category": "B"})
def GE_B_3(B_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
        '_gat': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553; _gat=1',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=HINQ&page=2',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'HINQ',
        'page': '3',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div',
                                    class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ", "")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)

    for i in range(len(courseID_list)):
        B_list.append({"ClssID": courseID_list[i], "Professor": professor_list[i], "Category": "B"})
def GE_B_4(B_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=HINQ&page=3',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'HINQ',
        'page': '4',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div',
                                    class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ", "")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)

    for i in range(len(courseID_list)):
        B_list.append({"ClssID": courseID_list[i], "Professor": professor_list[i], "Category": "B"})
def GE_C_1(C_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553',
        'Referer': 'https://webreg.usc.edu/Departments',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'SANA',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div',
                                    class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ", "")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)

    for i in range(len(courseID_list)):
        C_list.append({"ClssID": courseID_list[i], "Professor": professor_list[i], "Category": "C"})
def GE_C_2(C_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
        '_gat': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553; _gat=1',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=SANA',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'SANA',
        'page': '2',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div',
                                    class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ", "")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)

    for i in range(len(courseID_list)):
        C_list.append({"ClssID": courseID_list[i], "Professor": professor_list[i], "Category": "C"})
def GE_C_3(C_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
        '_gat': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553; _gat=1',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=SANA&page=2',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'SANA',
        'page': '3',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div',
                                    class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ", "")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)

    for i in range(len(courseID_list)):
        C_list.append({"ClssID": courseID_list[i], "Professor": professor_list[i], "Category": "C"})
def GE_D_1(D_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553',
        'Referer': 'https://webreg.usc.edu/Departments',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'LIFE',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div',
                                    class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ", "")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)

    for i in range(len(courseID_list)):
        D_list.append({"ClssID": courseID_list[i], "Professor": professor_list[i], "Category": "D"})
def GE_D_2(D_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
        '_gat': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553; _gat=1',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=LIFE',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'LIFE',
        'page': '2',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div',
                                    class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ", "")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)

    for i in range(len(courseID_list)):
        D_list.append({"ClssID": courseID_list[i], "Professor": professor_list[i], "Category": "D"})
def GE_D_3(D_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
        '_gat': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553; _gat=1',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=LIFE&page=2',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'LIFE',
        'page': '3',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div',
                                    class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ", "")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)

    for i in range(len(courseID_list)):
        D_list.append({"ClssID": courseID_list[i], "Professor": professor_list[i], "Category": "D"})
def GE_E_1 (E_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553',
        'Referer': 'https://webreg.usc.edu/Departments',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'PSC',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div', class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ","")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)


    for i in range(len(courseID_list)):
        E_list.append({"ClssID": courseID_list[i], "Professor":professor_list[i], "Category": "E"})
def GE_E_2 (E_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
        '_gat': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553; _gat=1',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=PSC',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'PSC',
        'page': '2',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div', class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ","")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)


    for i in range(len(courseID_list)):
        E_list.append({"ClssID": courseID_list[i], "Professor":professor_list[i], "Category": "E"})
def GE_F_1 (F_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553',
        'Referer': 'https://webreg.usc.edu/Departments',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'QREA',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div', class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ","")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)


    for i in range(len(courseID_list)):
        F_list.append({"ClssID": courseID_list[i], "Professor":professor_list[i], "Category": "F"})
def GE_F_2 (F_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=QREA',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'QREA',
        'page': '2',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div', class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ","")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)


    for i in range(len(courseID_list)):
        F_list.append({"ClssID": courseID_list[i], "Professor":professor_list[i], "Category": "F"})
def GE_G_1 (G_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
        '_gat': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553; _gat=1',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=GPG&page=2',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'GPG',
        'page': '1',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div', class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ","")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)


    for i in range(len(courseID_list)):
        G_list.append({"ClssID": courseID_list[i], "Professor":professor_list[i], "Category": "G"})
def GE_G_2 (G_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=GPG&page=1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'GPG',
        'page': '2',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div', class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ","")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)


    for i in range(len(courseID_list)):
        G_list.append({"ClssID": courseID_list[i], "Professor":professor_list[i], "Category": "G"})
def GE_H_1 (H_list):
    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553',
        'Referer': 'https://webreg.usc.edu/Departments',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'GPH',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div', class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ","")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)


    for i in range(len(courseID_list)):
        H_list.append({"ClssID": courseID_list[i], "Professor":professor_list[i], "Category": "H"})
def GE_H_2 (H_list):
    import requests

    cookies = {
        '_fbp': 'fb.1.1660143419481.1774693115',
        'hubspotutk': '157060071e99684796a07a20953fdb34',
        '_ga_DX7N3XJJJC': 'GS1.1.1660143948.1.1.1660144911.0',
        '_ga_KDLL9QH186': 'GS1.1.1660144328.1.1.1660144912.0',
        '_ga_C314QG7LHT': 'GS1.1.1661985748.1.1.1661986491.0.0.0',
        '_ga_JTPM4PFWLH': 'GS1.1.1662269446.1.0.1662269475.0.0.0',
        '_ga_303839482': 'GS1.1.1662269446.1.0.1662270144.0.0.0',
        'ASP.NET_SessionId': 'doenjwlcnxneniqefrq0lghn',
        'WWTRBQJP': '0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw',
        '__hssrc': '1',
        '_ga_YRR9RE26RP': 'GS1.1.1666119283.5.1.1666119358.0.0.0',
        '_ga_HSNT8SE8SL': 'GS1.1.1666304531.3.0.1666304531.0.0.0',
        '_ga_VR9Z4L09HL': 'GS1.1.1666818098.4.1.1666818223.0.0.0',
        '__hstc': '77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3',
        '_ga_1QLNE3QTRJ': 'GS1.1.1667250357.6.1.1667250483.0.0.0',
        '_ga_P8VVN700QW': 'GS1.1.1667435206.2.1.1667435743.0.0.0',
        '_ga': 'GA1.2.544327619.1658791229',
        '_ga_VHVPE97PCE': 'GS1.1.1667588081.2.0.1667588081.0.0.0',
        '_gid': 'GA1.2.1376182604.1668547553',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_fbp=fb.1.1660143419481.1774693115; hubspotutk=157060071e99684796a07a20953fdb34; _ga_DX7N3XJJJC=GS1.1.1660143948.1.1.1660144911.0; _ga_KDLL9QH186=GS1.1.1660144328.1.1.1660144912.0; _ga_C314QG7LHT=GS1.1.1661985748.1.1.1661986491.0.0.0; _ga_JTPM4PFWLH=GS1.1.1662269446.1.0.1662269475.0.0.0; _ga_303839482=GS1.1.1662269446.1.0.1662270144.0.0.0; ASP.NET_SessionId=doenjwlcnxneniqefrq0lghn; WWTRBQJP=0297a45327-1bed-4fQuquDMQX1m8QKKHc6lOSK2N8FMht51WvxsH26fYIZJEZgteo1eGtNVwnesaYVe-oiLw; __hssrc=1; _ga_YRR9RE26RP=GS1.1.1666119283.5.1.1666119358.0.0.0; _ga_HSNT8SE8SL=GS1.1.1666304531.3.0.1666304531.0.0.0; _ga_VR9Z4L09HL=GS1.1.1666818098.4.1.1666818223.0.0.0; __hstc=77507402.157060071e99684796a07a20953fdb34.1660143419524.1665019903424.1666903504984.3; _ga_1QLNE3QTRJ=GS1.1.1667250357.6.1.1667250483.0.0.0; _ga_P8VVN700QW=GS1.1.1667435206.2.1.1667435743.0.0.0; _ga=GA1.2.544327619.1658791229; _ga_VHVPE97PCE=GS1.1.1667588081.2.0.1667588081.0.0.0; _gid=GA1.2.1376182604.1668547553',
        'Referer': 'https://webreg.usc.edu/Courses?DeptId=GPH',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'DeptId': 'GPH',
        'page': '2',
    }

    response = requests.get('https://webreg.usc.edu/Courses', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    courseID_list = []
    courseID = soup.find_all('span', class_="crsID")
    for c in courseID:
        c = c.text[:-1]
        courseID_list.append(c)

    professor_list = []
    courseContainer = soup.find_all('div', class_="col-xs-12 col-sm-12 col-md-12 col-lg-12 collapse crs-accordion-content-area")
    for course in courseContainer:
        professor = course.find('span', class_='instr_alt1 col-xs-12 col-sm-12 col-md-1 col-lg-1').text
        x = professor.split(':')
        y = x[1].split(',')
        z = ""
        i = len(y) - 1
        while i > 0:
            q = y[i].replace(" ","")
            z += q
            i -= 1
        z += y[i]

        professor_list.append(z)


    for i in range(len(courseID_list)):
        H_list.append({"ClssID": courseID_list[i], "Professor":professor_list[i], "Category": "H"})

def main():
    A_list = []
    B_list = []
    C_list = []
    D_list = []
    E_list = []
    F_list = []
    G_list = []
    H_list = []

    GE_A_scraper(A_list)
    GE_B_scraper(B_list)
    GE_C_scraper(C_list)
    GE_D_scraper(D_list)
    GE_E_scraper(E_list)
    GE_F_scraper(F_list)
    GE_G_scraper(G_list)
    GE_H_scraper(H_list)

    courseList = A_list + B_list +C_list + D_list + E_list + F_list +G_list + H_list

    jsonString = json.dumps(courseList, indent=2)

    with open("courseData.json", "w") as write_file:
        write_file.write(jsonString)

if __name__ == "__main__":
    main()