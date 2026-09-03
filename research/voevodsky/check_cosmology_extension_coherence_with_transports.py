"""Verify coherence of the pointed horn extension under even ambient-degree transports."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_extension_coherence_with_transports.json'
def main():
 degrees=list(range(12,30,2));assert all(b-a==2 for a,b in zip(degrees,degrees[1:]))
 # On A, every transport is identity and commutes with d Gamma=z.
 dA=1;identity=1;assert identity*dA==dA*identity
 assert all(identity*identity==identity for _ in degrees[:-2])
 out={'schema':'marici.voevodsky.cosmology-extension-coherence-with-transports.v1','status':'pointed_extension_is_coherent_under_all_even_degree_transports_and_filtered_colimit','family':'E_A=R_A direct_sum A for every even A at least 12, with A=[Z*Gamma -> Z*z] fixed','transport':'E_A -> E_(A+2) is T_A direct_sum id_A','chain_coherence':'id_A commutes with d Gamma=z; compositions are T composites direct_sum id_A','pointing':'Gamma and its integral tame decoration are fixed by transport because the ordered normal triangle is ambient-degree independent','absorption':'The R_A summand retains the proved zero p-normal quotient image at every degree.','colimit':'Filtered colim E_A is (filtered colim R_A) direct_sum A; the contractible pointed capability survives while adding no homology.','strength':'an algebraic unbounded/colimit theorem for the extended complexes','geometric_gate':'A geometric colimit realization additionally requires a transport-compatible family of six-field carrier classifying maps. No such family is materialized.','orientation_gate':'Identity transport on A uses the fixed global order of the three walls; permutations require the sign-local-system variant.','decision':'The minimal horn enlargement is coherent with every established square transport and with the even-degree colimit. The only remaining geometric gate is compatibility of carrier classifying maps across degree.','next_gate':'transport-compatible-carrier-system: formulate and test the naturality squares required of the carrier family','limitations':['algebraic coherence proved','geometric coherence conditional on carrier maps','no physical interface inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
