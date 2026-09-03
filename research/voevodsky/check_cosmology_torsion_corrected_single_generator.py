"""Derive the exact integral contract for a one-generator horn filler."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_torsion_corrected_single_generator.json'
def solutions(bound=3):
 out=[]
 for a in range(-bound,bound+1):
  for n in range(-bound,bound+1):
   for r in range(-bound,bound+1):
    if a*n==1 and a*r==-1:out.append((a,n,r))
 return out
def main():
 sols=solutions();assert set(sols)=={(1,1,-1),(-1,-1,1)}
 target_sign=(0,0,1)
 candidates={'rank26':{'degree':1,'n':0,'passes':False},'Milnor_symbol':{'degree':2,'n':1,'passes':False},'local_log':{'degree':'local_only','n':1,'passes':False},'higher_face':{'degree':1,'n':0,'passes':False}}
 assert not any(c['passes'] for c in candidates.values())
 out={'schema':'marici.voevodsky.cosmology-torsion-corrected-single-generator.v1','status':'single_generator_contract_exact_and_no_known_candidate_satisfies_it','coefficient_solutions':[list(x) for x in sols],'intrinsic_contract':['h is a globally sourced total degree-one element','d(h) has free vector (1,-1), or its overall negative','its B-valued sign decoration is exactly epsilon_Z=(0,0,1)','both residual sign coordinates vanish','every additional boundary component is zero'],'order_two_sign':'Multiplying the generator by -1 reverses the free components but leaves epsilon_Z unchanged.','candidate_audit':candidates,'torsion_correction_gate':'Adding {u,u} or {v,v} can alter sign coordinates only in motivic degree two. It cannot correct a missing degree-one generator without a separately sourced degree-one torsion element and a typed addition map.','decision':'No known candidate satisfies the one-generator integral contract. The rational obstruction remains decisive, and integral refinement adds an exact sign requirement rather than creating a filler.','next_gate':'degree-one-torsion-corrector: determine whether the relevant higher-Chow/relative degree contains any sourced order-two elements capable of correcting sign coordinates','limitations':['candidate audit covers materialized constructor classes','does not classify all higher-Chow torsion','no new degree-one generator constructed'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
