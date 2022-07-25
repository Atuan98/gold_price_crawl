from fastapi import APIRouter, Request, Depends, HTTPException
from routes.base_route import BaseRoute
from schemas.data_by_area import data_by_area

router = APIRouter(route_class=BaseRoute)

@router.get("/get_list_area")
async def get_listy_area():
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

