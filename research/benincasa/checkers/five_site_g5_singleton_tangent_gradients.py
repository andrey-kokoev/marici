import json, math
from pathlib import Path

from five_site_g5_source_residue import CI,L0,NN,HH,ci,ivecadd,ivecscale,idot

src=json.loads(Path('research/benincasa/results/five-site-g5-source-residue.json').read_text())
P=[(math.cos(2*math.pi*k/5),math.sin(2*math.pi*k/5),1.0) for k in range(5)]
C=[(0.,0.,0.)]
for k in range(4):C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda u,v:sum(a*b for a,b in zip(u,v))
sub=lambda u,v:tuple(a-b for a,b in zip(u,v))
add=lambda u,v:tuple(a+b for a,b in zip(u,v))
scale=lambda a,u:tuple(a*x for x in u)
norm=lambda u:math.sqrt(dot(u,u))
cuts={1:(4,0),2:(0,1),3:(1,2),4:(2,3),5:(3,4)}
records=[]
for sheet in src['records']:
    l=tuple(sheet['loop_point'])
    ne=scale(1/norm(sub(l,C[0])),sub(l,C[0]))
    rows=[]
    for site in range(1,5):
        e1,e2=cuts[site]
        grad=add(scale(1/norm(sub(l,C[e1])),sub(l,C[e1])),
                 scale(1/norm(sub(l,C[e2])),sub(l,C[e2])))
        tangent=sub(grad,scale(dot(grad,ne),ne))
        rows.append({'site':site,'relative_label_mod_5':(site-5)%5,
                     'tangent_gradient_norm_squared':dot(tangent,tangent),
                     'tangent_gradient_nonzero':dot(tangent,tangent)>1e-12})
    assert all(q['tangent_gradient_nonzero'] for q in rows)
    records.append({'sheet':sheet['sheet'],'singletons':rows})

exact=[]
for sheet in (-1,1):
    ll=ivecadd(L0,ivecscale(sheet*HH,NN))
    ne=ivecscale(ci.inv(),ll)
    rows=[]
    for site in range(1,5):
        e1,e2=cuts[site]
        d1=tuple(a-b for a,b in zip(ll,CI[e1]));d2=tuple(a-b for a,b in zip(ll,CI[e2]))
        y1i=idot(d1,d1);y2i=idot(d2,d2)
        # Certified distance intervals are obtained by the same enclosing sqrt.
        from five_site_g5_source_residue import sqrti
        grad=ivecadd(ivecscale(sqrti(y1i).inv(),d1),ivecscale(sqrti(y2i).inv(),d2))
        tangent=ivecadd(grad,ivecscale(-idot(grad,ne),ne))
        n2=idot(tangent,tangent);assert n2.l>0
        rows.append({'site':site,'norm_squared_interval':[str(n2.l),str(n2.h)],
                     'certified_nonzero':True})
    exact.append({'sheet':sheet,'singletons':rows})
packet={'schema':'marici.five_site_g5_singleton_tangent_gradients.discovery.v1',
        'records':records,'all_eight_tangent_gradients_nonzero':True,
        'exact_interval_certificates':exact,
        'precision':'exact rational interval certificates plus f64 discovery'}
Path('research/benincasa/results/five-site-g5-singleton-tangent-gradients.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
