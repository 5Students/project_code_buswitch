from distutils.log import ERROR
import json
from urllib import response
from elasticsearch import Elasticsearch
import urllib.request
import datetime
from dateutil.relativedelta import relativedelta
d = datetime.datetime.now()
d = d - relativedelta(days=7)
print(d.strftime('%Y%m%d'))
t = d.strftime('%H')
# Password for the 'elastic' user generated by Elasticsearch
ELASTIC_PASSWORD = "zC4so1Hmvt6PkSqA2UeFH6Aj"

# Found in the 'Manage Deployment' page
CLOUD_ID = "ontology:YXAtbm9ydGhlYXN0LTIuYXdzLmVsYXN0aWMtY2xvdWQuY29tOjQ0MyRmZmE2YzBmM2FlZDU0YjhjODhlMWZhMTEzNjllZDc0OSQ1NjU2NzA4NWYxZDM0NzdkOWY3ZTFmNDk2OTkwODE1NA==kibana"

# Create the client instance
client = Elasticsearch(
    cloud_id=CLOUD_ID,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)


# Successful response!
# print(client.info())/

#search index
def search_all_index(index):
  res=client.search(index=index, query={"match_all":{}})
  print(res)


ERROR=True
import requests
count=1
count_id=0
# 버스 승하차 일일 데이터 노선별 upload 코드 시간별로
while ERROR:
  url = 'http://openapi.seoul.go.kr:8088/6a4550546c6a683339326965757675/json/CardBusStatisticsServiceNew/'+str(count)+'/'+str(count+999)+'/'+d.strftime('%Y%m%d')+'/'
  response = urllib.request.urlopen(url)
  json_str = response.read().decode("utf-8")

  json_object = json.loads(json_str)

# bus routenumber, pasgr_num", ali
# "시군구 쿠드,"
  print(json_object)
  print(count)
  for a in range(1000):
    try:
      if json_object["CardBusStatisticsServiceNew"]["RESULT"]["CODE"] == 'INFO-000':
        sigungoo=json_object["CardBusStatisticsServiceNew"]["row"][a]["BSST_ARS_NO"]
        sigungoo='11'+sigungoo[:2]+'0'
        bus_station=json_object["CardBusStatisticsServiceNew"]["row"][a]["BSST_ARS_NO"]+json_object["CardBusStatisticsServiceNew"]["row"][a]["BUS_ROUTE_NO"]

        body={
          "BUS_STATION": bus_station,
          'ARS-ID' : json_object["CardBusStatisticsServiceNew"]["row"][a]["BSST_ARS_NO"],
          "노선명" : json_object["CardBusStatisticsServiceNew"]["row"][a]["BUS_ROUTE_NO"],            
          '시군구코드' : sigungoo,
          'RIDE_PASGR_NUM' : json_object["CardBusStatisticsServiceNew"]["row"][a]["RIDE_PASGR_NUM"],
          'ALIGHT_PASGR_NUM' : json_object["CardBusStatisticsServiceNew"]["row"][a]["ALIGHT_PASGR_NUM"]
        }
        client.index(index="buspassenger", id=count, body=body)
        count=count+1
        ERROR=True
      else:
       ERROR=False
    except:
       ERROR=False





