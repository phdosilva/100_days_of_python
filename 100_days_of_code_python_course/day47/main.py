from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                        headers={
                            "Accept-Language":"en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
                            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                            }
                        )

soup = BeautifulSoup(response.text, 'html.parser')

price = float(soup.find(class_="a-price-whole").text + soup.find(class_="a-price-fraction").text)

print(price)