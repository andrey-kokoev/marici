"""Compare tetrahedral 12/3 incidence with exact native image-channel maps."""
from itertools import permutations, combinations
from fractions import Fraction
from pathlib import Path
import json, hashlib
from assemble_metric_coefficient_protocol import read_operator, ZERO, ONE
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'

def rank(m,nrows,ncols):
    a=[[m.get((i,j),ZERO) for j in range(ncols)] for i in range(nrows)];k=0
    for j in range(ncols):
        pivot=next((i for i in range(k,nrows) if a[i][j]!=ZERO),None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k];s=a[k][j].inverse();a[k]=[x*s for x in a[k]]
        for i in range(k+1,nrows):
            if a[i][j]!=ZERO:
                t=a[i][j];a[i]=[x-t*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==nrows:break
    return k
# Twelve face/corner flags: omitted face vertex i, chosen corner j != i.
flags=list(permutations(range(4),2))
canon=lambda pairs:tuple(sorted(tuple(sorted(p)) for p in pairs))
partitions=sorted({canon([(0,j),tuple(i for i in range(4) if i not in (0,j))]) for j in (1,2,3)})
def quotient(flag):return partitions.index(canon([flag,tuple(i for i in range(4) if i not in flag)]))
Q={(quotient(f),j):ONE for j,f in enumerate(flags)};QT={(j,i):v for (i,j),v in Q.items()}
assert rank(Q,3,12)==rank(QT,12,3)==3
for p in permutations(range(4)):
    for f in flags:
        transformed=canon([tuple(p[i] for i in pair) for pair in partitions[quotient(f)]])
        assert partitions[quotient(tuple(p[i] for i in f))]==transformed
# S4 acts on matching/flag pairs with two orbits: incidence vs nonincidence.
pairs=list(__import__('itertools').product(range(3),range(12)));orbits=[];remaining=set(pairs)
while remaining:
    m,j=min(remaining);orbit=set()
    for p in permutations(range(4)):
        mm=partitions.index(canon([tuple(p[i] for i in pair) for pair in partitions[m]]));jj=flags.index(tuple(p[i] for i in flags[j]));orbit.add((mm,jj))
    remaining-=orbit;orbits.append(orbit)
assert sorted(map(len,orbits))==[12,24]
# Other equally symmetric scalar maps demonstrate that symmetry does not
# select the native rank-one transfer.
uniform={(i,j):ONE for i in range(3) for j in range(12)};assert rank(uniform,3,12)==1
path=BASE/'port-incidence-conjectures-v1.json';b=path.read_bytes();saved=json.loads(b);native={}
for species,row in saved['native_stage_interfaces'].items():
    inter=row['image_interface'];m=read_operator(inter['matrix'],max(inter['incoming'],inter['outgoing']));actual=rank(m,inter['outgoing'],inter['incoming']);assert actual==inter['transfer_rank'];native[species]={'incoming':inter['incoming'],'outgoing':inter['outgoing'],'exactRank':actual,'nonzeroCoefficients':len(m)}
assert native['proton']['exactRank']==native['neutron']['exactRank']==1;assert native['electron']['exactRank']==2
sector=saved['electron_sector_interface'];assert len(sector['ports'])==12
assert {(p['omitted_axis'],tuple(p['signs'])) for p in sector['ports']}=={(a,(s,t)) for a in range(3) for s in (-1,1) for t in (-1,1)}
out=BASE/'T-channel-incidence';out.mkdir(exist_ok=True)
result={'status':'geometric-incidence-versus-native-channels-tested','tetrahedron':{'flags':flags,'oppositeEdgePartitions':partitions,'flagToPartition':[quotient(f) for f in flags],'fiberSizes':[sum(quotient(f)==i for f in flags) for i in range(3)],'incidenceRank':3,'transposeRank':3,'incidenceNonzeros':len(Q),'equivarianceChecks':24*12,'equivariantMatrixOrbits':sorted(map(len,orbits)),'uniformAlternativeRank':1},'nativeImages':native,'electronSectorInterface':{'ports':len(sector['ports']),'fixedAxisSignDictionary':True,'orderedPairs':sector['ordered_pairs'],'distinctFrameMatrices':sector['distinct_frame_matrices'],'distinctTransferMatrices':sector['distinct_transfer_matrices']},'sourceSha256':{str(path.relative_to(ROOT)):hashlib.sha256(b).hexdigest()},'checkerSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'conclusion':'T facets canonically provide a 12-flag/3-partition incidence and its reverse, but that rank-3 map is not the rank-1 native baryon map. A different equally symmetric uniform map has rank 1, so geometry/symmetry does not select the source transfer. Electron 12 sectors are chart labels, while its image map is 4->2 of rank 2. A field/projector/metric law is needed to derive these together. No generator/viewer change.'}
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'geometricRanks':[3,3],'native':native,'electronPorts':len(sector['ports']),'equivariantMatrixOrbits':sorted(map(len,orbits))}))
