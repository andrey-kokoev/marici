"""One coherent profile over all actual cross-face edges of both carriers.

Both carriers have six disjoint cross-face contacts. Equal per-contact phases
and strengths are a declared interaction profile, not a measured mass fit.
"""
from itertools import combinations
from fractions import Fraction as F
from pathlib import Path
import json
from check_common_contact_dressing import port_projector
from check_constraint_energy_accounting import compose, times, trace, plus, identity
from check_seam_occupation_energy import matrix
from check_coupled_six_piece_belt import R, norm
from check_belt_three_by_twelve import decode
from check_geometric_cycle_reversal import geo
from check_reversed_coefficient_attachment import SOURCE

BASE=Path(__file__).resolve().parents[1]


def edges(triangles):
    return [(i,j) for i,j in combinations(range(len(triangles)),2)
            if triangles[i][0]!=triangles[j][0] and len(set(triangles[i])&set(triangles[j]))==2]


def main():
    store=json.loads((BASE/'results/native_operation_energy_lift_store.json').read_text())['carriers']
    packet=json.loads(SOURCE.read_bytes());objects=packet['objects']
    geometry=objects[objects[packet['root']]['geometry']]['payload']
    placements=sorted(geometry['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    points=dict(geo.POINTS)
    for face in ('ABC','ABD','ACD','BCD'):points['F_'+face]=geo.mean([points[v] for v in face])
    pmodes=[]
    for row in placements:
        X=geo.transpose(tuple(points[v] for v in row['triangle']))
        pmodes.append([(R(x[0]),R(x[1])) for x in geo.zmv(X,(geo.ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA)))])
    source=json.loads((BASE/'results/belt_three_by_twelve_store.json').read_text())
    ambient=json.loads((BASE/'results/coupled_six_piece_belt_store.json').read_text())['record']
    btriangles=[ambient['triangles'][i] for i in source['triangle_order']]
    z=[decode(c['selected_numerator']) for c in source['coordinates']]
    bmodes=[z[2*i:2*i+2] for i in range(18)]
    d=tuple(F(c['d']) for c in source['coordinates'])
    report={};r=F(2386,4485);a=F(4485,3292)
    for name,triangles,modes,metric in (
        ('proton',[row['triangle'] for row in placements],pmodes,(F(1),)*36),
        ('belt',btriangles,bmodes,d)):
        pairs=edges(triangles);vertices=[t for pair in pairs for t in pair]
        assert len(pairs)==6 and len(vertices)==len(set(vertices))==12
        width=len(modes[0]);mode_norms=[]
        for t in vertices:
            ns=sum((norm(v)/metric[width*t+i] for i,v in enumerate(modes[t])),R())
            mode_norms.append(ns)
        assert len(set(mode_norms))==1  # equal normalized contact weights
        # Six disjoint unit contact vectors have norm sqrt(6) when summed.
        # Their equal-phase sum is proportional to the retained modes below.
        W=port_projector({width*t+i:v for t in vertices for i,v in enumerate(modes[t])},metric)
        H=times(F(1,4),matrix(store[name]['entries']))
        N=matrix(store[name]['return_entries'])
        assert compose(W,W)==W and trace(W,36)==1
        overlap=trace(compose(W,N),36)
        if name=='proton':
            assert W==N and compose(H,W)=={}
            poles,weights=[F(0)],[F(1)]
        else:
            assert overlap==r
            assert compose(plus(H,times(-a,identity(36))),compose(H,W))=={}
            assert trace(compose(H,W),36)==(1-r)*a
            poles,weights=[F(0),a],[r,1-r]
        report[name]={'cross_face_edges':pairs,'covered_triangles':sorted(vertices),
                      'normalized_profile_poles':list(map(str,poles)),
                      'normalized_profile_weights':list(map(str,weights)),
                      'coherent_return_overlap_squared':str(overlap)}
    # Unnormalized equal per-contact coupling has six times the normalized
    # response on BOTH carriers. Its positive difference is exact.
    coefficient=6*(1-r)*a
    assert coefficient==F(6297,1646)
    Delta,g=F(1,2),F(1,2)
    xp=F(1)
    assert Delta+xp==6*g*g/xp
    lo,hi=F(0),xp
    for _ in range(80):
        x=(lo+hi)/2
        value=Delta+x-6*g*g*(r/x+(1-r)/(x+a))
        if value<0:lo=x
        else:hi=x
    assert 0<lo<hi<xp
    result={'verification_passed':True,'carriers':report,
            'profile_assumption':'Equal phase and equal strength at every geometrically shared cross-face edge; this is a declared coherent field profile.',
            'contacts_per_carrier':6,'additional_independent_seam_registers':0,
            'unnormalized_response_difference':'Rp(t)-Rb(t)=(6297/1646)/(t*(t+4485/3292))>0 for all t>0',
            'proton_binding_equation':'Delta+x_p=6*g^2/x_p',
            'belt_binding_equation':'Delta+x_b=6*g^2*[(2386/4485)/x_b+(2099/4485)/(x_b+4485/3292)]',
            'belt_cubic':'x^3+(Delta+a)*x^2+(Delta*a-6*g^2)*x-6*g^2*r*a=0; a=4485/3292,r=2386/4485',
            'common_offset_independent_splitting':'x_p-x_b>0; a stable empty reference requires common mu>x_p',
            'illustrative_parameters':{'Delta':str(Delta),'g_per_contact':str(g),'mu':'2'},
            'illustrative_proton_binding':'1','illustrative_belt_binding_interval':list(map(str,(lo,hi))),
            'illustrative_belt_minus_proton':float(xp-(lo+hi)/2),
            'scope':'All-contact completion of the conditional internal-channel law; no derivation of the field profile, auxiliary channel, clock scale or physical mass.'}
    (BASE/'results/all_face_contact.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
