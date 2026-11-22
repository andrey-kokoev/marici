"""Append to the two issued handoff events using only per-face successors. No lookup of a precomputed tour to construct the suffix. The original mark reader is applied after execution."""
from ramsey_flag_online_first_hit import run as traces,D,json
import sys
sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_seed_typed_execution import execute,validate,compose,registry
from check_seed_tour_family_transport import marked_reader,seam

def run():
    manifest=json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text());faces=[[a+b for a,b in zip(f,f[1:])] for f in manifest['retained_face_cycles']];succ={e:f[(k+1)%len(f)] for f in faces for k,e in enumerate(f)};records=[]
    for bind in traces():
        rows=[]
        for row in bind['rows']:
            h=tuple(step[0] for step in row['reads'] if step);a,b=h;base=registry[a][1];prefix=validate(execute(h));suffix=(succ[b],succ[succ[b]],succ[a],succ[succ[a]])
            path=validate(next(iter(compose({prefix},{execute(suffix)}))));assert path[:2]==prefix and len(path)==6 and path[0][0]==path[-1][1] and {e[3] for e in path}==set(registry);assert seam(path)==base
            # Negative control: greedily sticking to the receiving face on a third successor would reuse b, not close the cover.
            assert succ[suffix[1]]==b and registry[suffix[1]][1]==base==registry[suffix[2]][0];rows.append(dict(handoff=h,append=suffix,base=base,bit=marked_reader(path,bind['binding'][0])))
        assert rows[0]['bit']!=rows[1]['bit'];records.append(dict(binding=bind['binding'],rows=rows))
    return records
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_resume_handoff_receipt.json').write_text(json.dumps(out)+'\n')
