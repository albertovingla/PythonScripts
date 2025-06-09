#!/usr/bin/env python3
import sys
import urllib.parse
import urllib.request
import requests
import json

BASE_URL = "https://api.z-api.io"
INSTANCE_ID = "YOUR_INSTANCE_ID"
INSTANCE_TOKEN = "YOUR_INSTANCE_TOKEN"
CLIENT_TOKEN = "YOUT_CLIENT_TOKEN"

def send_whatsapp_message(phone):
    api_url = f"{BASE_URL}/instances/{INSTANCE_ID}/token/{INSTANCE_TOKEN}/send-text"

    payload = {
        "phone": phone,
        "message": "Olá! Me chamo NOME e este é um teste de uma AGI!"
    }

    headers = {
        "Content-Type": "application/json",
        "Client-Token": CLIENT_TOKEN
    }

    response = requests.post(api_url, json=payload, headers=headers)
    print(f"Response: {response.status_code} - {response.text}")

if __name__ == '__main__':
    phone = sys.argv[1] if len(sys.argv) > 1 else '00000000000'
    print("Enviando número:", phone)
    send_whatsapp_message(phone)
