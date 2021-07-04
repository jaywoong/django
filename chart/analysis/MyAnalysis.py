import csv
import random

from config.settings import DATA_DIRS
import numpy as np;
import pandas as pd;

class MyAnalysis:
    def wm(self,year,month):
        f = open(DATA_DIRS[0]+'\\ta.csv');
        data = csv.reader(f);
        next(data);
        htemp = [];
        ltemp = [];
        for row in data:
            if year == int(row[0].split('-')[0]) and month == int(row[0].split('-')[1]):
                ltemp.append(float(row[3]));
                htemp.append(float(row[4]));
        data = [{
            'name':'일별 최저 기온',
            'data':ltemp
        },{
            'name': '일별 최고 기온',
            'data': htemp
        }];
        return data;

    def localage(self,target):
        f = open(DATA_DIRS[0] + '\\age.csv');
        data = csv.reader(f);
        next(data);
        mcnt = [];
        for row in data:
            if target in row[0]:
                for i in row[3:104]: # 3 ~ 104, 106 ~ 207, 209 ~ 310
                    try:
                        mcnt.append(int(i)); #1,540
                    except:
                        mcnt.append(int(i.replace(',','')));

        data = [{
            'name':'Total',
            'data':mcnt
        }];
        return data;

    def genderage(self, target):
        f = open(DATA_DIRS[0] + '\\age.csv');
        data = csv.reader(f);
        next(data);
        m = [];
        f = [];
        for row in data:
            if target in row[0]:
                for i in row[106:207]:
                    m.append(-int(i.replace(',','')));
                for i in row[209:310]:
                    f.append(int(i.replace(',','')));
        data = [{
            'name':'Male',
            'data':m
        },{
            'name': 'Fmale',
            'data': f
        }];
        return data;

    def genderage2(self, target):
        f = open(DATA_DIRS[0] + '\\age.csv');
        data = csv.reader(f);
        next(data);
        m = 0;
        f = 0;
        for row in data:
            if target in row[0]:
                m = int(row[105].replace(',',''));
                f = int(row[208].replace(',',''));
        data = [{
            'name':'Male',
            'y': 100 * (m/(m+f))
        },{
            'name': 'Fmale',
            'y': 100 * (f/(m+f))
        }];
        return data;

    def iots(self):
       f = open(DATA_DIRS[0] + '\\mylog.csv');
       data = csv.reader(f);
       for d in data:
           print(d);

if __name__ == '__main__':
    MyAnalysis().iots();
