from urllib.robotparser import RobotFileParser


class MeiShiTianXiaSpider(object):

    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"
        self.data = list()
        self.path = "美食天下.csv"
        self.robots_url = "https://home.meishichina.com/robots.txt"
        self.url = "https://home.meishichina.com"

    def is_allow_crawl(self):
        rp = RobotFileParser()
        # rp.set_url(self.robots_url)
        # rp.read()
        #
        # print(rp.__str__(), "====")
        # # 检查特定的 User-agent 和 URL 是否被允许
        # url = self.url + "/show-top-type-recipe-page-1.html"
        # is_allowed = rp.can_fetch(self.user_agent, url)
        # print(f"User-agent '{self.user_agent}' can fetch '{url}': {is_allowed}")

        rp.set_url("https://www.huangrx.cn/robots.txt")
        rp.read()

        print(rp.can_fetch('*', 'https://www.huangrx.cn/blogs/category/all'))


if __name__ == '__main__':
    spider = MeiShiTianXiaSpider()
    spider.is_allow_crawl()