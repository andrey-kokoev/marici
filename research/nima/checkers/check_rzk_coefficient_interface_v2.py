"""Exact source-admissibility regressions, not compiled Rzk proofs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

# Sparse polynomials in independent variables u,v over Z.
def const(n):return {(0,0):n} if n else {}
def add(a,b):
    out=dict(a)
    for k,n in b.items():
        out[k]=out.get(k,0)+n
        if not out[k]:del out[k]
    return out
def neg(a):return {k:-n for k,n in a.items()}
def mul(a,b):
    out={}
    for (i,j),n in a.items():
        for (k,l),m in b.items():out=add(out,{(i+k,j+l):n*m})
    return out
def dot(a,b):
    out={}
    for x,y in zip(a,b):out=add(out,mul(x,y))
    return out
def at_units(a):return sum(a.values())
def at_u_zero(a):return {(i,j):n for (i,j),n in a.items() if i==0}

one=const(1);zero={};u={(1,0):1};v={(0,1):1}
d0=[[one,u,zero,zero],[one,zero,v,zero],
    [zero,neg(one),zero,v],[zero,zero,one,neg(u)]]
z=[neg(mul(u,v)),v,u,one]
assert all(not dot(row,z) for row in d0)
old=[zero,one,neg(one),zero]
obstruction=dot(old,z)
assert obstruction==add(v,neg(u)) and obstruction
# If h d0=old, multiplication by z contradicts d0 z=0. No cutoff on h.
new=[zero,u,neg(v),zero]
h=[zero,zero,neg(u),neg(v)]
assert [dot(h,list(col)) for col in zip(*d0)]==new
assert not dot(new,z)
assert new!=old  # A different boundary, not a filler for old.
assert [at_units(p) for p in new]==[at_units(p) for p in old]
assert at_units(obstruction)==0
# Restoring the unit specialisation can erase the obstruction; never use it
# as evidence of polynomial null-homotopy.

# Localization identity-column contract on independent source coordinates.
def missing_inverses(source,target):return sorted(set(source)-set(target))
forbidden=missing_inverses({'04'},{'03','05'})
assert forbidden==['04']
allowed=missing_inverses({'05','04'},{'03','05','04'})
assert allowed==[]
assert missing_inverses({'04'},{'04'})==[]
# The mathematical rejection proof is evaluation of the non-inverted
# coordinate at zero in the target, contradicting v04*f(v04^-1)=1.

# Universal normalisation obstruction: eval_u0 is a ring homomorphism,
# eval_u0(u)=0 and eval_u0(1)=1. Thus 1+u*b cannot be zero for ANY b.
assert at_u_zero(u)=={} and at_u_zero(one)==one
sample_b=add(add(const(-3),mul(u,v)),mul(v,v))
assert at_u_zero(add(one,mul(u,sample_b)))==one
# Sample is only a sanity check of the evaluator; universality is the
# multiplicative evaluation argument, not finite polynomial testing.

spec=Path('research/nima/rzk-coefficient-interface-v2.md')
result={'status':'passed','checked_at':datetime.now(timezone.utc).isoformat(),
'spec_sha256':hashlib.sha256(spec.read_bytes()).hexdigest(),
'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
'localization':{'forbidden_identity_column_missing_inverses':forbidden,'pair_local_column_missing_inverses':allowed,'scope':'independent-coordinate rings, identity-on-monomials maps'},
'weighted_block':{'cycle_verified':True,'old_obstruction':'v-u','old_filler_exists':False,'new_filler':['0','0','-u','-v'],'new_boundary':['0','u','-v','0'],'new_filler_equation_verified':True,'boundary_revision_required':True,'unit_specialization_agrees':True},
'normalization':{'unit_empty_coefficient_possible_over_Zuv':False,'proof':'Evaluate 1+u*b=0 at u=0 to obtain 1=0'},
'nonverification':['No Rzk code added or compiled','No full octagon source checker rerun','No global dihedral or filtration certificate constructed here','No full physical Gysin/PC/Rees comparison supplied']}
Path('research/nima/results/rzk_coefficient_interface_v2.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
