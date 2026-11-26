"""Compare the free involution to the marked C3 on its two triples. Check the actual permutation relation, not a choice of drawn orientation."""
from ramsey_wedge_stabilizer import rows,aut,orbit,V,W,P,json
out=[]
for row in rows:
 if row['stabilizer']!=3:continue
 x,a,b=t=row['wedge'];Q=set(W[t])|{a};seq=tuple(sorted(Q));S,_=aut([{x},{a},{b},V-set(t)]);B,_=aut([Q,V-Q]);rho=next(dict(zip(seq,p)) for p in orbit(seq,S) if p!=seq);single=next(i for i in W[t] if rho[i]==i);triples=[set(s) for s in row['completion_orbits'] if len(s)==3];rec=dict(wedge=t,multiplicity=row['orbit'],singles=[a,single],rotation=rho,reversals=[]);out.append(rec)
 for p in orbit(seq,B):
  f=dict(zip(seq,p));
  if not all(f[i]!=i and f[f[i]]==i for i in seq):continue
  rec['reversals'].append(dict(permutation=f,swaps_singles=f[a]==single,swaps_triples={f[i] for i in triples[0]}==triples[1],inverts_rotation=all(f[rho[f[i]]]==rho[rho[i]] for i in seq),commutes=all(f[rho[i]]==rho[f[i]] for i in seq)))
print(out);(P/'ramsey_wedge_join_reversal.json').write_text(json.dumps(out,indent=1)+'\n')
