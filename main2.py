import requests

courses = ['AALO', 'ACCT', 'AERO', 'AERS', 'AFST', 'AGCJ', 'AGEC', 'AGLS', 'AGSC', 'AGSM', 'ALEC', 'ALED', 'ANSC', 'ANTH', 'ARAB', 'ARCH', 'AREN', 'ARTS', 'ASCC', 'ASIA', 'ASTR', 'ATMO', 'ATTR', 'BAEN', 'BEFB', 'BESC', 'BICH', 'BIMS', 'BIOL', 'BMEN', 'BOTN', 'BUSN', 'CARC', 'CEHD', 'CHEM', 'CHEN', 'CHIN', 'CLAS', 'CLEN', 'COMM', 'COSC', 'CSCE', 'CVEN', 'CYBR', 'DAEN', 'DASC', 'DCED', 'DDHS', 'DIVE', 'ECCB', 'ECEN', 'ECHE', 'ECMT', 'ECON', 'EDCI', 'EHRD', 'ENDG', 'ENDS', 'ENGL', 'ENGR', 'ENST-', 'ENTC', 'ENTO', 'EPFB', 'EPSY', 'ESET', 'ESSM', 'EURO', 'EVEN', 'FILM', 'FINC', 'FIVS', 'FREN', 'FRSC', 'FSCI', 'FSTC', 'FYEX', 'GALV', 'GENE', 'GEOG', 'GEOL', 'GEOP', 'GEOS', 'GERM', 'HBRW', 'HEFB', 'HHUM', 'HISP', 'HIST', 'HLTH', 'HORT',
           'HUMA', 'IBUS', 'IDIS', 'INST-', 'INTS', 'ISEN', 'ISTM', 'ITAL', 'ITDE', 'JAPN', 'JOUR', 'KINE', 'KNFB', 'LAND', 'LBAR', 'LDEV', 'LING', 'LMAS', 'MARA', 'MARB', 'MARE', 'MARR', 'MARS', 'MART', 'MASC', 'MASE', 'MAST', 'MATH', 'MEEN', 'MEFB', 'MEPS', 'METR', 'MGMT', 'MICR', 'MKTG', 'MLSC', 'MMET', 'MODL', 'MSEN', 'MTDE', 'MUSC', 'MUST', 'MXET', 'NAUT', 'NRSC', 'NUEN', 'NURS', 'NUTR', 'NVSC', 'OCEN', 'OCNG', 'PBSI', 'PERF', 'PETE', 'PHIL', 'PHLT', 'PHYS', 'PLPA', 'POLS', 'PORT', 'POSC', 'RDNG', 'RELS', 'RENR', 'RPTS', 'RUSS', 'RWFM', 'SCEN', 'SCMT', 'SCSC', 'SEFB', 'SENG', 'SOCI', 'SOMS', 'SPAN', 'SPED', 'SPMT', 'STAT', 'TCMG', 'TEED', 'TEFB', 'UGST', 'URPN', 'VIBS', 'VIST', 'VLCS', 'VSCS', 'VTPB', 'VTPP', 'WFSC', 'WGST', 'ZOOL']


for x in courses:

    cookies = {
        'JSESSIONID': '271A986BC13A011D48E828A07C4B0E75',
        'TS01a9f0c5': '014200a85bf68ed13cd08cef806ae1cdc52c014ae67b77c1ff4a6768f89f715475455ea5c82a7f5d5a610cb2f22fb975bc3dcdfc357f801d33785e3e0d6ed7e181361ede759df966dbf9ef6703c433846d5eb62f52',
        'xe_prod_ssb': '!vg871PTBvtW/IyRxcfM42YaPjNcQdvqGHIT6K2HOcPEo1tzYVTOx5oXHD32Pr+ncQmXHUjxRddvu+HE=',
        'TS0114ff3e': '014200a85bcc47b7017b28652c061eeb78da39f624ff304bfe0f9e8483e1616f4f43350307315f87fa0558cb6ac8616e76d684beda3ed86a45766ca4309feb29f3c3604141',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'JSESSIONID=02CAE9BF515AC232058C4F024CEDBD5D; TS01a9f0c5=014200a85bf68ed13cd08cef806ae1cdc52c014ae67b77c1ff4a6768f89f715475455ea5c82a7f5d5a610cb2f22fb975bc3dcdfc357f801d33785e3e0d6ed7e181361ede759df966dbf9ef6703c433846d5eb62f52; xe_prod_ssb=!vg871PTBvtW/IyRxcfM42YaPjNcQdvqGHIT6K2HOcPEo1tzYVTOx5oXHD32Pr+ncQmXHUjxRddvu+HE=; TS0114ff3e=014200a85bcc47b7017b28652c061eeb78da39f624ff304bfe0f9e8483e1616f4f43350307315f87fa0558cb6ac8616e76d684beda3ed86a45766ca4309feb29f3c3604141',
        'Referer': 'https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/classSearch',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Synchronizer-Token': 'a2848a0a-82ca-479d-9e3d-b52e8174df6c',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'txt_subject': x,
        'txt_campus': 'CS',
        'txt_term': '202231',
        'startDatepicker': '',
        'endDatepicker': '',
        'uniqueSessionId': '8rcfk1662745867337',
        'pageOffset': '0',
        'pageMaxSize': '1000',
        'sortColumn': 'subjectDescription',
        'sortDirection': 'asc',
    }

    response = requests.get('https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults', params=params, cookies=cookies, headers=headers)

    f = open("outs/" + x + '.txt', 'w')
    f.write(response.text)