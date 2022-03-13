import requests
import re
import xlwt
import os
import json


class CnYq_Info:

    def get_yq_html(self):

        yq_url = "https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0"
        header = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
        }

        resp = requests.get(yq_url, headers=header)
        resp.encoding = "utf-8"
        #print(resp.text)
        #print(resp.content.decode("utf-8"))

        return resp.text

    def get_yq_dict(self):

        dict_info = self.get_yq_html()
        #reDict = re.findall('try { window.fetchRecentStatV2 = \[(.*?)catch\(e\)', dict_info)
        reDict = re.findall('try { window.fetchRecentStatV2 = (.*?)}catch\(e\)', dict_info)
        reDict_json = json.loads(reDict[0])

        #areas_type_dic_raw = re.findall('try { window.getAreaStat = (.*?)}catch\(e\)', self.get_yq_html())
        #areas_type_dic = json.loads(areas_type_dic_raw[0])
        #print(reDict_json)

        return reDict_json

    def write_yq_file(self):

        yqInfoContent = self.get_yq_dict()
        print(yqInfoContent)

        yqInfoFile = xlwt.Workbook()
        yqInfoSheet = yqInfoFile.add_sheet(u"全国疫情")

        yqInfoSheet.write(0, 1, '地区')
        yqInfoSheet.write(0, 2, "昨日本土新增")
        yqInfoSheet.write(0, 3, "现存确诊")
        yqInfoSheet.write(0, 4, "累计确诊")
        yqInfoSheet.write(0, 5, "死亡")
        yqInfoSheet.write(0, 6, "治愈")
        yqInfoSheet.write(0, 7, "风险地区")

        yqInfoFile.save("全国疫情数据.xlsx")




if __name__ == "__main__":

    CnYq_Info().write_yq_file()
































