from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import csv
import re
import time
from tqdm import tqdm


class HomeLinkSpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
        self.data = list()
        self.path = "郑州.csv"
        self.url = "https://zz.lianjia.com/ershoufang/zhongyuanqu1/a3p4/"

    def get_max_page(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            a = soup.select('div[class="page-box house-lst-page-box"]')
            if not a:
                print("未找到分页信息")
                return None
            try:
                # 使用eval是字符串转化为字典格式
                max_page = eval(a[0].attrs["page-data"])["totalPage"]
                return max_page
            except (KeyError, IndexError, SyntaxError) as e:
                print(f"解析分页信息出错: {e}")
                return None
        else:
            print("请求失败 status:{}".format(response.status_code))
            return None

    def parse_page(self):
        max_page = self.get_max_page()
        if not max_page:
            print("无法获取最大页数")
            return

        for i in tqdm(range(1, max_page + 1), desc="Parsing pages"):
            url = f'https://zz.lianjia.com/ershoufang/zhongyuanqu1/pg{i}a3p4/'
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                print(f"请求失败: {url} status: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            ul = soup.find_all("ul", class_="sellListContent")
            if not ul:
                print("未找到房源信息")
                continue

            li_list = ul[0].select("li")
            for li in li_list:
                detail = dict()
                detail['title'] = li.select('div[class="title"]')[0].get_text()

                house_info = li.select('div[class="houseInfo"]')[0].get_text()
                house_info_list = house_info.split(" | ")

                detail['bedroom'] = house_info_list[0]
                detail['area'] = house_info_list[1]
                detail['direction'] = house_info_list[2]

                floor_pattern = re.compile(r'\d{1,2}')
                match1 = re.search(floor_pattern, house_info_list[4])
                detail['floor'] = match1.group() if match1 else "未知"

                year_pattern = re.compile(r'\d{4}')
                match2 = re.search(year_pattern, house_info_list[5])
                detail['year'] = match2.group() if match2 else "未知"

                position_info = li.select('div[class="positionInfo"]')[0].get_text().split(' - ')
                detail['house'] = position_info[0]
                detail['location'] = position_info[1] if len(position_info) > 1 else "未知"

                price_pattern = re.compile(r'\d+')
                total_price = li.select('div[class="totalPrice totalPrice2"]')[0].get_text()
                detail['total_price'] = re.search(price_pattern, total_price).group()

                detail['unit_price'] = eval(li.select('div[class="unitPrice"]')[0].attrs["data-price"])

                self.data.append(detail)

    def write_csv_file(self):
        head = ["标题", "小区", "房厅", "面积", "朝向", "楼层", "年份", "位置", "总价(万)", "单价(元/平方米)"]
        keys = ["title", "house", "bedroom", "area", "direction", "floor", "year", "location", "total_price",
                "unit_price"]

        try:
            with open(self.path, 'w', newline='', encoding='utf_8_sig') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                if head is not None:
                    writer.writerow(head)
                for item in tqdm(self.data, desc="Writing to CSV"):
                    row_data = [item.get(k, "未知") for k in keys]
                    writer.writerow(row_data)
                print("Write a CSV file to path %s Successful." % self.path)
        except Exception as e:
            print("Fail to write CSV to path: %s, Case: %s" % (self.path, e))


if __name__ == '__main__':
    start = time.time()
    home_link_spider = HomeLinkSpider()
    home_link_spider.parse_page()
    home_link_spider.write_csv_file()
    end = time.time()
    print("耗时：{}秒".format(end - start))
