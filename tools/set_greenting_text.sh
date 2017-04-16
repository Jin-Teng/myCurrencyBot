#!/bin/sh

TOKEN="$1"
TEXT="$2"

curl -X POST \
  "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=$TOKEN" \
  -H 'content-type: application/json' \
  -d "{
  \"greeting\":[
    {
      \"locale\":\"default\",
      \"text\":\"$TEXT\"
    }
  ] 
}"
