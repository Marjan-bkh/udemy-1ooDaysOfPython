import requests
import datetime
pixel_endpoint ="https://pixe.la/v1/users"
token="afv45fd4vadfdf4v"
username="marjan"
graph_id="a123456"
graph_name="grapg1"
# today_date=datetime.datetime.now().strftime("%Y%m%d")


user_params={
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}
# response= requests.post(url=pixel_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixel_endpoint}/{username}/graphs"
graph_params={
    "id":graph_id,
    "name":graph_name,
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":token
}
# response= requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)
pixel_endpoint=f"{graph_endpoint}/{graph_id}"
today_date=datetime.datetime.now()#date(year=2022,month=5,day=23)
formatted_today_date=today_date.strftime("%Y%m%d")
print(formatted_today_date)
pixel_params={
    "date":formatted_today_date,
    "quantity":input("How many kilometers did you walk today?")
}

put_pixel_params={
    "quantity":"1.5"
}
response= requests.post(url=pixel_endpoint,json=pixel_params,headers=headers)
print(response.text)
update_endpoint=f"{pixel_endpoint}/{formatted_today_date}"
# response= requests.put(url=update_endpoint,json=put_pixel_params,headers=headers)
# print(response.text)
# response= requests.delete(url=update_endpoint,headers=headers)
# print(response.text)