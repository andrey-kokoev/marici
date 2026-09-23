"""Fixed-family fine archive and successor replay, independent of sessions."""
from fractions import Fraction as Q
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from verify_scalar_envelope_band import domain,envelopes
if not __debug__:raise RuntimeError('Assertions required')
FAMILY='owning-m4-moment-curve-two-history-v1'
def expected_archive(n,history):
 assert history in ('A','B');lower,upper=envelopes(n)
 rows=[{'normal':['0','0','-1'],'upper':'0'},{'normal':['0','0','1'],'upper':'1'}]
 for a,b,c in (lower if history=='A' else upper):
  normal,bound=((a,b,Q(-1)),-c) if history=='A' else ((-a,-b,Q(1)),c)
  rows.append({'normal':list(map(str,normal)),'upper':str(bound)})
 return {'family':FAMILY,'n':n,'history':history,'public_polygon':[list(map(str,p)) for p in domain(n)],
 'fine_rows':rows,'source_chart':'owning-m4-fixed-t1-51-v1'}
def verify(archive,event,ambiguity,successor):
 assert archive==expected_archive(archive['n'],archive['history'])
 request=ambiguity['request'];state=request['state'];op=request['operation']
 assert state['family']==archive['family'] and state['n']==archive['n']
 assert op['kind']=='append-fine-upper-then-exact-point-admission'
 expected={**archive,'retirement_event':event,'parent_request_digest':ambiguity['request_digest'],
 'fine_rows':archive['fine_rows']+[{'normal':['0','0','1'],'upper':str(Q(op['h_upper']))}],
 'capabilities':['exact-point-admission','exact-fine-lift'],'archive_reexposure':False}
 assert successor==expected
 return True
