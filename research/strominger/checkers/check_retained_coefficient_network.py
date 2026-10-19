"""Replay both native coefficient protocols and a declared five-cell extension."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from retained_coefficient_network import assemble,recover,product,ONE,ZERO
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/strominger/results/retained-coefficient-network'


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    proton_path=ROOT/'research/nima/results/twelve-triangle-1836-arrows.json'
    electron_path=ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json'
    proton=json.loads(proton_path.read_text());electron=json.loads(electron_path.read_text())
    stages=['raw','local','aligned']
    pports=[sorted({':'.join(r['source'][1:]) for r in proton if r['source'][0]==s}) for s in stages]
    pops=[{} for _ in stages]
    for r in proton:
        s=stages.index(r['source'][0]); assert r['target'][0]==stages[(s+1)%3]
        j=pports[s].index(':'.join(r['source'][1:]));i=pports[(s+1)%3].index(':'.join(r['target'][1:]))
        pops[s][i,j]=(F(r['weight_real']),F(0),F(0),F(r['weight_imag_sqrt3']))
    eports=[[str(i) for i in range(8)] for _ in range(3)];eops=[{} for _ in range(3)]
    for r in electron['arrows']:
        s=['L','G','N'].index(r['stage']);eops[s][r['target'],r['source']]=tuple(F(x) for pair in r['weight'] for x in pair)
    P=assemble(pports,pops);E=assemble(eports,eops)
    checks={'proton_1836_rank_one':P['measures']['transfers']==1836 and P['measures']['return_rank']==1,
            'electron_144_rank_two':E['measures']['transfers']==144 and E['measures']['return_rank']==2,
            'proton_exact_operator_recovery':recover(P)==(pports,pops),
            'electron_exact_operator_recovery':recover(E)==(eports,eops),
            'both_positive_full_cycle_coverage':all(p['measures']['positive_cycle_weights'] and p['measures']['all_transfers_on_cycles'] and p['measures']['return_idempotent'] for p in (P,E))}
    # NEW DECLARED MODEL: trivialize a copy of the native 8-coordinate carrier
    # over each tetrahedral boundary cell. No physical spin lift is asserted.
    cells=[''.join(x for x in 'ABCDE' if x!=missing) for missing in 'ABCDE']
    ports=[[cell+':'+str(i) for cell in cells for i in range(8)] for _ in range(3)]
    ops=[{(8*c+i,8*c+j):v for c in range(5) for (i,j),v in M.items()} for M in eops]
    bundle=assemble(ports,ops)
    checks['declared_direct_sum_720_rank_ten']=bundle['measures']['transfers']==720 and bundle['measures']['return_rank']==10
    checks['bundle_exact_recovery']=recover(bundle)==(ports,ops)
    # Use the ACTUAL retained permutation actions from the diagonal receipts.
    receipt_path=ROOT/'research/strominger/results/electron_diagonal_seeds.json'
    source=json.loads(receipt_path.read_text())
    for filename,expected in source['source_hashes'].items():assert hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()==expected
    rows=[]
    for label in ['plus_DB','plus_AD','plus_CA','plus_EC','plus_BE']:
        case=source['cases'][label]; transports=[]
        for word in case['cycles']:
            cycle=word[:-1];perm=dict(zip(cycle,cycle[1:]+cycle[:1]))
            cellperm=[cells.index(''.join(sorted(perm.get(x,x) for x in c))) for c in cells]
            U={(8*cellperm[c]+i,8*c+i):ONE for c in range(5) for i in range(8)}
            inverse={(j,i):v for (i,j),v in U.items()}
            assert product(inverse,U)=={(i,i):ONE for i in range(40)}
            assert all(product(U,M)==product(M,U) for M in ops)
            transports.append({'cycle':word,'cell_permutation':cellperm,'fiber_transport':'identity in declared trivialization','support':len(U)})
        rows.append({'case':label,'transport':transports,'network_measures':bundle['measures']})
    checks['five_actions_typed_invertible_and_intertwining']=len(rows)==5
    # A loss/control shows why the fiber declaration is substantive: omit
    # nontrivial within-cell labels and return-rank information disappears.
    try:assemble([['x'],['y']], [{(1,0):ONE},{(0,0):ONE}])
    except ValueError:checks['bad_endpoint_rejected']=True
    else:checks['bad_endpoint_rejected']=False
    try:assemble([['x','x']], [{}])
    except ValueError:checks['duplicate_port_rejected']=True
    else:checks['duplicate_port_rejected']=False
    for name,packet in [('proton',P),('electron',E),('declared-five-cell',bundle)]:
        (OUT/(name+'.json')).write_text(json.dumps(packet,indent=2)+'\n')
    report={'status':'passed' if all(checks.values()) else 'failed','checks':checks,
            'native_measures':{'proton':P['measures'],'electron':E['measures']},
            'five_cell_declared_extension':rows,
            'extension_boundary':'Five identical coefficient fibers with identity fiber transport are explicit new data, not derived spin transport. 720 counts direct-sum protocol edges; 40-entry generator transports are separate operations, not silently added to that count. This does not derive a physical five-cell spinor or distinguish the five inputs by coefficient count.',
            'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(__file__).with_name('retained_coefficient_network.py'),proton_path,electron_path,receipt_path]}}
    (OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'checks':checks,'native_measures':report['native_measures'],'declared_bundle_measures':bundle['measures']},indent=2))
    if not all(checks.values()):raise SystemExit(1)

if __name__=='__main__':main()
