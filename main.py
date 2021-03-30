#-*- encoding: utf-8 -*-
from marshmallow import fields, Schema, validate
import requests

class Activity: # <- dataclass não existe no python 2.7
    activity = ""
    participants = 0
    price = 0.0

    def __init__(self, *args, **kwargs):
        for k,v in kwargs.items():
            # TODO: validar o tipo e o nome dos dados válidos simulando dataclasses?
            setattr(self, k, v)

    def __str__(self):
        return "Activity(activity=\"{}\",participants={},price={})".format(self.activity,self.participants,self.price)
                      
class ActivitySchema(Schema):
    activity = fields.Str(required=True)
    participants = fields.Int(required=True)
    price = fields.Float(required=True)
                                          
def get_activity():
    resp = requests.get("https://www.boredapi.com/api/activity").json()
    validated_resp = ActivitySchema().load(resp)

    return Activity(
        activity=validated_resp.data["activity"],
        participants=validated_resp.data["participants"],
        price=validated_resp.data["price"]
    )

print(get_activity())

# Will print something like this:
# Activity(activity='Prepare a 72-hour kit', participants=1, price=0.5)