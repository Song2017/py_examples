import asyncio
import json

import arrow
import requests
import concurrent.futures


def local_test(payload_in: str = ""):
    url = "http://localhost:8080/z/callback/order?app_key=6910368270755923471_test&" \
          "timestamp=2022-12-18%2018%3A00%3A04&sign=519e243278ed45b84eb05fa7ee3f7eaa&Authorization=test"

    payload = {
        "logid": "20221218160000010210027143220B2568",
        "msg_type": "order_info_notify",
        "order_info_notify": {
            "actual_paid": 24600,
 
        }
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    return response.json(), response.status_code


async def main(info_in: list):
    print(arrow.now())
    result = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        loop_in = asyncio.get_event_loop()
        futures = [
            loop_in.run_in_executor(
                executor,
                local_test,
                data
            )
            for data in info_in
        ]
        for response in await asyncio.gather(*futures):
            result.append(response)
    print(arrow.now())
    with open('./test.json', 'w') as f:
        f.write(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    # payload = {
    #     "name": "string",
    #     "description": "string",
    #     "content": "string"
    # }
    #
    # local_test(payload)
    data_info = list(range(10))
    _loop = asyncio.get_event_loop()
    _loop.run_until_complete(main(data_info))
