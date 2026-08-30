import json,math
from pathlib import Path

from five_site_g5_source_residue import I,CI,idot,sqrti

src=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
L=CI[3]
yi=[sqrti(idot(tuple(a-b for a,b in zip(L,q)),tuple(a-b for a,b in zip(L,q)))) if i!=3 else I(0) for i,q in enumerate(CI)]
# E=-2*y12, X5=-y51, X1+X5=-y12, and X2=X3=X4 by a generic symmetric choice.
X5=-yi[4];X1=-yi[0]-X5;mid=-yi[0]/3;Xi=[X1,mid,mid,mid,X5]
def sites(label):return {int(c)-1 for c in label[2:]}
def cuts(A):return [e for e in range(5) if (e in A)!=((e+1)%5 in A)]
def wall(label):
    if label=='G':return sum(Xi,I(0))
    if label.startswith('G_minus_e'):return sum(Xi,I(0))+2*yi[int(label[-2])-1]
    A=sites(label);return sum((Xi[i] for i in A),I(0))+sum((yi[e] for e in cuts(A)),I(0))
for q in ('G_minus_e12','g_5','g_15','g_234'):
    z=wall(q);assert z.l<=0<=z.h,(q,z.l,z.h)
common=[q for q in src['common_prefactor'] if q!='g_5'];tot=I(0);terms=[];walls={}
for term in src['terms']:
    if not all(q in term for q in ('G_minus_e12','g_15','g_234')):continue
    labels=common+[q for q in term if q not in {'G_minus_e12','g_15','g_234'}]
    value=I(1)
    for q in labels:
        z=wall(q);assert not z.l<=0<=z.h,(q,z.l,z.h);walls[q]=[str(z.l),str(z.h)];value=value/z
    tot=tot+value;terms.append(term)
tot=tot/2
assert len(terms)==3 and not tot.l<=0<=tot.h
packet={'schema':'marici.five_site_g5_complement_soft_source_coefficient.v1',
        'corner':['G_minus_e12','g_5','g_15','g_234','y45=0'],
        'contributing_term_count':len(terms),'contributing_terms':terms,
        'remaining_wall_count':len(walls),'remaining_walls_certified_nonzero':True,
        'coefficient_interval':[str(tot.l),str(tot.h)],'coefficient_certified_nonzero':True,
        'radial_measure_order':2,'incident_denominator_order':4,
        'net_radial_integrand_order':-2,
        'classification':'nonzero source coefficient on doubled-occurrence defining-edge soft corner'}
Path('research/benincasa/results/five-site-g5-complement-soft-source-coefficient.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
