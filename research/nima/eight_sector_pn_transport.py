"""Read-only comparison embedding; not an assignment to four native N readers.

A separable tensor representation retains the actual anchored PN packet and
an eight-sector profile. Expanded blocks are generated on demand, not copied.
The profile choice is explicit extra data, not a physical attachment theorem.
"""
from copy import deepcopy
from fractions import Fraction as F
from anchored_contact_comparisons import R, recover, restore, binding_digest
from exact_multiradical import sqrt


def action(matrix, vector):
    return [sum((R(F(a))*b for a,b in zip(row, vector)),R()) for row in matrix]


def profile_in_chart(charts, chart, profile):
    assert chart in charts and len(profile)==8
    assert sum((v.conj()*v for v in profile),R())==R(1)
    return [x*sqrt(F(1,2)) for x in action(charts[chart],profile)]


def validate(packet, descriptor, charts, profile, provenance):
    assert packet['schema']=='marici.nima.eight-sector-PN.v1'
    assert packet['sourceDescriptorDigest']==binding_digest(descriptor)
    assert packet['provenance']==provenance
    assert packet['profile']==[x.record() for x in profile]
    expected=profile_in_chart(charts,packet['chart'],profile)
    assert packet['weights']==[x.record() for x in expected]
    recover(packet['core'],descriptor)
    return expected


def encode(core, descriptor, charts, profile, provenance, chart):
    recover(core,descriptor)
    return {'schema':'marici.nima.eight-sector-PN.v1',
            'sourceDescriptorDigest':binding_digest(descriptor),
            'provenance':deepcopy(provenance),'profile':[x.record() for x in profile],
            'chart':chart,'weights':[x.record() for x in profile_in_chart(charts,chart,profile)],
            'core':deepcopy(core),
            'scope':'Separable isometric comparison embedding of one full N field; not four independently populated native readers.'}


def transition(packet, target, descriptor, charts, transitions, profile, provenance):
    old=validate(packet,descriptor,charts,profile,provenance)
    assert target in charts
    weights=action(transitions[target,packet['chart']],old)
    out=deepcopy(packet);out['chart']=target;out['weights']=[x.record() for x in weights]
    validate(out,descriptor,charts,profile,provenance)
    return out


def expanded_block(packet, target, source, target_sector=None, source_sector=None):
    """C_new = W_target C_old W_source^sharp; P remains unchanged.

    A sector index is required precisely for N ports. Source weights are real
    in current tests; conjugation keeps the rule correct for complex profiles.
    The metric at every workspace summand is the original positive N metric.
    """
    weights=[restore(x) for x in packet['weights']]
    def weight(port,sector):
        if port.startswith('N:'):
            assert type(sector) is int and 0<=sector<8
            return weights[sector]
        assert sector is None
        return R(1)
    factor=weight(target,target_sector)*weight(source,source_sector).conj()
    return [[factor*restore(x) for x in row] for row in packet['core']['blocks'][target][source]]


def decode(packet, descriptor, charts, profile, provenance):
    # The retained core is the factored operator data, not an original field
    # side channel. Validate every source block and its amplitude anchor.
    validate(packet,descriptor,charts,profile,provenance)
    return deepcopy(packet['core'])
