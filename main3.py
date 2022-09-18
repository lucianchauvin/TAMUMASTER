
s1 = '''curl 'https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_subject=AEGD&txt_campus=CS&txt_term=202231&startDatepicker=&endDatepicker=&uniqueSessionId=8rcfk1662745867337&pageOffset=0&pageMaxSize=50&sortColumn=subjectDescription&sortDirection=asc' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H $'Cookie: JSESSIONID=02CAE9BF515AC232058C4F024CEDBD5D; TS01a9f0c5=014200a85bf68ed13cd08cef806ae1cdc52c014ae67b77c1ff4a6768f89f715475455ea5c82a7f5d5a610cb2f22fb975bc3dcdfc357f801d33785e3e0d6ed7e181361ede759df966dbf9ef6703c433846d5eb62f52; xe_prod_ssb=\u0021PzfVtuoRqD4nQBlxcfM42YaPjNcQdgnBmtUkc/FWxbAHTaE//5gygmld+lm3OLvfeOwvExMO4UwHK8Q=; TS0114ff3e=014200a85bd4815b005a9e92765658b2406d099e8901acadb6082f8cb0eeb8e48b3010cc1dfb36caaa124a0f620a439c84745444f491e3b6b6cd9b89cf546ef82a60bbc9e4' \
  -H 'Referer: https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/classSearch' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'X-Synchronizer-Token: 0765da9f-65ec-497c-b0ef-64274735a6f3' \
  -H 'sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed'''

s2 = '''curl 'https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_subject=AFST&txt_campus=CS&txt_term=202231&startDatepicker=&endDatepicker=&uniqueSessionId=8rcfk1662745867337&pageOffset=0&pageMaxSize=50&sortColumn=subjectDescription&sortDirection=asc' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H $'Cookie: JSESSIONID=02CAE9BF515AC232058C4F024CEDBD5D; TS01a9f0c5=014200a85bf68ed13cd08cef806ae1cdc52c014ae67b77c1ff4a6768f89f715475455ea5c82a7f5d5a610cb2f22fb975bc3dcdfc357f801d33785e3e0d6ed7e181361ede759df966dbf9ef6703c433846d5eb62f52; xe_prod_ssb=\u0021NRfsiXvJPCrS0LpxcfM42YaPjNcQdlN8HkI90JnORb2eCa+iw0GEbqliXUncxWNvfrwkdEeWMiojQvE=; TS0114ff3e=014200a85b1ace35f1f7c0307fe3b3e1a9e6e29f6201acadb6082f8cb0eeb8e48b3010cc1dfb36caaa124a0f620a439c84745444f45910738235ef777c7557f6490cc428cd' \
  -H 'Referer: https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/classSearch' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'X-Synchronizer-Token: 675928f2-634b-411f-afb1-a7ecf4445fb1' \
  -H 'sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed'''

cringe1 = ""
cringe2 = ""
for x in range(len(s1)):
    if s1[x] != s2[x]:
        cringe1 += s1[x]
        cringe2 += s2[x]

print(f'''{cringe1}
{cringe2}''')