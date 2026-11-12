import sqlite3
from .common import identifier
def run(data):
 values=data['values']
 if not isinstance(values,list)or not 1<=len(values)<=1000 or any(not isinstance(v,str)or len(v)>1000 for v in values):raise ValueError('values')
 with sqlite3.connect(':memory:')as db:
  for affinity in ['TEXT','NUMERIC']:
   db.execute('create table '+affinity+'(v '+affinity+')');db.executemany('insert into '+affinity+' values(?)',[(v,)for v in values])
  output={a:[dict(value=v,storage=t,column_equals_three=bool(c),expression_equals_three=bool(e))for v,t,c,e in db.execute('select v,typeof(v),v=3,+v=3 from '+a)]for a in ['TEXT','NUMERIC']}
 return output
