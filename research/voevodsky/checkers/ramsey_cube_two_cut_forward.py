"""Identify a found route in the predecessor catalogue; replay in catalogue labels."""
from ramsey_cube_retention_floor import G,D,CAT,decode,json,induced,iso,deg,wl
from ramsey_retention_slice import check
import gzip

def audit():
    cases=json.loads((D.parent/'ramsey_cube_two_cut_joint.json').read_text())['cases'];r=min((r for r in cases if r['wins']),key=lambda r:len(r['witness'][1]));V=json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];core=induced(G,V);s,adds,_=r['witness'];a=core[:]+[s];cuts=r['cuts']
    for i in range(26):a[i]|=(s>>i&1)<<26
    for i,j in cuts+adds:a[i]^=1<<j;a[j]^=1<<i
    assert check(a,(1<<27)-1,3,8);e=sum(v.bit_count() for v in a)//2;d=deg(a);sig=wl(a);w=bytes([(j-63).bit_count() if 63<=j<=126 else 0 for j in range(256)])
    for idx,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')):
        st=l.strip()
        if sum(st[1:].translate(w))!=e:continue
        b=decode(st.decode());
        if deg(b)!=d or wl(b)!=sig:continue
        f=iso(a,b)
        if f is None:continue
        flip=lambda ls:[[f[i],f[j]] for i,j in ls];remove=flip(adds);put=flip(cuts);c=b[:];
        for i,j in remove:assert c[i]>>j&1;c[i]^=1<<j;c[j]^=1<<i
        for i,j in put:assert not c[i]>>j&1;c[i]|=1<<j;c[j]|=1<<i
        assert induced(c,f[:26])==core;out=dict(record_zero_based=idx,deleted=f[26],remove=remove,add=put,retained_to_cube=list(zip(f[:26],V)));print(out);(D.parent/'ramsey_cube_two_cut_forward.json').write_text(json.dumps(out,indent=2)+'\n');return
    raise AssertionError('missing catalogue match')
if __name__=='__main__':audit()
