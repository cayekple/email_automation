#!/usr/bin/env python3

import os
import requests

BSD = os.path.expanduser("~")+"/supplier-data/descriptions/"
list_text = os.listdir(BSD)

BSI = os.path.expanduser("~")+"/supplier-data/images/"
list_images = os.listdir(BSI)
images = [image_name for image_name in list_images if '.jpeg' in image_name]


list = []

for texts in list_text:
  with open(BSD+texts, 'r') as f:
    data = {"name": f.readline().rstrip("\n"),
    "weight" : int(f.readline().rstrip("\n").split(' ')[0]),
    "description": f.readline().rstrip("\n")}
    for img in images:
      if img.split('.')[0] in texts.split('.')[0]:
        data['image_name'] = img
    list.append(data)

for item in list:
  resp = requests.post('http://localhost:80/fruits/', json=item)
  if resp.status_code != 201:
    raise Exception("POST error status={}".format(resp.status_code))
  print("Created feedback ID: {}".format(resp.json()["id"]))
