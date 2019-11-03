import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

import argparse
from selenium.common.exceptions import NoSuchElementException
usr = 'PUT YOUR LOGIN EMAIL'
pwd = 'PUT YOUR LOGIN PASSWORD'


driver = webdriver.Chrome('./chromedriver')

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="url",
                    default="https://mbasic.facebook.com/groups/search/?groupID=346318255539022&query=%EC%95%84%ED%8C%8C%EC%9A%94&ref=content_filter&tsid&source=typeahead&refsrc=https%3A%2F%2Fmbasic.facebook.com%2Fgroups%2Fsearch%2F%3Fref%3Dcontent_filter&cursor=Abp6BXqPS4n7Vnhg6pqsFdfx0KOWzrdob_3Hqy33O5jabwcxqcukaLZvU0MGNz7m_m6w34xqkafMsIHbSkDvOeIvda8n4hyrvNJBojAhn6yeYvG83i_aUNRxi4l9rQXWt2d35I2MSx1yo45C0Uu02zCtg6_BnKgJ-P5rc36iz7juCHy5uKyvfLsGb8Kys7DzvYvOLp90Yktzi1RB7g_qTMSXOOOVJWM0_o-b88AnXoIhhrvqEJT-7w5W48MItw-WpXPyRZfEabFtsMrmo8PZxQatZXn8STmrZyI3O4NucNtxp0fNx9Hgha9MLY0OdYPoswZUmgnqh13XgbSNQA58rdWwKIyrbkAMRWN18JXkWe4Sm7wjufcn4FDudpKVeMkvr5WmLsp5aWIS88_cH4e16TbHwh_MHVUOapDVivnCgLgQcylbuRJNNylFHS6WZIX9Xwb2S40Wl0kwPSlgDL9Y9ttJ9b31v6cHN2lxXD6sr78XwOChoY4QCRfOCvdCO_F2cCy14ygw9Sq3cS4GBw_k0oZnxs_g3806ku1RJRX8dWFKEIkx8HM7WTW-r08NHEFJjWdnp8_IBXL4_qa4sc3f5MdVgugwUeSUTpnT-_t4dgVlWJrlO_m9dEbd0hek7qyGo3ebGp3lk3OEjdQOOV_V5UDhk_9_qwxHFgp-ZdvGuX-ZPQeZDNwyjAeWtBvuh-tEADStQLTNBCO_SfSXctb5acRgpGjl5xh0dkN9C1m2KjVarNxi0Lsw9XtYAbsjRn2dz9uegw7g6ARO1_QX5y9h7y5Tov-2ynPBcwRJuVUdIC8sKJObFrk28A_yC3BmDGbO-u10sEJtIM0YEeVtROkFbAofAIXVEpm7u3WH0bYrZPDlEOGFYLCgj7ZKaPvo6-tA4kxhhGFQ_FFBTxmO6y5LBYYVqKfZQXN6jekRHzPrClcTGWi8bwjdbYdDNDFtiDZu5vRIHNIn2SwELz2TZVqlyzdgSk-FNmlN5crCRDg_mCUplVz5CZuL98EgtAHuMpnOdEjNWd48I-A9kkV9jNKU0LuvQv_lFFwrbjE5lVVupU3sUOWXGmVAbEHlkkVBJBrGTP-SlJR3OlhzRNInTUvfl1xxM6EG9hb8MoSWn0wfX1uk13kXS-UB6Fz4wRnd6-yf2JuIRVe0gqnUKqdMOkgHz9663HhD6dXMPYHgjcCbVwwanQYqmtHfTUZKO7F5cLdqzjArKIx_qN6skoL5oqvhMEzykvuF96yUPJCDv_3jsKSAhF19f60Q0m-IQZRvgyIsV5_VYhsWnr3gFtZydCyHmDa7xoHwhMjUU7TFIVmjFLiE2qH6Tok0sDJMjE-_yardwCW_8-CutBQv5T7X2Sb-WJmWjSz8xLAtilrKYkE-Yi2Qg9K2peBKwYIX-8dS-_h1QCGs-dlHgeo3sZQxLfKSIPNUHAdT3zQbTg6IHZDgYkltTNPKX59BKtC4K0jVUO7p7TjQ3R7j9yduZz4j-0lfARHiDWNRfCMB2R39hWIDT21TC2CVc5p4wX35h4hdnCk2jP54R4XOwyV51lB6PCDYQBMS0oDouPBP-LqlqcjXpwzK6WpYflQ0R0HycMHhK1BS7C5-EuMk31TZPBEmYvzwsk2qa6a2IZhvMPBOzaaXOkY72D4TYlikqg98zEcPDLOU0dIMem4YsZDg1FaMGt_Wm6f_gD1NKqSS5XfMuFLUDqz0VGnFNHo9qsQRlO_dOvAaYMxXJckissK_EZeeBMNeRZIibbn6iPrei-ECesyBkDB1OyIMc974TFulyPbgVsIGFFV7Ttbaxt_p-XcROeVR-ddCVBMQyqUvnIMEJUyawa61YKn8nbiCUqMiOGBFEl_kvkeeF7EDSa7l9Puvdx5uyQo9lxyFx_R8qTJI3Zjm6cFr5duP0m-fTw02pyKDIPdaxu8&pn=2&usid=596c2ae043c9eb49b9bddb49f5214683")
parser.add_argument("--out", help="out",
                    default="out.csv") #csv out file name
                    
args = parser.parse_args()

args.url = url

driver.get(args.url)

#automatically login to facebook
elem = driver.find_element_by_id("m_login_email")
elem.send_keys(usr)
elem = driver.find_element_by_name("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN) 
time.sleep(2)

while True:
    try :
        #scrolling til end
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        postlist = []
        # html_source = driver.page_source
        # data = html_source.encode('utf-8')
        # print(data)
        #print(driver.find_element_by_name('body').text)
        
        
       
        k  = driver.find_elements_by_css_selector("div.bw.bx.by") #find post list in current page

        for i in k:
            
            #post text including hashtag
            try :
                d  = i.find_element_by_css_selector("div.ci").text. 
            except  NoSuchElementException as e:
                d = None

            #post timestamp ex)"March 22, 2017 at 4:00 PM"
            try :
                timest = i.find_element_by_css_selector("div.cr.ch abbr").text
            except  NoSuchElementException as e:
                try :
                    timest = i.find_element_by_css_selector("div.cs.ch abbr").text
                except :
                    try :
                        timest = i.find_element_by_css_selector("div.cq.ch abbr").text
                    except:
                        timest =None
                        
            #post reaction count            
            try:
                reac = i.find_element_by_css_selector("a.cv.cw").text
            except  NoSuchElementException as e:
                try :
                    reac = i.find_element_by_css_selector("a.cw.cx").text
                except:
                    try:
                        reac = i.find_element_by_css_selector("a.cv.cu").text

                    except:
                        reac = None
                        
            #comment count ex) 7 Comments             
            try :
                comment = i.find_element_by_css_selector("div.cq > div:nth-child(2) > a.cw").text
            except  NoSuchElementException as e:
                try :
                    comment = i.find_element_by_css_selector("div.cq > div:nth-child(2) > a.cx").text
                except :
                    try :
                        comment = i.find_element_by_css_selector("div.cq > div:nth-child(2) > a.cu").text
                    except:
                        comment = None
                        
            #comment link per post that can be used later for comment crawling            
            try :
                commentlink = i.find_element_by_css_selector("div.cq > div:nth-child(2) > a.cw").get_attribute('href')
            except  NoSuchElementException as e:
                try:
                    commentlink = i.find_element_by_css_selector("div.cq > div:nth-child(2) > a.cx").get_attribute('href')
                except:
                    try:
                        commentlink = i.find_element_by_css_selector("div.cq > div:nth-child(2) > a.cu").get_attribute('href')

                    except:

                        commentlink = None
                        
                        
            #print([d,timest,reac,comment,commentlink])
            postlist.append([d,timest,reac,comment,commentlink])
            
            
        with open(args.out, 'a', encoding='utf-8') as toWrite:
            writer = csv.writer(toWrite)
            writer.writerows(postlist)
            #print(len(k),len(d),len(timest),len(reac),len(comment))

        
        #comment = driver.find_elements_by_xpath('//a.cw[text()="Comments"]') #comment link
        #comment.click()

        time.sleep(4)
        driver.find_element_by_xpath('//span[contains(., "See More")]/..').click() #click to next page
        
    except:  # done if it's end of the page
        #toWrite.close()
        print("done")
        break
