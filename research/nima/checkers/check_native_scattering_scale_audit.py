"""Retained real-axis interval replay and exact relative-scale nuisance rival."""
import json
import sys
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import sympy as S

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/nima'
CONTRACT=HOME/'contracts/native-scattering-scale-audit.v1.json'


def require(ok,message):
    if not ok: raise ValueError(message)


def sha(p): return sha256(p.read_bytes()).hexdigest()


def main():
    c=json.loads(CONTRACT.read_text())
    base=ROOT/'research/voevodsky'
    sys.path.insert(0,str(base/'checkers'))
    import check_slater_real_axis_native as h
    I=h.Interval
    paths={CONTRACT,Path(__file__)}
    def load(name):
        p=ROOT/name;paths.add(p)
        r=json.loads(p.read_text())
        require(r['verification_passed'],'source receipt failed')
        for relative,expected in r['source_hashes'].items():
            dep=(base/relative).resolve()
            require(dep.is_relative_to(ROOT) and sha(dep)==expected,'source drift: '+relative)
            paths.add(dep)
        return r
    src=load(c['source_result'])
    endpoint=load('research/voevodsky/results/offcenter_endpoint_dispersion.json')
    energy=load('research/voevodsky/results/multiobject_energy_response.json')
    native=load('research/voevodsky/results/native_spinor_pair_adapter.json')
    response=next(r for r in endpoint['real_axis_reports'] if r['energy']=='4')['response_used']
    ap,av,bp,bv=[h.read_interval(response[name]) for name in ('a_pair','a_vector3','b_pair','b_vector3')]
    aa=h.read_interval(src['Slater_real_at_4'])
    density=next(r for r in energy['real_axis_density_reports'] if r['energy']=='4')['refinements'][-1]['rho_scalar3']
    pl,ph=h.pi_bounds()
    ba=h.grid_out(I(pl,ph)*h.read_interval(density))
    require(bp.low>0 and bv.low>0 and ba.low>0,'not open channel fixture')
    r6=I(Q(h.root_fixed(6)[0],h.G),Q(h.root_fixed(6)[1],h.G))
    r5=I(Q(h.R5[0],h.G),Q(h.R5[1],h.G))
    cores=[11-2*r6-r5,11-2*r6+r5]
    for option in (0,1):
        expected=h.A(11)-2*h.S2*h.S3+(-h.S5 if option==0 else h.S5)
        reports=[r for r in native['adapter_reports'] if r['doublet_option']==option]
        require(len(reports)==2 and all(h.matrix([[r['pair_conditional_core_energy']]])[0][0]==expected for r in reports),
                'native pair core formula changed')
    def flux(core):
        ds=4-core-2*ap-aa;dv=4-core-ap-av
        den=ds.square()+(2*bp+ba).square();denv=dv.square()+(bp+bv).square()
        t2=4*bp.square()/den;ta=4*bp*ba/den;rs=(ds.square()+ba.square())/den
        unit=I(0,1)
        t2=h.intersect(t2,unit);ta=h.intersect(ta,unit);rs=h.intersect(rs,unit)
        t2=h.intersect(t2,1-ta-rs);ta=h.intersect(ta,1-t2-rs);rs=h.intersect(rs,1-t2-ta)
        tv=4*bp*bv/denv;rv=(dv.square()+(bp-bv).square())/denv
        tv=h.intersect(tv,1-rv);rv=h.intersect(rv,1-tv)
        p2=t2/4;pa=ta/4;pv=Q(3,4)*tv;p3=pa+pv
        survive=h.intersect(rs/4+Q(3,4)*rv,1-p2-p3)
        require((p2+p3+survive).contains(1),'optical sum enclosure')
        require(all(0<=x.low<=x.high<=1 for x in (p2,pa,pv,p3,survive)),'probability bound')
        return {k:v.record() for k,v in [('two_output',p2),('scalar_three_output',pa),('vector_three_output',pv),('all_three_output',p3),('survival',survive)]}
    fixtures=[]
    for option,core in enumerate(cores):
        replay=flux(core)
        previous=next(r for r in src['source_core_fixtures'] if r['option']==option)
        require(replay=={k:previous[k] for k in replay},'original interval replay changed')
        for s in c['relative_scale_grid']:
            fixtures.append({'option':option,'relative_scale':s,'flux':flux(Q(s)*core)})
    e0=11-2*S.sqrt(6)-S.sqrt(5);e1=11-2*S.sqrt(6)+S.sqrt(5)
    ratio=S.cancel(e0/e1)
    require(S.simplify(ratio*e1-e0)==0,'exact rival core match')
    require(cores[0].low>0 and cores[1].low>cores[0].high,'positive ordered energies')
    E,delta,ap_s,aa_s,av_s,bp_s,ba_s,bv_s=S.symbols('E delta ap aa av bp ba bv',real=True)
    ds=E-delta-2*ap_s-aa_s;dv=E-delta-ap_s-av_s
    denominators=[ds+S.I*(2*bp_s+ba_s),dv+S.I*(bp_s+bv_s)]
    for d in denominators:
        require(S.simplify(d.subs(delta,e0)-d.subs(delta,ratio*e1))==0,'response alias')
    # Common symmetric scale bounds: [1-d,1+d] around the independently
    # calibrated unit. Core intervals do not overlap iff d < threshold.
    threshold=S.simplify((e1-e0)/(e1+e0))
    require(S.simplify(e0*(1+threshold)-e1*(1-threshold))==0,'calibration boundary')
    require(S.simplify(threshold-S.sqrt(5)/(11-2*S.sqrt(6)))==0,'threshold expression')
    for d,expected in [(S.Rational(1,4),True),(S.Rational(1,2),False)]:
        require(bool(e0*(1+d)<e1*(1-d))==expected,'calibration control')
    result={'schema':'marici.scattering.native-scale-audit-result.v1','status':'pass',
            'conjecture_disposition':'doublet_flux_identification_fails_with_free_relative_scale',
            'original_unit_scale_intervals_reproduced_exactly':True,'fixed_scale_grid':fixtures,
            'alias':{'option0_scale':'1','option1_scale':str(ratio),'option1_scale_decimal':float(ratio),
                     'common_core':str(e0),'common_E4_flux':flux(cores[0]),
                     'identity_scope':'Identical scalar/vector encounter resolvents and optical amplitudes in the same declared encounter/output channel coordinates, for identical self-energies and couplings. Does not identify native embeddings, native states or physical representations.'},
            'calibration_excludes_core_alias':{'symmetric_relative_halfwidth_strict_bound':str(threshold),
                'decimal':float(threshold),'quarter_width_excludes':True,'half_width_does_not_exclude':True,
                'qualification':'Excludes this equal-core rival only; not proof that all intensity, coupling or preparation degeneracies are removed.'},
            'energy_scan_boundary':'Where the same channel laws apply, the symbolic alias persists at every E. More energies alone cannot separate option and relative scale in this selected scalar-core model.',
            'continuum_integrals_rerun':False,'physical_scale_fitted_or_admitted':False,
            'physical_scattering_explained':False,'root_outcome':None,
            'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted(paths)}}
    output=HOME/'results/native-scattering-scale-audit.json'
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'conjecture_disposition':result['conjecture_disposition'],
                      'alias_scale':float(ratio),'calibration_halfwidth_boundary':float(threshold),
                      'original_intervals_exactly_replayed':True,'root_outcome':None},indent=2))


if __name__=='__main__': main()
