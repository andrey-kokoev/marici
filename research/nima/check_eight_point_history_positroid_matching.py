#!/usr/bin/env python3
"""Match 20 sourced n=8 histories to classified rational G_+(2,8) cells."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r,theta_coefficients
from dual_spinor_kinematics import momentum_conserving_kinematics,transport_spinor
from momentum_twistor_constructors import four_bracket
from momentum_twistor_super import SuperTwistor,super_line_plane_point
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
n=8;lam,til,x=momentum_conserving_kinematics([(1,j*j+j+1) for j in range(1,n+1)],[(1,j**3+2*j+1) for j in range(1,n-1)]);eps=s.Matrix([[0,1],[-1,0]]);th=theta_coefficients(lam,n);Z={}
for j in range(1,n+1):
 lj=eps*lam[j];Z[j]=SuperTwistor(lam[j].col_join(x[j].T*lj),{k:s.factor((lj.T*v)[0]) for k,v in th[j].items() if (lj.T*v)[0]!=0})
def bracket(vertices):
 qs=[four_bracket(vertices[(r+1)%5].z,vertices[(r+2)%5].z,vertices[(r+3)%5].z,vertices[(r+4)%5].z) for r in range(5)];q={}
 for c,v in zip(qs,vertices):
  for k,w in v.chi.items():q[k]=s.expand(q.get(k,0)+c*w)
 return q,s.prod(qs)
def rot(j,r):return (j+r-1)%n+1
def point(token,r):
 if isinstance(token,int):return Z[rot(token,r)]
 a,b,c,d,e=token;return super_line_plane_point(Z[rot(a,r)],Z[rot(b,r)],Z[rot(c,r)],Z[rot(d,r)],Z[rot(e,r)])
def mapped_point(token,mp):
 if isinstance(token,int):return Z[mp[token]]
 a,b,c,d,e=token;return super_line_plane_point(Z[mp[a]],Z[mp[b]],Z[mp[c]],Z[mp[d]],Z[mp[e]])
I456_78=(7,8,4,5,6);I45_678=(4,5,6,7,8);I23_456=(2,3,4,5,6);I234_56=(5,6,2,3,4);I34_567=(3,4,5,6,7);I345_67=(6,7,3,4,5)
seeds={'A':((1,2,3,I456_78,8),(4,5,6,7,8)),'B':((1,2,3,4,8),(4,5,6,7,8)),'C':((1,2,3,I45_678,8),(4,5,6,7,8)),'D':((1,2,3,I45_678,I456_78),(4,5,6,7,8)),'E':((1,2,3,4,I456_78),(4,5,6,7,8)),'F':((1,2,I23_456,I234_56,6),(2,3,4,5,6)),'G':((1,2,I34_567,I345_67,7),(3,4,5,6,7)),'H':((1,2,3,I345_67,7),(3,4,5,6,7))};subsets=list(itertools.combinations(range(1,n+1),4));cands=[]
def add_candidate(name,tag,V1,V2):
 q1,d1=bracket(V1);q2,d2=bracket(V2);form={S:s.factor(s.det(s.Matrix([[lam[j][0] for j in S],[lam[j][1] for j in S],[q1.get(j,0) for j in S],[q2.get(j,0) for j in S]]))/(d1*d2)) for S in subsets};cands.append((name,tag,form))
for name,(L,R) in seeds.items():
 if name in 'ABCDE':
  for r in range(n):add_candidate(name,r,tuple(point(t,r) for t in L),tuple(point(t,r) for t in R))
 else:
  support=6 if name=='F' else 7
  for chosen in itertools.combinations(range(1,n+1),support):
   for r in range(support):
    order=chosen[r:]+chosen[:r];mp={j:order[j-1] for j in range(1,support+1)};add_candidate(name,{'support':list(chosen),'rotation':r},tuple(mapped_point(t,mp) for t in L),tuple(mapped_point(t,mp) for t in R))
def proportional(A,B):
 supportA={p for p in subsets if A[p]!=0};supportB={p for p in subsets if B[p]!=0}
 if supportA!=supportB:return None
 p=next(iter(supportA));q=s.factor(A[p]/B[p]);return q if all(s.factor(A[k]-q*B[k])==0 for k in subsets) else None
groups={'A':((1,2,3),(4,5,6),(7,),(8,)),'B':((1,2,3),(4,),(5,6,7),(8,)),'C':((1,2,3),(4,5),(6,7),(8,)),'D':((1,2,3),(4,5),(6,),(7,8)),'E':((1,2,3),(4,),(5,6),(7,8)),'F':((1,),(2,),(3,),(4,),(5,),(6,)),'G':((1,2),(3,4),(5,),(6,),(7,)),'H':((1,2),(3,),(4,5),(6,),(7,))}
def cell_key(name,embedding):
 if isinstance(embedding,int):mp={j:rot(j,embedding) for j in range(1,9)}
 else:
  chosen=tuple(embedding['support']);r=embedding['rotation'];order=chosen[r:]+chosen[:r];mp={j:order[j-1] for j in range(1,len(chosen)+1)}
 cls=tuple(sorted(tuple(sorted(mp[j] for j in g)) for g in groups[name]));support={j for g in cls for j in g};zeros=tuple(j for j in range(1,9) if j not in support);return (cls,zeros)
matches=[]
for hi,h in enumerate(compile_nnmhv_histories(n)):
 _,o=generalized_r(lam,x,n,(),h.outer_pair,lam[h.outer_pair[0]-1].T*eps,lam[h.outer_pair[1]].T*eps);st=terminal_r_state(h);_,inn=generalized_r(lam,x,n,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,st.lower_spinor.vertices),transport_spinor(lam,x,st.upper_spinor.vertices));H={S:s.factor(o['prefactor']*inn['prefactor']*s.det(s.Matrix([[lam[j][0] for j in S],[lam[j][1] for j in S],[o['xi_coefficients'].get(j,0) for j in S],[inn['xi_coefficients'].get(j,0) for j in S]]))) for S in subsets}
 for name,r,C in cands:
  q=proportional(H,C)
  if q is not None:matches.append({'history_index':hi,'seed_type':name,'embedding':r,'cell_key':cell_key(name,r),'form_ratio':str(q)})
unique={}
for m in matches:unique.setdefault((m['history_index'],m['cell_key']),m)
matches=list(unique.values())
for m in matches:m['cell_key']={'parallel_classes':[list(g) for g in m['cell_key'][0]],'zero_columns':list(m['cell_key'][1])}
checks={'twenty_histories_matched_once':len(matches)==20 and sorted(m['history_index'] for m in matches)==list(range(20)),'all_matches_unique':len({m['history_index'] for m in matches})==20,'twenty_distinct_positroid_cells':len({str(m['cell_key']) for m in matches})==20,'only_sourced_rational_seed_types':all(m['seed_type'] in seeds for m in matches)}
out={'schema':'marici.nima.eight-point-history-positroid-matching.v1','source':'1212.5605 Table g2n_yangian_invariants','matches':matches,'checks':checks,'passed':all(checks.values()),'scope':'Exact all-70 full one-SU(4) degree-four coefficients including five-bracket denominators; enough to identify each classified positroid canonical form projectively.'};p=ROOT/'research/nima/results/eight-point-history-positroid-matching.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
