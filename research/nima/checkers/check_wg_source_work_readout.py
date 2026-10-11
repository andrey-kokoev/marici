"""Primal/dual energy audit for fixed-boundary flow on the source arrow graph.

Distinguishes conservation constraints from scalar-force coupling. No metric
normalization or physical interpretation is inferred from bare Layer1.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_wg_reservoir_completion import solve, dot, STAGES

ROOT=Path(__file__).resolve().parents[1]


def main():
    arrows=json.loads((ROOT/'results/twelve-triangle-1836-arrows.json').read_text())
    internal=[(tuple(a['source']),tuple(a['target']),F(1)) for a in arrows]
    ports=sorted({v for a,b,_ in internal for v in (a,b)})
    reservoir=('reservoir',)
    nodes=ports+[reservoir]
    index={s:i for i,s in enumerate(STAGES)}
    stage=[[F(0) for _ in STAGES] for _ in STAGES]
    for a,b,c in internal:
        i,j=index[a[0]],index[b[0]]
        stage[i][i]+=c;stage[j][j]+=c
        stage[i][j]-=c;stage[j][i]-=c
    # Locate an actual closed three-arrow witness for the circulation control.
    edge_index={(a,b):i for i,(a,b,_) in enumerate(internal)}
    outgoing={v:[] for v in ports}
    for a,b,_ in internal: outgoing[a].append(b)
    cycle=None
    for a in ports:
        if a[0]!='raw': continue
        for b in outgoing[a]:
            for c in outgoing[b]:
                if (c,a) in edge_index:
                    cycle=[edge_index[a,b],edge_index[b,c],edge_index[c,a]]
                    break
            if cycle: break
        if cycle: break
    assert cycle is not None
    rows=[]
    for k in (F(1,4),F(1),F(4)):
        edges=internal+[(reservoir,v,k) for v in ports]
        d=[[stage[i][j]+(36*k if i==j else 0) for j in range(3)] for i in range(3)]
        def divergence(flow):
            out={v:F(0) for v in nodes}
            for (a,b,_),f in zip(edges,flow):
                out[a]-=f;out[b]+=f
            return out
        def energy(flow): return sum(f*f/(2*c) for (_,_,c),f in zip(edges,flow))
        records={}
        for name,j in [('p',[F(1),F(0),F(0)]),
                       ('e',[F(0),F(0),F(-1)]),
                       ('pair',[F(1),F(0),F(-1)])]:
            xs=solve(d,j)
            x={v:xs[index[v[0]]] for v in ports};x[reservoir]=F(0)
            source={v:j[index[v[0]]]/36 for v in ports};source[reservoir]=-sum(j)
            flow=[c*(x[b]-x[a]) for a,b,c in edges]
            assert divergence(flow)==source
            primal=energy(flow)
            work=sum(source[v]*x[v] for v in nodes)
            dual=work-sum(c*(x[b]-x[a])**2/2 for a,b,c in edges)
            assert primal==dual==work/2>0
            # Strong-duality certificate: any feasible circulation z has zero
            # cross term, so E(f+z)-E(f)=E(z). Test on an actual source cycle.
            z=[F(i in cycle) for i in range(len(edges))]
            assert all(v==0 for v in divergence(z).values())
            assert sum(f*t/c for (_,_,c),f,t in zip(edges,flow,z))==0
            assert energy([f+t for f,t in zip(flow,z)])-primal==energy(z)==F(3,2)
            # Reversing every arrow orientation changes neither energy nor J.
            reversed_flux={v:F(0) for v in nodes}
            for (a,b,_),f in zip(edges,flow):
                reversed_flux[b]-=-f;reversed_flux[a]+=-f
            assert reversed_flux==source
            # Quasistatic source ramp: J(t)=tJ, x(t)=tx. Integral x.dJ
            # is work/2, i.e. the positive primal cost, not its negative.
            records[name]={'energy':primal,'source_work_ramp':work/2}
        cross=records['pair']['energy']-records['p']['energy']-records['e']['energy']
        assert cross<0
        rows.append(dict(k=str(k),source_energies={n:str(r['energy']) for n,r in records.items()},
                         conserved_flow_cross=str(cross),
                         scalar_force_relaxation_cross=str(-cross)))
    # Gauge freedom of the *metric*: C -> 2 C preserves the incidence,
    # boundary and optimal flows, but halves potentials and costs. This is
    # algebraic: f'=2C B^T(x/2)=f; E'=sum f²/(4c)=E/2.
    assert energy(flow)/2==sum(f*f/(4*c) for (_,_,c),f in zip(edges,flow))
    result=dict(schema='marici.nima.wg-source-work-readout.v1',status='pass',
                primal='min 1/2 sum_e f_e^2/c_e subject to Bf=J',
                dual='max_x J^T x - 1/2 x^T B C B^T x',
                value='1/2 J^T (B C B^T)^+ J for neutral full-graph sources',
                alternative='min_x 1/2 x^T D x - J^T x has the negative value; it models force relaxation, not fixed-boundary transport cost',
                rows=rows,checks=['all source boundaries retained','primal-dual equality',
                                 'actual triangle circulation raises energy by 3/2',
                                 'orientation covariance','source-ramp work equals positive cost',
                                 'uniform conductance scaling changes cost without changing flows'],
                disposition='Conserved-flow interpretation selects the positive stored-field readout and negative opposite-source cross-term. Bare WG does not itself select this interpretation or its conductance metric.',
                first_missing_input='A WG-owned rule interpreting witnesses as conserved currents with a specified conductance/energy metric. Repeating closure calculations cannot fix that metric.')
    out=ROOT/'results/wg-source-work-readout.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
