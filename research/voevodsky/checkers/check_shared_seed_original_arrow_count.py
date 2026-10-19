"""Fresh original-convention count, not compiler instructions or geometric edges.
Run the two owning source checkers unmodified in an isolated output directory,
then independently enumerate the full positive closed-return arrow support.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from fractions import Fraction as F
from collections import Counter,defaultdict
from hashlib import sha256
import contextlib,io,json,runpy,sys

ROOT=Path(__file__).resolve().parents[3]
OWNER=ROOT/'research/nima'
sys.path.insert(0,str(OWNER/'checkers'))
from check_triangle_half_phase import zmul
from check_twelve_triangle_positive_geometry import rotation,det

OUT=ROOT/'research/voevodsky/results/shared_seed_original_arrow_count.v1.json'
SOURCE_SCRIPTS=('check_twenty_four_triangle_shared_seed.py','check_pair_arrow_ledger.py')

def certify(records):
    edges={};stages=Counter();partitions=Counter();incoming=defaultdict(list)
    next_stage={'raw':'local','local':'aligned','aligned':'raw'}
    def side(port):
        p=tuple('ABCD'.index(c) for c in port[1]);return 1 if det(rotation(p))==1 else -1
    for record in records:
        a,b=tuple(record['source']),tuple(record['target']);weight=F(record['real']),F(record['imag_sqrt3'])
        assert (a,b) not in edges,'duplicate primitive endpoints'
        assert a!=b and b[0]==next_stage[a[0]],'wrong primitive port types'
        assert weight!=(0,0),'zero is not a transfer arrow'
        edges[a,b]=weight;stages[a[0]]+=1;incoming[b].append(a)
        partitions['between_bodies' if side(a)!=side(b) else 'body_A' if side(a)==1 else 'body_B']+=1
    assert stages=={'raw':216,'local':1728,'aligned':5184}
    assert partitions=={'body_A':1836,'body_B':1836,'between_bodies':3456}
    ports={p for edge in edges for p in edge}
    assert len(ports)==216 and all(sum(p[0]==s for p in ports)==72 for s in next_stage)
    used=set();cycle_count=0;total=F(0);deletion_loss=defaultdict(F)
    for (aligned,raw),closing in edges.items():
        if aligned[0]!='aligned':continue
        paths=[(local,edges[raw,local],edges[local,aligned]) for local in incoming[aligned] if (raw,local) in edges]
        assert len(paths)==1,'dense closing edge must have its exact source return path'
        local,w0,w1=paths[0];weight=zmul(zmul(w0,w1),closing)
        assert weight[1]==0 and weight[0]>0
        cycle=((raw,local),(local,aligned),(aligned,raw))
        used.update(cycle);cycle_count+=1;total+=weight[0]
        for e in cycle:deletion_loss[e]+=weight[0]
    assert used==set(edges) and cycle_count==5184 and total==1
    assert set(deletion_loss)==set(edges) and min(deletion_loss.values())>0
    # The source's count is the union of primitive endpoint arrows in the
    # complete return, not 3 times the number of cycles or an execution length.
    return {'primitive_arrow_count':len(edges),'port_configuration_count':len(ports),
        'stage_counts':dict(stages),'body_partition':dict(partitions),
        'positive_three_step_cycles':cycle_count,'return_trace':'1',
        'every_arrow_in_closed_return':True,'minimum_single_arrow_trace_loss':str(min(deletion_loss.values())),
        'fixed_weight_pruning_minimal':True,'unrestricted_minimality_claimed':False}

def main():
    with TemporaryDirectory(prefix='shared-seed-original-count-') as temp:
        sandbox=Path(temp);(sandbox/'checkers').mkdir();(sandbox/'results').mkdir()
        outputs=[]
        for name in SOURCE_SCRIPTS:
            source=OWNER/'checkers'/name;copy=sandbox/'checkers'/name;copy.write_bytes(source.read_bytes())
            assert copy.read_bytes()==source.read_bytes()
            with contextlib.redirect_stdout(io.StringIO()) as stream:
                runpy.run_path(str(copy),run_name='__main__')
            outputs.append(stream.getvalue().strip())
        construction=json.loads((sandbox/'results/twenty-four-triangle-shared-seed.json').read_text())
        ledger=json.loads((sandbox/'results/pair-arrow-ledger.json').read_text())
        raw=(sandbox/'results/pair-dense-7128-arrows.json').read_bytes();records=json.loads(raw)
        proof=certify(records)
        assert construction['seed_arrows']==['AB','AD','BA','BC','CA','DB']
        assert construction['audit_assertions_passed'] and ledger['audit_assertions_passed']
        assert proof['primitive_arrow_count']==ledger['dense_1836_convention']['unique_arrows']
        # Bind the independently replayed source record, not our discarded
        # record-instruction convention. Existing source outputs stay untouched.
        assert raw==(OWNER/'results/pair-dense-7128-arrows.json').read_bytes()
        files=[OWNER/'checkers'/name for name in SOURCE_SCRIPTS]+[
            OWNER/'checkers/check_twelve_triangle_positive_geometry.py',OWNER/'checkers/check_triangle_half_phase.py',
            OWNER/'checkers/check_collective_four_state_identity.py',OWNER/'results/pair-dense-7128-arrows.json',Path(__file__)]
        result={'schema':'marici.voevodsky.original-arrow-count.v1','verification_passed':True,
            'seed_arrows':construction['seed_arrows'],'seed_cycles':construction['seed_cycles'],
            'construction':'shared-seed two-body area-packet realization with the original local/alignment/dense-return architecture',
            'primitive':'one nonzero coefficient-transfer arrow between distinct typed (stage, triangle, coordinate) endpoints, counted once',
            'counting_convention_changed':False,'compiler_instruction_count_included':False,
            'full_three_stage_support':proof,'dense_records_sha256':sha256(raw).hexdigest(),
            'original_checker_outputs':outputs,'original_files_rewritten':False,
            'scope':'Full 7128-arrow support of this specified original-convention construction. Not a claim that the bare seed uniquely selects the architecture, not a scalar-arithmetic construction cost, and not an independent physical mass calibration.',
            'source_hashes':{p.resolve().relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in files}}
        OUT.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(proof,indent=2))

if __name__=='__main__':main()
