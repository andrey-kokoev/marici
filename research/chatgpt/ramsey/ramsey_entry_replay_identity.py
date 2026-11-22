"""Distinguish reconstructed Hall flag values, freshly emitted native events, and provenance the native validator never receives. Use only the entry/current flags to choose the handoff."""
import sys
from ramsey_folded_entry_handoff import X,P,T,D,json,permutations
sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_seed_typed_execution import registry,execute,validate
from check_seed_tour_family_transport import marked_reader

def run():
    man=json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text());faces=[[a+b for a,b in zip(f,f[1:])] for f in man['retained_face_cycles']];succ={e:f[(i+1)%3] for f in faces for i,e in enumerate(f)};out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        rows=[]
        for row,j,k,d in [('BRNN',16,19,7),('BNRN',17,27,4)]:
            incoming,=set(T[j-15])&set(T[k-15]);flags={1:0,3:P.index(incoming),4:d};support={s:{e for e in registry if any(set(e)=={p[v-1] for v in X[h]} for h in P[i])} for s,i in flags.items()};tail=p[row.index('R')];head,={'C','D'}-{tail};fits=[(a,b,i,l) for i,l in [(1,4),(4,3)] for a in support[i] for b in support[l] if a[0]==tail and a[1]==b[0] and b[1]==head];(a,b,i,l),=fits;word=(a,b,succ[b],succ[succ[b]],succ[a],succ[succ[a]]);x,y=[validate(execute(word)) for _ in range(2)];assert {e[2] for e in x}.isdisjoint(e[2] for e in y);mark=p[0];bit=marked_reader(x,mark);assert bit==marked_reader(y,mark)
            # The flag value is a pair, not an issued native event ID.
            try:validate(((x[0][0],x[0][1],(flags[i],j),a),)+x[1:])
            except ValueError:pass
            else:raise AssertionError('unissued ID accepted')
            rows.append(dict(row=row,source_slots=[i,l],word=word,bit=bit,replay_ids_disjoint=True))
        assert rows[0]['bit']!=rows[1]['bit'];out.append(dict(binding=''.join(p),rows=rows))
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_entry_replay_identity.json').write_text(json.dumps(out)+'\n')
