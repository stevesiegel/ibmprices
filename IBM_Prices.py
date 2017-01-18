# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 13:28:55 2017

@author: Steve Siegel
"""

import pandas as pd


prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=IBM')

prices_df.to_csv('/tmp/prices_IBM.csv', float_format='%4.2f', index=False)



