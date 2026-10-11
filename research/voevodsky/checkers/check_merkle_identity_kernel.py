"""Regression and hostile tests for typed Merkle polynomial equality proofs."""
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

from merkle_identity_kernel import Builder, verify, digest
from check_merkle_identity_surface import cube, encode, verify as verify_surface, inverse

BASE=Path(__file__).resolve().parents[1]
KERNEL=Path(__file__).with_name('merkle_identity_kernel.py')

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError,ZeroDivisionError): return True
    return False

def face_expression(surface,face):
    """Compile the committed signed affine boundary into the polynomial language."""
    b=Builder(); x=b.var('x'); term=x
    for step in face['boundary']:
        edge=surface['objects'][step['edge']]; affine=tuple(map(Q,edge['map']))
        if step['direction']==-1: affine=inverse(affine)
        term=b.term('add',b.term('mul',b.const(affine[0]),term),b.const(affine[1]))
    proof=b.proof('ring',term,x)
    return b.artifact(['x'],{},proof)

def verify_bridge(packet):
    surface=packet['surface']; report=verify_surface(surface)
    if not report['coherent_closed_surface']: raise ValueError('invalid surface')
    faces=surface['objects'][surface['root']]['faces']
    if len(packet['faces'])!=len(faces): raise ValueError('missing face proofs')
    for ref,row in zip(faces,packet['faces']):
        if row['face']!=ref: raise ValueError('face attachment mismatch')
        expected=verify(face_expression(surface,surface['objects'][ref]))
        actual=verify(row['proof'])
        if not actual['unconditional'] or (actual['lhs'],actual['rhs'])!=(expected['lhs'],expected['rhs']):
            raise ValueError('proof not attached to this boundary')
    return True

def main():
    b=Builder(); x,y,z=(b.var(n) for n in ('x','y','z')); one=b.const(1)
    # Nonlinear multivariable identity, universally quantified over Q.
    lhs=b.term('mul',b.term('add',x,y),b.term('add',x,b.term('neg',y)))
    rhs=b.term('add',b.term('mul',x,x),b.term('neg',b.term('mul',y,y)))
    ring=b.proof('ring',lhs,rhs); artifact=b.artifact(['x','y'],{},ring)
    checks={'nonlinear_difference_of_squares':verify(artifact)['unconditional']}
    distributive=b.proof('ring',b.term('mul',x,b.term('add',y,z)),b.term('add',b.term('mul',x,y),b.term('mul',x,z)))
    checks['three_variable_distributivity']=verify(b.artifact(['x','y','z'],{},distributive))['unconditional']
    sym=b.proof('sym',rhs,lhs,premises=[ring])
    trans=b.proof('trans',lhs,lhs,premises=[ring,sym])
    checks['explicit_symmetry_and_transitivity']=verify(b.artifact(['x','y'],{},trans))['unconditional']
    refl=b.proof('refl',x,x)
    checks['reflexivity']=verify(b.artifact(['x'],{},refl))['unconditional']
    hyp=b.proof('assumption',x,y,label='h')
    xx,yy=b.term('mul',x,x),b.term('mul',y,y)
    congruence=b.proof('congruence',xx,yy,premises=[hyp,hyp])
    conditional=b.artifact(['x','y'],{'h':[x,y]},congruence)
    result=verify(conditional)
    checks['congruence_retains_exact_assumption']=result['used_assumptions']==['h'] and not result['unconditional']
    checks['unused_hypothesis_not_promoted_to_dependency']=verify(b.artifact(['x','y'],{'h':[x,y]},refl))['used_assumptions']==[]
    checks['unscoped_assumption_rejected']=rejected(lambda:verify(b.artifact(['x','y'],{},congruence)))
    checks['false_unconditional_equality_rejected']=rejected(lambda:verify(b.artifact(['x','y'],{},b.proof('ring',x,y))))
    checks['wrong_transitivity_middle_rejected']=rejected(lambda:verify(b.artifact(['x','y'],{},b.proof('trans',lhs,rhs,premises=[ring,ring]))))
    checks['wrong_congruence_endpoint_rejected']=rejected(lambda:verify(b.artifact(['x','y'],{'h':[x,y]},b.proof('congruence',xx,xx,premises=[hyp,hyp]))))
    checks['unknown_rule_rejected']=rejected(lambda:verify(b.artifact(['x'],{},b.proof('trust-me',x,x))))
    checks['undeclared_variable_rejected']=rejected(lambda:verify(b.artifact(['x'],{},ring)))
    sine=b.term('sin',x)
    checks['unsupported_analytic_constructor_rejected']=rejected(lambda:verify(b.artifact(['x'],{},b.proof('ring',sine,sine))))
    division=b.term('div',x,x)
    checks['division_without_nonzero_witness_rejected']=rejected(lambda:verify(b.artifact(['x'],{},b.proof('ring',division,one))))
    boolterm=b.put({'kind':'term','type':'Bool','op':'var','name':'x'})
    checks['wrong_type_rejected']=rejected(lambda:verify(b.artifact(['x'],{},b.proof('refl',boolterm,boolterm))))
    malformed=b.put({'kind':'term','type':'Q','op':'const','value':'2/2'})
    checks['noncanonical_rational_rejected']=rejected(lambda:verify(b.artifact([],{},b.proof('refl',malformed,malformed))))
    extra=b.put({'kind':'term','type':'Q','op':'var','name':'x','trusted':True})
    checks['unknown_record_field_rejected']=rejected(lambda:verify(b.artifact(['x'],{},b.proof('refl',extra,extra))))
    forged=deepcopy(artifact); forged['objects'][lhs]['op']='add'
    checks['unrehashed_tamper_rejected']=rejected(lambda:verify(forged))
    missing=deepcopy(artifact); del missing['objects'][x]
    checks['missing_term_rejected']=rejected(lambda:verify(missing))
    deep=x
    for _ in range(102): deep=b.term('neg',deep)
    checks['term_depth_limit_enforced']=rejected(lambda:verify(b.artifact(['x'],{},b.proof('refl',deep,deep))))
    checks['json_round_trip_reverifies']=verify(json.loads(json.dumps(artifact)))==verify(artifact)
    surface=encode(cube()); faces=surface['objects'][surface['root']]['faces']
    bridge={'schema':'marici.polynomial-surface-bridge.v1','surface':surface,
            'faces':[{'face':f,'proof':face_expression(surface,surface['objects'][f])} for f in faces]}
    checks['all_six_cube_faces_verified_by_expression_kernel']=verify_bridge(bridge)
    detached=deepcopy(bridge); detached['faces'][0]['proof']=artifact
    checks['valid_but_unrelated_identity_cannot_fill_face']=rejected(lambda:verify_bridge(detached))
    checks['serialized_bridge_reverifies']=verify_bridge(json.loads(json.dumps(bridge)))
    out=BASE/'results'; out.mkdir(exist_ok=True)
    paths={'identity':out/'merkle_polynomial_identity.json','conditional':out/'merkle_conditional_identity.json',
           'bridge':out/'merkle_polynomial_surface_bridge.json'}
    for name,obj in [('identity',artifact),('conditional',conditional),('bridge',bridge)]:
        paths[name].write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    unconditional=subprocess.run([sys.executable,str(KERNEL),str(paths['identity']),'--require-unconditional'],capture_output=True,text=True)
    scoped=subprocess.run([sys.executable,str(KERNEL),str(paths['conditional'])],capture_output=True,text=True)
    refused=subprocess.run([sys.executable,str(KERNEL),str(paths['conditional']),'--require-unconditional'],capture_output=True,text=True)
    checks['external_unconditional_proof_accepted']=unconditional.returncode==0
    checks['external_conditional_proof_marked']=scoped.returncode==0 and not json.loads(scoped.stdout)['unconditional']
    checks['conditional_proof_not_accepted_as_unconditional']=refused.returncode==1
    result={'schema':'marici.merkle-identity-kernel-check.v1','passed':all(checks.values()),'checks':checks,
            'unconditional_example':verify(artifact),'conditional_example':verify(conditional),
            'cube_surface_root':surface['root'],'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'kernel_sha256':sha256(KERNEL.read_bytes()).hexdigest(),
            'scope':'Typed commutative Q-polynomials and explicit equality proofs with scoped assumptions. Not arbitrary mathematical identities or automatic surface gluing.'}
    (out/'merkle_identity_kernel.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
