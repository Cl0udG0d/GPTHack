import requests
import uuid
def main():
    url = "https://liaobots.work"
    headers = {
        "authority": "liaobots.work",
        "content-type": "application/json",
        "origin": url,
        "referer": f"{url}/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    }
    _auth_code = None
    proxy = None
    messages = [{"role": "user", "content": "一个猎人往北走了一英里，往东走了一英里，往南走了一英里，然后回到了起点。这时他看到一只熊。这只熊是什么颜色?"}]
    model = {"id": "gpt-4-plus", "name": "GPT-4-Plus", "maxLength": 130000, "tokenLimit": 31000, "context": "32K"}
    print(messages)
    with requests.Session() as session:
        if not _auth_code:
            response = session.post(
                "https://liaobots.work/recaptcha/api/login",
                proxies={"http": proxy, "https": proxy},
                data={"token": "abcdefghijklmnopqrst"},
                headers=headers,
                verify=False
            )
            response.raise_for_status()

            response = session.post(
                "https://liaobots.work/api/user",
                proxies={"http": proxy, "https": proxy},
                json={"authcode": ""},
                headers=headers,
                verify=False
            )
            print(response.text)
            response.raise_for_status()
            _auth_code = response.json()["authCode"]
            print(_auth_code)

        data = {
            "conversationId": str(uuid.uuid4()),
            "model": model,
            "messages": messages,
            "key": "",
            "prompt": "你是 ChatGPT，一个由 OpenAI 训练的大型语言模型，请仔细遵循用户的指示。",
        }
        # print(data)

        headers["x-auth-code"] = _auth_code
        # response = __make_request(session)
        response = session.post(
            "https://liaobots.work/api/chat",
            proxies={"http": proxy, "https": proxy},
            json=data,
            headers=headers,
            verify=False
        )
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()