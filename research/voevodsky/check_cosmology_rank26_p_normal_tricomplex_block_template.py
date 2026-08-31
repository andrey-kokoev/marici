"""Test stable tri-complex block support across nonminimum source expansions."""
from __future__ import annotations
import json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import check_cosmology_rank26_p_normal_source_template_census as census
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_tricomplex_block_template.json'
def main():
 prior=json.loads((RES/'cosmology_rank26_p_normal_source_template_census.json').read_text()); assert prior['passed']
 desc=census.descriptors(); samples=('lower_quartile','median','upper_quartile','maximum'); blocks={}; detailed={}
 for sample in samples:
  counts=Counter()
  for kind,index,_a in census.coefficients(sample):
   d=desc[index]; block=(kind,d['family'],d['k_pole'],d.get('mark','-')); counts[block]+=1
  blocks[sample]=set(counts); detailed[sample]={f'{a}:{b}:k{c}:{d}':v for (a,b,c,d),v in sorted(counts.items())}
 common=set.intersection(*(blocks[s] for s in samples)); union=set.union(*(blocks[s] for s in samples))
 common_six={( 'S','IBP',k,'-') for k in (0,1)}|{('S','K',k,'-') for k in (0,1)}
 common_q={('S','q',k,mark) for k in (0,1) for mark in ('g1','g2','g3','g23','g31')}
 assert common_six|common_q <= common
 # T support is sparse and sample-dependent; inspect its common intersection separately.
 common_T={b for b in common if b[0]=='T'}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-tricomplex-block-template.v1','status':'stable_special_tricomplex_core_with_sample_dependent_tangent_correction','samples':list(samples),'block_counts':{s:len(blocks[s]) for s in samples},'common_blocks_count':len(common),'union_blocks_count':len(union),'common_special_core':{'IBP_poles':[0,1],'K_poles':[0,1],'q_poles':[0,1],'q_marks':['g1','g2','g3','g23','g31'],'block_count':len(common_six|common_q)},'common_tangent_blocks':[f'{a}:{b}:k{c}:{d}' for a,b,c,d in sorted(common_T)],'sample_block_counts':detailed,'decision':'A reusable block template exists at support level: every nonminimum expansion uses the same 14-block special core coupling IBP and K at poles 0,1 with every marked-q wall at poles 0,1. Tangent corrections are not captured by one common block and remain sample-dependent.','limitations':['support-level template only','does not constrain coefficients or monomial shifts','four nonminimum samples','single prime'],'next_leaf':'factor sample-dependent tangent correction against target pole/mark data','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
