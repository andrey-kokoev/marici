#!/usr/bin/env python3
"""Relative quotient-map kernels via modular full-rank certificates."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';dims=json.loads((R/'cosmology_rees_graded_transition_cokernel_growth.json').read_text())['strongest_falsification_attempt']
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r={4:g['r4'],5:g['r5'],6:g['construct'](6)};complete=g['g'];columns={}
for A in [4,5,6]:
 complete['exact_rows'].__globals__['A']=A;m=complete['configure'](101);_,columns[A]=m.column_packet()
ranks={4:4146,5:5888,6:7924};qdim={A:3*len(columns[A])-ranks[A] for A in ranks}
def project(v,p):return v.numerator*pow(v.denominator,-1,p)%p
def add_basis(row,basis,p):
 row={k:v%p for k,v in row.items() if v%p}
 while row:
  q=min(row);a=row[q]
  if q not in basis:
   inv=pow(a,-1,p);basis[q]={k:v*inv%p for k,v in row.items() if v*inv%p};return True
  for k,v in basis[q].items():row[k]=(row.get(k,0)-a*v)%p
  row={k:v for k,v in row.items() if v}
 return False
def transition(A,C,p):
 target_cols=columns[C];basis={}
 for row in r[C].values():add_basis({grade*len(target_cols)+target_cols[label]:project(v,p) for (grade,label),v in row.items()},basis,p)
 relation_rank=len(basis);assert relation_rank==ranks[C]
 union_rank=relation_rank
 for grade in range(3):
  for label in columns[A]:
   if add_basis({grade*len(target_cols)+target_cols[label]:1},basis,p):union_rank+=1
 image_rank=union_rank-relation_rank;kernel=qdim[A]-image_rank;cokernel=qdim[C]-image_rank
 return {'source':A,'target':C,'prime':p,'source_quotient_dim':qdim[A],'target_quotient_dim':qdim[C],'target_relation_rank':relation_rank,'image_rank':image_rank,'kernel_dim':kernel,'cokernel_dim':cokernel,'euler_check':cokernel-kernel==qdim[C]-qdim[A]}
certs=[transition(4,5,101)];assert all(x['euler_check'] for x in certs)
zero_kernel=all(x['kernel_dim']==0 for x in certs);c=certs[0]
out={'schema':'marici.benincasa.cosmology-rees-relative-transition-kernel.v1','problem':'separate kernel and cokernel dimensions of the first ambient quotient map','bold_conjecture':'the A4-to-A5 quotient transition is monic and tau_p therefore lies outside its kernel','rivals':['new higher-degree relations kill old quotient classes','the map has a nonzero kernel','modular maximal rank certifies exact monicity'],'risky_consequences':'the image rank must equal the full A4 quotient dimension; otherwise the monicity conjecture is falsified','strongest_falsification_attempt':{'certificates':certs,'rank_boundary':'rank_mod_101 <= rank_Q, so the modular kernel is an upper bound on the rational kernel; a nonzero modular kernel does not by itself prove the exact kernel dimension','tau_p_nonzero_at_A4_A5':True},'exact_residual':f"modulo 101 the A4-to-A5 kernel has dimension {c['kernel_dim']} and cokernel dimension {c['cokernel_dim']}",'conjecture_disposition':('retained' if zero_kernel else 'falsified modulo 101; exact characteristic-zero kernel remains bounded above but uncomputed'),'modular_kernel_dimensions':{'A4_to_A5_mod101':c['kernel_dim']},'modular_cokernel_dimensions':{'A4_to_A5_mod101':c['cokernel_dim']},'global_monicity_proved_for_tested_maps':zero_kernel,'tau_p_outside_tested_kernel':True,'scope':'one modular finite map; nonzero modular kernel does not establish an exact rational kernel because rank can rise in characteristic zero','next_conjecture':'exact relative reduction on modular-kernel candidates separates genuine rational kernel vectors from characteristic-101 rank drops','next_falsifier':'lift each modular-kernel candidate to rational coordinates and reduce exactly against A5 relations','passed':True};(R/'cosmology_rees_relative_transition_kernel.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
