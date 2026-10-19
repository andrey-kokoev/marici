"""C10: exact depth-zero contraction obstruction for the fixed raw macro map."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/scattering/low-energy'
CANDIDATE=ROOT/'research/scattering/seed-composition/three-vertex-candidate.v1.json'
RESULT=HOME/'results/raw-macro-readout.v1.json'
PROOF=HOME/'RAW-MACRO-READOUT-OBSTRUCTION.md'


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def audit():
    candidate=json.loads(CANDIDATE.read_text(encoding='utf-8'))
    primitives={(a,b) for cycle in candidate['primitive_cycles'].values() for a,b in zip(cycle,cycle[1:])}
    composites={tuple(e['edge']):e['path'] for e in candidate['displayed_composites']}
    records=[]
    for support,pair in enumerate(candidate['displayed_triangle_pairs']):
        for triangle,cycle in enumerate(pair):
            for edge,(a,b) in enumerate(zip(cycle,cycle[1:])):
                word=composites.get((a,b),[a,b]);assert word[0]==a and word[-1]==b
                assert all((x,y) in primitives for x,y in zip(word,word[1:]))
                records.append({'support':support,'triangle':triangle,'edge':edge,'source':a,'target':b,'primitive_word':word})
    assert len(records)==12 and sum(len(r['primitive_word'])-1 for r in records)==18
    D=[[int(a['support']==b['support'] and a['target']==b['source']) for a in records] for b in records]
    degrees=[sum(row[a] for row in D) for a in range(12)]
    assert degrees==[1,2,2,1,2,2,1,2,2,1,2,2]
    # Histories retain their initial slot, so columns of A0 have disjoint supports.
    histories=[(a,b) for a in range(12) for b in range(12) if D[b][a]]
    assert len(histories)==len(set(histories))==20
    for a in range(12):assert sum((Fraction(1,degrees[a]) for x,y in histories if x==a),Fraction(0))==1
    witness=next(a for a,d in enumerate(degrees) if d>1)
    targets=[b for b in range(12) if D[b][witness]]
    assert witness==1 and targets==[2,3]
    # Exact hostile: deleting one allowed continuation changes the declared D.
    bad=[row[:] for row in D];bad[targets[0]][witness]=0
    assert bad!=D and sum(row[witness] for row in bad)==1
    paths=[CANDIDATE,PROOF,Path(__file__),HOME/'C8-MACRO-CONTROLLER.md',HOME/'SPECTRAL-AND-HISTORY-CONJECTURES.md']
    return {'schema':'marici.scattering.raw-macro-readout.v1','status':'pass','C10_disposition':'refuted',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'records':records,'D':D,'column_norms_squared':degrees,'one_step_history_count':len(histories),
            'A0_column_norms_squared':['1']*12,'A0_columns_have_disjoint_history_support':True,
            'witness':{'input_slot':witness,'input_record':records[witness],'output_slots':targets,
                       'input_norm_squared':1,'A0_input_norm_squared':1,'D_input_norm_squared':2},
            'deduction':'R1 A0=D R0=D with R0=I would give ||D e1||<=||A0 e1||=1, but ||D e1||²=2. Hence no required family of contractions exists.',
            'minimal_obstruction_depth':0,'delete_branch_control':'changes the specified map, not a remedy within C10',
            'all_retained_constructions_refuted':False,'physical_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale C10 certificate'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: C10 refuted at depth zero, exact squared norms 2 > 1; richer construction classes not excluded.')


if __name__=='__main__':main()
