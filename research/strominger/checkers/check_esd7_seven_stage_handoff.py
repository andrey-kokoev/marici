"""Read-only extraction and signed rotation audit of the prior esd7 census."""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
SOURCE='research/voevodsky/results/esd7_explicit_analytical_census.json'


def main():
    data=json.loads((ROOT/SOURCE).read_text(encoding='utf-8'))
    checks=[]
    def check(name,condition):
        if not condition: raise AssertionError(name)
        checks.append(name)
    vertices={r['id']:tuple(r['cumulative']) for r in data['vertices']}
    def bary(z):return (z[0],z[1]-z[0],z[2]-z[1],7-z[2])
    def cumulative(a):return (a[0],a[0]+a[1],a[0]+a[1]+a[2])
    def rho(z):
        a=bary(z);return cumulative((a[3],a[0],a[1],a[2]))
    cells={}
    for dim,kind in enumerate(['vertices','edges','triangles','tetrahedra']):
        for r in data[kind]:
            vs=(vertices[r['id']],) if dim==0 else tuple(sorted(vertices[v] for v in r['vertices']))
            cells[r['id']]={'id':r['id'],'dimension':dim,'vertices':vs}
    lookup={c['vertices']:id for id,c in cells.items()}
    check('prior geometric f vector', [sum(c['dimension']==d for c in cells.values()) for d in range(4)]==[120,560,784,343])
    for c in cells.values():
        vs=c['vertices']
        c['boundary']=[] if c['dimension']==0 else [(lookup[vs[:i]+vs[i+1:]],(-1)**i) for i in range(len(vs))]
        rotated=[rho(v) for v in vs]
        c['rho']=lookup[tuple(sorted(rotated))]
        c['rho_sign']=(-1)**sum(rotated[i]>rotated[j] for i in range(len(vs)) for j in range(i+1,len(vs)))
    def coefficients(terms):
        out=defaultdict(int)
        for id,sign in terms:out[id]+=sign
        return {id:sign for id,sign in out.items() if sign}
    check('signed boundary squared vanishes on all cells',all(not coefficients((g,s*t) for f,s in c['boundary'] for g,t in cells[f]['boundary']) for c in cells.values()))
    check('quarter-chart action commutes with signed boundaries on all 1807 cells',all(
        coefficients((f,c['rho_sign']*s) for f,s in cells[c['rho']]['boundary']) ==
        coefficients((cells[f]['rho'],s*cells[f]['rho_sign']) for f,s in c['boundary']) for c in cells.values()))
    for c in cells.values():
        id=c['id'];sign=1
        for _ in range(4):sign*=cells[id]['rho_sign'];id=cells[id]['rho']
        assert id==c['id'] and sign==1
    checks.append('four chart turns restore every oriented chain cell')
    check('all stored triangular and tetrahedral boundaries match reconstructed incidence',all(
        set(r['edges'])=={id for id,_ in cells[r['id']]['boundary']} for r in data['triangles']) and all(
        set(r['faces'])=={id for id,_ in cells[r['id']]['boundary']} for r in data['tetrahedra']))
    blocks=[]
    for j in range(4):
        k=(j+1)%4;points=[]
        for m in range(8):
            a=[0]*4;a[j]=7-m;a[k]=m;points.append(cumulative(a))
        edge_records=[]
        for m,(a,b) in enumerate(zip(points,points[1:])):
            id=lookup[tuple(sorted((a,b)))];assert cells[id]['dimension']==1
            edge_records.append({'step':m+1,'edge':id,'orientation_sign':1 if a<b else -1,
                                 'source':lookup[(a,)],'target':lookup[(b,)],
                                 'incident_faces':[r['id'] for r in data['triangles'] if id in r['edges']]})
        blocks.append({'chart':j,'barycentric_vertices':[bary(p) for p in points],
                       'vertex_ids':[lookup[(p,)] for p in points],'edges':edge_records})
    check('all four extracted conductors have seven actual edges',all(len(b['edges'])==7 for b in blocks))
    check('successive rotated conductors share endpoint/start vertices',all(blocks[j]['vertex_ids'][-1]==blocks[(j+1)%4]['vertex_ids'][0] for j in range(4)))
    check('rotation intertwines every oriented conductor step',all(
        cells[e['edge']]['rho']==blocks[(j+1)%4]['edges'][m]['edge'] and
        e['orientation_sign']*cells[e['edge']]['rho_sign']==blocks[(j+1)%4]['edges'][m]['orientation_sign']
        for j,b in enumerate(blocks) for m,e in enumerate(b['edges'])))
    central_vs=tuple(sorted(cumulative(a) for a in set(permutations((1,2,2,2)))))
    central=cells[lookup[central_vs]]
    check('central tetrahedron has exact centroid (7/4,7/4,7/4,7/4)',all(sum(Fraction(bary(v)[i],4) for v in central_vs)==Fraction(7,4) for i in range(4)))
    check('central cell is fixed setwise by chart rotation',central['rho']==central['id'])
    check('central cell orientation reverses under one chart turn',central['rho_sign']==-1)
    check('boundary conductors do not visit the central cell vertices',all(id not in {lookup[(v,)] for v in central_vs} for b in blocks for id in b['vertex_ids']))
    check('depth-four middle edge is not the tetrahedron center', all(
        tuple((Fraction(a)+Fraction(b))/2 for a,b in zip(block['barycentric_vertices'][3],block['barycentric_vertices'][4])) != (Fraction(7,4),)*4 for block in blocks))
    check('closed boundary loop has 28 distinct edge occurrences',len({e['edge'] for b in blocks for e in b['edges']})==28)
    flag_bridges=[]
    for order in permutations(central_vs):
        flag=[lookup[tuple(sorted(order[:n]))] for n in range(1,5)]
        rotated=[cells[id]['rho'] for id in flag]
        bridge=flag+list(reversed(rotated[:-1]))
        flag_bridges.append({'ascending_flag':flag,'rotated_flag':rotated,'seven_presentations':bridge,
                             'dimensions_plus_one':[cells[id]['dimension']+1 for id in bridge],
                             'directions':['inclusion']*3+['reverse-incidence']*3})
    check('24 central flag bridges realize the seven-term depth profile',len(flag_bridges)==24 and all(b['dimensions_plus_one']==[1,2,3,4,3,2,1] for b in flag_bridges))
    check('every flag bridge uses actual consecutive incidences',all(
        a in {id for id,_ in cells[b]['boundary']} or b in {id for id,_ in cells[a]['boundary']}
        for bridge in flag_bridges for a,b in zip(bridge['seven_presentations'],bridge['seven_presentations'][1:])))
    check('each bridge shares the central tetrahedron once',all(b['seven_presentations'].count(central['id'])==1 for b in flag_bridges))
    check('chart rotation preserves the complete family of flag bridges',
          {tuple(cells[id]['rho'] for id in b['seven_presentations']) for b in flag_bridges}==
          {tuple(b['seven_presentations']) for b in flag_bridges})
    check('central flag endpoints are local rather than outer vertices',all(
        max(bary(cells[b['seven_presentations'][i]]['vertices'][0]))==2
        for b in flag_bridges for i in [0,-1]))
    report={'status':'passed','check_count':len(checks),'checks':checks,'source':SOURCE,
            'source_sha256':hashlib.sha256((ROOT/SOURCE).read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'blocks':blocks,'central_flag_bridges':flag_bridges,'central_cell':{**central,'barycentric_vertices':[bary(v) for v in central_vs]},
            'central_faces':[{**cells[id],'boundary':cells[id]['boundary']} for id,_ in central['boundary']],
            'scope':'Geometric incidence and signed chain naturality only. Four boundary conductors are not the proposed center-to-vertex passage. Central flag bridges have seven cell presentations but six incidence transitions; reverse-incidence legs are not asserted to be inverse analytic maps. Rotation maps endpoint to rotated endpoint; concatenation uses old endpoint=new start and is not itself a full-state chart-handoff proof. No analytic face realization, P/E readout, suspension or depth law is newly proved.',
            'disposition':'Actual seven-edge blocks and all-cell signed rotation recovered. Center passage and convolution-depth binding remain separate obligations; pure rho fixes the central cell.'}
    dest=ROOT/'research/strominger/results/esd7-seven-stage-handoff.json'
    dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'cells':len(cells),'central_cell':central['id'],'central_rotation_sign':central['rho_sign'],'conductor_edges':[[e['edge'] for e in b['edges']] for b in blocks],'result':str(dest)}))


if __name__=='__main__':main()
