"""Synchronized fine path/thin arrow record; no historical authorization."""
from pathlib import Path
import json
roots=('low-x','high-x','low-y','high-y')
def rot(t):
 if isinstance(t,str):return set()
 x,y=t;out=set()
 if isinstance(x,tuple):out.add((x[0],(x[1],y)))
 out|={(v,y) for v in rot(x)}|{(x,v) for v in rot(y)}
 return out
def record(path,root_ids,declared_thin=None):
 if tuple(root_ids)!=roots:raise PermissionError('SOURCE_ROOT_MISMATCH')
 if not path or any(y not in rot(x) for x,y in zip(path,path[1:])):raise ValueError('INVALID_FINE_PATH')
 thin=(path[0],path[-1])
 if declared_thin is not None and declared_thin!=thin:raise ValueError('FORGED_THIN_ENDPOINT')
 return {'fine':tuple(path),'thin':thin,'roots':tuple(root_ids)}
def compose(a,b):
 if a['roots']!=b['roots']:raise PermissionError('SOURCE_ROOT_MISMATCH')
 if a['thin'][1]!=b['thin'][0] or a['fine'][-1]!=b['fine'][0]:raise ValueError('NONCOMPOSABLE_ENDPOINTS')
 return record(a['fine']+b['fine'][1:],a['roots'],(a['thin'][0],b['thin'][1]))
def authorize_actual_history(_):raise PermissionError('NO_EXECUTION_AUTHORITY_FROM_THIN_ARROW')
a=((('a','b'),'c'),'d');mid=(('a','b'),('c','d'));end=('a',('b',('c','d')))
assert mid in rot(a) and end in rot(mid)
short=compose(record((a,mid),roots),record((mid,end),roots))
long1=(('a',('b','c')),'d');long2=('a',(('b','c'),'d'))
assert long1 in rot(a) and long2 in rot(long1) and end in rot(long2)
long=compose(compose(record((a,long1),roots),record((long1,long2),roots)),record((long2,end),roots))
assert short['thin']==long['thin'] and short['fine']!=long['fine']
try:record((a,mid),roots[:-1])
except PermissionError:pass
else:raise AssertionError('missing source root')
try:record((a,mid),roots,(a,end))
except ValueError:pass
else:raise AssertionError('forged thin')
try:compose(record((a,mid),roots),record((long1,long2),roots))
except ValueError:pass
else:raise AssertionError('noncomposable paths')
try:authorize_actual_history(short)
except PermissionError:pass
else:raise AssertionError('thin arrow promoted to authority')
report={'passed':True,'two_routes_same_thin':True,'fine_paths_distinct':True,'projection_preserves_composition':True,'refused':['missing-source-root','forged-thin-endpoint','noncomposable-path','actual-history-authorization'],'scope':'Formal synchronized record on fixed four-leaf primitive source. Root IDs are declarations not independent authentication, and no analytic role functor or historical equality is supplied.'}
out=Path(__file__).resolve().parents[1]/'results/tagged-thin-product.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
