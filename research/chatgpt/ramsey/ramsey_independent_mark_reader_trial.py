"""Use the pre-existing marked_reader verbatim. Whole-tour rotations versus recutting each closed triangle before sewing; retain the same six event objects. Mark is the reader's existing A/B argument, not an edited event endpoint."""
from pathlib import Path
import sys,json
D=Path(__file__).resolve().parent;sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_seed_tour_family_transport import marked_reader,seam,seed

def run():
    p,q=seed.paths[:2];original=p+q;issued=dict(seed.emitted);results={}
    for intervention in ('rotate_tour','resew_triangles'):
        raw=[];seams=[];words=[]
        for start,mark in [('A','A'),('B','A'),('A','B'),('B','B')]:
            tour=original if start=='A' else (original[1:]+original[:1] if intervention=='rotate_tour' else p[1:]+p[:1]+q[2:]+q[:2]);seed.validate(tour);assert tour[0][0]==start and {id(e) for e in tour}=={id(e) for e in original};raw.append(marked_reader(tour,mark));seams.append(seam(tour));words.append([e[3] for e in tour]);
        results[intervention]=dict(raw=raw,changes=[v^raw[0] for v in raw],seams=seams,words=words)
    assert seed.emitted==issued;return results
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_independent_mark_reader_trial.json').write_text(json.dumps(out)+'\n')
