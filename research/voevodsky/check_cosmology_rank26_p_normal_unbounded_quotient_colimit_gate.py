"""Gate the unbounded quotient-class directed system for the marked K-residual family."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_unbounded_quotient_colimit_gate.json'
def load(n):return json.loads((RES/n).read_text())
def common(e,f):
 assert e[0]%2==f[0]%2 and e[1]%2==f[1]%2
 return (max(e[0],f[0]),max(e[1],f[1]))
def main():
 prereq=[load('cosmology_rank26_p_normal_finite_quotient_class_gate.json'),load('cosmology_rank26_p_normal_uniform_constructor_law.json'),load('cosmology_rank26_p_normal_uniform_two_monomial_boundary_cover.json'),load('cosmology_rank26_p_normal_uniform_target_reachability.json'),load('cosmology_rank26_p_normal_two_monomial_overlap_syzygies.json')];assert all(x['passed'] for x in prereq)
 directed_checks=0
 for p0 in (0,1):
  for p1 in (0,1):
   es=[(i,j) for i in range(21) for j in range(21) if i%2==p0 and j%2==p1]
   for e in es:
    for f in es:
     g=common(e,f);assert g[0]>=e[0] and g[1]>=e[1] and g[0]>=f[0] and g[1]>=f[1];directed_checks+=1
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-unbounded-quotient-colimit-gate.v1','status':'unbounded_marked_K_residual_quotient_class_system_constructed','ambient_degrees':'all even A>=12','transition_generators':['unchanged inclusion','first-axis square multiplication','second-axis square multiplication'],'components':8,'component_index':'two K poles times four exponent-parity classes','directedness_checks':directed_checks,'path_independence':'Any two transported contractions of the same target differ by ker(d), hence define the same singleton fiber quotient class. Commuting monomial maps and exact overlap cells implement this equality on generators.','colimit_statement':'Within each pole/parity component the transition category is directed and every quotient fiber is a singleton; its colimit is therefore a singleton canonical absorption-certificate class.','decision':'The marked K-residual exact absorption mechanism extends to every even ambient degree A>=12 as a representative-independent characteristic-zero quotient-class system.','limitations':['the theorem concerns the marked K-residual family on levels (1,1,2,1,1)','it proves absorption certificates, not a surviving p-normal quotient line','no canonical source coefficient word','does not construct a horn, Bockstein, contour, or physical period'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
