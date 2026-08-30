import json, math
from pathlib import Path

from five_site_g5_source_residue import I,si,CI,L0,NN,HH,ivecadd,ivecscale,idot,sqrti

src=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
base=json.loads(Path('research/benincasa/results/five-site-g5-source-residue.json').read_text())
cm=json.loads(Path('research/benincasa/results/five-site-g5-cm-domain.json').read_text())
t=-math.sqrt(cm['x']); E=5*t
P=[(math.cos(2*math.pi*k/5),math.sin(2*math.pi*k/5),1.0) for k in range(5)]
C=[(0.,0.,0.)]
for k in range(4):C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda u,v:sum(a*b for a,b in zip(u,v))
norm=lambda u:math.sqrt(dot(u,u))
cuts=lambda sites:[e for e in range(5) if (e in sites)!=((e+1)%5 in sites)]
def wall(label,X,y):
    if label=='G':return sum(X)
    if label.startswith('G_minus_e'):return sum(X)+2*y[int(label[-2])-1]
    sites={int(c)-1 for c in label[2:]}
    return sum(X[i] for i in sites)+sum(y[e] for e in cuts(sites))

records=[]
for sh in base['records']:
    l=sh['loop_point'];y=[norm(tuple(l[k]-q[k] for k in range(3))) for q in C]
    for site in range(1,5):
        boundary=cuts({site-1}); xj=-sum(y[e] for e in boundary)
        candidates=[]
        for comp in [q for q in range(1,5) if q!=site]:
            X=[t]*5; delta=xj-X[site-1];X[site-1]=xj;X[comp-1]-=delta
            assert abs(sum(X)-E)<1e-10 and abs(wall('g_5',X,y))<1e-8
            assert abs(wall(f'g_{site}',X,y))<1e-8
            common=[q for q in src['common_prefactor'] if q not in {'g_5',f'g_{site}'}]
            vals=[];total=0.;ok=True
            for term in src['terms']:
                if 'G_minus_e12' not in term:continue
                labels=common+[q for q in term if q!='G_minus_e12']
                zs=[wall(q,X,y) for q in labels]
                if min(abs(z) for z in zs)<1e-9:ok=False;break
                vals.extend(zs);total+=math.prod(1/z for z in zs)
            if ok:candidates.append((min(abs(z) for z in vals),comp,X,total/2))
        assert candidates
        sep,comp,X,total=max(candidates)
        records.append({'sheet':sh['sheet'],'site':site,'compensator_site':comp,
                        'energies':X,'minimum_remaining_wall_abs':sep,
                        'quadruple_residue_coefficient':total,
                        'discovery_nonzero':abs(total)>1e-12})
assert all(q['discovery_nonzero'] for q in records)

exact=[]
for rec in records:
    ll=ivecadd(L0,ivecscale(rec['sheet']*HH,NN))
    yi=[sqrti(idot(tuple(a-b for a,b in zip(ll,q)),tuple(a-b for a,b in zip(ll,q)))) for q in CI]
    ti=-si; Ei=5*ti; site=rec['site'];comp=rec['compensator_site']
    boundary=cuts({site-1});xj=-sum((yi[e] for e in boundary),I(0))
    Xi=[ti for _ in range(5)];delta=xj-Xi[site-1];Xi[site-1]=xj;Xi[comp-1]=Xi[comp-1]-delta
    def iw(label):
        if label=='G':return sum(Xi,I(0))
        if label.startswith('G_minus_e'):return sum(Xi,I(0))+2*yi[int(label[-2])-1]
        sites={int(c)-1 for c in label[2:]}
        return sum((Xi[i] for i in sites),I(0))+sum((yi[e] for e in cuts(sites)),I(0))
    common=[q for q in src['common_prefactor'] if q not in {'g_5',f'g_{site}'}]
    tot=I(0);walls={}
    for term in src['terms']:
        if 'G_minus_e12' not in term:continue
        labels=common+[q for q in term if q!='G_minus_e12'];value=I(1)
        for q in labels:
            z=iw(q);assert not z.l<=0<=z.h;walls[q]=[str(z.l),str(z.h)];value=value/z
        tot=tot+value
    tot=tot/2;assert not tot.l<=0<=tot.h
    exact.append({'sheet':rec['sheet'],'site':site,'compensator_site':comp,
                  'residue_interval':[str(tot.l),str(tot.h)],
                  'remaining_wall_count':len(walls),'certified_nonzero':True})
packet={'schema':'marici.five_site_g5_singleton_source_coefficients.discovery.v1',
        'records':records,'all_eight_discovery_coefficients_nonzero':True,
        'exact_interval_certificates':exact,'all_eight_exact_coefficients_nonzero':True,
        'precision':'exact rational interval certificates plus f64 discovery'}
Path('research/benincasa/results/five-site-g5-singleton-source-coefficients.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
