import requests
#print('Answer code: ' + str(requests.get('https://google.com/').status_code))


websites = [
    'https://xakep.ru/',
    'https://google.com/',
    'https://rostov.cian.ru/',
    'https://volgoschool61.ucoz.ru/',
    'http://лицей2-34.рф/',
    'https://www.avito.ru/volgograd',
    'https://ruchoco.ru/',
    'https://vkontakte.ru'
]

for site in websites:
    #count = 0
    for count in range(1):
       #print('Answer #'+str(count+1)+' from '+ site +': ' + str(requests.get(site).status_code))
       print(requests.get(site).status_code)
       count += 1

requests.get('https://tobiz.net/support/sistemy-obnaruzheniya-vtorzhenij-ids/').text

