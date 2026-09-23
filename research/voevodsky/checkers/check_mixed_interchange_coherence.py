"""Repeated redistribution: parallel derivations of mixed-interchange coherence."""
from fractions import Fraction as Q
from pathlib import Path
import json
p=(Q(1),Q(2),Q(0),Q(1));T=Q(3);theta=Q(1,2);phi=Q(1,2);c=p[3]
def valid(q):
 a,u,v,s=q;return min(q)>=0 and u+v-a==1 and u+v+s==T
def r(q,x):
 assert valid(q);a,u,v,s=q;x=Q(x);assert -v<=x<=u
 z=(a,u-x,v+x,s);assert valid(z);return z
def n(q,side):
 assert valid(q);a,u,v,s=q
 z=(a+s,u+s,v,Q(0)) if side=='A' else (a+s,u,v+s,Q(0))
 assert valid(z);return z
start_intermediate=r(r(p,theta),phi);tip=n(start_intermediate,'B')
assert tip==r(n(p,'A'),c+theta+phi)
# Distinct proofs on which the local mixed filler is instantiated.
assert n(r(p,theta),'B')==r(n(p,'A'),c+theta)
assert n(r(r(p,theta),phi),'B')==r(n(r(p,theta),'A'),c+phi)
# Apply the proposed mixed 3-cell after aggregating R_theta,R_phi, versus
# applying it at the innermost compatible region then composing. Both end
# in the same 2-cell boundary but are different 3-cell derivation strings.
aggregate=(('compose_R',str(theta),str(phi)),('mixed',str(theta+phi)),('compose_R',str(c),str(theta+phi)))
staged=(('mixed',str(phi)),('commute_NA_R',str(theta)),('compose_R',str(c+phi),str(theta)))
assert aggregate!=staged
assert r(n(p,'A'),c+theta+phi)==tip
# The cell instantiated at phi is typed on q=R_theta(p); amount c+phi
# can be applied to N_A(q), and afterwards the remaining R_theta rewrites.
q=r(p,theta)
assert r(n(q,'A'),c+phi)==tip
# Free 3-cell path presentation: no 4-cell equates these derivation strings.
def admit(packet):
 if packet.get('from')!=aggregate or packet.get('to')!=staged:return 'WRONG_BOUNDARY'
 if packet.get('constructor')=='same_packet_tip':return 'MISSING_COHERENCE_4CELL'
 return 'UNVERIFIED_NEW_CONSTRUCTOR'
assert admit({'from':aggregate,'to':staged,'constructor':'same_packet_tip'})=='MISSING_COHERENCE_4CELL'
report={'passed':True,'starting_proof':['1','2','0','1'],'theta':'1/2','phi':'1/2','common_tip':['2','1','2','0'],'aggregate_3cell_path':aggregate,'staged_3cell_path':staged,'parallel_path_strings_distinct':True,'missing_obligation':'coherence 4-cell for mixed 3-cell against redistribution composition','scope':'Exact rational packet boundaries and distinct formal higher paths. Mixed 3-cell itself not sourced/admitted; this does not provide a 4-cell, proof-history identity or analytic correspondence.'}
out=Path(__file__).resolve().parents[1]/'results/mixed-interchange-coherence.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
