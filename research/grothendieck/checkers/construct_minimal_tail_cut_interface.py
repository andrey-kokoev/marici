"""Exact continuation quotient of a frozen rational cut family.
This control is not the actual fixed-hat kernel or a source-protocol adapter.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,combinations
import json,hashlib
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# Prefix (p,q,t) in [0,1]^3, completion y in [0,1], F=t-y.
# All row coefficients are in the order p,q,t,y.
rows=[([1,0,0,1],1),([0,1,0,2],2),([1,1,0,3],3),([2,0,0,2],2),([1,0,0,1],2)]
contract={'schema':'minimal-tail-cut-interface.v1','prefix_coordinates':['p','q','t'],'suffix_coordinate':'y','box':'all coordinates in [0,1]','objective':'t-y','rows':[{'coefficients':a,'upper':b} for a,b in rows],'continuation_language':'all exact rational completions y, observing admission and terminal objective; future finite linear constraints on y are allowed, but no new reads of forgotten p or q','grid_denominator':4,'scope':'Exact rational control plus continuum proof; no uniform interface dimension or actual-prime application is asserted.'}
cp=R/'minimal-tail-cut-interface-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
def cap(p,q,t):return min(1-p,1-q/2)
def admitted(prefix,y):
 return 0<=y<=1 and all(sum(Q(a)*z for a,z in zip(coef,(*prefix,y)))<=b for coef,b in rows)
def signature(prefix):return cap(*prefix),prefix[2]
points=list(product([Q(i,4) for i in range(5)],repeat=3));classes={}
for j,prefix in enumerate(points):classes.setdefault(signature(prefix),[]).append(j)
class_rows=[{'cap':str(h),'objective_offset':str(t),'members':members} for (h,t),members in classes.items()]
# A separating completion is constructed for every inequivalent grid pair.
pair_witnesses=[];equal_pairs=0
for i,j in combinations(range(len(points)),2):
 a,b=points[i],points[j];ha,ta=signature(a);hb,tb=signature(b)
 if (ha,ta)==(hb,tb):equal_pairs+=1;continue
 y=(ha+hb)/2 if ha!=hb else Q(0)
 aa,ab=admitted(a,y),admitted(b,y)
 assert aa!=ab or (aa and ta-y!=tb-y)
 pair_witnesses.append({'left':i,'right':j,'completion':str(y)})
# Check the quotient against all row breakpoints and intervening rationals.
for prefix in points:
 h,t=signature(prefix);breaks={Q(0),Q(1),h}
 for coef,b in rows:breaks.add((Q(b)-sum(Q(a)*v for a,v in zip(coef[:3],prefix)))/coef[3])
 cuts=sorted(breaks);probes=cuts+[(a+b)/2 for a,b in zip(cuts,cuts[1:])]
 for y in probes:assert admitted(prefix,y)==(0<=y<=h)
# Nonempty residual suffix intervals update by intersection. Exhaustively
# test two future bound frames on each initial quotient, including empty.
labels=[('lower',Q(i,4)) for i in range(-1,6)]+[('upper',Q(i,4)) for i in range(-1,6)]
def update(state,label):
 if state is None:return None
 lo,hi,t=state;kind,v=label;lo=max(lo,v) if kind=='lower' else lo;hi=min(hi,v) if kind=='upper' else hi
 return None if lo>hi else (lo,hi,t)
checks=0
for h,t in classes:
 for first,second in product(labels,repeat=2):
  state=update(update((Q(0),h,t),first),second)
  lo=max([Q(0)]+[v for k,v in (first,second) if k=='lower']);hi=min([h]+[v for k,v in (first,second) if k=='upper'])
  expected=None if lo>hi else (lo,hi,t);assert state==expected;checks+=1
controls={
 'same_interface_different_prefix':{'left':['1/2','0','1/2'],'right':['0','1','1/2']},
 'same_optimum_different_completions':{'left':['1/2','0','1/2'],'right':['0','0','1'],'completion':'3/4'},
 'omit_cap':{'left':['0','0','0'],'right':['1/2','0','0'],'completion':'3/4'},
 'omit_objective_offset':{'left':['0','0','0'],'right':['0','0','1'],'completion':'0'}}
# A linear sufficient summary L must have trivial kernel: in the open region
# p>q/2, preserving h,t requires v_p=v_t=0; in p<q/2 it requires v_q=v_t=0.
# These exact independent coefficient rows span all three prefix dimensions.
linear_necessary_rows=[[1,0,0],[0,Q(1,2),0],[0,0,1]]
out={'schema':'minimal-tail-cut-interface-result.v1','contract_sha256':sha(cp),'prefixes':[[str(v) for v in p] for p in points],'classes':class_rows,'equivalent_pairs':equal_pairs,'distinguishing_completions':pair_witnesses,'two_frame_update_checks':checks,'controls':controls,'linear_necessary_rows':[[str(v) for v in row] for row in linear_necessary_rows],'linear_rank':3,'piecewise_interface':['min(1-p,1-q/2)','t'],'redundancy_certificates':[{'target':2,'base_weights':[1,1],'rhs_slack':0},{'target':3,'base_weights':[2,0],'rhs_slack':0},{'target':4,'base_weights':[1,0],'rhs_slack':1}],'bindings':{str(p):sha(p) for p in (Path(__file__),cp)},'scope':'Minimal as continuation equivalence; two retained fields each necessary. No lower bound on arbitrary discontinuous encodings is claimed.'}
(R/'minimal-tail-cut-interface.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'prefixes':len(points),'classes':len(classes),'equal_pairs':equal_pairs,'distinguishing_pairs':len(pair_witnesses),'update_checks':checks,'necessary_linear_rank':3,'piecewise_fields':2},indent=2))
