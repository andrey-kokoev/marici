#!/usr/bin/env python3
"""Extract canonical marked-q interior seeds at a selected prime and cutoff."""
import argparse,hashlib,json,os,sys
from itertools import product
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009,32027,32029,32051,32057));ap.add_argument('--ambient',type=int,required=True,choices=(12,14,16));args=ap.parse_args();os.environ['MARICI_FIELD_PRIME']=str(args.prime);os.environ['MARICI_AMBIENT']=str(args.ambient)
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_canonical_q_lifts as lifts
# Physical square-root twist; the imported chart default 5 is generic and nonphysical.
charts.GAMMA=-pow(2,-1,base.PRIME)%base.PRIME
VRES=ROOT/'research'/'voevodsky'/'results';OUT=ROOT/'research'/'benincasa'/'results'/f'cosmology_canonical_q_seed_signature_a{args.ambient}_p{args.prime}.json';A=rees.AMBIENT
def count(n):return len(base.monomials_at_most(n))
def qdesc():
 out=[]
 for qi,name in enumerate(rees.NAMES):
  for kp in range(charts.K_DEPTH+1):
   for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    if levels[qi]==charts.Q_DEPTH:continue
    for exp in base.monomials_at_most(A-1):out.append((name,kp,levels,exp))
 return out
def main():
 assert A==args.ambient and base.PRIME==args.prime
 protocol=json.loads((VRES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));tangent,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*count(A);nK=64*count(A-4);targets=dx[nI:nI+nK];qrows=special[nI+nK:];descriptors=qdesc();assert len(qrows)==len(descriptors)
 pivots={}
 for row in tangent+special[nI:nI+nK]:lifts.insert(row,pivots)
 for qi,row in enumerate(qrows):lifts.insert(row,pivots,{qi:1})
 Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(A-4):Kdesc.append((kp,levels,exp))
 signatures={};levels=(1,1,2,1,1)
 for kp in (0,1):
  ti=Kdesc.index((kp,levels,(0,0)));prov=lifts.reduce_with_prov(targets[ti],pivots);terms=[]
  for qi,a in prov.items():
   mark,qkp,qlevels,exp=descriptors[qi];terms.append((mark,qkp,qlevels,exp,a))
  terms=sorted(terms);digest=hashlib.sha256(repr(terms).encode()).hexdigest();signatures[f'k{kp}']={'q_rows':len(terms),'descriptor_coefficient_sha256':digest,'terms':[{'mark':m,'q_pole':qk,'levels':list(l),'exponent':list(e),'coefficient':a} for m,qk,l,e,a in terms]}
 out={'schema':'marici.benincasa.cosmology-canonical-q-seed-signature.v1','field':base.PRIME,'gamma_mod_prime':charts.GAMMA,'physical_gamma':'-1/2','ambient':A,'signatures':signatures,'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'field':base.PRIME,'ambient':A,'signatures':{k:{x:y for x,y in v.items() if x!='terms'} for k,v in signatures.items()},'passed':True},indent=2))
if __name__=='__main__':main()
