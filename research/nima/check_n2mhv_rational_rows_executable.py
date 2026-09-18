#!/usr/bin/env python3
"""Execute every plain/ordinary line-plane row in the 14-class fixture."""
import itertools,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from momentum_twistor_super import external_supertwistor,super_line_plane_point,super_five_bracket,super_five_bracket_product_component
fixture=json.loads((ROOT/'research/nima/fixtures/n2mhv-yangian-invariant-constructor-coverage.v1.json').read_text())
xs=list(map(s.Integer,(1,2,4,7,11,16,22,29,37,46)));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)};S={i:external_supertwistor(i,Z[i]) for i in Z}
def split_args(text):
 out=[];start=0;depth=0
 for i,ch in enumerate(text):
  depth += (ch=='(')-(ch==')')
  if ch==',' and depth==0:out.append(text[start:i]);start=i+1
 out.append(text[start:]);return out
def digits(group):return [int(c) for c in group]
def atom(text):
 text=text.strip()
 if text.isdigit():return S[int(text)]
 m=re.fullmatch(r'\((\d+)\)cap\((\d+)\)',text);assert m,text
 left,right=digits(m.group(1)),digits(m.group(2))
 line,plane=(left,right) if len(left)==2 else (right,left)
 assert len(line)==2 and len(plane)==3
 return super_line_plane_point(S[line[0]],S[line[1]],S[plane[0]],S[plane[1]],S[plane[2]])
def evaluate(formula):
 groups=re.findall(r'\[([^\]]+)\]',formula);assert len(groups)==2
 polys=[super_five_bracket(tuple(atom(x) for x in split_args(g))) for g in groups]
 labels=sorted(set().union(*(set(m) for p in polys for m in p)))
 for a,b in itertools.combinations(labels,2):
  pairs=((a,b),)*4;v=super_five_bracket_product_component(polys[0],polys[1],pairs)
  if v!=0:return pairs,v,len(polys[0]),len(polys[1])
 raise ValueError('no nonzero component found')
rows=[]
for row in fixture['cyclic_classes']:
 if row['kind'] not in ('plain','line-plane'):continue
 pairs,value,nl,nr=evaluate(row['formula']);rows.append({'id':row['id'],'kind':row['kind'],'component_pair':list(pairs[0]),'coefficient':str(value),'left_coefficients':nl,'right_coefficients':nr})
checks={'all_twelve_nonexceptional_rational_rows_executed':len(rows)==12,'all_selected_components_nonzero':all(s.sympify(r['coefficient'])!=0 for r in rows),'all_products_degree_eight':all(r['left_coefficients']>0 and r['right_coefficients']>0 for r in rows)}
out={'schema':'marici.nima.n2mhv-rational-rows-executable.v1','source_fixture':'research/nima/fixtures/n2mhv-yangian-invariant-constructor-coverage.v1.json','rows':rows,'checks':checks,'passed':all(checks.values()),'scope':'One automatically selected exact nonzero degree-eight component for each of the 12 plain/ordinary line-plane cyclic classes; phi and psi are checked separately.'}
p=ROOT/'research/nima/results/n2mhv-rational-rows-executable.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
