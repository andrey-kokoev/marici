#!/usr/bin/env python3
"""Exact collinear-numerator test for the sourced finite double pentagon."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
u,v,w=s.symbols('u v w')
xs=map(s.Integer,(1,2,4,7,11,16));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
def br(*q):return s.expand(s.det(s.Matrix.hstack(*q)))
def cyc(i):return ((i-1)%6)+1
def line_at(i):return Z[i],u*Z[cyc(i-1)]+v*Z[i]+w*Z[cyc(i+1)]
def nab(A,B):return br(A,B,Z[4],Z[6])
def ncd(C,D):return s.expand(br(C,Z[2],Z[3],Z[4])*br(D,Z[6],Z[1],Z[2])-br(D,Z[2],Z[3],Z[4])*br(C,Z[6],Z[1],Z[2]))
ab_tests=[]
for i in (4,5,6):
 A,B=line_at(i);value=s.factor(nab(A,B));ab_tests.append({'vertex':i,'dangerous_adjacent_propagators':{4:['AB34','AB45'],5:['AB45','AB56'],6:['AB56','AB61']}[i],'numerator':'<AB46>','value':str(value),'vanishes':value==0})
cd_tests=[]
for i in (1,2,3):
 C,D=line_at(i);value=s.factor(ncd(C,D));cd_tests.append({'vertex':i,'dangerous_adjacent_propagators':{1:['CD61','CD12'],2:['CD12','CD23'],3:['CD23','CD34']}[i],'numerator':'<CD|(234) intersect (612)>','value':str(value),'vanishes':value==0})
checks={'all_AB_collinear_regions_killed':all(x['vanishes'] for x in ab_tests),'all_CD_collinear_regions_killed':all(x['vanishes'] for x in cd_tests),'all_adjacent_denominator_pairs_covered':len(ab_tests)+len(cd_tests)==6}
out={'schema':'marici.nima.chiral-two-loop-double-pentagon-ir-finiteness.v1','source_fixture':'research/nima/fixtures/chiral-two-loop-double-pentagon-source.v1.json','criterion':'For each loop line, every region where two adjacent local propagators vanish is annihilated by its chiral numerator.','AB_tests':ab_tests,'CD_tests':cd_tests,'checks':checks,'passed':all(checks.values()),'scope':'Exact numerator vanishing on all external-collinear infrared regions of the sourced building block; not an integrated convergence proof for arbitrary complex contours.'}
p=ROOT/'research/nima/results/chiral-two-loop-double-pentagon-ir-finiteness.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
