"""Same local symmetric-edge contact and reference rule on both carriers.

Exact source response ordering; illustrative shared reference parameters are
not fits or physical charge/reference identifications.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
from check_seam_occupation_energy import matrix
from check_constraint_energy_accounting import identity, plus, times, compose, trace
from check_coupled_six_piece_belt import R, Z, mul, conj, norm, scale
from check_belt_three_by_twelve import decode
from check_reversed_coefficient_attachment import SOURCE
from check_geometric_cycle_reversal import geo
from check_collective_carrier_spectrum import polynomial_product

BASE=Path(__file__).resolve().parents[1]


def port_projector(vector,metric):
    ns=sum((norm(v)/metric[i] for i,v in vector.items()),R())
    return {(i,j):scale(1/(ns*metric[j]),mul(a,conj(b))) for i,a in vector.items() for j,b in vector.items() if a!=Z and b!=Z}


def add_poly(a,b):
    n=max(len(a),len(b));a=[F(0)]*(n-len(a))+a;b=[F(0)]*(n-len(b))+b
    return [x+y for x,y in zip(a,b)]


def rational_response(roots,weights):
    denominator=[F(1)];numerator=[]
    for root in roots:denominator=polynomial_product(denominator,[F(1),root])
    for i,w in enumerate(weights):
        term=[w]
        for j,root in enumerate(roots):
            if i!=j:term=polynomial_product(term,[F(1),root])
        numerator=add_poly(numerator,term)
    return numerator,denominator


def main():
    energy_raw=(BASE/'results/native_operation_energy_lift_store.json').read_bytes()
    store=json.loads(energy_raw)['carriers']
    p_raw=SOURCE.read_bytes();packet=json.loads(p_raw);objects=packet['objects']
    geometry=objects[objects[packet['root']]['geometry']]['payload']
    placements=sorted(geometry['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    points=dict(geo.POINTS)
    for face in ('ABC','ABD','ACD','BCD'):points['F_'+face]=geo.mean([points[v] for v in face])
    vector={};selected=[]
    for t,row in enumerate(placements):
        if row['outer_arrow'] not in ('AB','BA'):continue
        selected.append(row['triangle'])
        X=geo.transpose(tuple(points[v] for v in row['triangle']))
        v=geo.zmv(X,(geo.ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA)))
        vector.update({3*t+i:(R(x[0]),R(x[1])) for i,x in enumerate(v)})
    assert len(selected)==2 and len(set(selected[0])&set(selected[1]))==2
    Wp=port_projector(vector,(F(1),)*36)
    Hp=times(F(1,4),matrix(store['proton']['entries']))
    phase=plus({(i,j):v for (i,j),v in Hp.items() if i//3==j//3},times(-1,identity(36)))
    align=plus(Hp,times(-1,phase))
    assert compose(phase,Wp)=={}
    proots=[F(0),F(1,2),F(1),F(3,2)];pweights=[]
    for root in proots:
        P=identity(36)
        for other in proots:
            if root!=other:P=compose(P,times(1/(root-other),plus(align,times(-other,identity(36)))))
        pweights.append(trace(compose(Wp,P),36))
    assert sum(pweights)==1 and pweights[0]==F(1,6)

    belt_source=json.loads((BASE/'results/belt_three_by_twelve_store.json').read_text())
    d=tuple(F(c['d']) for c in belt_source['coordinates'])
    z=[decode(c['selected_numerator']) for c in belt_source['coordinates']]
    Wb=port_projector({i:z[i] for i in (0,1,6,7)},d)
    Hb=times(F(1,4),matrix(store['belt']['entries']))
    even_roots=[F(0),F(4485,3292),F(5391,3292)]
    even_weights=[F(1193,4485),F(2099,8970),F(1,2)]
    broots=[];bweights=[]
    for shift,factor in ((F(0),F(1,3)),(F(3,4),F(2,3))):
        broots.extend(root+shift for root in even_roots)
        bweights.extend(w*factor for w in even_weights)
    # This time use one LOCAL bridge on both carriers, not a sector-averaged
    # belt contact compared with a single proton contact.
    moment= Wb
    for k in range(6):
        assert trace(moment,36)==sum(w*r**k for r,w in zip(broots,bweights))
        moment=compose(Hb,moment)
    annihilator=Wb
    for root in broots:annihilator=compose(plus(Hb,times(-root,identity(36))),annihilator)
    assert annihilator=={} and bweights[0]==F(1193,13455)
    pn,pd=rational_response(proots,pweights);bn,bd=rational_response(broots,bweights)
    difference=add_poly(polynomial_product(pn,bd),[-x for x in polynomial_product(bn,pd)])
    assert all(x>=0 for x in difference) and any(x>0 for x in difference)
    # Denominators are positive for t>0; nonnegative numerator coefficients
    # certify Sp(-t)>Sb(-t) for EVERY positive t, not a parameter scan.
    def response(roots,weights,t):return sum(w/(root+t) for root,w in zip(roots,weights))
    epsilon,g,mu=F(1),F(1,2),F(1,2)
    assert epsilon>g*g*response(proots,pweights,mu)
    rows={}
    for name,roots,weights in (('proton',proots,pweights),('belt',broots,bweights)):
        lo=F(0);hi=min(epsilon,mu)
        for _ in range(70):
            mid=(lo+hi)/2
            value=epsilon-mid-g*g*response(roots,weights,mu-mid)
            if value>0:lo=mid
            else:hi=mid
        E=(lo+hi)/2
        susceptibility_norm=sum(w/(mu+r-E)**2 for r,w in zip(roots,weights))
        reference_probability=1/(1+g*g*susceptibility_norm)
        coherent_fraction=(weights[0]/(mu-E)**2)/susceptibility_norm
        assert 0<reference_probability<1 and 0<coherent_fraction<1
        rows[name]={'interval':[str(lo),str(hi)],'energy_decimal':float(E),
                    'reference_probability_numerical':float(reference_probability),
                    'coherent_fraction_within_carrier_numerical':float(coherent_fraction)}
    p_lo,p_hi=map(F,rows['proton']['interval']);b_lo,b_hi=map(F,rows['belt']['interval'])
    assert b_lo>p_hi
    report={
        'verification_passed':True,'contact_rule':'one normalized symmetric local shared-edge contact on each actual carrier',
        'proton_contact':'AB/BA source triangles','belt_contact':'triangles 0/3, one paired sector; NOT its C3 average',
        'proton_poles':list(map(str,proots)),'proton_weights':list(map(str,pweights)),
        'belt_poles':list(map(str,broots)),'belt_weights':list(map(str,bweights)),
        'positive_response_difference_numerator_descending':list(map(str,difference)),
        'response_order':'Sp(-t)>Sb(-t) for all t>0',
        'conditional_energy_order':'For identical epsilon>mu>0, nonzero g, and a stable empty reference, the carrier-connected lowest belt dressed excitation exceeds the proton dressed excitation.',
        'dressed_state_equals_bare_return':False,
        'state_tracking':'For epsilon>mu, the lower branch tends to the original coherent carrier as g tends to zero; finite coupling dresses both the reference and internal carrier modes.',
        'reason':'The proton contact has the larger below-spectrum response and is lowered more strongly by the identical reference coupling.',
        'shared_illustrative_parameters':{'epsilon':str(epsilon),'g':str(g),'mu':str(mu)},
        'illustrative_lowest_energies':rows,
        'illustrative_belt_minus_proton':float((b_lo+b_hi-p_lo-p_hi)/2),
        'no_separate_particle_offset_or_coupling_fit':True,
        'physical_charge_caveat':'Identical mathematical exchange blocks do not establish a common physical field: a charged proton excitation requires a charge-compatible reference/reservoir, whereas the belt is proposed neutral.',
        'scope':'Source-specific contact-response comparison under a supplied shared dressing law, not a physical neutron mass or a derived common vacuum.',
        'source_sha256':{'energy_store':sha256(energy_raw).hexdigest(),'proton_geometry':sha256(p_raw).hexdigest()}}
    (BASE/'results/common_contact_dressing.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
