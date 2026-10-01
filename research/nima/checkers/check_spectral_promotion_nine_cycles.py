"""Nine re-entry rounds through existing spectral promotion, exact arithmetic.

The next identity reopens its retained root; it does not create a new operand
constructor or recursively increase packet ancestry. Execution receipts are
separate from the reused depth-three packet tree. C/S powers are diagnostics,
not an implicit physical evolution caused by promotion.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_record4_spectral_promotion import (
    SpectralLedger, TwoPacket, MODES, ONE, OMEGA, MAX_DEPTH,
    spectral_projector, zjson, ztrace, dagger,
)
from check_triangle_half_phase import (
    I, ZERO, mm, transpose, add, sub, scale,
    zreal, zmm, zmscale, zmul, zconj, znorm,
)

ROUNDS=9


def main():
    ledger=SpectralLedger()
    packets=(TwoPacket('AB:seed','A','B'),TwoPacket('BC:seed','B','C'),TwoPacket('CA:seed','C','A'))
    root=ledger.record4(packets);C=ledger.validate_root(root)
    Q=scale(add(add(I,C),mm(C,C)),F(1,3));P=sub(I,Q)
    S=add(add(Q,scale(P,F(1,2))),scale(sub(C,transpose(C)),F(1,2)))
    assert mm(S,S)==C
    streams={};all_labels=set()
    for mode,lam in MODES.items():
        _,expected=spectral_projector(C,mode)
        half=ONE if mode=='common' else (F(1,2),F(1,2) if mode=='positive' else F(-1,2))
        vector=(ONE,)*3 if mode=='common' else (ONE,lam,zmul(lam,lam))
        seed_vector=tuple((z,) for z in vector)
        cyclic_vector=seed_vector;half_vector=seed_vector
        cyclic_phase=half_phase=ONE
        previous=None;receipts=[]
        for n in range(1,ROUNDS+1):
            # Re-entry is through the prior identity's window into this same root.
            if previous is not None:
                assert ledger.resolve(previous) is root
                reopened=ledger.deconstruct(previous)
            else: reopened=packets
            assert reopened==packets
            # Fold views reconstructed from recovered primitive occurrences.
            a,b,c=reopened
            through_B=((a,b),(c,));through_C=((a,),(b,c))
            assert through_B==root.fold_through_B and through_C==root.fold_through_C
            assert (a,(b,c))==(root.entry,root.continuation)
            identity=ledger.promote(root,mode)
            assert identity.projector==expected
            assert identity.depth==MAX_DEPTH==3
            assert zmm(identity.projector,identity.projector)==identity.projector
            assert dagger(identity.projector)==identity.projector and ztrace(identity.projector)==ONE
            assert ledger.resolve(identity) is root and ledger.deconstruct(identity)==packets
            assert identity.label not in all_labels;all_labels.add(identity.label)
            # Separately evaluate existing C and S at the same round index.
            cyclic_vector=zmm(zreal(C),cyclic_vector)
            half_vector=zmm(zreal(S),half_vector)
            cyclic_phase=zmul(cyclic_phase,lam);half_phase=zmul(half_phase,half)
            assert cyclic_vector==zmscale(seed_vector,cyclic_phase)
            assert half_vector==zmscale(seed_vector,half_phase)
            assert znorm(cyclic_phase)==znorm(half_phase)==1
            assert zmm(identity.projector,cyclic_vector)==cyclic_vector
            assert zmm(identity.projector,half_vector)==half_vector
            for v in (cyclic_vector,half_vector):
                assert sum(znorm(z[0]) for z in v)==3
            if mode!='common':
                assert (cyclic_phase==ONE)==(n%3==0)
                assert (half_phase==ONE)==(n%6==0)
                if n in (3,9): assert half_phase==(F(-1),F(0))
            receipts.append({'round':n,'input_identity':previous.label if previous else None,
                'output_identity':identity.label,'retained_root':root.label,
                'active_arity':1,'reopened_primitive_arrows':len(reopened),
                'packet_ancestry_depth':identity.depth,'projector_rank':1,
                'projector_unchanged':True,'source_occurrences':[p.label for p in reopened],
                'cycle_power_phase_diagnostic':zjson(cyclic_phase),
                'half_phase_power_diagnostic':zjson(half_phase),
                'note':'Phase powers are separate operator diagnostics; promotion itself does not execute a rotation.'})
            previous=identity
        for n,row in enumerate(receipts,1):
            assert row['input_identity']==(None if n==1 else receipts[n-2]['output_identity'])
            assert ledger.resolve(ledger.identities[row['output_identity']]) is root
        streams[mode]=receipts
    assert len(ledger.identities)==27 and len(ledger.roots)==1
    assert len(all_labels)==27
    for i,mode in enumerate(MODES):
        for other in list(MODES)[i+1:]:
            a=ledger.identities[streams[mode][-1]['output_identity']]
            b=ledger.identities[streams[other][-1]['output_identity']]
            assert zmm(a.projector,b.projector)==zreal(ZERO)
    result={'status':'passed','rounds_per_mode':ROUNDS,'mode_count':3,
            'promoted_identity_records':len(ledger.identities),'retained_nested_roots':len(ledger.roots),
            'primitive_arrow_occurrences':3,'max_packet_ancestry_depth':MAX_DEPTH,
            'streams':streams,
            'outcome':'All projector identities are fixed; fresh promotion receipts accumulate and history remains recoverable.',
            'cycle_power_period':3,'half_phase_power_period':6,
            'scope':'Nine re-entry/promote rounds on one retained triangle. No recursive next-level arrow generation, no ancestry truncation and no physical-time law.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'spectral-promotion-nine-cycles.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: 9 rounds x 3 modes; 27 fresh identities; exact projector stability; full recovery; depth 3. Separate C/S diagnostics return in 3/6 steps.')

if __name__=='__main__': main()
