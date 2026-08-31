"""Extract and normalize q-lift signatures for all degree-8--10 cutoff-boundary K residuals."""
from __future__ import annotations
import hashlib,json,sys
from collections import Counter,defaultdict
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_canonical_q_lifts as lifts
import check_cosmology_rank26_p_normal_source_template_census as census
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_K_q_boundary_signature_census.json'
def add(d,k,v):
 v=(d.get(k,0)+v)%base.PRIME
 if v:d[k]=v
 else:d.pop(k,None)
def main():
 assert rees.AMBIENT==14 and base.PRIME==32003
 closure=json.loads((RES/'cosmology_rank26_p_normal_K_q_lift_shift_closure.json').read_text()); assert not closure['passed']
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); td=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); special=list(rees.raw_relations(point,columns)); tangent,_=adapter.derivative_rows(columns,point,td); dx,_=adapter.derivative_rows(columns,point,nx); targets=dx[480:4704]; qrows=special[4704:]
 pivots={}
 for row in tangent+special[480:4704]:lifts.insert(row,pivots)
 base_pivots={p:(dict(r),{}) for p,(r,_c) in pivots.items()}
 for qi,row in enumerate(qrows):lifts.insert(row,pivots,{qi:1})
 Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(rees.AMBIENT-4):Kdesc.append((kp,levels,exp))
 Kindex={d:i for i,d in enumerate(Kdesc)}; qdesc=census.descriptors()[4704:]; levels=(1,1,2,1,1); groups=defaultdict(list); records=[]
 for kp in (0,1):
  for exp in [e for e in base.monomials_at_most(10) if 8<=sum(e)<=10]:
   ti=Kindex[(kp,levels,exp)]; prov=lifts.reduce_with_prov(targets[ti],pivots)
   check=dict(targets[ti])
   signature=[]
   for qi,a in prov.items():
    for c,v in qrows[qi].items():add(check,c,a*v)
    d=qdesc[qi]; signature.append((d['mark'],d['k_pole'],tuple(d['levels']),d['exponent'][0]-exp[0],d['exponent'][1]-exp[1],a))
   assert not base.reduce_row(check,{p:dict(r) for p,(r,_c) in base_pivots.items()})
   signature=tuple(sorted(signature)); digest=hashlib.sha256(repr(signature).encode()).hexdigest(); groups[(kp,sum(exp))].append(digest)
   records.append({'k_pole':kp,'exponent':list(exp),'q_rows':len(prov),'signature_sha256':digest,'q_marks':dict(Counter(qdesc[i]['mark'] for i in prov))})
 summaries={}
 for key,digests in sorted(groups.items()):summaries[f'k{key[0]}_degree{key[1]}']={'rows':len(digests),'distinct_normalized_signatures':len(set(digests)),'signature_multiplicities':dict(Counter(digests))}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-signature-census.v1','status':'all_60_boundary_q_lifts_reconstructed_and_normalized','field':base.PRIME,'ambient_relation_degree':14,'summaries':summaries,'records':records,'six_templates_suffice':all(x['distinct_normalized_signatures']==1 for x in summaries.values()),'decision':'Six pole/degree templates suffice.' if all(x['distinct_normalized_signatures']==1 for x in summaries.values()) else 'Boundary q-lifts vary with monomial direction; pole and total degree alone do not determine them.','limitations':['single prime','pivot-order-dependent provenance','normalization by target exponent','does not compare ambient degrees'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
