import requests
from bs4 import BeautifulSoup # Python library to pull or extract XML or HTML data
import smtplib

# The url of the given laptop
URL='https://www.amazon.in/dp/B0844516K1/ref=pc_mcnc_merchandised-search-12_?pf_rd_s=merchandised-search-12&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=6A16R9XBKKYW1VFT3C36&pf_rd_p=af95eec5-2478-46bb-8cc8-b82677ccd271'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}


def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')
    title= soup.find(id='productTitle').get_text()
    price=soup.find(id='priceblock_ourprice').get_text()
    price.strip()
    converted_price=float(price[2:4]+price[5:8])
    print(converted_price)
    if(converted_price< 90000.0):
        send_mail()
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() # To identify itself when connecting to another email
    server.starttls() #Opportunistic TLS
    server.ehlo()

    server.login('shrikeshs98@gmail.com','obfmarzuhmgzzhqn')

    subject = "Hey! The Price has gone down"

    body = 'Check this link: https://www.amazon.in/dp/B0844516K1/ref=pc_mcnc_merchandised-search-12_?pf_rd_s=merchandised-search-12&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=6A16R9XBKKYW1VFT3C36&pf_rd_p=af95eec5-2478-46bb-8cc8-b82677ccd271'

    msg = f"Subject : {subject}\n\n{body}"
    
    server.sendmail(
        'shrikeshs98@gmail.com',
        'shrikeshs98@gmail.com',
        msg
    ) # sends the required message.
    print('Email has been sent')
    server.quit()

check_price()