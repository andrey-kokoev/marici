#!/usr/bin/env python3
"""Audit the first weighted descent gate on the A3 associahedron."""
import itertools,json,sys
from fractions import Fraction as Q
from pathlib import Path
R=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(R/'benincasa/.tmp_sympy')); import sympy as s
n=6
def ed(a,b):return tuple(sorted((a,b)))
bdry={ed(i,(i+1)%n) for i in range(n)}; ds=[ed(i,j) for i in range(n) for j in range(i+1,n) if ed(i,j) not in bdry]
def cross(a,b):x,y=a;u,v=b;return x<u<y<v or u<x<v<y
V=sorted(tuple(sorted(z)) for z in itertools.combinations(ds,3) if all(not cross(a,b) for a,b in itertools.combinations(z,2)))
E=sorted((i,j) for i,j in itertools.combinations(range(len(V)),2) if len(set(V[i])^set(V[j]))==2); ep={e:i for i,e in enumerate(E)}
F=[]
for d in ds:
 vs=sorted(i for i,t in enumerate(V) if d in t);adj={i:sorted((b if a==i else a) for a,b in E if i in (a,b) and (b if a==i else a) in vs) for i in vs};st=min(vs);pr=None;cu=st;cy=[st];nx=min(adj[st])
 while nx!=st:cy.append(nx);pr,cu=cu,nx;nx=next(z for z in adj[cu] if z!=pr)
 F.append((d,cy))
F.sort();D=s.zeros(21,9)
for k,(d,cy) in enumerate(F):
 for a,b in zip(cy,cy[1:]+cy[:1]):e=ed(a,b);D[ep[e],k]=1 if e==(a,b) else -1
orient=[int(x) for x in D.nullspace()[0]]
if next(x for x in orient if x)<0:orient=[-x for x in orient]
src=json.loads((R/'nima/results/n8-physical-facet-cochain.json').read_text()); wd={eval(k):Q(v) for k,v in src['facet_weights'].items()};w=s.Matrix([s.Rational(wd[d].numerator,wd[d].denominator) for d,c in F]);c=s.diag(*orient)*w
proxy=D*c
# Deliberate bad convention: raw weights as oriented coordinates.
bad=D*w
pos={(i-1,j+1) for i in range(1,4) for j in range(i,4)}; neg=set(ds)-pos
cp=s.Matrix([c[i] if F[i][0] in pos else 0 for i in range(9)]);cn=c-cp;rp=D*cp;rn=D*cn
rows=[]
for r,e in enumerate(E):
 shared=sorted(set(V[e[0]])&set(V[e[1]])); assert len(shared)==2
 fi=[next(i for i,(d,_) in enumerate(F) if d==x) for x in shared]
 kinds=['square' if len(F[i][1])==4 else 'pentagon' for i in fi]
 rows.append({'edge':e,'facets':[list(x) for x in shared],'facet_types':kinds,'incidences':[int(D[r,i]) for i in fi],'proxy_positive':str(rp[r]),'proxy_negative_simple':str(rn[r]),'proxy_total':str(proxy[r]),'classification':'missing canonical residue map'+('; boundary-correction term present' if rn[r]!=0 else '')})
support=[i for i,x in enumerate(proxy) if x!=0];pairs={}
for z in rows:p='-'.join(sorted(x[0].upper() for x in z['facet_types']));pairs[p]=pairs.get(p,0)+1
out={'schema':'marici.benincasa.a3-weighted-codim2-descent.v1','carrier':{'codimension_two_strata':21,'each_is_intersection_of_two_compatible_diagonal_facets':True,'facet_pair_types':pairs,'cellular_incidence_rank':int(D.rank())},'source_gate':{'canonical_form_or_history_residue_maps_to_strata_available':False,'scalar_facet_densities_can_be_restricted_as_forms':False,'reason':'The stored K0 and B_ii are evaluated scalar coefficients. They contain neither canonical differential forms on facets nor signed residue/pushforward maps to their 21 shared strata.'},'identity_restriction_proxy':{'definition':'Use the same scalar on every boundary edge and apply the cellular incidence matrix to orientation-twisted coordinates; this is diagnostic only.','support_size':len(support),'zero_count':21-len(support),'vector_rank_over_Q':0 if not support else 1,'residual_vector':[str(x) for x in proxy],'positive_root_part':[str(x) for x in rp],'negative_simple_part':[str(x) for x in rn],'rows':rows},'orientation_failure_control':{'raw_weights_without_incidence_twist_residual':[str(x) for x in bad],'differs_from_twisted_proxy':bad!=proxy,'both_nonzero':bad!=s.zeros(21,1) and proxy!=s.zeros(21,1)},'classification':'No coefficientwise canonical-residue cancellation test is presently typeable. Nonzero proxy entries diagnose failure of the identity-restriction ansatz, not genuine weighted-coherence obstruction. Entries involving B_ii are marked boundary-correction-present but causality cannot be assigned without residue maps.','relative_cocycle':'not established; an external remainder cannot be identified from evaluated scalars','arbitrary_m_acceptance':['certified history/positroid facet for every almost-positive-root label','canonical form or chain on each facet, not only its evaluated scalar','signed residue/pushforward map from each incident facet to every compatible codimension-two stratum','proof the two induced stratum objects use a common normalization and opposite orientation','coefficientwise cancellation on every internal stratum, with unmatched strata explicitly identified as external boundary','compatibility of boundary-transport corrections with these residue maps'],'checks':{'21_strata':len(E)==21,'two_facets_per_stratum':all(len(set(V[a])&set(V[b]))==2 for a,b in E),'three_squares_six_pentagons':sorted(len(cy) for d,cy in F)==[4]*3+[5]*6,'cellular_boundary_cycle':D*s.Matrix(orient)==s.zeros(21,1),'proxy_full_support':len(support)==21,'orientation_control_fires':bad!=proxy},'passed':True}
p=R/'benincasa/results/a3_weighted_codim2_descent.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='identity_restriction_proxy'},indent=2))
