"""Exact replay contract for durable rank26 source-word certificates."""
from __future__ import annotations
from fractions import Fraction
import copy,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_exact_source_certificate_contract.json'
def canon(x): return json.dumps(x,sort_keys=True,separators=(',',':'))
def digest(x): return hashlib.sha256(canon(x).encode()).hexdigest()
def replay(c):
    required=('schema','canonical_target_id','descriptor','basis','basis_digest','matrix','matrix_digest','target','target_digest','sparse_word','generator')
    if not all(k in c for k in required): return False,'missing_field'
    if c['schema']!='marici.voevodsky.exact-source-certificate.v1': return False,'schema'
    if c['canonical_target_id']!='target:'+digest(c['descriptor']): return False,'target_id'
    if digest(c['basis'])!=c['basis_digest'] or digest(c['matrix'])!=c['matrix_digest'] or digest(c['target'])!=c['target_digest']: return False,'digest'
    if not c['generator'].get('path') or not c['generator'].get('source_digest') or not c['generator'].get('command'): return False,'provenance'
    n=len(c['basis']);word=[Fraction(0) for _ in range(n)];seen=set()
    for term in c['sparse_word']:
        i=term['basis_index'];den=term['denominator'];num=term['numerator']
        if not 0<=i<n or i in seen or den<=0: return False,'sparse_word'
        seen.add(i);word[i]=Fraction(num,den)
    residual=[]
    for row,b in zip(c['matrix'],c['target']): residual.append(sum(Fraction(x)*w for x,w in zip(row,word))-Fraction(b))
    if any(residual): return False,'nonzero_residual'
    return True,'ok'
def main():
    descriptor={'family':'K','ambient_degree':12,'pole':0,'levels':[1,1,1,1,1],'exponent':[0,0]}
    basis=['T:g0','S_K:g1'];matrix=[[1,1],[2,-1]];target=[1,2]
    good={'schema':'marici.voevodsky.exact-source-certificate.v1','descriptor':descriptor,'canonical_target_id':'target:'+digest(descriptor),'basis':basis,'basis_digest':digest(basis),'matrix':matrix,'matrix_digest':digest(matrix),'target':target,'target_digest':digest(target),'sparse_word':[{'basis_index':0,'numerator':1,'denominator':1}], 'generator':{'path':'research/voevodsky/<seed-generator>.py','source_digest':'sha256:required','command':['python','<seed-generator>.py']}}
    assert replay(good)==(True,'ok')
    tampered=copy.deepcopy(good);tampered['sparse_word'][0]['numerator']=2;assert replay(tampered)==(False,'nonzero_residual')
    reordered=copy.deepcopy(good);reordered['basis'].reverse();assert replay(reordered)==(False,'digest')
    flag_only={'full_reconstruction':True};assert replay(flag_only)==(False,'missing_field')
    out={'schema':'marici.voevodsky.cosmology-exact-source-certificate-contract.v1','status':'replay_contract_implemented_and_mutation_tests_passed','certificate_schema':'marici.voevodsky.exact-source-certificate.v1','required_payloads':['canonical descriptor-derived target ID','ordered basis manifest and digest','exact matrix and digest','exact target and digest','normalized sparse rational word','generator path, source digest, and argv command'],'replay_test':'Exact Fraction arithmetic verifies A*w=target with zero residual.','deliberate_failures':{'coefficient_tamper':'nonzero_residual','basis_reorder':'digest','full_reconstruction_only':'missing_field'},'population_status':'contract implemented; existing 1,224 seed records remain unpopulated because their generating source paths and words are not referenced by durable results.','decision':'No seed may claim replayable reconstruction without passing this contract.','next_gate':'locate-seed-generator-provenance','passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
