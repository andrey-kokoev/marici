#!/usr/bin/env python3
"""Derive vector fields that do not create forbidden double poles on simple G12 walls."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
a,b,c=s.symbols('a b c');Aa,Ab,Ac=s.symbols('Aa Ab Ac')
B=c+3;g3=a+b+1
# A(B)=Ac and A(g3)=Aa+Ab. Avoiding B^-2 and g3^-2 forces both zero.
sol=s.linsolve([Ac,Aa+Ab],[Aa,Ab,Ac]);h=s.symbols('h');generator=s.Matrix([1,-1,0])
# Action on the remaining linear walls.
walls={'g1':b+c+1,'g2':a+c+1,'s23':b+c+2,'s31':a+c+2}
def act(q):return s.expand(generator.dot(s.Matrix([s.diff(q,a),s.diff(q,b),s.diff(q,c)])))
action={k:int(act(q)) for k,q in walls.items()}
# Exchange sends coordinates and vector components; pushforward of (1,-1,0) is (-1,1,0).
checks={'solution_module_rank_one':sol=={(-Ab,Ab,0)},'generator_tangent_B12':act(B)==0,'generator_tangent_g3':act(g3)==0,'action_matches_shape_derivative':action=={'g1':-1,'g2':1,'s23':-1,'s31':1},'generator_exchange_odd':[-1,1,0]==[-x for x in generator]}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-twisted-Hermite-tangent-module.v1','simple_pole_walls':['B12=c+3','g3=a+b+1'],'no_new_double_pole_equations':['A(B12)=A_c=0','A(g3)=A_a+A_b=0'],'solution_module':'Q[a,b,c]*(partial_a-partial_b)','primitive_generator':[1,-1,0],'action_on_cubic_walls':action,'exchange_character':-1,'result':'Preserving the already-simple B12 and g3 poles forces every polynomial Hermite vector field to be a multiple of the physical exchange-odd shape direction. There is no three-component freedom left for a generic Jacobian-ideal solve.','twisted_operator_for_A=hV':'div(hV) -(3/2)h V(K0)/K0 -2h[V(g1)/g1+V(g2)/g2+V(s23)/s23+V(s31)/s31], with V=partial_a-partial_b, plus V(h)','next_task':'Solve the resulting scalar Hermite equation for polynomial/rational h in the antisymmetric sector and test whether its residual has only simple g1,g2,s23,s31 poles.','checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/G12_twisted_Hermite_tangent_module.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'module':out['solution_module'],'actions':action,'next':out['next_task']}))
