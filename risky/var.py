import io
import pandas as pd
import logging
import matplotlib.pyplot as plt
import numpy as np
import requests
##from scipy.stats import norm

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Starting point.')


class Calc_VaR(object):
    '''????'''

    def __init__(self, ticker_url=None, date_start=None, date_end=None, freq=None):
        self.ticker_url = ticker_url
        self.date_start = date_start
        self.date_end = date_end
        self.freq = freq

    def get_data(self, ticker_url, close_only=True):
        '''???'''    
        data = requests.get((ticker_url)).content.decode("utf-8").split()
        data[0] = data[0].replace('<', '').replace('>', '').lower()
        return pd.read_csv(io.StringIO('\n'.join(data)), sep=',')

    def process_data(self, df):
        '''???'''
        # add log returns
        df['returns'] = np.log(df['close']) - np.log(df['close'].shift(1))

        # add squared returns column
        return df
        
    def hVar(self, df, confidence=0.99):
        '''???'''
        # 300, 1000
        np.percentile(a, 1 - confidence)
        pass

    def nVar(self, df, confidence=0.99):
        '''???'''
        # for 300, 1000, 10 days 300, 300 T-student
        # rolling array as input for std and mean
        norm.ppf(1 - confidence) * np.std() - np.mean()
        
        pass

    def main(self):
        data = self.get_data(self.ticker_url)
        return self.process_data(data)


class Visualize(object):
    '''???'''
    def __init__(self):
        pass


    

if __name__ == '__main__':
    ##ticker_url = 'http://export.finam.ru/GAZP_101101_171101.csv?market=1&em=16842&code=GAZP&apply=0&df=1&mf=10&yf=2010&from=01.11.2010&dt=1&mt=10&yt=2017&to=01.11.2017&p=8&f=GAZP_101101_171101&e=.csv&cn=GAZP&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=3&sep2=1&datf=1&at=1'
    ticker_url = 'http://export.finam.ru/ROSN_101101_171101.csv?market=1&em=17273&code=ROSN&apply=0&df=1&mf=10&yf=2010&from=01.11.2010&dt=1&mt=10&yt=2017&to=01.11.2017&p=8&f=ROSN_101101_171101&e=.csv&cn=ROSN&dtf=4&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1'
    calc = Calc_VaR(ticker_url)
    df = calc.main()
    
#ToDO: NVaR & HVaR. Calc parametric VaR using t-Student distr. Explain
#ToDO:​ VaR методом EWMA. Explain
#ToDO:​ Calc Expected Shortfall (aka Expected Tail Loss). Explain
#ToDO: Выводы об уровне рыночного риска по Вашей акции
#ToDO:​ Back-testing. В учебнике J.Daniellson
