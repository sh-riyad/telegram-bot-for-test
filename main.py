import requests
base_url = "https://api.telegram.org/bot5880364183:AAGKDV9-wvcEkWnJiOhStvGxsCWC__F3TBY"


def readMessage(offset) :
  parameters = {
      "offset" : offset
  }
  resp = requests.get(base_url + "/getUpdates",parameters)
  data = resp.json()
  for item in data["result"]:
    chat_id = item["message"]["chat"]["id"]
    user_id = item["message"]["from"]["id"]
    message = item["message"]["text"]
  # user_name = item["from"].get("username",user_id)
    sendMessage(chat_id,user_id,message)
  if data["result"] :
    return data["result"][-1]["update_id"]+1



def sendMessage(chat_id,user_id,message) : 
  parameters = {
      "chat_id" : chat_id,
      "text" : message
  }
  resp = requests.get(base_url + "/sendMessage",parameters)
  # print(resp.text)


offset=0
while True :
  offset = readMessage(offset)
