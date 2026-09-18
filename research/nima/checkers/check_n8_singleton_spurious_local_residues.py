#!/usr/bin/env python3
"""Exact local pushforward residues for singleton nonstandard n=8 target hypersurfaces."""
from pathlib import Path
import json,sys,itertools
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
grp=json.loads((ROOT/'research/nima/results/n8-target-boundary-grouping.json').read_text());matches={x['history_index']:x for x in json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches']};a=s.symbols('a1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
M={'F':s.Matrix([[1,A1+A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,1,A5,A6,A7,A8]]),'G':s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'H':s.Matrix([[1,A1,A2+A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'A':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'B':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'C':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'D':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]]),'E':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]])}
def embed(q,mat):
 emb=q['embedding'];sup=list(range(1,9)) if isinstance(emb,int) else emb['support'];rot=emb if isinstance(emb,int) else emb['rotation'];out=s.zeros(2,8)
 for j in range(mat.cols):out[:,sup[(j+rot)%len(sup)]-1]=(-1 if j+rot>=len(sup) else 1)*mat[:,j]
 return out
Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])};single=[]
for g in grp['groups']:
 if g['kind']!='standard_bracket' and g['multiplicity']==1:single.append((g['target_label'],g['branches'][0]))
rows=[]
for label,b in single:
 q=matches[b['history_index']];e=b['alpha'];free=[x for i,x in enumerate(a,1) if i!=e];Y=embed(q,M[q['seed_type']]).subs(a[e-1],0)*Z;piv=next((i,j) for i in range(6) for j in range(i+1,6) if s.det(Y[:,[i,j]]).subs(vals)!=0);N=s.simplify(Y[:,list(piv)].inv()*Y);coords=[N[i,j] for i in range(2) for j in range(6) if j not in piv];J=s.Matrix(coords).jacobian(free).subs(vals);_,inds=J.T.rref();chosen=list(inds);minor=J[chosen,:].det();prod=s.prod(vals[x] for x in free);density=s.cancel(s.Integer(b['source_coefficient'])/(prod*minor));rows.append({'target_label':label,'history_index':b['history_index'],'seed':b['seed'],'alpha':e,'source_coefficient':b['source_coefficient'],'target_pivot_columns':[i+1 for i in piv],'chosen_target_coordinate_indices':[i+1 for i in chosen],'jacobian_minor':str(minor),'local_pushforward_density':str(density),'nonzero':density!=0})
checks={'expected_seven_singletons':len(rows)==7,'all_jacobian_minors_nonzero':all(s.Rational(r['jacobian_minor'])!=0 for r in rows),'all_local_pushforward_densities_nonzero':all(r['nonzero'] for r in rows)};out={'schema':'marici.nima.n8-singleton-spurious-local-residues.v1','evaluation_parameters':{str(k):int(v) for k,v in vals.items()},'singleton_hypersurfaces':len(rows),'details':rows,'checks':checks,'passed':all(checks.values()),'interpretation':'Each reported source sheet has a nonzero local pushforward residue at the exact regular point. This excludes pointwise Jacobian vanishing, but not cancellation in the field trace over multiple preimages belonging to the same parametrized sheet.'};p=ROOT/'research/nima/results/n8-singleton-spurious-local-residues.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
