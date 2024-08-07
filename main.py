import aiohttp
import asyncio
from time import sleep
import datetime

ddos = 0.5

async def find_reg_number(session, type_si):
    
    async with session.get('https://fgis.gost.ru/fundmetrology/api/registry/4/data',
                           params = {
                               'pageNumber': 1,
                               'pageSize': 20,
                               'orgID': 'CURRENT_ORG',
                               'filterBy': 'foei:DesignationSI',
                               'filterValues': type_si
                               }
                           ) as response:
        return await response.json()
        
    
    
async def find_verification(session, mod_si:str, number:str, date_veri):
    year_now = int(date_veri[-4:])
    for year in range(year_now-2, year_now - 7, -1):
        if year > datetime.date.today().year:
            continue
           
        params = {
                "fq": [
                    f"verification_year:{year}",
                    #f"org_title:{org}",
                    #"mi.mitnumber":reg_number,
                    #"mi.mititle": name_si,
                    #"mi.mitype": type_si,
                    f"mi.modification:{mod_si}",
                    f"mi.number:{number}"
                    ],
                "q": '*',
                "fl": "vri_id,org_title,mi.mitnumber,mi.mititle,mi.mitype,mi.modification,mi.number,verification_date,valid_date,",
                #"sort": "verification_date+desc",
                "rows": 20,
                "start": 0
                }
        async with session.get('https://fgis.gost.ru/fundmetrology/cm/xcdb/vri/select', params=params) as response:
                #print(response.url)
            #print("Status:", await response.status)
                #print("Content-type:", response.headers['content-type'])

            json = await response.json()
            if json['response']["numFound"] > 1:
                print(f"Много результатов {mod_si}#{number} в {year} году")
                sleep(ddos)
            elif json['response']["numFound"] == 1:
                for item in json['response']['docs']:
                    print(f'{item["org_title"]} - {item["mi.modification"]} - #{item["mi.number"]} - {item["verification_date"]}')
                    sleep(ddos)
                    return item
                break
            else:
                print(f"Не нашел {mod_si}#{number} в {year} году")
                sleep(ddos)
    

async def get_items(json, type_si):
    for item_result in json['result']['items']:
            for item_prop in item_result['properties']:
                if not item_prop['name'] == 'foei:DesignationSI':
                    continue
                if type_si.lower() in map(lambda x: x.lower(), item_prop['value'][0]):# Продумать поиск
                    return item_result
    
                    
                

async def get_number(item_result):
    for item_prop in item_result['properties']:
        if item_prop['name'] == 'foei:NumberSI':
            return item_prop['value']
    
                            
                                  
                    


async def main():
    async with aiohttp.ClientSession() as session:
        with open("base_verif.txt", "r", encoding="utf-8") as bv:
            lines = [line for line in bv]
            for line in lines:
                type_si, number, date_veri = line.split()
                print(type_si, number, date_veri)
                
                json = await find_verification(session, type_si, number, date_veri)
                #json = await find_reg_number(session, type_si)
                if json is None:
                    continue
                print(f'{json["org_title"]} {json["mi.mititle"]} {json["mi.mitype"]}({json["mi.mitnumber"]}) - {json["mi.modification"]} - #{json["mi.number"]} - {json["verification_date"]}-{json["valid_date"]}')
                #['result']['totalCount'])
                #if int(json['result']['totalCount']) > 1:
                #    item_result = await get_items(json, type_si)
                    #print(item_result)
                #else:
                 #   item_result = json['result']['items'][0]
                #if item_result:
                #    number = await get_number(item_result)
                #    print(number)
                #else:
                #    print("not found")
        
            
     



if __name__ == '__main__':
    asyncio.run(main())
    
