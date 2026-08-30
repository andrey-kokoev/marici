import json
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
def sites(q): return {int(c)-1 for c in q[2:]}
def cuts(A): return [e for e in range(5) if (e in A)!=((e+1)%5 in A)]
def vec(q):
 z=[0]*10
 if q=='G_minus_e12': z[:5]=[1]*5; z[5]=2
 else:
  A=sites(q)
  for i in A:z[i]=1
  for e in cuts(A):z[5+e]=1
 return z
add=lambda *vs:[sum(q) for q in zip(*vs)]

tests=[
 {'pair':['g_15','g_34'],'remainders':['g_1345','g_234'],'carrier_identity':['G_minus_e12','g_34']},
 {'pair':['g_23','g_45'],'remainders':['g_145','g_2345'],'carrier_identity':['G_minus_e12','g_45']},
]
for q in tests:
 a,b=q['pair']; terms=[t for t in src['terms'] if {'G_minus_e12',a,b}.issubset(t)]
 assert len(terms)==2
 rem=[next(x for x in t if x not in {'G_minus_e12',a,b}) for t in terms]
 assert sorted(rem)==sorted(q['remainders'])
 assert add(*(vec(x) for x in q['remainders']))==add(*(vec(x) for x in q['carrier_identity']))
 q['source_term_count']=2
 q['exact_cancellation']=True
 q['reason']='the two remaining denominators are negatives on the frozen carrier intersection'
packet={'schema':'marici.five_site_g5_transverse_pair_exact_cancellations.v1','records':tests,
 'exact_zero_pair_count':2,
 'conclusion':'two transverse source-supported pair coefficients vanish by carrier-linear identities'}
Path('research/benincasa/results/five-site-g5-transverse-pair-exact-cancellations.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
