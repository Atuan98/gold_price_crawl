from fastapi import FastAPI
import pymongo
from typing import Union
import datetime

app = FastAPI()
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["gold_price"]


@app.get('/get_list_area')
def get_list_area():
    mycol = mydb["area"]
    list_area = []
    data_resp = []
    final_data_resp = []
    for x in mycol.find({}):
        for i in x:
            area = x['area']
        list_area.append(area)
    final_list = list(dict.fromkeys(list_area))

    for x in mycol.find({}):
        remove_keys = ["_id", "website"]
        resp = {remove_key: x[remove_key] for remove_key in x if remove_key not in remove_keys}
        data_resp.append(resp)

    for i in data_resp:
        if i not in final_data_resp:
            final_data_resp.append(i)

    return {
        'total': len(final_list),
        'code': 0,
        'data': final_data_resp
    }


@app.get('/get_list_types/{area}')
def get_list_types(area):
    mycol = mydb["realtime_price"]
    data_resp = []
    final_data_resp = []
    for x in mycol.find({'area': area}):
        remove_keys = ["_id", 'website', 'buyPrice', 'sellPrice', 'date_time', 'website']
        resp = {remove_key: x[remove_key] for remove_key in x if remove_key not in remove_keys}
        data_resp.append(resp)

    for i in data_resp:
        if i not in final_data_resp:
            final_data_resp.append(i)

    return {
        'area': area,
        'code': 0,
        'data': final_data_resp
    }






