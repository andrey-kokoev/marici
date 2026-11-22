"""Execute directly from two retained matchings, alternating lookup (no stored cycle or tour lookup). Compare exit-stop / first-return-stop / bounded continuation. Flags are reusable lookup data, not executed native events."""
from ramsey_seed_affine_witness import m,mate,P
from ramsey_first_fan_rim_probe import apex,X,D,json
from itertools import permutations
import sys
sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_seed_typed_execution import execute,validate,registry,compose
from check_seed_tour_family_transport import marked_reader

def run():
    seed=json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text());faces=[[a+b for a,b in zip(f,f[1:])] for f in seed['retained_face_cycles']];succ={e:f[(k+1)%3] for f in faces for k,e in enumerate(f)};out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        pair=[]
        for row,M,N in [('BRNN',m,mate),('BNRN',mate,m)]:
            forward=dict(M);back=dict((j,i) for i,j in N);x=0;v=None;prefix=();log=[];checkpoints={}
            for k in range(12):
                if k%2==0:
                    d=x;x=forward[x];
                    if v is None and apex(d)==row.index('R')+1:start=v=p[apex(d)-1]
                else:x=back[x];d=x
                if v is not None:
                    opts=[e for e,(s,t) in registry.items() if s==v and any({s,t}=={p[col-1] for col in X[h]} for h in P[d])];assert len(opts)<=1
                    if opts:
                        e,=opts;event=execute((e,));prefix=event if not prefix else next(iter(compose({prefix},{event})));v=registry[e][1];log.append((k+1,e))
                if k+1 in (5,10):checkpoints[k+1]=(x,len(prefix))
                if v is not None and v in {'C','D'}-{start}:break
            assert checkpoints[5]==(29,0) and checkpoints[10][0]==0 and checkpoints[10][1]<2 and len(prefix)==2
            a,b=[e[3] for e in prefix];suffix=execute((succ[b],succ[succ[b]],succ[a],succ[succ[a]]));receipt=validate(next(iter(compose({prefix},{suffix}))));assert receipt[:2]==prefix and {e[3] for e in receipt}==set(registry);pair.append(dict(row=row,stops=checkpoints,handoff=log,receipt=[e[3] for e in receipt],bit=marked_reader(receipt,p[0])))
        assert pair[0]['bit']!=pair[1]['bit'];out.append(dict(binding=''.join(p),rows=pair))
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_live_matching_receipt.json').write_text(json.dumps(out)+'\n')
