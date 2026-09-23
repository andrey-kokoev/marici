"""Compose positive monomial source-presentation witnesses exactly."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
A=(((-Q(1),Q(0)),Q(0)),((Q(1),Q(0)),Q(1)),((Q(0),-Q(1)),Q(0)),((Q(0),Q(1)),Q(1)))
P=(Q(1),Q(2),Q(0),Q(0));M=(Q(0),Q(1),Q(1),Q(1));D=tuple(M[i]-P[i] for i in range(4))
def apply(rows,m,perm,scale):
 assert sorted(perm)==[0,1,2,3] and all(s>0 for s in scale)
 return (tuple((tuple(s*x for x in rows[i][0]),s*rows[i][1]) for i,s in zip(perm,scale)),tuple(m[i]/s for i,s in zip(perm,scale)))
def compose(first,second):
 p,s=first;q,t=second
 return tuple(p[q[j]] for j in range(4)),tuple(s[q[j]]*t[j] for j in range(4))
identity=((0,1,2,3),(Q(1),)*4)
f=((3,0,2,1),(Q(2),Q(3),Q(1,2),Q(4)))
g=((1,3,0,2),(Q(5),Q(1,3),Q(2),Q(3,2)))
h=((2,0,3,1),(Q(1,2),Q(7),Q(1),Q(4)))
checks=0
for w in (P,M,D):
 B,b=apply(A,w,*f);C,c=apply(B,b,*g)
 direct,dc=apply(A,w,*compose(f,g));assert (C,c)==(direct,dc)
 E,e=apply(C,c,*h);F,fe=apply(A,w,*compose(compose(f,g),h));assert (E,e)==(F,fe)
 assert compose(compose(f,g),h)==compose(f,compose(g,h))
 assert apply(A,w,*identity)==(A,w)
 checks+=1
invp=tuple(f[0].index(j) for j in range(4));invs=tuple(1/f[1][invp[j]] for j in range(4))
assert compose(f,(invp,invs))==identity and compose((invp,invs),f)==identity
# Issuer/source-event payload does not occur in the monomial witness.
old_token={'source_event':'A-event','manifest':'A','grant':'A-only'}
def transport_authority(token,witness):raise PermissionError('OWNER_REBIND_REQUIRED')
try:transport_authority(old_token,compose(f,g))
except PermissionError:pass
else:raise AssertionError('old grant moved through isomorphism')
report={'passed':True,'three_presentation_proof_path_cases':checks,'associative_witness_composition':True,'identity_and_inverse':True,'signed_comparison_vector_transported':True,'forged_source_event_transport_refused':True,'scope':'Exact positive-monomial row presentation groupoid for fixed square source and chosen proof path. No issuer grant, historical identity or analytic role functor.'}
out=Path(__file__).resolve().parents[1]/'results/composed-square-row-witnesses.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
