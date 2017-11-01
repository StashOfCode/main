import io
import pandas as pd
import logging
import numpy as np
import requests


class Calc_VaR(object):
    '''????'''

    def __init__(self, ticker=None, date_start=None, date_end=None, freq=None):
        self.ticker = ticker
        self.date_start = date_start
        self.date_end = date_end
        self.freq = freq


    def get_data(self, ticker_url):
        '''???'''
    
        data = requests.get((ticker_url)).content.decode("utf-8").split()
        data[0] = data[0].replace('<', '').replace('>', '')
        
        return pd.read_csv(io.StringIO('\n'.join(data)), sep=',')


    def hVar(self, data):
        '''???'''
        pass


    def nVar(self, data):
        '''???'''
        pass


    def main():
        data = get_data()
        

if __name__ == '__main__':
    ##ticker_url = 'http://export.finam.ru/GAZP_101101_171101.csv?market=1&em=16842&code=GAZP&apply=0&df=1&mf=10&yf=2010&from=01.11.2010&dt=1&mt=10&yt=2017&to=01.11.2017&p=8&f=GAZP_101101_171101&e=.csv&cn=GAZP&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=3&sep2=1&datf=1&at=1'
    ticker_url = 'http://export.finam.ru/ROSN_101101_171101.csv?market=1&em=17273&code=ROSN&apply=0&df=1&mf=10&yf=2010&from=01.11.2010&dt=1&mt=10&yt=2017&to=01.11.2017&p=8&f=ROSN_101101_171101&e=.csv&cn=ROSN&dtf=4&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1'
    calc = Calc_VaR()
    calc.main()
    
#ToDO: VaR нормальным и историческим методом. Calc param. VaR using t-Student distr. Explain
#ToDO:​ VaR методом EWMA. Explain
#ToDO:​ Calc Expected Shortfall (aka Expected Tail Loss). Explain
#ToDO: Выводы об уровне рыночного риска по Вашей акции
#ToDO:​ Back-testing. В учебнике J.Daniellson
