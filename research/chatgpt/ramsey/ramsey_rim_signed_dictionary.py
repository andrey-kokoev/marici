"""Compare the even powers of the antiunitary rim lift to the actual signed electron packet dictionary. Replay only admitted linear operations, not a fictitious archive of antiunitary steps."""
from ramsey_electron_anti_quarterturn import D,json,decode,A,ONE,product
from electron_packet_interface import E,I,sm,Interface,G1,G0,adj,gmm

def as_op(m):return {(i,j):decode({'0':str(x),'8':str(y)}) for i,row in enumerate(m) for j,(x,y) in enumerate(row) if x or y}
def run():
    data=json.loads((D/'ramsey_electron_anti_quarterturn.json').read_text());h=decode({'1':'1/2'});gates={'H':{(0,0):h,(1,0):h,(0,1):h,(1,1):-h},'S':{(0,0):ONE,(1,1):decode({'8':'1'})}};f=Interface();seed=f.seed((G1,G0));out=[]
    for r in data:
        U=as_op(I)
        for ch in r['apply_before_K'].split(': ')[1]:U=product(gates[ch],U)
        sq=product(U,{k:z.flip(8) for k,z in U.items()});axis,sign,e=next((i+1,s,sm(s,m)) for i,m in enumerate(E) for s in (1,-1) if as_op(sm(s,m))==sq);z=sm(-1,I);assert gmm(e,e)==z
        two=f.source_step(seed,e);four=f.source_step(two,e);direct=f.source_step(seed,z);assert four.raw==direct.raw!=seed.raw and four.archive.word!=direct.archive.word;back=f.source_step(four,z);assert back.raw==seed.raw and back.archive!=seed.archive;relative=gmm(adj(f.raw_actions[I]),f.raw_actions[z]);assert relative==sm(-1,f.N);out.append(dict(binding=r['binding'],faces=r['face_permutation'],axis=axis,sign=sign,relative='-N',corrected='N'))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_rim_signed_dictionary.json').write_text(json.dumps(out)+'\n')
