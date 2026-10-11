"""Test native coefficient intensities as the retained graph's response metric.

The c=|amplitude|^2 interpretation is an explicit rival to unit arrow costs.
All relative weights come from the frozen source; no mass target is fitted.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict
import hashlib
import json
from check_wg_reservoir_completion import solve

ROOT=Path(__file__).resolve().parents[1]
STAGES=('raw','local','aligned')


def main():
    source=ROOT/'results/twelve-triangle-1836-arrows.json'
    raw=source.read_bytes()
    records=json.loads(raw)
    def amplitude_norm(a):
        return F(a['weight_real'])**2+3*F(a['weight_imag_sqrt3'])**2
    internal=[(tuple(a['source']),tuple(a['target']),amplitude_norm(a)) for a in records]
    assert len(internal)==1836 and all(c>0 for _,_,c in internal)
    ports=sorted({v for a,b,_ in internal for v in (a,b)})
    assert len(ports)==108
    # diag(local projector)/12 = diag(collective projector) for this source.
    w={}
    for a in records:
        u,v=tuple(a['source']),tuple(a['target'])
        if u[0]=='raw' and v[0]=='local' and u[1:]==v[1:]:
            assert F(a['weight_imag_sqrt3'])==0
            w[u[1:]]=F(a['weight_real'])/12
    assert len(w)==36 and sum(w.values())==1
    assert set(w.values())=={F(1,180),F(7,180)}
    for a,b,c in internal:
        if a[0]=='aligned' and b[0]=='raw':
            assert c==w[a[1:]]*w[b[1:]]
    totals=defaultdict(F)
    for a,b,c in internal: totals[(a[0],b[0])]+=c
    assert dict(totals)=={('raw','local'):12,('local','aligned'):3,('aligned','raw'):1}

    # One shared reservoir. Each copy of its normalized mode u/sqrt(80)
    # supplies squared link amplitude w_i. No additional relative multiplier.
    reservoir=('reservoir',)
    edges=internal+[(reservoir,v,w[v[1:]]) for v in ports]
    classes=[(s,t) for s in STAGES for t in sorted(set(w.values()))]
    ci={c:i for i,c in enumerate(classes)}
    def klass(v):return ci[(v[0],w[v[1:]])]
    matrix=[[F(0) for _ in classes] for _ in classes]
    for a,b,c in edges:
        j=klass(b)
        matrix[j][j]+=c
        if a!=reservoir:
            i=klass(a)
            matrix[i][i]+=c;matrix[i][j]-=c;matrix[j][i]-=c
    rows={}
    energies={}
    for name,sgn in [('proton',{'raw':1}),('witness',{'aligned':-1}),
                     ('pair',{'raw':1,'aligned':-1})]:
        j={v:F(sgn.get(v[0],0))*w[v[1:]] for v in ports}
        j[reservoir]=-sum(j.values())
        rhs=[F(0) for _ in classes]
        for v in ports:rhs[klass(v)]+=j[v]
        xs=solve(matrix,rhs)
        x={v:xs[klass(v)] for v in ports};x[reservoir]=F(0)
        flux={v:F(0) for v in ports+[reservoir]}
        flow=[]
        for a,b,c in edges:
            f=c*(x[b]-x[a]);flow.append(f)
            flux[b]+=f;flux[a]-=f
        assert flux==j  # Full 109 equations certify the six-class reduction.
        energy=sum(f*f/(2*c) for (_,_,c),f in zip(edges,flow))
        assert energy==sum(j[v]*x[v] for v in j)/2>0
        # Multiplying all conductances by 2 leaves f and boundary invariant.
        scaled=sum(f*f/(4*c) for (_,_,c),f in zip(edges,flow))
        assert scaled==energy/2
        energies[name]=energy
        rows[name]={'field_cost':str(energy),'decimal':float(energy),
                    'class_potentials':list(map(str,xs)), 'reservoir_source':str(j[reservoir])}
    cross=energies['pair']-energies['proton']-energies['witness']
    assert cross<0
    ratio=energies['proton']/energies['witness']
    pair_ratio=energies['pair']/energies['witness']
    delta_ratio=cross/energies['witness']
    assert pair_ratio==ratio+1+delta_ratio
    assert (energies['proton']/2)/(energies['witness']/2)==ratio
    # A falsifier for the proposed identification, not a target used by solve.
    assert ratio!=1836
    result=dict(schema='marici.nima.native-coefficient-response-metric.v1',status='pass',
                source_sha256=hashlib.sha256(raw).hexdigest(),
                internal_conductance_totals={f'{a}->{b}':str(t) for (a,b),t in totals.items()},
                reservoir_conductance_total='3',
                metric='native arrow |complex coefficient|^2; reservoir links diag(N) on each stage',
                source_profiles='native collective mode intensities on raw and aligned stages',
                interpretation_assumptions=['squared amplitude interpreted as conductance',
                                            'one shared normalized collective-mode reservoir attached to all three stages',
                                            'opposite signs for the two fixed source profiles',
                                            'conserved-flow cost used as trial readout'],
                responses=rows,cross_term=str(cross),
                scale_free={'proton_over_witness':str(ratio),'proton_over_witness_decimal':float(ratio),
                            'pair_over_witness':str(pair_ratio),'pair_over_witness_decimal':float(pair_ratio),
                            'binding_over_witness':str(delta_ratio),'binding_over_witness_decimal':float(delta_ratio)},
                controls=['all 109 equations','native projector-intensity identities',
                          'positive primal cost equals half source work','common metric scale cancels in ratios'],
                disposition='The source-weighted conserved-flow readout does not reproduce 1836 as the proton/witness cost ratio. This falsifies that readout identification, not the 1836 arrow-count theorem.',
                residual='No free stiffness scale can repair a scale-free mismatch. A different source-derived readout would require independent justification, not fitting to masses.')
    out=ROOT/'results/native-coefficient-response-metric.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
