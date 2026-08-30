import json
from fractions import Fraction as F
from pathlib import Path

from five_site_g5_source_residue import I,si,CI,L0,NN,HH,ivecadd,ivecscale,idot,sqrti

src=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
disc=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-source-census.json').read_text())
cancel={tuple(q['pair']) for q in json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-exact-cancellations.json').read_text())['records']}
def sites(q): return {int(c)-1 for c in q[2:]}
def cuts(A): return [e for e in range(5) if (e in A)!=((e+1)%5 in A)]
def invert3(A):
 M=[[F(A[i][j]) for j in range(3)]+[F(int(i==j)) for j in range(3)] for i in range(3)]
 for c in range(3):
  p=next((r for r in range(c,3) if M[r][c]),None)
  assert p is not None
  M[c],M[p]=M[p],M[c]; z=M[c][c]; M[c]=[q/z for q in M[c]]
  for r in range(3):
   if r!=c:
    z=M[r][c]; M[r]=[M[r][j]-z*M[c][j] for j in range(6)]
 return [r[3:] for r in M]
def iw(q,X,y):
 if q=='G':return sum(X,I(0))
 if q.startswith('G_minus_e'):return sum(X,I(0))+I(2)*y[int(q[-2])-1]
 A=sites(q);return sum((X[i] for i in A),I(0))+sum((y[e] for e in cuts(A)),I(0))

cert=[]
for rec in disc['records']:
 if rec['status']!='isolated' or tuple(rec['walls']) in cancel:continue
 sheet=rec['sheet'];a,b=rec['walls'];inds=[i-1 for i in rec['adjusted_sites']]
 ll=ivecadd(L0,ivecscale(sheet*HH,NN))
 y=[sqrti(idot(tuple(x-z for x,z in zip(ll,q)),tuple(x-z for x,z in zip(ll,q)))) for q in CI]
 Aa,Ab=sites(a),sites(b); fixed=[i for i in range(5) if i not in inds]
 mat=[[1,1,1],[int(i in Aa) for i in inds],[int(i in Ab) for i in inds]]; inv=invert3(mat)
 rhs=[I(-5)*si-sum(((-si) for _ in fixed),I(0)),
      -sum((y[e] for e in cuts(Aa)),I(0))-sum(((-si) for i in fixed if i in Aa),I(0)),
      -sum((y[e] for e in cuts(Ab)),I(0))-sum(((-si) for i in fixed if i in Ab),I(0))]
 sol=[sum((I(inv[i][j])*rhs[j] for j in range(3)),I(0)) for i in range(3)]
 X=[-si for _ in range(5)]
 for i,z in zip(inds,sol):X[i]=z
 common=[q for q in src['common_prefactor'] if q!='g_5']; total=I(0); walls={}; n=0
 for term in src['terms']:
  if not {'G_minus_e12',a,b}.issubset(term):continue
  labs=common+[q for q in term if q not in {'G_minus_e12',a,b}]; value=I(1)
  for q in labs:
   z=iw(q,X,y); assert not z.l<=0<=z.h,(sheet,a,b,q,z.l,z.h)
   walls[q]=[str(z.l),str(z.h)];value=value/z
  total=total+value;n+=1
 total=total/2
 assert n==rec['term_count']
 assert not total.l<=0<=total.h,(sheet,a,b,total.l,total.h)
 cert.append({'sheet':sheet,'walls':[a,b],'adjusted_sites':rec['adjusted_sites'],'term_count':n,
  'remaining_wall_count':len(walls),'residue_interval':[str(total.l),str(total.h)],'certified_nonzero':True})
assert len(cert)==44
packet={'schema':'marici.five_site_g5_transverse_pair_exact_coefficients.v1','certificates':cert,
 'active_pair_count_per_sheet':22,'all_active_coefficients_certified_nonzero':True,
 'precision':'exact rational interval arithmetic'}
Path('research/benincasa/results/five-site-g5-transverse-pair-exact-coefficients.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({'certificate_count':len(cert),'active_pair_count_per_sheet':22,
 'all_active_coefficients_certified_nonzero':True},sort_keys=True))
