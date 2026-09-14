#!/usr/bin/env python3
"""First simultaneous Griffiths-Dwork reduction of the cleared G12 odd jet."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text())
a,b,c=s.symbols('a b c');L={'a':a,'b':b,'c':c}
K=s.sympify(data['K0'],locals=L)
D=s.expand((c+3)*(b+c+1)*(a+c+1)*(a+b+1)*K)
N=s.expand(s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L)-s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L))
gens=[s.diff(D,a),s.diff(D,b),s.diff(D,c),D]
G=s.groebner(gens,a,b,c,order='grevlex',domain=s.QQ);quot,rem=G.reduce(N);rem=s.expand(rem)
swap={a:b,b:a};class_odd_remainder=s.expand(G.reduce(s.expand(rem+rem.xreplace(swap)))[1])
encoded=s.sstr(rem).encode();sample=s.factor(rem.subs({a:0,b:1,c:2}))
checks={'squarefree_product_degree_eight':s.Poly(D,a,b,c).total_degree()==8,'odd_target_degree_fourteen':s.Poly(N,a,b,c).total_degree()==14,'groebner_basis_nonempty':len(G.polys)==10,'division_reconstructs':s.expand(sum(q*p.as_expr() for q,p in zip(quot,G.polys))+rem-N)==0,'remainder_nonzero':rem!=0,'remainder_class_exchange_odd':class_odd_remainder==0,'nonzero_exact_sample':sample!=0}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-odd-squarefree-Jacobian-reduction.v1','squarefree_divisor':'B12*g1*g2*g3*K0','divisor_degree':8,'target_degree':14,'jacobian_generators':['d_a D','d_b D','d_c D','D'],'groebner_order':'graded reverse lexicographic (a,b,c)','groebner_basis_size':len(G.polys),'jacobian_membership':False,'normal_form':{'degree':s.Poly(rem,a,b,c).total_degree(),'monomial_count':len(s.Poly(rem,a,b,c).terms()),'sha256':hashlib.sha256(encoded).hexdigest(),'sample_a0_b1_c2':s.sstr(sample)},'exchange_statement':'Although the chosen monomial order is not swap-invariant, rem(a,b,c)+rem(b,a,c) reduces to zero in the Jacobian quotient. Hence the surviving quotient class is exchange-odd.','result':'The cleared odd jet is not wholly reducible by a squarefree global divergence. Simultaneous Griffiths-Dwork division leaves a nonzero exchange-odd Jacobian-ring class.','interpretation_boundary':'This is a global algebraic survivor, not yet the simple mixed-residue matrix: actual unequal pole multiplicities, relative boundaries, and integral normalization remain to be incorporated.','next_task':'Lift the Groebner quotient coefficients to the actual multiplicity vector (B12,K0^2,g1^3,g2^3,g3,s^3), subtract the exact divergence, and compute the simple-wall residues of the surviving normal form.','checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/G12_odd_squarefree_Jacobian_reduction.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'membership':False,'remainder_terms':out['normal_form']['monomial_count'],'odd_class':True,'sample':out['normal_form']['sample_a0_b1_c2']}))
