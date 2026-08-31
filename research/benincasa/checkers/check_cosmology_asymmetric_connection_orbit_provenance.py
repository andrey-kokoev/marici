#!/usr/bin/env python3
"""Retain exact finite-field connection-word provenance for the exceptional difference."""
import argparse,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009,32027));a=ap.parse_args();P=a.prime;os.environ['MARICI_FIELD_PRIME']=str(P);sys.path.insert(0,str(ROOT/'research'/'benincasa'));import physical_four_mark_residue_twisted_derham as m
 names=('g1','g2','g3','g23','g31');gamma=-pow(2,-1,P)%P;low,cols,qpiv,free=m.presentation(names,gamma,10,5,minimum_q_level=0);labels={c:l for l,c in cols.items()}
 def qc(l):return m.quotient_coordinates(l,cols,qpiv,free)
 A=qc((0,1,1,1,0,1,(0,0)));B=qc((0,1,1,1,1,0,(0,0)));source=dict(A);difference=dict(A)
 for c,v in B.items():m.add_value(source,c,v);m.add_value(difference,c,-v)
 def add(dst,src,k):
  for c,v in src.items():m.add_value(dst,c,k*v)
 def conn(v,axis):
  out={}
  for c,k in v.items():
   for d,w in m.connection_image(labels[c],names,gamma,axis,cols).items():m.add_value(out,d,k*w)
  out=m.reduce_row(out,qpiv);return {c:out[c] for c in free if c in out}
 def reduce_pair(row,prov,piv):
  row,prov=dict(row),dict(prov)
  while row and max(row) in piv:
   p=max(row);q,pr=piv[p];k=row[p];add(row,q,-k);add(prov,pr,-k)
  return row,prov
 piv={};raw=[];words=[];queue=[(source,())];seen=set()
 while queue:
  v,w=queue.pop(0);key=(w,tuple(sorted(v.items())))
  if key in seen:continue
  seen.add(key);idx=len(raw);raw.append(v);words.append(w);r,pr=reduce_pair(v,{idx:1},piv)
  if not r:continue
  p=max(r);iv=pow(r[p],-1,P);r={c:x*iv%P for c,x in r.items()};pr={c:x*iv%P for c,x in pr.items()};piv[p]=(r,pr)
  for axis in (0,1):queue.append((conn(v,axis),w+(axis,)))
 residual,prov=reduce_pair(difference,{},piv);assert not residual
 replay={}
 for i,k in prov.items():add(replay,raw[i],k)
 check=dict(difference);add(check,replay,1);assert not check
 used=[{'raw_index':i,'word_axes':list(words[i]),'word':'source'+''.join(f'->D{axis}' for axis in words[i]),'coefficient_in_negative_replay':k,'support':len(raw[i])} for i,k in sorted(prov.items())]
 out={'schema':'marici.benincasa.cosmology-asymmetric-connection-orbit-provenance.v1','prime':P,'gamma_mod_prime':gamma,'orbit_rank':len(piv),'raw_words_generated':len(raw),'difference_replay_term_count':len(used),'max_connection_word_depth':max((len(x['word_axes']) for x in used),default=0),'replay_terms':used,'identity':'difference + sum(coefficient_i * connection_word_i(source_sum)) = 0','exact_replay_zero':True,'integral_reconstruction_attempted':False,'unit_principal_selector_constructed':False,'scope':'finite-field connection-word identity at ambient 10 cutoff 5; coefficients are modular and do not authorize division by two','passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_asymmetric_connection_orbit_provenance_p{P}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
