"""Analyze the saved exact kernels without redoing the large eliminations."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
from check_fcc_gaussian_boundary import BASE, OUT, mesh, vertices, action, distance

def decode(data):
    values=list(map(Q,data['values']))
    return [[values[i] for i in row] for row in data['matrix']]

def main():
    receipt=json.loads((OUT/'verification.json').read_text()); assert receipt['status']=='pass'
    assert receipt['sourceHash']==hashlib.sha256((BASE/'checkers/check_fcc_gaussian_boundary.py').read_bytes()).hexdigest()
    cells=mesh(4,'O'); center=(4,4,4); neighbor=(5,5,4)
    assert sum(center in c for c in cells)==14
    assert sum(center in c and neighbor in c for c in cells)==4
    rows=[]
    for kind in ('T','O'):
        base=vertices(mesh(1,kind))
        for level in range(4):
            path=OUT/f'{kind}-level-{level}.json'; data=json.loads(path.read_text())
            s=decode(data['inheritedPorts']['kernel']); n=2**level
            adjacent=[s[i][j] for i in range(len(base)) for j in range(i) if distance(base[i],base[j])==2]
            spring=-4*adjacent[0]; mass=14*sum(s[0])
            family=[[mass*Q(i==j,14)+spring*Q((3 if kind=='T' else 4) if i==j else (-1 if distance(base[i],base[j])==2 else 0),4)
                     for j in range(len(base))] for i in range(len(base))]
            fit=s==family
            opposite=[s[i][j] for i in range(len(base)) for j in range(i) if distance(base[i],base[j])==4]
            if kind=='T': assert fit
            if kind=='O': assert fit==(level==0)
            norm=data['inheritedPorts']['normalization']
            if level: assert norm['twoPiPower']>0
            # Defined logical storage proxy, not measured optimal compression.
            bit_proxy=data['dictionaryBitCost']+data['indexBitsUpperBound']+data['determinantBitCost']
            rows.append({'grain':kind,'level':level,'boundaryDOF':data['boundaryDOF'],
                         'nonzeroUpperEntries':data['nonzeroUpperEntries'],
                         'distinctRationalEntries':data['distinctRationalEntries'],
                         'maxEntryBitCost':data['maxEntryBitCost'],
                         'logicalEncodingBitProxy':bit_proxy,
                         'logicalEncodingBitsPerBoundaryDOF':str(Q(bit_proxy,data['boundaryDOF'])),
                         'jsonArtifactBytes':path.stat().st_size,
                         'inheritedPortNearestNeighborFamilyClosed':fit,
                         'fittedMassSquared':str(mass) if fit else None,
                         'fittedSpring':str(spring) if fit else None,
                         'inheritedOppositeCoupling':str(opposite[0]) if opposite else None,
                         'inheritedKernel':data['inheritedPorts']['kernel'],
                         'inheritedNormalization':norm})
    result={'schema':'marici.fcc-gaussian-boundary-analysis.v1','status':'pass',
            'sourceHashes':{str(p.relative_to(BASE.parents[1])):hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in (Path(__file__),BASE/'checkers/check_fcc_gaussian_boundary.py',OUT/'verification.json')},
            'ownershipIncidenceChecks':{'interiorVertexCells':14,'interiorEdgeCells':4},
            'bitProxyDefinition':'sum bit lengths of distinct rational entries + fixed-width upper-triangle dictionary indices + determinant bit length; excludes geometry, two-pi count, dictionary metadata, and program; not minimal complexity',
            'rows':rows,
            'disposition':'T fixed-corner two-parameter closure is forced by full tetrahedral symmetry and is not full-interface recursive closure. O fails even fixed-corner nearest-neighbor closure at level 1. Neither the finite dictionary nor its bit proxy proves an indefinite-scale law.'}
    (OUT/'analysis.json').write_text(json.dumps(result,indent=2)+'\n')
    print('grain level boundary nonzeroUpper unique maxEntryBits encodingBitProxy NN-family')
    for r in rows: print(*(r[k] for k in ('grain','level','boundaryDOF','nonzeroUpperEntries','distinctRationalEntries','maxEntryBitCost','logicalEncodingBitProxy','inheritedPortNearestNeighborFamilyClosed')))

if __name__=='__main__':main()
