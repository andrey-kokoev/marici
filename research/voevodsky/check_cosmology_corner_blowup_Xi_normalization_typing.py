"""Audit the attempted identification of Xi_log with dlog(p) on the corner blow-up."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_corner_blowup_Xi_normalization_typing.json'
def load(name): return json.loads((RES/name).read_text())
def main():
    local=load('cosmology_corner_blowup_log_gysin_unit.json')
    horn=load('cosmology_tau_lift_formal_problem.json')
    denom=load('cosmology_log_denominator_primitive_gate.json')
    assert local['passed'] and horn['passed'] and denom['passed']
    xi_degree=2; dlog_p_degree=1
    direct_identification_typed=(xi_degree==dlog_p_degree)
    assert not direct_identification_typed
    out={
      'schema':'marici.voevodsky.cosmology-corner-blowup-Xi-normalization-typing.v1',
      'status':'unit_valuation_is_necessary_but_direct_Xi_equals_dlog_p_identification_is_type_invalid',
      'source_facts':{
        'blowup_center':'(u,v,p)=(0,0,0)',
        'ord_E_p':local['exceptional_valuations']['p'],
        'Res_E_dlog_p':1,
        'dlog_p_cochain_degree':dlog_p_degree,
        'Xi_log_target_degree':xi_degree,
        'Xi_log_role':'degree-two logarithmic circuit/residue class in the formal horn'
      },
      'direct_identification_Xi_log_with_dlog_p':False,
      'reason':'The classes occupy different cochain degrees. Exceptional valuation fixes the scalar of a possible residue/Gysin comparison but does not supply its degree-shifting chain map.',
      'required_map':'an explicitly sourced connecting/Gysin morphism from the resolved blow-up cone cell to the degree-two Xi_log class, compatible with the exceptional Cech face and total differential',
      'correction':'Withdraw the claim that ord_E(p)=1 alone constructs the missing Xi_log leg. Retain it only as the forced unit-normalization test for any future comparison morphism.',
      'next_gate':'construct the degree-shifting resolved/Rees or logarithmic Cech-de Rham connecting map and verify its image column is (1,1)',
      'relative_bockstein_constructed':False,
      'physical_period_constructed':False,
      'passed':True
    }
    OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
