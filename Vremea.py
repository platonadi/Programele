from requests_html import HTMLSession

s = HTMLSession()

query = input("Introdu zona: "  ' ')

url = f'https://www.google.ro/search?q=vremea+ {query}'
r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})

temp = (r.html.find('span#wob_tm', first=True).text)
unit = (r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text)
desc = (r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text)

print('In ' + query, 'sunt ' + temp,'si este ' +desc)
