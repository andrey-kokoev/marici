#!/usr/bin/env python3
"""Joint E7 character multiplicities of commuting coordinate reflections."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
g=json.loads((ROOT/'research/voevodsky/results/global_del_pezzo_double_cover.json').read_text())
a,b,h,x,y,z=s.symbols('a b h x y z');G=s.sympify(g['G'])
# One nonzero discriminant specialization proves each binary-quartic restriction is generically smooth.
Gs=G.subs({x:2,y:3,z:4})
fixed_line_data=[]
for reflection,var,u,v in [('ra',a,b,h),('rb',b,a,h),('rh',h,a,b)]:
 f=s.factor(Gs.subs(var,0).subs(v,1));disc=s.factor(s.discriminant(f,u))
 opposite={a:0,b:0,h:0};opposite[var]=1
 fixed_line_data.append({'reflection':reflection,'affine_quartic':str(f),'discriminant':str(disc),'opposite_value':str(s.factor(Gs.subs(opposite)))})
# n=(++,+-,-+,--); total and traces of ra, rb, ra*rb are 7,-1,-1,-1.
A=s.Matrix([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])
y=s.Matrix([7,-1,-1,-1]);n=A.inv()*y
checks={
 'global_coordinate_reflections':all(k in g['global_involutions'] for k in ('r_a','r_b')),
 'ra_E7_multiplicities':g['fixed_locus_r_a']['E7_eigen_multiplicities']=={'+1':3,'-1':4},
 'all_fixed_line_quartics_generically_smooth':all(s.sympify(r['discriminant'])!=0 for r in fixed_line_data),
 'all_isolated_points_have_two_cover_points':all(s.sympify(r['opposite_value'])!=0 for r in fixed_line_data),
 'joint_multiplicities':n==s.Matrix([1,2,2,2]),
 'ra_fixed_rank':int(n[0]+n[1])==3,
 'rb_fixed_rank':int(n[0]+n[2])==3,
 'common_fixed_rank':int(n[0])==1,
 'nonnegative_integral':all(v.is_integer and v>=0 for v in n),
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.joint-reflection-character-decomposition.v1','passed':True,'fixed_locus_genericity_witness':{'parameters':{'x':2,'y':3,'z':4},'coordinate_reflections':fixed_line_data},'E7_traces':{'ra':-1,'rb':-1,'ra_rb_equals_rh':-1},'joint_characters':{'++':1,'+-':2,'-+':2,'--':2},'ra_fixed_rank':3,'rb_fixed_rank':3,'common_fixed_rank':1,'consequence':'the two rank-three pencil sectors share only one rational ambient direction; a rank-two return correspondence is extra data','checks':checks}
p=ROOT/'research/voevodsky/results/joint_reflection_character_decomposition.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'joint_multiplicities':[int(v) for v in n],'common_fixed_rank':1}))
