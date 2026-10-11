"""Proof-preserving substitution between scoped Q-polynomial contexts.
Target assumptions are not inferred: every used source assumption needs an
explicit target proof of its substituted equality. Proof structure is retained.
"""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import argparse
import json

from merkle_identity_kernel import Builder, Kernel, verify as verify_proof

def digest(rec):
    return sha256(b'marici.witness-transport.v1\0'+json.dumps(rec,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def translate(source,builder,variables,assumptions,mapping,discharges):
    sk=Kernel(source); judgment=sk.verify()
    if set(mapping)!=sk.variables: raise ValueError('substitution must cover exactly the source variables')
    if set(discharges)!=set(judgment['used_assumptions']): raise ValueError('exactly the used assumptions require discharge proofs')
    zero=builder.const(0); seed=builder.proof('refl',zero,zero)
    tk=Kernel(builder.artifact(variables,assumptions,seed))
    # New immutable content-addressed objects are appended during translation.
    tk.store=builder.objects
    for ref in mapping.values(): tk.term(ref)
    term_cache={}; proof_cache={}
    def term(ref):
        if ref in term_cache: return term_cache[ref]
        r=sk.get(ref)
        if r['op']=='var': result=mapping[r['name']]
        elif r['op']=='const': result=builder.const(r['value'])
        else: result=builder.term(r['op'],*(term(a) for a in r['args']))
        term_cache[ref]=result; return result
    def proof(ref):
        if ref in proof_cache: return proof_cache[ref]
        r=sk.get(ref); lhs,rhs=term(r['lhs']),term(r['rhs'])
        if r['rule']=='assumption':
            result=discharges[r['label']]
            a,b,_=tk.proof(result)
            if (a,b)!=(lhs,rhs): raise ValueError('discharge proof has wrong substituted endpoints')
        else:
            extra={'premises':[proof(p) for p in r['premises']]} if 'premises' in r else {}
            result=builder.proof(r['rule'],lhs,rhs,**extra)
        proof_cache[ref]=result; return result
    target=builder.artifact(variables,assumptions,proof(sk.proof_root))
    verify_proof(target)
    return target

def construct(source,builder,variables,assumptions,mapping,discharges):
    target=translate(source,builder,variables,assumptions,mapping,discharges)
    rec={'kind':'scoped-polynomial-proof-transport','source':source['root'],'target':target['root'],
         'substitution':mapping,'discharges':discharges,'rule':'structural-substitution-with-explicit-assumption-proofs'}
    return {'schema':'marici.witness-transport-store.v1','source':deepcopy(source),'target':target,
            'certificate':rec,'root':digest(rec)}

def verify(packet):
    if set(packet)!={'schema','source','target','certificate','root'} or packet['schema']!='marici.witness-transport-store.v1': raise ValueError('transport schema')
    rec=packet['certificate']
    if set(rec)!={'kind','source','target','substitution','discharges','rule'} or digest(rec)!=packet['root'] or rec['kind']!='scoped-polynomial-proof-transport' or rec['rule']!='structural-substitution-with-explicit-assumption-proofs': raise ValueError('certificate schema/hash')
    if rec['source']!=packet['source']['root'] or rec['target']!=packet['target']['root']: raise ValueError('transport endpoint binding')
    source=verify_proof(packet['source']); target=verify_proof(packet['target'])
    tk=Kernel(packet['target']); root=tk.get(tk.root); context=tk.get(root['context'])
    b=Builder(); b.objects=deepcopy(packet['target']['objects'])
    expected=translate(packet['source'],b,context['variables'],context['assumptions'],rec['substitution'],rec['discharges'])
    if expected['root']!=packet['target']['root']: raise ValueError('target is not the transported proof')
    return {'verified':True,'transport_root':packet['root'],'source_root':rec['source'],'target_root':rec['target'],
            'source_assumptions':source['used_assumptions'],'target_assumptions':target['used_assumptions'],
            'target_unconditional':target['unconditional'],
            'scope':'Structural proof substitution in scoped Q-polynomial equality; not arbitrary dependent-type transport or proof irrelevance.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('packet',type=Path); args=parser.parse_args()
    try:
        if args.packet.stat().st_size>10_000_000: raise ValueError('file size limit')
        print(json.dumps(verify(json.loads(args.packet.read_text(encoding='utf-8'))),indent=2))
    except (ValueError,KeyError,TypeError,ZeroDivisionError,RecursionError) as error:
        print(json.dumps({'verified':False,'error':str(error)})); raise SystemExit(1)
