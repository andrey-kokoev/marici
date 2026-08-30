import json, math
from pathlib import Path

from five_site_g5_source_residue import CI,L0,NN,HH,ci,ivecadd,ivecscale,idot,sqrti

packet=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
physical=json.loads(Path('research/benincasa/results/five-site-g5-source-residue.json').read_text())
labels=sorted(set(packet['common_prefactor']+sum(packet['terms'],[])))
regions=[q for q in labels if q.startswith('g_') and len(q[2:])>=2]
P=[(math.cos(2*math.pi*k/5),math.sin(2*math.pi*k/5),1.0) for k in range(5)]
C=[(0.,0.,0.)]
for k in range(4):C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda u,v:sum(a*b for a,b in zip(u,v))
sub=lambda u,v:tuple(a-b for a,b in zip(u,v))
add=lambda u,v:tuple(a+b for a,b in zip(u,v))
scale=lambda a,u:tuple(a*x for x in u)
norm=lambda u:math.sqrt(dot(u,u))
def cuts(label):
    sites={int(c)-1 for c in label[2:]}
    return [e for e in range(5) if (e in sites)!=((e+1)%5 in sites)]
records=[]
for sh in physical['records']:
    l=tuple(sh['loop_point']);ne=scale(1/norm(sub(l,C[0])),sub(l,C[0]));rows=[]
    for q in regions:
        grad=(0.,0.,0.)
        for e in cuts(q):grad=add(grad,scale(1/norm(sub(l,C[e])),sub(l,C[e])))
        tangent=sub(grad,scale(dot(grad,ne),ne));n2=dot(tangent,tangent)
        rows.append({'label':q,'boundary_edges':[e+1 for e in cuts(q)],
                     'tangent_gradient_norm_squared':n2,
                     'vanishes_numerically':n2<1e-12})
    records.append({'sheet':sh['sheet'],'walls':rows})
zero=sorted(set(q['label'] for r in records for q in r['walls'] if q['vanishes_numerically']))
exact=[]
for sheet in (-1,1):
    ll=ivecadd(L0,ivecscale(sheet*HH,NN));ne=ivecscale(ci.inv(),ll);rows=[]
    for q in regions:
        grad=(ci-ci,ci-ci,ci-ci)
        for e in cuts(q):
            d=tuple(a-b for a,b in zip(ll,CI[e]));grad=ivecadd(grad,ivecscale(sqrti(idot(d,d)).inv(),d))
        tangent=ivecadd(grad,ivecscale(-idot(grad,ne),ne));n2=idot(tangent,tangent)
        assert n2.l>0
        rows.append({'label':q,'norm_squared_interval':[str(n2.l),str(n2.h)],'certified_nonzero':True})
    exact.append({'sheet':sheet,'walls':rows})
packet_out={'schema':'marici.five_site_g5_region_wall_tangent_census.discovery.v1',
            'region_wall_count':len(regions),'records':records,
            'numerically_vanishing_labels':zero,
            'exact_interval_certificates':exact,
            'all_thirty_tangent_gradients_certified_nonzero':True,
            'precision':'exact rational interval certificates plus f64 discovery'}
Path('research/benincasa/results/five-site-g5-region-wall-tangent-census.json').write_text(
 json.dumps(packet_out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({'region_wall_count':len(regions),'numerically_vanishing_labels':zero,
                  'minimum_nonzero':min(q['tangent_gradient_norm_squared'] for r in records for q in r['walls'] if not q['vanishes_numerically'])},sort_keys=True))
