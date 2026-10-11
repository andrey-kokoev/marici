"""Fresh source-coherence audit plus a hydrogen-held-out binding discriminator.

The electronic law is an explicit countermodel family, not a native WG map.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent


def main():
    with redirect_stdout(io.StringIO()):
        source=runpy.run_path(str(HERE/'check_mass_source_interchange_cells.py'))
        runpy.run_path(str(HERE/'check_proton_hydrogen_helium_structure.py'),run_name='__main__')
    inputs=json.loads((ROOT/'results/proton-hydrogen-helium-structure.json').read_text())['inputs']
    a=F(inputs['hydrogen_binding_eV']);he=F(inputs['helium_electronic_binding_eV'])
    # On the actual source graph any vertex potential yields an exact edge
    # difference, hence preserves every admitted square and cube boundary.
    slots=source['slots']
    potential=[F(int(s[1][0]=='state')) for s in slots]
    checked=0
    def check_square(v):
        nonlocal checked
        differences=[potential[v[i+1]]-potential[v[i]] for i in range(3)]
        differences.append(potential[v[0]]-potential[v[-1]])
        assert sum(differences)==0
        checked+=1
    index=source['index']
    for o0,o1 in source['outer_arcs']:
        for d0,d1 in source['inner_arcs']:
            check_square([index[o0,d0],index[o1,d0],index[o1,d1],index[o0,d1]])
    for o in source['outer_vertices']:
        for a0,a1 in source['outer_arcs']:
            for b0,b1 in source['outer_arcs']:
                check_square([index[o,('arrow',a0,b0)],index[o,('arrow',a1,b0)],
                              index[o,('arrow',a1,b1)],index[o,('arrow',a0,b1)]])
    assert checked==52488
    assert any(potential[y]!=potential[x] for x,y in source['operation_edges'])
    # Separate electronic trial domain: fixed nucleus Z and retained subset
    # of electron labels. Hydrogen supplies a, NOT an electron-pair coupling b.
    rows=[]
    for b in (F(0),a,2*a):
        def energy(z, labels):
            n=len(labels)
            return -a*z*z*n+b*n*(n-1)/2
        for z in (1,2):
            final=[]
            for order in permutations(('e1','e2')):
                labels=();changes=[];record=[]
                for e in order:
                    new=labels+(e,)
                    changes.append(energy(z,new)-energy(z,labels))
                    record.append(e);labels=new
                assert sum(changes)==energy(z,labels)-energy(z,())
                # Two positive traversal charges coexist with a signed energy
                # change; the complementary reservoir balances that change.
                work=-sum(changes)
                assert energy(z,labels)+work==energy(z,())
                final.append((energy(z,labels),len(record)))
            assert final[0]==final[1]
        assert energy(1,('e1',))==-a
        connected=energy(2,('e1','e2'))-energy(2,('e1',))-energy(2,('e2',))+energy(2,())
        assert connected==b
        predicted=-energy(2,('e1','e2'))
        assert predicted!=he
        rows.append(dict(pair_coupling_eV=str(b),hydrogen_binding_eV=str(a),
                         helium_binding_eV=str(predicted),error_eV=str(predicted-he),
                         connected_energy_eV=str(connected)))
    required=8*a-he
    assert required==F('29.7820')
    result=dict(schema='marici.nima.binding-composition-coherence.v1',status='pass',
                obligation='source route/coherence compatibility; independent electronic readout countermodels',
                source_squares_rechecked=checked,source_vertex_counterterm='indicator of state-comparison rather than arrow-comparison slot',
                source_result='Nonconstant vertex counterterms change edge energy differences without changing square closure; positive traversal resource remains separate.',
                atomic_trial='E_Z(S)=-a Z^2 |S| + b |S|(|S|-1)/2; E measured relative to separated electrons and fixed nucleus',
                atomic_trial_source_status='Explicit rival family, not an identified native WG electronic operator',
                trials=rows,helium_reference_eV=str(he),
                diagnostic_required_connected_energy_eV=str(required),
                disposition='Hydrogen calibration and order-coherent composition do not determine helium binding. Connected two-electron energy is the held-out discriminator.',
                residual='Need native electronic sector and coupled operator giving binding with fixed units. The 29.7820 eV number is a residual of a calibrated Z-squared trial, not measured pure repulsion or a WG prediction. Nuclear binding is separate.')
    (ROOT/'results/binding-composition-coherence.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
