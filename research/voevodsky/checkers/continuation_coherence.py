"""Proof-relevant paths, exact semantic comparison, explicit retained defect.
Fixed owning m4 chart. Equality certificate is canonical row-set identity,
not a general polyhedral equivalence solver or a higher-simplex assertion.
"""
from fractions import Fraction as Q
import json,hashlib
from verify_fine_successor import expected_archive
from verify_scalar_envelope_band import cross
from approximate_section_checkpoint import source
if not __debug__:raise RuntimeError('Assertions required')
def freeze(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def digest(x):return hashlib.sha256(freeze(x).encode()).hexdigest()
def row(raw):
 assert set(raw)=={'normal','upper'} and len(raw['normal'])==3
 return {'normal':list(map(str,map(Q,raw['normal']))),'upper':str(Q(raw['upper']))}
def canon(rows):
 # Only exact duplicate elimination and rational normalization; not an H-polytope quotient.
 return [json.loads(s) for s in sorted({freeze(row(r)) for r in rows})]
def root(archive,event,context):
 assert archive==expected_archive(archive['n'],archive['history'])
 return {'event':event,'context':context,'archive_digest':digest(archive)}
def semantic(archive,ops):
 return {'family':archive['family'],'n':archive['n'],'public_polygon':archive['public_polygon'],
  'source_chart':archive['source_chart'],'fine_rows':canon(archive['fine_rows']+ops)}
def make_path(archive,binding,batches):
 seen=[];edges=[];parent=digest({'binding':binding,'semantic':semantic(archive,[])})
 for batch in batches:
  normalized=[row(r) for r in batch];seen+=normalized
  edge={'parent':parent,'binding':binding,'operations':normalized,'successor':semantic(archive,seen)}
  parent=digest(edge);edges.append(edge)
 return {'binding':binding,'edges':edges,'tip':parent}
def verify_path(archive,expected_binding,expected_batches,path):
 assert expected_binding['archive_digest']==digest(archive)
 assert archive==expected_archive(archive['n'],archive['history'])
 assert path['binding']==expected_binding and len(path['edges'])==len(expected_batches)
 seen=[];parent=digest({'binding':expected_binding,'semantic':semantic(archive,[])})
 for batch,edge in zip(expected_batches,path['edges']):
  operations=[row(r) for r in batch];seen+=operations
  assert edge=={'parent':parent,'binding':expected_binding,'operations':operations,'successor':semantic(archive,seen)}
  parent=digest(edge)
 assert path['tip']==parent
 return semantic(archive,seen)
def compare(archive,binding,left_batches,left,right_batches,right):
 a=verify_path(archive,binding,left_batches,left);b=verify_path(archive,binding,right_batches,right)
 assert a==b
 return {'same_fine_relation':True,'same_public_image':True,'same_admissible_fine_lifts':True,
  'semantic_digest':digest(a),'left_tip':left['tip'],'right_tip':right['tip'],
  'proof_paths_identical':left['tip']==right['tip']}
def point_query(state,p):
 p=tuple(map(Q,p));assert len(p)==2;poly=[tuple(map(Q,v)) for v in state['public_polygon']]
 if not all(cross(a,b,p)>=0 for a,b in zip(poly,poly[1:]+poly[:1])):return {'admitted':False}
 lower=[];upper=[]
 for raw in state['fine_rows']:
  a,b,c=map(Q,raw['normal']);rhs=Q(raw['upper'])-a*p[0]-b*p[1]
  if c>0:upper.append(rhs/c)
  elif c<0:lower.append(rhs/c)
  elif rhs<0:return {'admitted':False}
 lo,hi=max(lower),min(upper)
 if lo>hi:return {'admitted':False,'interval':[str(lo),str(hi)]}
 h=(lo+hi)/2
 return {'admitted':True,'interval':[str(lo),str(hi)],'source_lift':list(map(str,source(*p,h)))}
def transport_defect(package,expected_binding,parent,operations):
 # A proof record cannot issue its own identity authority. The expected
 # binding must come from an owning authority before this arithmetic gate.
 assert package['binding']==expected_binding
 assert digest(package['retained_archive'])==expected_binding['archive_digest']
 assert package['tip']==parent
 return {'binding':expected_binding,'tip':digest({'parent':parent,'operations':[row(r) for r in operations],
  'binding':expected_binding}),'retained_archive':package['retained_archive']}
