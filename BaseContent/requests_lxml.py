import csv

import requests
from lxml import etree
from tqdm import tqdm

print('信息爬取中:\n')


class HouseParse(object):
    # 初始化
    def __init__(self):
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'
        }
        # 列表存放数据
        self.data_list = []

    def Sponsor(self):
        # 翻页数据
        for i in tqdm(range(1, 6)):
            url = f'https://cs.lianjia.com/ershoufang/rs{i}/'
            response = requests.get(url=url, headers=self.headers)
            html = etree.HTML(response.content.decode('utf-8'))
            # 找到内容所在的li标签下
            elements = html.xpath('//div/ul[@class="sellListContent"]/li')
            # print(elements)
            for element in elements:
                # 创建字典
                dict_ = {}
                # 标题
                dict_['title'] = element.xpath('./div[1]/div[1]/a/text()')[0]
                # 地址
                dict_['flood'] = ''.join([i.strip() for i in element.xpath('./div[1]/div[@class="flood"]//text()')])
                # 简介
                dict_['introduction'] = element.xpath('./div[1]/div[@class="address"]/div/text()')[0]
                # 价格
                dict_['price'] = ''.join(
                    [i.strip() for i in element.xpath('./div/div[@class="priceInfo"]/div//text()')])
                # print(dict_)
                self.data_list.append(dict_)
                self.data_list.append(dict_)

    def save_data(self):
        # 保存数据
        with open('lianjia.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'flood', 'introduction', 'price'])
            writer.writeheader()
            writer.writerows(self.data_list)

    def main(self):
        self.Sponsor()
        self.save_data()


if __name__ == '__main__':
    house = HouseParse()
    house.main()

    print('\n爬取成功！')
