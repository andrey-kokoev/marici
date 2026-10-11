"""Witness substitution, assumption discharge and compositional route tests."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

from merkle_identity_kernel import Builder, verify as verify_proof
from merkle_witness_transport import construct, verify, digest

BASE=Path(__file__).resolve().parents[1]
MODULE=Path(__file__).with_name('merkle_witness_transport.py')

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError,ZeroDivisionError): return True
    return False

def rehash(packet): packet['root']=digest(packet['certificate']); return packet

def main():
    s=Builder(); x,y=s.var('x'),s.var('y'); h=s.proof('assumption',x,y,label='h')
    square=s.proof('congruence',s.term('mul',x,x),s.term('mul',y,y),premises=[h,h])
    source=s.artifact(['x','y'],{'h':[x,y]},square)
    # Translate h:x=y into the derived equality a+1=b+1, under ab:a=b.
    b=Builder(); a,bb=b.var('a'),b.var('b'); one=b.const(1)
    ab=b.proof('assumption',a,bb,label='ab'); refl1=b.proof('refl',one,one)
    a1,b1=b.term('add',a,one),b.term('add',bb,one)
    discharge=b.proof('congruence',a1,b1,premises=[ab,refl1])
    first=construct(source,b,['a','b'],{'ab':[a,bb]},{'x':a1,'y':b1},{'h':discharge})
    result=verify(first)
    checks={'nonlinear_witness_family_transported':result['verified'],
            'assumption_dependency_transported_not_erased':result['source_assumptions']==['h'] and result['target_assumptions']==['ab'] and not result['target_unconditional'],
            'substitution_changes_term_and_proof_root':source['root']!=first['target']['root']}
    # Next substitute a=2u,b=2v; the hypothesis itself needs a derived proof.
    c=Builder(); u,v=c.var('u'),c.var('v'); two=c.const(2); one2=c.const(1)
    uv=c.proof('assumption',u,v,label='uv'); refl2=c.proof('refl',two,two)
    u2,v2=c.term('mul',two,u),c.term('mul',two,v)
    scaled=c.proof('congruence',u2,v2,premises=[refl2,uv])
    second=construct(first['target'],c,['u','v'],{'uv':[u,v]},{'a':u2,'b':v2},{'ab':scaled})
    shifted=c.proof('congruence',c.term('add',u2,one2),c.term('add',v2,one2),premises=[scaled,c.proof('refl',one2,one2)])
    direct=construct(source,c,['u','v'],{'uv':[u,v]},{'x':c.term('add',u2,one2),'y':c.term('add',v2,one2)},{'h':shifted})
    checks['sequential_and_direct_transports_verify']=verify(second)['verified'] and verify(direct)['verified']
    checks['composition_coherence_exact_target_proof_hash']=second['target']['root']==direct['target']['root']
    checks['composition_retains_final_context_dependency']=verify(second)['target_assumptions']==['uv']
    identity_builder=Builder(); identity_builder.objects=deepcopy(source['objects'])
    identity=construct(source,identity_builder,['x','y'],{'h':[x,y]},{'x':x,'y':y},{'h':h})
    checks['identity_transport_preserves_judgment_root']=identity['target']['root']==source['root'] and verify(identity)['verified']
    # Identification substitution legitimately discharges h by reflexive equality.
    d=Builder(); w=d.var('w'); rw=d.proof('ring',w,w)
    discharged=construct(source,d,['w'],{},{'x':w,'y':w},{'h':rw})
    checks['genuinely_proved_assumption_can_be_discharged']=verify(discharged)['target_unconditional'] and verify(discharged)['target_assumptions']==[]
    checks['missing_assumption_discharge_rejected']=rejected(lambda:construct(source,b,['a','b'],{'ab':[a,bb]},{'x':a1,'y':b1},{}))
    checks['missing_variable_substitution_rejected']=rejected(lambda:construct(source,b,['a','b'],{'ab':[a,bb]},{'x':a1},{'h':discharge}))
    wrong=b.proof('refl',a,a)
    checks['valid_proof_with_wrong_attachment_rejected']=rejected(lambda:construct(source,b,['a','b'],{'ab':[a,bb]},{'x':a1,'y':b1},{'h':wrong}))
    false=b.proof('ring',a1,b1)
    checks['unproved_hypothesis_cannot_be_dropped']=rejected(lambda:construct(source,b,['a','b'],{},{'x':a1,'y':b1},{'h':false}))
    checks['extra_unaccounted_discharge_rejected']=rejected(lambda:construct(source,b,['a','b'],{'ab':[a,bb]},{'x':a1,'y':b1},{'h':discharge,'extra':wrong}))
    rogue=b.var('outside')
    checks['target_context_variable_scope_enforced']=rejected(lambda:construct(source,b,['a','b'],{'ab':[a,bb]},{'x':rogue,'y':b1},{'h':discharge}))
    # A distinct correct target proof is NOT silently identified with the transported one.
    alternative=deepcopy(first); tb=Builder(); tb.objects=deepcopy(first['target']['objects'])
    old=first['target']['objects'][first['target']['root']]['proof']; eq=verify_proof(first['target'])
    back=tb.proof('sym',eq['rhs'],eq['lhs'],premises=[old])
    forward=tb.proof('sym',eq['lhs'],eq['rhs'],premises=[back])
    alternative['target']=tb.artifact(['a','b'],{'ab':[a,bb]},forward)
    alternative['certificate']['target']=alternative['target']['root']; rehash(alternative)
    checks['different_valid_proof_history_detected']=verify_proof(alternative['target'])['verified'] and rejected(lambda:verify(alternative))
    tamper=deepcopy(first); tamper['certificate']['substitution']['x']=b1
    checks['unrehashed_certificate_tampering_rejected']=rejected(lambda:verify(tamper))
    rehash(tamper)
    checks['honestly_rehashed_wrong_substitution_rejected']=rejected(lambda:verify(tamper))
    badsource=deepcopy(first); badsource['certificate']['source']='0'*64; rehash(badsource)
    checks['certificate_source_binding_enforced']=rejected(lambda:verify(badsource))
    missing=deepcopy(first); del missing['target']['objects'][discharge]
    checks['missing_discharge_proof_object_rejected']=rejected(lambda:verify(missing))
    checks['serialized_transport_reverifies']=verify(json.loads(json.dumps(first)))==result
    out=BASE/'results'; out.mkdir(exist_ok=True)
    path=out/'merkle_witness_transport_store.json'; path.write_text(json.dumps(first,indent=2)+'\n',encoding='utf-8')
    (out/'merkle_witness_transport_composition.json').write_text(json.dumps({'first':first,'second':second,'direct':direct},indent=2)+'\n',encoding='utf-8')
    cli=subprocess.run([sys.executable,str(MODULE),str(path)],capture_output=True,text=True)
    checks['fresh_cli_transport_verification']=cli.returncode==0 and json.loads(cli.stdout)['verified']
    receipt={'schema':'marici.merkle-witness-transport-check.v1','passed':all(checks.values()),'checks':checks,
             'first_transport':result,'composed_target_root':second['target']['root'],
             'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'module_sha256':sha256(MODULE.read_bytes()).hexdigest(),
             'scope':'Explicit proof substitution and hypothesis discharge in Q-polynomial contexts; not arbitrary dependent types.'}
    (out/'merkle_witness_transport.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2))
    if not receipt['passed']: raise SystemExit(1)

if __name__=='__main__': main()
