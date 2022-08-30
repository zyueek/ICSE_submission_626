#!/usr/bin/python2.7
def bonus_win1(df,start,end,central):
  df_com=df.ix[start:end]
  group=df.ix[central,"Funcnum"]
  num=0
  sus=0
  for x in range(start,end):
    if(df_com.ix[x,"Funcnum"]==group):
      sus=sus+float(df_com.ix[x,"Suspiciousness"])
      num=num+1
  result=sus/num
  return result
if __name__ == '__main__':
  import csv
  import pandas as pd
  import argparse
  from pandas.core.frame import DataFrame
  parser=argparse.ArgumentParser()
  parser.add_argument('--input',required=True)
  parser.add_argument('--output',required=True)
  parser.add_argument('--window',required=True)
  args=parser.parse_args()
  df=pd.read_csv(args.input)
  length=len(df)
  win=int(args.window)
  code=[0 for x in range(0,length)]
  codeline=[0 for x in range(0,length)]
  for i in range(0,length):
    code[i]=df.ix[:,0].values.tolist()[i].split('#',1)[0]
    codeline[i]=int(df.ix[:,0].values.tolist()[i].split('#',1)[1])
  df["Code"]=code
  df["Codeline"]=codeline
  df.sort_values(by = ['Code','Codeline'],ascending=[False,True],inplace=True)
  df.to_csv(args.output, encoding='utf-8', index=False)
  df=pd.read_csv(args.output)
  funnum=0
  fun_l=[]
  fun_l.append(0)
  for i in range(1,length):
    if(df.ix[i-1,"Code"]!=df.ix[i,"Code"]):
      funnum=funnum+1
    fun_l.append(funnum)
    i=i+1
  df["Funcnum"]=fun_l
  df.to_csv(args.output, encoding='utf-8', index=False)
  df=pd.read_csv(args.output)
  result_l=[]
  for i in range(0,length):
    if(i<win):
      result_l.append(bonus_win1(df,0,i+win,i))
    elif(i>length-win):
      result_l.append(bonus_win1(df,i-win,length,i))
    else:
      result_l.append(bonus_win1(df,i-win,i+win,i))
  df["Suspiciousness"]=result_l
  df["uncertain"]=1-df["Suspiciousness"]
  df.drop(labels="Code",axis=1, index=None, columns=None, inplace=True)
  df.drop(labels="Codeline",axis=1, index=None, columns=None, inplace=True)
  df.sort_values(by="Rank",axis=0,ascending=True,inplace=True)
  df.to_csv(args.output, encoding='utf-8', index=False)



  
