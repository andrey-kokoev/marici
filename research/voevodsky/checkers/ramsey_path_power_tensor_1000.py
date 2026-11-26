"""Exact arbitrary-width version of ramsey_path_power_tensor_26.py. Compress equal-capacity singleton footprints, and retain only the smallest nested prefix at each capacity. No extrapolation of bands. CSV is gzip-compressed; PNG uses standard library."""
import csv,gzip,struct,zlib,collections
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results'

def cell(l,k):
 if l==1 or k==1:return '-',None,None
 if l==2 and k>2:return 'x',None,None
 n=(l-1)*(k-2);h,r=divmod(n,l);colors=(1<<l)-1;full=(1<<(l+1))-1;first=(1<<r)-1;ends=(1,1<<(l-1));data=[]
 for root in ends:
    groups=[]
    for mask,v in [(first,h+1),(colors^first,h)]:
        if mask&root:groups.append((root,k-1-v))
        if mask&~root:groups.append((mask&~root,k-2-v))
    # Non-singleton prefixes contain both root labels. Greedy independent-set position j (0-based) is j*l-min(j,t) for a prefix of length t+1 < l. Hence only t=1 and the first rise in ceil((n+t)/l) matter. Full footprint must also be checked. Include empty footprint for newcomer-only blue cliques.
    prefs=[(0,k-2),(colors,k-1-(k-2))]
    for t in {1,l-r+1 if r else 1}:
        if 1<=t<l-1:
            f=1|(((1<<t)-1)<<(l-t));alpha=min(k-2,(n+t+l-1)//l);prefs.append((f,k-1-alpha))
    data.append((groups,prefs))
 def feasible(q,allowed,cs):
    if q>allowed.bit_count():return False
    forced=0
    for mask,cap in cs[0]:
        if q>cap+1:return False
        if q>cap:forced|=mask
    left=q-forced.bit_count()
    if left<0 or forced&~allowed:return False
    avail=allowed&~forced
    # The prefix constraints can be satisfied simultaneously by filling in nested-prefix order.
    for f,cap in cs[1]:
        if q-cap>(forced&f).bit_count()+min(left,(avail&f).bit_count()):return False
    return True
 ds=[];rep=[]
 for i,cs in enumerate(data):
    # Only the two singleton endpoint footprints have capacities differing by root. The other endpoint is the tighter singleton for this root.
    other=ends[1-i];q=k-1-(h+int(bool(other&first)))
    if feasible(q,full^other,data[1-i]):ds.append(q)
    lo,hi=0,l+2
    while hi-lo>1:
        mid=(hi+lo)//2
        if feasible(mid,full,cs):lo=mid
        else:hi=mid
    rep.append(l+1-lo)
 return str(min(ds)) if ds else '=',*rep

def png(path,pixels,n):
 def chunk(k,b):return struct.pack('>I',len(b))+k+b+struct.pack('>I',zlib.crc32(k+b))
 import colorsys
 pal=[(245,245,245),(120,120,120),(220,220,220)]+[tuple(round(255*x) for x in colorsys.hsv_to_rgb(.64*(1-min(i,32)/32),.85,min(1,.68+i/110))) for i in range(1,128)]
 path.write_bytes(b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>2I5B',n,n,8,3,0,0,0))+chunk(b'PLTE',bytes(x for c in pal[:128] for x in c))+chunk(b'IDAT',zlib.compress(b''.join(b'\0'+pixels[j:j+n] for j in range(0,len(pixels),n)),9))+chunk(b'IEND',b''))
if __name__=='__main__':
 old={(int(z['l']),int(z['k'])):(z['first_difference'],z['repair_A'],z['repair_C']) for z in csv.DictReader((D/'ramsey_path_power_tensor_grid_100.csv').open())};hist=collections.Counter();pix=bytearray();best=0;at=[]
 with gzip.open(D/'ramsey_path_power_tensor_grid_1000.csv.gz','wt',newline='') as fp,(D/'ramsey_path_power_tensor_bands_1000.csv').open('w',newline='') as bf:
    w=csv.writer(fp);w.writerow(['l','k','first_difference','repair_A','repair_C']);bw=csv.writer(bf);bw.writerow(['l','first_k','last_k','first_difference']);
    for l in range(1,1001):
        prev=None
        for k in range(1,1001):
            t,a,c=cell(l,k);w.writerow((l,k,t,a,c));hist[t]+=1;pix.append({'-':0,'x':1,'=':2}.get(t,0) if not t.isdigit() else 2+int(t));
            if (l,k) in old:assert old[l,k]==(t,'' if a is None else str(a),'' if c is None else str(c)),(l,k,old[l,k],t,a,c)
            if t!=prev:
                if prev is not None:bw.writerow([l,start,k-1,prev]);
                start=k;prev=t
            if t.isdigit() and int(t)>=best:
                if int(t)>best:best=int(t);at=[]
                at.append((l,k))
        bw.writerow([l,start,1000,prev]);
 png(D/'ramsey_path_power_tensor_grid_1000.png',pix,1000);print(hist);print('max',best,'cells',at)
