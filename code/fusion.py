#!/usr/bin/python2.7
import numpy as np
import csv
import pandas as pd
import argparse
from pandas.core.frame import DataFrame
def DSfusion1(r1,n1,r2,n2):
  l1=[r1,0,n1]
  l2=[r2,0,n2]
  i=0
  k=0
  sum1=0
  collision_rate=r1*r2+r1*n2+r2*n1+n1*n2
  factor=1/collision_rate
  r=factor*(r1*r2+r1*n2+r2*n1)
  n=factor*(n1*n2)
  l3=[r,0,n]
  return l3
def DSfusion2(r1,n1,r2,n2):
  l1=[r1,n1,0]
  l2=[r2,n2,0]
  i=0
  k=0
  sum1=0
  collision_rate=r1*r2+n1*n2
  factor=1/collision_rate
  r=factor*(r1*r2)
  n=factor*(n1*n2)
  l3=[r,n,0]
  return l3
if __name__ == '__main__':
  parser=argparse.ArgumentParser()
  parser.add_argument('--input1',required=True)
  parser.add_argument('--input2',required=True)
  parser.add_argument('--input3',required=True)
  parser.add_argument('--output',required=True)
  args=parser.parse_args()
  df1=pd.read_csv(args.input1)
  df2=pd.read_csv(args.input2)
  df3=pd.read_csv(args.input3)
  tmp1=(DSfusion1(df1.ix[:,1],df1.ix[:,2],df2.ix[:,1],df2.ix[:,2]))[0]
  #tmp1=pd.DataFrame(tmp1)
  tmp2=(DSfusion1(df1.ix[:,1],df1.ix[:,2],df2.ix[:,1],df2.ix[:,2]))[2]
  #tmp2=pd.DataFrame(tmp2)
  tmp3=(DSfusion1(tmp1,tmp2,df3.ix[:,1],df3.ix[:,2]))[0]
  tmp3=pd.DataFrame(tmp3)
  #tmp3.drop(0,axis=0,inplace=False)
  #df1.drop(0,axis=0,inplace=False)
  df=df1['Line'].values.tolist()
  print(df[0])
  tmp3=tmp3[0].values.tolist()
  fusion=pd.DataFrame({'Line':df,'Suspiciousness':tmp3})
  fusion.to_csv(args.output, encoding='utf-8',index=False)
