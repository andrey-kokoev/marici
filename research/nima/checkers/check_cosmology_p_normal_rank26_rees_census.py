"""Finite-cutoff Rees census of the full labelled relation module along p=0."""
from __future__ import annotations
import argparse, importlib, json, os, struct, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def write_row(s,kind,row,prime):
 items=sorted((c,v%prime) for c,v in row.items() if v%prime); s.write(struct.pack('<BI',kind,len(items)))
 for c,v in items:s.write(struct.pack('<II',c,v))
def run(prime:int,ambient:int,normal:str,gamma_mode:str):
 os.environ['MARICI_FIELD_PRIME']=str(prime);os.environ['MARICI_AMBIENT']=str(ambient);os.environ['MARICI_POINT']='2,3,-5'
 sys.path.insert(0,str(ROOT/'research'/'benincasa'))
 rees=importlib.import_module('check_rank26_total_energy_triple_relation_module'); charts=rees.charts
 if gamma_mode=='half': charts.GAMMA=-(pow(2,-1,prime))%prime
 point=(3,6,-3); offsets=rees.OFFSETS; width_packet=rees.column_packet(); low,cols=width_packet;width=len(cols)
 direction=(1,0,0) if normal=='x' else (0,1,0)
 shifted=lambda o: tuple(point[i]+o*direction[i] for i in range(3))
 samples=[rees.raw_relations(shifted(o),cols) for o in offsets]
 check=rees.raw_relations(shifted(rees.CHECK_OFFSET),cols)
 w1=rees.interpolation_weights(1);w2=rees.interpolation_weights(2);wc=rees.evaluation_weights(rees.CHECK_OFFSET)
 engine=ROOT/'.narada'/'runtime'/'nima'/'sparse_modular_rank_stream.exe';assert engine.exists()
 proc=subprocess.Popen([str(engine)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE);s=proc.stdin;s.write(struct.pack('<I',prime));count=checks=0
 for rows in zip(*samples,check,strict=True):
  count+=1; sampled=rows[:-1]; expected=rees.combine(sampled,wc);assert rees.combine((expected,rows[-1]),(1,-1))=={};checks+=1
  r0=dict(sampled[offsets.index(0)]);r1=rees.combine(sampled,w1);r2=rees.combine(sampled,w2)
  write_row(s,0,r0,prime);write_row(s,1,rees.shifted_row(r0,width,1),prime);write_row(s,1,rees.assemble((r0,r1),width),prime)
  write_row(s,2,rees.shifted_row(r0,width,2),prime);write_row(s,2,rees.assemble(({},r0,r1),width),prime);write_row(s,2,rees.assemble((r0,r1,r2),width),prime)
 s.close();out,err=proc.communicate() if False else (proc.stdout.read(),proc.stderr.read());rc=proc.wait();assert rc==0,err.decode();rank=json.loads(out)
 olda,oldc=charts.AMBIENT,charts.CUTOFF;charts.AMBIENT,charts.CUTOFF=ambient,rees.CUTOFF
 try: generic=charts.presentation(rees.base.fiber_data,shifted(1),rees.NAMES)
 finally: charts.AMBIENT,charts.CUTOFF=olda,oldc
 rs,rd,rt=rank['relation_ranks']; ds=width-rs;dg=width-len(generic['pivots']);dd=2*width-rd;dt=3*width-rt
 excess=ds-dg;l1=2*ds-dd;l2=2*dd-ds-dt;l3=excess-l1-l2
 payload={'schema':'marici.cosmology-p-normal-rank26-rees-census.v1','prime':prime,'ambient':ambient,'point':list(point),'p':0,'total_energy':sum(point),'normal':f'{normal} shift with dp=1','twist_gamma_mod_prime':charts.GAMMA,'gamma_mode':gamma_mode,'column_count':width,'raw_relation_count':count,'interpolation_checks':checks,'relation_ranks':{'generic':len(generic['pivots']),'special':rs,'dual':rd,'triple':rt},'cokernel_dimensions':{'generic':dg,'special':ds,'dual':dd,'triple':dt},'support_excess':excess,'elementary_length_census':{'length_1':l1,'length_2':l2,'length_at_least_3':l3},'nonnegative_census':min(excess,l1,l2,l3)>=0,'scope':'finite-cutoff full labelled presentation; no tau comparison or physical period','passed':min(excess,l1,l2,l3)>=0}
 tag='' if gamma_mode=='generic' else '_half';path=ROOT/'research'/'nima'/'results'/f'cosmology_p_normal_rank26_rees_census{tag}_{normal}_p{prime}.json';path.write_text(json.dumps(payload,indent=2)+'\n');print(json.dumps(payload,indent=2))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True);ap.add_argument('--ambient',type=int,default=8);ap.add_argument('--normal',choices=('x','y'),default='x');ap.add_argument('--gamma',choices=('generic','half'),default='generic');a=ap.parse_args();run(a.prime,a.ambient,a.normal,a.gamma)
if __name__=='__main__':main()
