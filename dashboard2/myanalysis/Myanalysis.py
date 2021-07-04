import csv

import bs4
import pandas as pd;
import numpy as np;
import requests

from config.settings import DATA_DIRS


class Titanic:
    def d1s(self,option):
        df = pd.read_csv(DATA_DIRS[0]+'\\train.csv');

        survived = df[df['Survived'] == 1][option].value_counts();
        dead = df[df['Survived'] == 0][option].value_counts();
        df2 = pd.DataFrame([survived, dead])
        df2.index = ['Survived', 'Dead'];
        result = [];
        for i in range(len(df2.columns)):
            d = {};
            d['name'] = np.str(df2.columns[i]);
            d['data'] = df2.iloc[:, i].tolist();
            result.append(d);
        print(result);
        return result;

class Galaxy:
    def g1(self):
        df = pd.read_csv(DATA_DIRS[0]+'\\spstat1.csv',encoding='euc-kr');
        print(df);

class Naver:
    def n1(self):
        df = pd.read_html('https://finance.naver.com/marketindex/?tabSel=materials#tab_section',
                          encoding='euc-kr');
        print(df);

class Open:
    def o1(self):
        #df = pd.read_json(
        #'http://apis.data.go.kr/6410000/GOA/GOA002?type=json&busno=23054&ServiceKey=NuvoUrkE7SSIULP315eGuE9WgDLpDXwL3jkfiG9ftsOB63tR6TPYmNT45fOg%2FKSOSN6n%2BWYJp1dE7bHXzQyfzg%3D%3D');
        #print(df.columns);
        #print(df['result']);
        url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=NuvoUrkE7SSIULP315eGuE9WgDLpDXwL3jkfiG9ftsOB63tR6TPYmNT45fOg%2FKSOSN6n%2BWYJp1dE7bHXzQyfzg%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200310&endCreateDt=20200315';
        result = requests.get(url);
        response = result.text.encode('utf-8');
        xml_obj = bs4.BeautifulSoup(response, 'lxml-xml');
        rows = xml_obj.find_all('item');
        print(rows);

if __name__ == '__main__':
    Open().o1();