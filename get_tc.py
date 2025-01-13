import requests
import json
import io

# smeToken
AUTH_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI5NGYyYmY0NS0yYjRhLTRlZjQtOWJiMS05ZjkyMDFkZTZjOTQiLCJ1bmEiOiJOR1VZRU5OR09DIiwiYXV0IjoiMCIsInVlbSI6InR1eWV0bmdvYzkxLmtyYkBnbWFpbC5jb20iLCJuYmYiOjE3MzYyMjIwOTEsImV4cCI6MTczNjMwODUxNywiaWF0IjoxNzM2MjIyMDkxLCJpc3MiOiJNSVNBSlNDIn0.XUpdf42UsV7bJSYneMBt6d6TVcNHRE8dtX5eg31JCas"
my_headers = {
    "Accept" : "application/json, text/plain, */*",
    "Accept-Encoding" : "gzip, deflate, br, zstd",
    "Accept-Language" : "en-US,en;q=0.9,vi;q=0.8", 
    "Authorization" : f"Bearer {AUTH_TOKEN}",
    "Connection" : "keep-alive",
    "Content-Type" : "application/json",
    "Cookie" : "env=g2; env_b06b55db_a9f5_44b0_975b_1109f4ea6404_12_29_2024=g2; dbid=44ccc375-765c-447e-a1a8-176925051543; env_44ccc375_765c_447e_a1a8_176925051543_12_29_2024=g2; TS01a7d1ca=019ba1692d1cdf94e989b1aedcead44b5ddc0813364c192f8788ff93404556101599bda894b3ff14f19c5df0d5e2252d2ba01d354f",
    "Host" : "actapp.misa.vn",
    "Origin" : "https://actapp.misa.vn",
    "Referer" : "https://actapp.misa.vn/app/SA/SAVoucher",
    "Sec-Fetch-Dest" : "empty",
    "Sec-Fetch-Mode" : "cors",
    "Sec-Fetch-Site" : "same-origin",
    "X-Device" : "93cb8228535738a13fa88ff719acf469",
    "X-MISA-Context": "{\"TenantId\":\"a933309c-b6b1-4148-ab04-916e297998e4\",\"TenantCode\":\"DPRVDCS2\",\"DatabaseId\":\"44ccc375-765c-447e-a1a8-176925051543\",\"BranchId\":\"c9707f99-d9c5-49d7-9be0-8f6a8061c479\",\"WorkingBook\":0,\"Language\":\"vi\",\"IncludeDependentBranch\":\"false\",\"SessionId\":\"ss1b585558e49f49a2bc9616c8a74b7475.93cb8228535738a13fa88ff719acf469.b06b55dba9f544b0975b1109f4ea6404.638711095725021734\",\"DBType\":1,\"AuthType\":0,\"AmisSessionId\":\"YQA5ADMAMwAzADAAOQBjAGIANgBiADEANAAxADQAOABhAGIAMAA0ADkAMQA2AGUAMgA5ADcAOQA5ADgAZQA0ADkANwA1AGMAOABhADQAMQBiAGIAYwAwADQAMQAzAGUAOAA0ADEAOAA4ADcAOQA0ADQAMgAxADAAOQA5AGQANAA=\",\"HasAgent\":false,\"UserType\":1,\"art\":2,\"UserId\":\"1b585558-e49f-49a2-bc96-16c8a74b7475\",\"isc\":false}",
}

def get_bill_info(bill_id, debug = False):
    global my_headers
    r = requests.post(
        url = "https://actapp.misa.vn/g2/api/sa/v1/sa_voucher_get/paging_filter_v2",
        headers = my_headers,
        json = {
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
                ],
                "data_type": 1
            }]
        }
    )
    response = json.load(io.BytesIO(r.content))
    newest_bill = response["Data"]["PageData"][0]
    tax_code = newest_bill["account_object_tax_code"]
    total_amount_on_bill = newest_bill["total_amount"]
    # print(response["Data"]["PageData"])
    if debug:
        return newest_bill
    return tax_code, total_amount_on_bill
