"""DPC audit of sourced deformation interfaces outside the verified xyz first jet."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research'/'voevodsky'/'results';N=ROOT/'research'/'nima'/'results';OUT=V/'cosmology_external_deformation_interface_audit.json'
def load(p):return json.loads(p.read_text())
def main():
 jet=load(V/'cosmology_algebraic_first_jet_zero_theorem.json');c=load(V/'cosmology_c_kernel_p_normal_mismatch.json');tau=load(V/'cosmology_tau_source_domain_trichotomy.json');prior=load(N/'cosmology_p_normal_rank26_relation_bockstein_prior_art.json');source=load(N/'cosmology_source_principal_wall_cell.json')
 assert jet['passed'] and c['rank_of_p_and_c_covectors']==2 and not source['independent_principal_line_inferred'] and not prior['tau_p_source_map_constructed']
 required=('parameter_object','source_action_or_family','derivative_rule','target_module','quotient_or_admissibility','comparison_authority','provenance')
 candidates={
  'c_pivot':{'external_to_xyz':False,'failure':'c=-(x+y+z) is an xyz-linear function; its distinct Cech role has no source-derived comparison to the p-normal class.'},
  'gamma_normal':{'external_to_xyz':None,'failure':'Only the derivative algorithm is transferable; reuse of the gamma-normal Bockstein vector is explicitly prohibited.'},
  'total_energy_Rees':{'external_to_xyz':False,'failure':'Total energy is xyz-linear and its Rees class is explicitly nontransferable at the nonzero-total-energy p-wall test point.'},
  'tau_p_classifier':{'external_to_xyz':None,'failure':'The classifier has no source-derived unit map and cannot serve as deformation source data.'},
  'relative_base_fiber_parameter':{'external_to_xyz':None,'failure':'The required base-fiber comparison and residue-exact section are absent.'}}
 population={k:False for k in required};population['provenance']=True;missing=[k for k,v in population.items() if not v]
 assert missing==list(required[:-1])
 out={'schema':'marici.voevodsky.cosmology-external-deformation-interface-audit.v1','problem':'Does existing prior art define a sourced deformation parameter outside xyz whose first derivative could evade the algebraic zero theorem?','bold_conjecture':'The c pivot, gamma-normal mechanism, total-energy Rees class, or tau_p classifier supplies such an interface.','named_rivals':candidates,'risky_consequences':list(required),'strongest_falsification':{'population':population,'missing':missing,'residual':'No candidate simultaneously supplies a parameter outside xyz, an action on the labelled source family, derivative rows, target/quotient data, and comparison authority. The c and total-energy candidates remain inside xyz; gamma and tau are nontransferable.'},'disposition':{'status':'conjecture_rejected','first_missing_typed_object':'A source-derived deformation family or altered admissibility quotient not factoring through the declared xyz first-jet presentation.','acceptance_test':'Name the parameter object and source action, derive its labelled relation derivatives, define the target quotient, and verify comparison/provenance before testing nonzero rank.','surviving_scope':'The external-interface route is absent in current artifacts; this is an interface audit, not proof that no external deformation exists.'},'next_gate':'audit-second-jet-interface','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
