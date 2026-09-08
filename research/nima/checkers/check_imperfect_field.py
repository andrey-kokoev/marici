"""Polynomial certificates for an imperfect-field recovery obstruction."""
import json
from pathlib import Path
from sympy import symbols, Poly
v,u,x=symbols('v u x')
records=[]
for p,e in [(2,1),(3,1),(2,2),(3,2)]:
    m=p**e;n=m+3
    f=Poly(x**m-u,x)
    assert f.LC()==1 and f.TC()==-u
    assert all(f.nth(j)==0 for j in range(1,m))
    assert Poly(x**m-u,x,u,modulus=p).diff(x).is_zero
    assert Poly(Poly(v**m-u,u,v,modulus=p).as_expr().subs(u,v**m),v,modulus=p).is_zero
    assert Poly((x-v)**m-(x**m-v**m),x,v,modulus=p).is_zero
    assert 1%m!=0
    records.append({'p':p,'n':n,'extension_degree':m,'valuation_obstruction':[m,1],'unique_geometric_root':True,'root_polynomial':'x^%d-u'%m,'reconstruction':'v^%d=u'%m})
result={'status':'passed','records':records,'scope':'Eisenstein coefficient conditions and Frobenius identities; generic proof supplies irreducibility and minimal extension, not sample root search.'}
Path('research/nima/results/imperfect_field.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
