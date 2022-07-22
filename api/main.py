from fastapi import FastAPI
import pymongo
from typing import Union
import datetime

app = FastAPI()
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = myclient["gold_price"]


@app.get('/get_list_area')
def get_list_area():
    try:
        myCollection = myDB["area"]
        list_area = []
        data_resp = []
        final_data_resp = []
        for x in myCollection.find({}):
            for i in x:
                area = x['area']
            list_area.append(area)
        final_list = list(dict.fromkeys(list_area))

        for x in myCollection.find({}):
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

    except:
        return {
            'code': 1,
            'description': 'Something went wrong!'
        }


@app.get('/get_list_types/{area}')
def get_list_types(area):
    if area.isupper() is not True:
        return {
            'code': 1,
            'description': 'City name is not valid!'
        }
    else:
        myCollection = myDB["type_gold"]
        data_resp = []
        final_data_resp = []
        for x in myCollection.find({'area': area}):
            remove_keys = ["_id", 'website']
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


@app.get('/get_daily_price/{from_date}/{to_date}')
def get_daily_price(from_date: Union[str, None], to_date: Union[str, None], area: Union[str, None] = None, type_: Union[str, None] = None):
        myCollection = myDB["daily_price"]
        data_resp = []
        final_data_resp = []
        from_date = datetime.datetime.strptime(from_date, '%d%m%Y')
        to_date = datetime.datetime.strptime(to_date, '%d%m%Y')
        to_date += datetime.timedelta(days=1)
        # original_query = {"date_time": {"$gte": from_date.isoformat(), "$lte": to_date.isoformat()},
        #                   "area": area,
        #                   "type": type_}

        if type_ and area:
            for data in myCollection.find({"date_time": {"$gte": from_date.isoformat(), "$lte": to_date.isoformat()},
                                           "area": area,
                                           "type": type_}):
                remove_keys = ["_id"]
                resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
                data_resp.append(resp)

            for data in data_resp:
                if data not in final_data_resp:
                    final_data_resp.append(data)

            return {
                'data': final_data_resp,
            }

        if type_ and not area:
            for data in myCollection.find(
                    {"date_time": {"$gte": from_date.isoformat(), "$lte": to_date.isoformat()}, "type": type_}):
                remove_keys = ["_id"]
                resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
                data_resp.append(resp)

            for data in data_resp:
                if data not in final_data_resp:
                    final_data_resp.append(data)

            return {
                'data': final_data_resp,
            }

        if area and not type_:
            for data in myCollection.find(
                    {"date_time": {"$gte": from_date.isoformat(), "$lte": to_date.isoformat()}, "area": area}):
                remove_keys = ["_id"]
                resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
                data_resp.append(resp)

            for data in data_resp:
                if data not in final_data_resp:
                    final_data_resp.append(data)

            return {
                'data': final_data_resp,
            }

        if type_ is None and area is None:
            for data in myCollection.find(
                    {"date_time": {"$gte": from_date.isoformat(), "$lte": to_date.isoformat()}}):
                remove_keys = ["_id"]
                resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
                data_resp.append(resp)

            for data in data_resp:
                if data not in final_data_resp:
                    final_data_resp.append(data)

            return {
                'data': final_data_resp,
            }


@app.get('/get_realtime_price/{from_date}/{to_date}')
def get_realtime_price(from_date: Union[str, None], to_date: Union[str, None], type_: Union[str, None] = None):
        myCollection = myDB["realtime_price"]
        data_resp = []
        final_data_resp = []
        from_date = datetime.datetime.strptime(from_date, '%d%m%Y')
        to_date = datetime.datetime.strptime(to_date, '%d%m%Y')
        to_date += datetime.timedelta(days=1)

        if type_:
            for data in myCollection.find({"date_time": {"$gte": from_date.isoformat(), "$lte": to_date.isoformat()},
                                           "type": type_}):
                remove_keys = ["_id"]
                resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
                data_resp.append(resp)

            for data in data_resp:
                if data not in final_data_resp:
                    final_data_resp.append(data)

            return {
                'data': final_data_resp,
            }

        else:
            for data in myCollection.find(
                    {"date_time": {"$gte": from_date.isoformat(), "$lte": to_date.isoformat()}}):
                remove_keys = ["_id"]
                resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
                data_resp.append(resp)

            for data in data_resp:
                if data not in final_data_resp:
                    final_data_resp.append(data)

            return {
                'data': final_data_resp,
            }
