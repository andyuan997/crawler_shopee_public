from config.config import settings
from view.utils import timer
from view.check_ip_pool import CheckIPAddress
from view.api_v4_get_shop_detail import CrawlerShopDetail

# from view.api_v2_get_shop_detail import CrawlerShopDetail
# from view.api_v2_get_product_url import CrawlerProductId
# from view.api_v2_get_product_detail import CrawlerProductDetail
# from view.clean_data import run_clean

# from google.cloud import bigquery as bq

import pandas as pd


class Crawler:
    def __init__(self, user_dict):
        # # connect to bigqeury
        # self.client = bq.Client()

        # init
        self.input_shop_names = user_dict["input_shop_names"]
        self.user_email = user_dict["user_info"]["Email"]
        self.user_name = user_dict["user_info"]["Name"]

    @timer
    def __call__(self):

        # # Step 0 > check ip pool as expected (This step is not necessary.)
        # check_ip = CheckIPAddress()
        # check_ip(test_times=5)

        # Step 1 > input shop_names > get shop_detail
        crawler_shop_detail = CrawlerShopDetail()
        result_shop_detail = crawler_shop_detail(self.input_shop_names)
        print("step1_爬取商家數量：", len(result_shop_detail.index))

        # # Step 2 > input shop_detail > get product_id
        # crawler_product_id = CrawlerProductId()
        # result_product_id = crawler_product_id(result_shop_detail)
        # print("step2_爬取商家產品數：", len(result_product_id.index))

        # # Step 3 > input product_id > get product_detail
        # crawler_product_detail = CrawlerProductDetail()
        # result_product_detail = crawler_product_detail(result_product_id)
        # print("step3_爬取產品細節：", len(result_product_detail.index))

        # # Step 4 > combin & claen data > save data to Bigquery
        # df = pd.merge(
        #     result_product_detail, result_shop_detail, on=["shopid"], how="outer"
        # )

        # df["hashtag_list"] = df["hashtag_list"].astype(str)
        # df["time_stamp"] = df["time_stamp"].astype(str)
        # df["user_Name"] = self.user_name
        # df["user_Email"] = self.user_email
        # print("step4_清理資料 & 存入：", len(df.index))

        # To bigquery
        # table = self.client.dataset('crawler_product_detail').table('data')
        # job = self.client.load_table_from_dataframe(df, table)
        # job.result()


if __name__ == "__main__":

    # Insert your email and the shop names you want to crawl
    user_dict = {
        "a0025071@gmail.com": {
            "user_info": {
                "Email": "a0025071@gmail.com",
                "Name": "Max",
            },
            "input_shop_names": [
                "fulinxuan",
                "pat6116xx",
                "join800127",
                "ginilin0982353562",
                "ru8285fg56",
                "wangshutung",
                "taiwan88888",
                "cyf66666",
                "buddha8888",
                "dragon9168",
                "sinhochen77",
                "baoshenfg",
                "s0985881631",
                "jouhsuansu",
            ],
            "input_product_ids": [],
        }
    }

    user_dict = user_dict["a0025071@gmail.com"]
    do = Crawler(user_dict)
    do()
