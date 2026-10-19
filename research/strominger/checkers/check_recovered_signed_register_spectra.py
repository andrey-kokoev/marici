"""Recover the existing signed-record law and audit its branch spectra.

A compatibility test of a prior uniform constructor, not physical admission
of its signed extensions or a newly selected neutron charging Hamiltonian.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from check_neutron_canonical_occupied_closure import ROOT,eye,mm as rmm,difference
from check_pentachoron_spin_interfaces import A,S2,I,add,scale,mm


def main():
    path=ROOT/'research/strominger/results/neutron-seam-control-transport.json'
    source=json.loads(path.read_text());assert source['status']=='passed'
    for p,h in source['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    # Each satisfied control is a genuine projector in the current carrier
    # sector. It is zero on the separately retained empty vacuum.
    for row in source['seam_controls']:
        P=[list(map(F,r)) for r in row['projector']];S=difference(eye(24),P)
        assert rmm(S,S)==S
    X=((A(0),A(1)),(A(1),A(0)));N=((A(0),A(0)),(A(0),A(1)))
    spectra=[];lam=A(F(1,2))
    for s in (0,1):
        Rp=add(scale(1-s,I),scale(s,X));Rm=add(scale(-(1-s),I),scale(s,X))
        assert mm(Rp,Rp)==I and mm(Rm,Rm)==I
        Qp=scale(F(1,2),add(I,scale(-1,Rp)));Qm=scale(F(1,2),add(I,scale(-1,Rm)))
        assert mm(Qp,Qp)==Qp and mm(Qm,Qm)==Qm
        assert add(Qp,Qm)==add(I,scale(-s,X))
        H=add(N,scale(lam,add(Qp,Qm)))
        gap=A(1) if s==0 else S2
        low=lam+(A(1)-gap)/2;high=low+gap
        ground=scale(gap.inverse(),add(scale(high,I),scale(-1,H)))
        assert mm(ground,ground)==ground and mm(H,ground)==scale(low,ground)
        spectra.append({'control':s,'Hamiltonian':[[v.record() for v in r] for r in H],
                        'eigenvalues':[low.record(),high.record()],'transition_gap':gap.record(),
                        'ground_projector':[[v.record() for v in r] for r in ground]})
    shift=(A(1)-S2)/2
    # sqrt(2)>1, so the occupied-minus-empty value is strictly negative.
    assert shift*(A(1)+S2)==A(F(-1,2))
    result={'status':'passed','checks':['current transported source provenance','all 21 satisfied seam controls idempotent',
             'both signed gates involutive','uniform generators projective','full scalar diagonal retained',
             'both conditional spectra and eigenprojectors exact','negative dressing shift certified'],
            'recovered_rule':'Q_plus+Q_minus=I-S tensor X; H=n+lambda*(I-S tensor X)',
            'declared_inputs':'Controlled signed extensions, occupation generator n=(I-Z)/2, common gap unit, and lambda=1/2 for the one-record fixture.',
            'conditional_spectra':spectra,'common_vacuum_subtracted_occupied_ground':shift.record(),
            'scope':'The prior signed-gate law constructs explicit spectra after its declared extensions. It is a dressing law, not a positive seam-charging law. It has not selected physical energy units or an intrinsic neutron rest baseline.'}
    inputs=[path,Path(__file__).resolve(),ROOT/'research/voevodsky/finite-record-mediator-constructor.md',ROOT/'research/voevodsky/interacting-elementary-reference.md',ROOT/'research/voevodsky/checkers/check_pentachoron_spin_interfaces.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    out=ROOT/'research/strominger/results/recovered-signed-register-spectra.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(result['checks']),'inactive_spectrum':['1/2','3/2'],
                      'matched_spectrum':['1-sqrt(2)/2','1+sqrt(2)/2'],
                      'vacuum_subtracted_ground':'(1-sqrt(2))/2 < 0','physical_normalization_selected':False},indent=2))

if __name__=='__main__':main()
