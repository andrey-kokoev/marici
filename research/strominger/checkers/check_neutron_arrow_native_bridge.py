"""Bind the real/complex arrow source to prior native coefficients and energy.

Reuse the existing bridge in an isolated BASE with the newly inferred action.
Retain its ordered corners, frame, grouping and occupation law as model inputs.
"""
from pathlib import Path
from fractions import Fraction as F
from tempfile import TemporaryDirectory
from contextlib import redirect_stdout
import io,json,hashlib,shutil
from assemble_real_complex_arrows import ROOT,run
import check_geometric_phase_energy_bridge as bridge
import check_seam_occupation_energy as occupation
from check_belt_three_by_twelve import decode,sparse_product
from check_coupled_six_piece_belt import R,Z,ONE,add,mul,conj,scale,norm,encoded


def main():
    source_path=ROOT/'research/strominger/inputs/neutron-real-complex-arrows.json'
    assembled=run(json.loads(source_path.read_text()))
    base=ROOT/'research/voevodsky'
    names=['results/four_six_center_cones.json','results/belt_three_by_twelve_store.json',
           'results/coupled_six_piece_belt_store.json','results/native_operation_energy_lift_store.json','inputs/relative-proton.json']
    hashes={name:hashlib.sha256((base/name).read_bytes()).hexdigest() for name in names}
    original_bridge_base=bridge.BASE;original_occupation_base=occupation.BASE
    with TemporaryDirectory(prefix='neutron-arrow-native-') as tmp:
        isolated=Path(tmp)
        for name in names:
            dest=isolated/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(base/name,dest)
        (isolated/'inputs/mode-neutron.json').write_text(json.dumps(assembled['decoded_source']))
        try:
            bridge.BASE=isolated
            targets,_=bridge.load_targets()
            reports,_=bridge.native_bridge(targets)
            occupation.BASE=isolated
            with redirect_stdout(io.StringIO()):occupation.main()
            energy=json.loads((isolated/'results/seam_occupation_energy.json').read_text())
        finally:
            bridge.BASE=original_bridge_base;occupation.BASE=original_occupation_base
    assert all(hashlib.sha256((base/name).read_bytes()).hexdigest()==h for name,h in hashes.items())
    # Bridge above reconstructs all 18 native modes from this source and
    # compares every numerator and the native return. Rebuild its retained
    # three-sector protocol using the verified numerators, not stored edges.
    store=json.loads((base/'results/belt_three_by_twelve_store.json').read_text())
    ambient=json.loads((base/'results/coupled_six_piece_belt_store.json').read_text())
    assert hashlib.sha256(json.dumps(ambient['record'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==ambient['root']
    assert store['source_root']==ambient['root']
    assert ambient['record']['geometry_sha256']==hashes['results/four_six_center_cones.json']
    z=tuple(decode(c['selected_numerator']) for c in store['coordinates'])
    d=tuple(F(c['d']) for c in store['coordinates'])
    assert len(z)==36 and z[:12]==z[12:24]==z[24:] and d[:12]==d[12:24]==d[24:]
    sector_norm=sum((norm(z[i])/d[i] for i in range(12)),R());full_norm=3*sector_norm
    L={(i,j):scale(1/sector_norm,mul(z[i],conj(z[j]))) for i in range(36) for j in range(36) if i//12==j//12}
    G={(i,j):(R(d[i]/3),R()) for i in range(36) for j in range(36) if i%12==j%12}
    N={(i,j):scale(1/full_norm,mul(z[i],conj(z[j]))) for i in range(36) for j in range(36)}
    ops=[L,G,N]
    retained=[{} for _ in ops]
    for row in store['arrows']:retained['LGN'.index(row['stage'])][row['target'],row['source']]=decode(row['numerator'])
    assert ops==retained
    assert sparse_product(G,L,d)==N and sparse_product(N,N,d)==N
    used=[set(),set(),set()];cycle_sum=Z;cycles=0
    for (i,k),g in G.items():
        for j in range(12*(k//12),12*(k//12+1)):
            w=scale(1/(d[j]*d[i]*d[k]),mul(N[j,i],mul(g,L[k,j])))
            assert w[1]==0 and w[0].b==0 and w[0].a>0
            cycle_sum=add(cycle_sum,w);cycles+=1
            used[0].add((k,j));used[1].add((i,k));used[2].add((j,i))
    assert cycle_sum==ONE and all(set(m)==s for m,s in zip(ops,used))
    arrows=[{'stage':name,'target':i,'source':j,'numerator':encoded(v)} for name,M in zip('LGN',ops) for (i,j),v in sorted(M.items())]
    assert [{(r['target'],r['source']):decode(r['numerator']) for r in arrows if r['stage']==name} for name in 'LGN']==ops
    assert energy['source_sha256']==hashes['results/native_operation_energy_lift_store.json']
    zero=next(t for t in energy['exact_trials'] if t['g']=='0')
    assert zero['twenty_one_seam_increment']=={'0':'21/4'}
    packet={'source':assembled['arrow_source'],'decoded_source':assembled['decoded_source'],
            'coordinates':store['coordinates'],'triangle_order':store['triangle_order'],'arrows':arrows,
            'coefficient_convention':'numerator_ij/sqrt(d_i*d_j); coefficients in Q(sqrt(2),i sqrt(3)); use denominator-aware composition',
            'measures':{'stage_supports':list(map(len,ops)),'transfers':sum(map(len,ops)),'complex_coordinates':36,'return_rank':1,'positive_closed_cycles':cycles,'cycle_weight_sum':'1','all_transfers_on_cycles':True},
            'native_bridge':reports['belt'],'occupation_certificate':energy,
            'scope':'Existing intrinsic three-sector native protocol reconstructed after source-mode binding. Ordered corners, character, intrinsic frame, sector grouping and occupation law remain supplied. No arrow-only coefficient derivation or mass calibration.'}
    out=ROOT/'research/strominger/results/neutron-arrow-native-bridge.json'
    bound=[source_path,Path(__file__).resolve(),ROOT/'research/strominger/checkers/assemble_real_complex_arrows.py',Path(bridge.__file__),Path(occupation.__file__),base/'checkers/check_belt_three_by_twelve.py',base/'checkers/assemble_relative_geometry.py',base/'checkers/evolve_relative_geometry_modes.py',bridge.SOURCE]+[base/n for n in names]
    packet['status']='passed';packet['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in bound}
    out.write_text(json.dumps(packet,indent=2)+'\n')
    print(json.dumps({'status':'passed','measures':packet['measures'],'native_energy_on_return':reports['belt']['native_constraint_energy_on_return'],
                      'seam_projectors':reports['belt']['source_grouping_seam_projectors'],'declared_occupation_increment':zero['twenty_one_seam_increment'],'shared_inputs_unchanged':True},indent=2))

if __name__=='__main__':main()
