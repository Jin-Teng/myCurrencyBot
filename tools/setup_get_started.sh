#!/bin/sh

TOKEN="$1"
echo $TOKEN
curl -X POST \
  "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=$TOKEN" \
  -H 'content-type: application/json' \
  -d '{ 
  "get_started":{
    "payload":"GET_STARTED"
  }
}'
