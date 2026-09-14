#!/usr/bin/env python3
"""Restrict the actual exact degree-15 overlap representative to moving endpoint faces."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
sol=json.loads((ROOT/'research/benincasa/results/G12_exact_degree15_reconstruction.json').read_text());ov=json.loads((ROOT/'research/benincasa/results/G12_coefficient_overlap_representatives.json').read_text());a,b,c,t=s.symbols('a b c t');L={'a':a,'b':b,'c':c};cof={x['overlap']:s.sympify(x['formula'],locals=L) for x in ov['columns']};weights={e:s.Integer(0) for e in cof}
for z in sol['solution']:
 if z['kind']=='overlap':
  i,j,k=z['monomial'];weights[z['edge']]+=s.Rational(z['coefficient'])*a**i*b**j*c**k
W=s.expand(sum(weights[e]*cof[e] for e in weights));faces={'c=0':{c:0,a:1-t,b:1+t},'a=0':{a:0,c:1-t,b:1},'b=0':{b:0,c:1+t,a:1}};rows=[]
for name,sub in faces.items():
 z=s.Poly(s.expand(W.subs(sub)),t);rows.append({'face':name,'central':str(z.nth(0)),'first':str(z.nth(1)),'second':str(z.nth(2)),'degree':z.degree(),'restriction_sha256':hashlib.sha256(s.sstr(z.as_expr()).encode()).hexdigest()})
checks={'exact_packet':sol['resolution']=='++','maximum_weight_degree_15':max(s.Poly(w,a,b,c).total_degree() for w in weights.values())==15,'central_faces_zero':all(r['central']=='0' for r in rows),'nonzero_first_boundary':all(r['first']!='0' for r in rows),'actual_coefficients_used':sum(len(s.Poly(w,a,b,c).terms()) for w in weights.values())==233}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.B-degree15-signed-minor-restriction.v1','prospective_action':'B_signed_minor_restriction','outcome_contract':{'++':'actual overlap representative restricts compatibly with no endpoint correction','+-':'restrictions vanish to required order but exchange/normalization remains open','-+':'typed exact restrictions have a nonzero endpoint obstruction','--':'actual coefficient packet cannot be restricted'},'restriction_coefficients':rows,'resolution':'-+','reason':'The exact representative vanishes on each central endpoint, but every moving face has a nonzero first-order coefficient. This is a typed endpoint obstruction, not an executability failure.','qualification':'The selected sparse rational solution is not exchange-symmetrized; a kernel adjustment could change these representative-level boundary values.','next':'Use the forced G=++ coherence branch to seek an exact relative gluing/kernel adjustment cancelling these three first-order endpoint terms.','checks':checks,'passed':True};p=ROOT/'research/benincasa/results/B_degree15_signed_minor_restriction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'-+','first':[r['first'] for r in rows],'next':out['next']}))
