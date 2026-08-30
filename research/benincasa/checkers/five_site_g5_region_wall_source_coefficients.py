import json, math
from pathlib import Path

from five_site_g5_source_residue import I,si,CI,L0,NN,HH,ivecadd,ivecscale,idot,sqrti

src=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
base=json.loads(Path('research/benincasa/results/five-site-g5-source-residue.json').read_text())
cm=json.loads(Path('research/benincasa/results/five-site-g5-cm-domain.json').read_text())
census=json.loads(Path('research/benincasa/results/five-site-g5-region-wall-tangent-census.json').read_text())
labels=sorted(q['label'] for q in census['records'][0]['walls'])
t=-math.sqrt(cm['x']);E=5*t
P=[(math.cos(2*math.pi*k/5),math.sin(2*math.pi*k/5),1.0) for k in range(5)]
C=[(0.,0.,0.)]
for k in range(4):C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda u,v:sum(a*b for a,b in zip(u,v));norm=lambda u:math.sqrt(dot(u,u))
def sites(label):return {int(c)-1 for c in label[2:]}
def cuts(A):return [e for e in range(5) if (e in A)!=((e+1)%5 in A)]
def wall(label,X,y):
    if label=='G':return sum(X)
    if label.startswith('G_minus_e'):return sum(X)+2*y[int(label[-2])-1]
    A=sites(label);return sum(X[i] for i in A)+sum(y[e] for e in cuts(A))
records=[];blocked=[]
for sh in base['records']:
    l=sh['loop_point'];y=[norm(tuple(l[k]-q[k] for k in range(3))) for q in C]
    for label in labels:
        source_term_count=sum('G_minus_e12' in term and label in term for term in src['terms'])
        if source_term_count==0:
            blocked.append({'sheet':sh['sheet'],'label':label,
                            'reason':'no source term contains both labelled walls'})
            continue
        A=sites(label);inside=[i for i in A if i!=4];outside=[i for i in range(4) if i not in A]
        if not inside or not outside:
            blocked.append({'sheet':sh['sheet'],'label':label,'reason':'not independently tunable at fixed E_T and X_5'})
            continue
        candidates=[];degenerate=[]
        for adj in inside:
            for comp in outside:
                X=[t]*5;delta=-wall(label,X,y);X[adj]+=delta;X[comp]-=delta
                assert abs(sum(X)-E)<1e-9 and abs(wall('g_5',X,y))<1e-8 and abs(wall(label,X,y))<1e-8
                common=[q for q in src['common_prefactor'] if q!='g_5'];terms=[];vals=[]
                for term in src['terms']:
                    if 'G_minus_e12' not in term or label not in term:continue
                    labs=common+[q for q in term if q not in {'G_minus_e12',label}]
                    zs=[wall(q,X,y) for q in labs]
                    zeros=[q for q,z in zip(labs,zs) if abs(z)<1e-9]
                    if zeros:degenerate.extend(zeros);terms=[];break
                    vals.extend(zs);terms.append(math.prod(1/z for z in zs))
                if terms:candidates.append((min(abs(z) for z in vals),adj,comp,X,sum(terms)/2,len(terms)))
        if not candidates:
            blocked.append({'sheet':sh['sheet'],'label':label,
                            'reason':'forced deeper marked incidence at fixed threshold geometry',
                            'additional_zero_labels':sorted(set(degenerate))})
            continue
        sep,adj,comp,X,total,count=max(candidates)
        records.append({'sheet':sh['sheet'],'label':label,'adjusted_site':adj+1,'compensator_site':comp+1,
                        'term_count':count,'minimum_remaining_wall_abs':sep,
                        'residue_coefficient':total,'discovery_nonzero':abs(total)>1e-12})
exact=[]
for rec in records:
    ll=ivecadd(L0,ivecscale(rec['sheet']*HH,NN))
    yi=[sqrti(idot(tuple(a-b for a,b in zip(ll,q)),tuple(a-b for a,b in zip(ll,q)))) for q in CI]
    Xi=[-si for _ in range(5)];label=rec['label'];A=sites(label)
    def iw(q):
        if q=='G':return sum(Xi,I(0))
        if q.startswith('G_minus_e'):return sum(Xi,I(0))+2*yi[int(q[-2])-1]
        B=sites(q);return sum((Xi[i] for i in B),I(0))+sum((yi[e] for e in cuts(B)),I(0))
    adj=rec['adjusted_site']-1;comp=rec['compensator_site']-1;delta=-iw(label);Xi[adj]=Xi[adj]+delta;Xi[comp]=Xi[comp]-delta
    common=[q for q in src['common_prefactor'] if q!='g_5'];tot=I(0);walls={};count=0
    for term in src['terms']:
        if 'G_minus_e12' not in term or label not in term:continue
        labs=common+[q for q in term if q not in {'G_minus_e12',label}];value=I(1)
        for q in labs:
            z=iw(q);assert not z.l<=0<=z.h;walls[q]=[str(z.l),str(z.h)];value=value/z
        tot=tot+value;count+=1
    tot=tot/2;assert count==rec['term_count'] and not tot.l<=0<=tot.h
    exact.append({'sheet':rec['sheet'],'label':label,'term_count':count,
                  'remaining_wall_count':len(walls),'residue_interval':[str(tot.l),str(tot.h)],
                  'certified_nonzero':True})
packet={'schema':'marici.five_site_g5_region_wall_source_coefficients.discovery.v1',
        'records':records,'blocked':blocked,
        'tested_count':len(records),'blocked_count':len(blocked),
        'zero_discovery_labels':sorted(set(q['label'] for q in records if not q['discovery_nonzero'])),
        'exact_interval_certificates':exact,'all_tested_coefficients_certified_nonzero':True,
        'precision':'exact rational interval certificates plus f64 discovery'}
Path('research/benincasa/results/five-site-g5-region-wall-source-coefficients.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({'tested_count':len(records),'blocked':blocked,'zero_discovery_labels':packet['zero_discovery_labels'],
                  'term_counts':sorted(set(q['term_count'] for q in records))},sort_keys=True))
