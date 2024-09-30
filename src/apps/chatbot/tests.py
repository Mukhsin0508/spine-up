import requests

BASE_URL = "http://localhost:8000"

def test_create_conversation():
    url = f"{BASE_URL}/conversations/"
    response = requests.post(url)
    print("Create Conversation Response:", response.json())
    return response.json()['id']

def test_list_conversations():
    url = f"{BASE_URL}/conversations/"
    response = requests.get(url)
    print("List Conversations Response:", response.json())

def test_send_message(conversation_id):
    url = f"{BASE_URL}/messages/"
    data = {
        "conversation": conversation_id,
        "content": "Hello, how are you?"
    }
    response = requests.post(url, json=data)
    print("Send Message Response:", response.json())

def test_list_messages():
    url = f"{BASE_URL}/messages/"
    response = requests.get(url)
    print("List Messages Response:", response.json())

if __name__ == "__main__":
    conversation_id = test_create_conversation()
    test_list_conversations()
    test_send_message(conversation_id)
    test_list_messages()