import requests
import json
import io
import os
from dotenv import load_dotenv
load_dotenv()
AUTH_TOKEN = os.getenv('ATMN_TOKEN')

def get_bill_info(bill_id):
    cookies = {
        'cf_clearance': 'wd2f8L.7ie3w2qUzu6rjMwj.8ytKtkxeMqq1mAp0mVw-1735491457-1.2.1.1-KHH9DiP1flNz32OvxN8uWgX.r.dMx9OkRUeEezQmK1exnYDb5ahlPs05TMeTTxhh3jj3OD59tPFjZdNNMD5M54kqBfexGu8swd6Z9rR0aYqyHCi459hWP_Xg0GB4kb19Ufh027vg1WnQeTGPFwvn57nJp2Um8APL8wT6IRk.ZmPnBzbt8UKixpfG.QmDOJN4dGx8Zjs9YpBzil7XU_oHSHUB5WG2YHQRA0X3f_.V3zhyTNoUqqoiOKmu3jOHEjKMwisGvg4ISt0SdC8Z_Px5j2chKP2.rqOPZvKLbBYWFSFR4zuWEi3uTv6RVdL9eg_lnEqSGSleE04Kwk6X1M8U0gpEEUyFe6r0tD1H8ENd7k5E9.F35DxrOb7xOtvas0lz9zNrp2akB1x_5VRRsq.CBg',
        'env': 'g1',
        'dbid': 'b06b55db-a9f5-44b0-975b-1109f4ea6404',
        'env_b06b55db_a9f5_44b0_975b_1109f4ea6404_1_13_2025': 'g1',
        'TS01a7d1ca': '019ba1692d975c0345ffdef2fea5ec17f18909d80d71fc39dcc4c76a21cd7f022f4c9698c475d2fc22eced4385a26d8e2a3cb44617',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Authorization': f'Bearer {AUTH_TOKEN}',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'cf_clearance=wd2f8L.7ie3w2qUzu6rjMwj.8ytKtkxeMqq1mAp0mVw-1735491457-1.2.1.1-KHH9DiP1flNz32OvxN8uWgX.r.dMx9OkRUeEezQmK1exnYDb5ahlPs05TMeTTxhh3jj3OD59tPFjZdNNMD5M54kqBfexGu8swd6Z9rR0aYqyHCi459hWP_Xg0GB4kb19Ufh027vg1WnQeTGPFwvn57nJp2Um8APL8wT6IRk.ZmPnBzbt8UKixpfG.QmDOJN4dGx8Zjs9YpBzil7XU_oHSHUB5WG2YHQRA0X3f_.V3zhyTNoUqqoiOKmu3jOHEjKMwisGvg4ISt0SdC8Z_Px5j2chKP2.rqOPZvKLbBYWFSFR4zuWEi3uTv6RVdL9eg_lnEqSGSleE04Kwk6X1M8U0gpEEUyFe6r0tD1H8ENd7k5E9.F35DxrOb7xOtvas0lz9zNrp2akB1x_5VRRsq.CBg; env=g1; dbid=b06b55db-a9f5-44b0-975b-1109f4ea6404; env_b06b55db_a9f5_44b0_975b_1109f4ea6404_1_13_2025=g1; TS01a7d1ca=019ba1692d975c0345ffdef2fea5ec17f18909d80d71fc39dcc4c76a21cd7f022f4c9698c475d2fc22eced4385a26d8e2a3cb44617',
        'Origin': 'https://actapp.misa.vn',
        'Referer': 'https://actapp.misa.vn/app/SA/SAVoucher',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'X-Device': '93cb8228535738a13fa88ff719acf469',
        'X-MISA-Context': '{"TenantId":"a933309c-b6b1-4148-ab04-916e297998e4","TenantCode":"DPRVDCS2","DatabaseId":"b06b55db-a9f5-44b0-975b-1109f4ea6404","BranchId":"21f30aff-b592-4fcd-8efd-652a57aee401","WorkingBook":0,"Language":"vi","IncludeDependentBranch":"false","SessionId":"ss3ddc267c2ec943309a1c6494bbc0a653.93cb8228535738a13fa88ff719acf469.b06b55dba9f544b0975b1109f4ea6404.638723932729033674","DBType":1,"AuthType":0,"AmisSessionId":"YQA5ADMAMwAzADAAOQBjAGIANgBiADEANAAxADQAOABhAGIAMAA0ADkAMQA2AGUAMgA5ADcAOQA5ADgAZQA0AGMANABjAGQAZQA2ADcAYQBmADQAYwAzADQAOQA0ADkAOAA3AGYAZABiAGIAOAAwADkAMwA3ADgANwA3ADkAZAA=","HasAgent":false,"UserType":1,"art":0,"UserId":"3ddc267c-2ec9-4330-9a1c-6494bbc0a653","isc":false}',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'sort': '[{"property":3654,"desc":true,"data_type":3,"operand":1},{"property":4018,"desc":true,"data_type":1,"operand":1}]',
        'filter': [
            {
                'property': 3654,
                'value': '2023-12-31T17:00:00.00Z',
                'operator': 10,
                'operand': 1,
                'data_type': 3,
            },
            {
                'property': 3654,
                'value': '2025-01-13T12:27:53.555Z',
                'operator': 12,
                'operand': 1,
                'data_type': 3,
            },
        ],
        'customFilter': [
            {
                'property': 4018,
                'value': bill_id,
                'operator': 1,
                'operand': 1,
                'childrens': [
                    {
                        'property': 2189,
                        'value': bill_id,
                        'operator': 1,
                        'operand': 2,
                        'data_type': 1,
                    },
                    {
                        'property': 57,
                        'value': bill_id,
                        'operator': 1,
                        'operand': 2,
                        'data_type': 1,
                    },
                ],
                'data_type': 1,
            },
        ],
        'pageIndex': 1,
        'pageSize': 20,
        'useSp': False,
        'view': 1,
        'summaryColumns': [
            5126,
            5068,
            5141,
            5039,
        ],
        'loadMode': 2,
    }

    r = requests.post(
        'https://actapp.misa.vn/g1/api/sa/v1/sa_voucher_get/paging_filter_v2',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    response = json.load(io.BytesIO(r.content))

    if "Data" in response and "PageData" in response["Data"] and len(response["Data"]["PageData"]) > 0:
        newest_bill = response["Data"]["PageData"][0]
        tax_code = newest_bill["account_object_tax_code"]
        total_amount_on_bill = newest_bill["total_amount"]
        ref_id = newest_bill["refid"]
        return tax_code, total_amount_on_bill, ref_id
    else:
        return ""

def get_paging_detail(refid):
    global AUTH_TOKEN
    cookies = {
        'cf_clearance': 'wd2f8L.7ie3w2qUzu6rjMwj.8ytKtkxeMqq1mAp0mVw-1735491457-1.2.1.1-KHH9DiP1flNz32OvxN8uWgX.r.dMx9OkRUeEezQmK1exnYDb5ahlPs05TMeTTxhh3jj3OD59tPFjZdNNMD5M54kqBfexGu8swd6Z9rR0aYqyHCi459hWP_Xg0GB4kb19Ufh027vg1WnQeTGPFwvn57nJp2Um8APL8wT6IRk.ZmPnBzbt8UKixpfG.QmDOJN4dGx8Zjs9YpBzil7XU_oHSHUB5WG2YHQRA0X3f_.V3zhyTNoUqqoiOKmu3jOHEjKMwisGvg4ISt0SdC8Z_Px5j2chKP2.rqOPZvKLbBYWFSFR4zuWEi3uTv6RVdL9eg_lnEqSGSleE04Kwk6X1M8U0gpEEUyFe6r0tD1H8ENd7k5E9.F35DxrOb7xOtvas0lz9zNrp2akB1x_5VRRsq.CBg',
        'TS01a7d1ca': '019ba1692d27e1cb38348ecaff8fd70ed64617eea2846bda75cf1ad7b7d7c2a72928e2c242695684bf3e90187785eed1a106341ffc',
        'env': 'g1',
        'env_44ccc375_765c_447e_a1a8_176925051543_1_12_2025': 'g1',
        'dbid': 'b06b55db-a9f5-44b0-975b-1109f4ea6404',
        'env_b06b55db_a9f5_44b0_975b_1109f4ea6404_1_12_2025': 'g1',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Authorization': f'Bearer {AUTH_TOKEN}',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'cf_clearance=wd2f8L.7ie3w2qUzu6rjMwj.8ytKtkxeMqq1mAp0mVw-1735491457-1.2.1.1-KHH9DiP1flNz32OvxN8uWgX.r.dMx9OkRUeEezQmK1exnYDb5ahlPs05TMeTTxhh3jj3OD59tPFjZdNNMD5M54kqBfexGu8swd6Z9rR0aYqyHCi459hWP_Xg0GB4kb19Ufh027vg1WnQeTGPFwvn57nJp2Um8APL8wT6IRk.ZmPnBzbt8UKixpfG.QmDOJN4dGx8Zjs9YpBzil7XU_oHSHUB5WG2YHQRA0X3f_.V3zhyTNoUqqoiOKmu3jOHEjKMwisGvg4ISt0SdC8Z_Px5j2chKP2.rqOPZvKLbBYWFSFR4zuWEi3uTv6RVdL9eg_lnEqSGSleE04Kwk6X1M8U0gpEEUyFe6r0tD1H8ENd7k5E9.F35DxrOb7xOtvas0lz9zNrp2akB1x_5VRRsq.CBg; TS01a7d1ca=019ba1692d27e1cb38348ecaff8fd70ed64617eea2846bda75cf1ad7b7d7c2a72928e2c242695684bf3e90187785eed1a106341ffc; env=g1; env_44ccc375_765c_447e_a1a8_176925051543_1_12_2025=g1; dbid=b06b55db-a9f5-44b0-975b-1109f4ea6404; env_b06b55db_a9f5_44b0_975b_1109f4ea6404_1_12_2025=g1',
        'Origin': 'https://actapp.misa.vn',
        'Referer': 'https://actapp.misa.vn/app/SA/SAVoucher',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'X-Device': '93cb8228535738a13fa88ff719acf469',
        'X-MISA-Context': '{"TenantId":"a933309c-b6b1-4148-ab04-916e297998e4","TenantCode":"DPRVDCS2","DatabaseId":"b06b55db-a9f5-44b0-975b-1109f4ea6404","BranchId":"21f30aff-b592-4fcd-8efd-652a57aee401","WorkingBook":0,"Language":"vi","IncludeDependentBranch":"false","SessionId":"ss3ddc267c2ec943309a1c6494bbc0a653.93cb8228535738a13fa88ff719acf469.44ccc375765c447ea1a8176925051543.638722906280862638","DBType":1,"AuthType":0,"AmisSessionId":"YQA5ADMAMwAzADAAOQBjAGIANgBiADEANAAxADQAOABhAGIAMAA0ADkAMQA2AGUAMgA5ADcAOQA5ADgAZQA0AGMANABjAGQAZQA2ADcAYQBmADQAYwAzADQAOQA0ADkAOAA3AGYAZABiAGIAOAAwADkAMwA3ADgANwA3ADkAZAA=","HasAgent":false,"UserType":1,"art":0,"UserId":"3ddc267c-2ec9-4330-9a1c-6494bbc0a653","isc":false}',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'columns': [
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
            2358,
        ],
        'sort': '[{"property":4555,"desc":false,"data_type":4,"operand":1}]',
        'filter': [
            {
                'property': 3993,
                'operator': 7,
                'operand': 1,
                'value': refid,
                'data_type': 10,
            },
        ],
        'pageIndex': 1,
        'pageSize': 20,
        'useSp': False,
        'view': 96,
        'summaryColumns': [
            3488,
            3870,
            308,
            5350,
        ],
        'loadMode': 2,
    }

    r = requests.post(
        'https://actapp.misa.vn/g1/api/sa/v1/sa_voucher_get/get_paging_detail',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    response = json.load(io.BytesIO(r.content))
    print(response)
    if "Data" in response and "PageData" in response["Data"] and len(response["Data"]["PageData"]) > 0:
        print(len(response["Data"]["PageData"]))
        newest_bill = response["Data"]["PageData"][0]
        good_code = newest_bill["inventory_item_code"]
        print(good_code)
        if good_code == "KIEM DINH":
            return "Thu tiền kiểm định HD " 
        if good_code == "HUAN LUYEN":
            return "Thu tiền huấn luyện HD "
        else:
            return "Thu tiền đào tạo HD "
    else:
        return ""
    
# print(get_paging_detail("02a922c7-1b02-4030-b68a-1f6ec1362665"))
# print(get_paging_detail("2a4ce4ad-ee84-4049-9d2f-12f6d0f74220"))

print(get_bill_info("001697"))
print(get_paging_detail(get_bill_info("001697")[-1]))