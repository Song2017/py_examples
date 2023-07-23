from locust import HttpUser, task, between


class Order(HttpUser):
    # locust -f order_callback.py --host=http://localhost:8080
    wait_time = between(1, 2)

    # def on_start(self):
    #     self.client.post("/login", json={"username": "foo", "password": "bar"})

    @task
    def hello_world(self):
        url = "http://localhost:8080/z/callback/order?app_key=6910368270755923471_test&" \
              "timestamp=2022-12-18%2018%3A00%3A04&sign=519e243278ed45b84eb05fa7ee3f7eaa&Authorization=test"

        payload = {
            "logid": "20221218160000010210027143220B2568",
            "msg_type": "order_info_notify",
            "order_info_notify": {
                "actual_paid": 24600,
                "buyer_id_number": "530102198502043747",
                "buyer_id_type": 1,
                "buyer_name": "薛晗",
                "buyer_reg_no": "1748671504562191836",
                "buyer_telephone": "13378846119",
                "carrier_code": "",
                "consignee": "筠涵",
                "consignee_address": "{\"province\":{\"id\":\"53\",\"name\":\"云南省\"},\"city\":{\"id\":\"530100\",\"name\":\"昆明市\"},\"town\":{\"id\":\"530112\",\"name\":\"西山区\"},\"street\":{\"id\":\"530112005\",\"name\":\"前卫街道\"},\"detail\":\"广福路1006号香槟小镇十栋三单元\"}",
                "consignee_telephone": "13378846119",
                "create_time": 1671357603,
                "currency": "142",
                "customs_clear_type": 2,
                "customs_code": "5141",
                "discount": 0,
                "ebp_code": "11089697EJ",
                "ebp_name": "北京空间变换科技有限公司",
                "exp_ship_time": 1671789602,
                "extend": "{\"inventoryDeclare\":\"F\",\"logisticsDeclare\":\"F\",\"orderDeclare\":\"F\"}",
                "freight": 0,
                "goods_value": 22548,
                "ie_flag": "I",
                "insured_fee": 0,
                "note": "",
                "order_detail_list": [
                    {
                        "bar_code": "5017205012658",
                        "brand_name": "Napiers",
                        "country": "303",
                        "currency": "142",
                        "first_measure_qty": 0.1,
                        "first_measure_unit": "千克",
                        "g_model": "4|3|护肤|100ml/罐|Napiers",
                        "gnum": 1,
                        "gross_weight": 0.2,
                        "hs_code": "3304990039",
                        "ingredient_desc": "水、高岭土、植物甘油、山梨醇橄榄酸酯、鲸蜡酰橄榄酸酯、麦片醇、洋甘菊、硬脂酸，氧化锌、苄醇、水杨酸、甘油、抗坏血酸磷酸钠、山梨酸、油酸钾、椰酸钾、柠檬酸钾、柠檬酸、库拉索芦荟、金盏草提取物粉、维生素E、乳酸、天竺葵、柠檬汁CI 77820、麦芽糊精",
                        "is_otc": 0,
                        "item_describe": "",
                        "item_id": "7171697279542362399",
                        "item_name": "【直邮】Napiers微银深层清洁面膜100ml",
                        "item_no": "5017205012658",
                        "net_weight_qty": 0.1,
                        "otc_reg_no": "",
                        "postal_code": "",
                        "price": 22548,
                        "qty": 1,
                        "record_name": "",
                        "record_name_en": "Napiers深层清洁面膜100ml/罐",
                        "record_part_no": "7172022220586483979",
                        "second_measure_qty": 1,
                        "second_measure_unit": "件",
                        "sku_id": 1752380153583719,
                        "specification": "4|3|护肤|100ml/罐|Napiers",
                        "total_price": 22548,
                        "unit": "罐",
                        "unit_declare": "罐"
                    }
                ],
                "order_id": "test",
                "pack_no": 1,
                "pay_code": "4201960AED",
                "pay_name": "武汉合众易宝科技有限公司",
                "pay_time": 1671350402,
                "pay_transaction_id": "HZ7178395319825072138101",
                "port_code": "5141",
                "pre_sale_type": 0,
                "scsp_warehouse_code": "SFBCJH06",
                "shop_id": 1815694,
                "tax_total": 2052,
                "warehouse_code": "SFBCJH06",
                "wh_type": 2
            }
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = self.client.request("POST", url, headers=headers, json=payload)
        print(response.text)

    # @task(3)
    # def view_item(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
