import requests
import json
import io

# smeToken
AUTH_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI5NGYyYmY0NS0yYjRhLTRlZjQtOWJiMS05ZjkyMDFkZTZjOTQiLCJ1bmEiOiJOR1VZRU5OR09DIiwiYXV0IjoiMCIsInVlbSI6InR1eWV0bmdvYzkxLmtyYkBnbWFpbC5jb20iLCJuYmYiOjE3MzY2NDE1MzAsImV4cCI6MTczNjcyNzkzMiwiaWF0IjoxNzM2NjQxNTMwLCJpc3MiOiJNSVNBSlNDIn0.g065p9W3py4hYJer3ORag_gKpGsP5HYQHnBCcjClRB4"
my_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8",
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Connection": "keep-alive",
    "Content-Length": "765",
    "Content-Type": "application/json",
    "Cookie": "env=g1; cf_clearance=qL71AP1NkCallzlxiURqQfHJd9Xp0l7LDVOjJxWNN7c-1736245682-1.2.1.1-MSKAhnxbpD0kICNsDibjdonIA8ym9Hwo72xEcpfsql2C.4y0vQDwm2KNgGZIUsjS3nSKk.62axxfLQG7nijt7KlExcBrzpChwCQZsY4F5JCVeFtC0ThXDww.7flNBJeU2AdM5QuwGL9HXkuq3AiLdI0UVCnEwszVcdzRK90LmB5ZIW5KTensc0ruSKR01seJQ9g9lxl7pSZVxXhQNh_i_UkUYHF48OEcjxzYe57qAtUAlPXOB4aSkWS2xoGYA_vkR4IvbHD89vPvaw_yWBBpAZeQzJKSC5cSa9d4RzgCir1DSP1y4uqT6gngTeXMs30biNrledtSlyJ4uscjbjobOvAOGf9h3V142ccdg8C4rv4iJWO3c8tBLgu_pAsavxzNmN5mFHx5oHgkCLbJHGAdRw; _ga_YH7NZ9JK2J=GS1.1.1736243693.1.1.1736246109.0.0.0; env_b06b55db_a9f5_44b0_975b_1109f4ea6404_10_1_2025=g1; env_44ccc375_765c_447e_a1a8_176925051543_10_1_2025=g1; _gid=GA1.2.2110962665.1736480298; _ga_4N8J1W6EBF=GS1.1.1736480298.2.0.1736480298.0.0.0; _ga=GA1.1.1663517630.1736221990; dbid=b06b55db-a9f5-44b0-975b-1109f4ea6404; TS01a7d1ca=019ba1692d0d8e0292d6748b52712a9f7834369310651cde1c37ce1e80b66c7d1423cdd6b7c4a94af6202b6f378605ae5ff4497631; _ga_2B9RDZ4E89=GS1.1.1736480289.3.1.1736481537.0.0.0",
    "Host": "actapp.misa.vn",
    "Origin": "https://actapp.misa.vn",
    "Referer": "https://actapp.misa.vn/app/SA/SAVoucher",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "X-Device": "2d0521caaf1af634bc3c9170f3186cd2",
    "X-MISA-Context": '{"TenantId":"a933309c-b6b1-4148-ab04-916e297998e4","TenantCode":"DPRVDCS2","DatabaseId":"b06b55db-a9f5-44b0-975b-1109f4ea6404","BranchId":"21f30aff-b592-4fcd-8efd-652a57aee401","WorkingBook":0,"Language":"vi","IncludeDependentBranch":"False","SessionId":"ss94f2bf452b4a4ef49bb19f9201de6c94.2d0521caaf1af634bc3c9170f3186cd2.44ccc375765c447ea1a8176925051543.638721023098029132","DBType":1,"AuthType":0,"AmisSessionId":"YQA5ADMAMwAzADAAOQBjAGIANgBiADEANAAxADQAOABhAGIAMAA0ADkAMQA2AGUAMgA5ADcAOQA5ADgAZQA0AGIANwA2ADkAYgBiAGIAZQA1ADAAOAA0ADQAZQBmAGYAOQA3ADYAMAA0ADIAMwA0ADkAMABmADcAMwBlAGIANQA=","HasAgent":False,"UserType":1,"art":0,"UserId":"94f2bf45-2b4a-4ef4-9bb1-9f9201de6c94","isc":False}',
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

# ...existing code...

def get_bill_info(bill_id):
    response = requests.post(
        url="https://actapp.misa.vn/g1/api/sa/v1/sa_voucher_get/paging_filter_v2",
        headers=my_headers,
        json={
            "customFilter": [
                {
                    "property": 4018,
                    "value": bill_id,
                    "operator": 1,
                    "operand": 1,
                    "childrens": [
                        {
                            "property": 2189,
                            "value": bill_id,
                            "operator": 1,
                            "operand": 2,
                            "data_type": 1
                        },
                        {
                            "property": 34,
                            "value": bill_id,
                            "operator": 1,
                            "operand": 2,
                            "data_type": 1
                        },
                        {
                            "property": 57,
                            "value": bill_id,
                            "operator": 1,
                            "operand": 2,
                            "data_type": 1
                        }
                    ]
                }
            ]
        }
    ).json()

    if "Data" in response and "PageData" in response["Data"] and len(response["Data"]["PageData"]) > 0:
        newest_bill = response["Data"]["PageData"][0]
        tax_code = newest_bill["account_object_tax_code"]
        total_amount_on_bill = newest_bill["total_amount"]
        return tax_code, total_amount_on_bill
    else:
        return ""
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8",
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Connection": "keep-alive",
    "Content-Length": "387",
    "Content-Type": "application/json",
    "Cookie": "env=g1; dbid=b06b55db-a9f5-44b0-975b-1109f4ea6404; env_b06b55db_a9f5_44b0_975b_1109f4ea6404_1_12_2025=g1; _ga_4N8J1W6EBF=GS1.1.1736641511.15.0.1736641511.0.0.0; _gid=GA1.2.1513097689.1736641511; _ga=GA1.1.1300888454.1734964560; mp_844407e91b119d6a00359efeff26eaa4_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A193f3f273596645-05d82df40412cc-4c657b58-100200-193f3f273596646%22%2C%22%24device_id%22%3A%20%22193f3f273596645-05d82df40412cc-4c657b58-100200-193f3f273596646%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Factapp.misa.vn%2F%22%2C%22%24initial_referring_domain%22%3A%20%22actapp.misa.vn%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Factapp.misa.vn%2F%22%2C%22%24initial_referring_domain%22%3A%20%22actapp.misa.vn%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; TS01a7d1ca=019ba1692d5fdb8624c0314bfdbbc493b2f0fdfa0660e6c65896c8ffb333d4dc79802f9ea8f876de4af0e97e2fe89c0861c3712a7f; _ga_2B9RDZ4E89=GS1.1.1736650750.23.1.1736650874.0.0.0",
    "Host": "actapp.misa.vn",
    "Origin": "https://actapp.misa.vn",
    "Referer": "https://actapp.misa.vn/app/SA/SAVoucher",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "X-Device": "5535b7b93e5e3323a8273b7f0f46a7f1",
    "X-MISA-Context": json.dumps({
        "TenantId": "a933309c-b6b1-4148-ab04-916e297998e4",
        "TenantCode": "DPRVDCS2",
        "DatabaseId": "b06b55db-a9f5-44b0-975b-1109f4ea6404",
        "BranchId": "21f30aff-b592-4fcd-8efd-652a57aee401",
        "WorkingBook": 0,
        "Language": "vi",
        "IncludeDependentBranch": "False",
        "SessionId": "ss94f2bf452b4a4ef49bb19f9201de6c94.5535b7b93e5e3323a8273b7f0f46a7f1.b06b55dba9f544b0975b1109f4ea6404.638722635305500969",
        "DBType": 1,
        "AuthType": 0,
        "AmisSessionId": "YQA5ADMAMwAzADAAOQBjAGIANgBiADEANAAxADQAOABhAGIAMAA0ADkAMQA2AGUAMgA5ADcAOQA5ADgAZQA0ADEANQAzADYAZgA4ADkAMAA2ADIAMgBkADQAYQA4ADEAYgBmAGMAMAAwADIAOQAyADIAYgAxAGQAZgA4AGYAZgA=",
        "HasAgent": False,
        "UserType": 1,
        "art": 0,
        "UserId": "94f2bf45-2b4a-4ef4-9bb1-9f9201de6c94",
        "isc": False
    }),  
}
def get_paging_detail(refid):
    response = requests.post(
        url= "https://actapp.misa.vn/g1/api/sa/v1/sa_voucher_get/get_paging_detail",
        headers=headers,
        json= {"columns": [
                    2157,
                    1355,
                    1195,
                    1065,
                    5274,
                    3870,
                    5279,
                    308,
                    5364,
                    5350,
                    5347,
                    2818,
                    1684,
                    3404,
                    5476,
                    2358
                ],
                "sort": [
                    {
                    "property": 4555,
                    "desc": False,
                    "data_type": 4,
                    "operand": 1
                    }
                ],
                "filter": [
                    {
                    "property": 3993,
                    "operator": 7,
                    "operand": 1,
                    "value": refid,
                    "data_type": 10
                    }
                ],
                "pageIndex": 1,
                "pageSize": 20,
                "useSp": False,
                "view": 96,
                "summaryColumns": [
                    3488,
                    3870,
                    308,
                    5350
                ],
                "loadMode": 2
                }

    ).json()
    print(response)
    if "Data" in response and "PageData" in response["Data"] and len(response["Data"]["PageData"]) > 0:
        newest_bill = response["Data"]["PageData"][0]
        good_code = newest_bill["inventory_item_code"]
        print(good_code)
        if good_code == "KIEM DINH":
            return "Thu tieenf kieemr ddinhj HD " 
        if good_code == "HUAN LUYEN":
            return "Thu tieenf huaans luyeenj HD "
        else:
            return "Thu tieenf ddaof taoj HD "
    else:
        return "KO"
print(get_paging_detail("2d351f0c-aa09-4824-8538-424e7c2a48e6"))