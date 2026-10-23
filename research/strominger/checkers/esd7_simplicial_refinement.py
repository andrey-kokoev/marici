"""Canonical finite edgewise nerve lift, not a supplied analytical realization.
For r=7, a fine d-simplex is a parent-nerve (7(d+1)-1)-simplex.
The parent alphabet is ordered1<2<3<4; fine vertex order reverses the
cumulative-coordinate order. This orientation change is explicit.
"""
from itertools import combinations

KINDS=('vertices','edges','triangles','tetrahedra')


def require(value,message):
    if not value:raise ValueError(message)


def vertex_word(bary,scale):
    require(len(bary)==4 and all(type(n) is int and n>=0 for n in bary) and sum(bary)==scale,'invalid barycentric word')
    return [i+1 for i,n in enumerate(bary) for _ in range(n)]


def lift(assembly):
    r=assembly['scale']; require(type(r) is int and r>=1,'positive integral scale')
    words={v['id']:vertex_word(v['barycentric'],r) for v in assembly['vertices']}
    index={}; rows=[]
    for d,kind in enumerate(KINDS):
        for c in assembly[kind]:
            require(c['id'] not in index,'duplicate cell ID')
            # Original geometry is lexicographic cumulative order. A parent
            # monotone word requires the opposite orientation on fine cells.
            vs=list(reversed(c['vertices'])); require(len(vs)==d+1 and len(set(vs))==d+1,'simplex arity')
            require(all(v in words for v in vs),'unknown vertex')
            word=[words[v][k] for k in range(r) for v in vs]
            require(word==sorted(word),'not an edgewise simplex: parent word is not monotone')
            support=sorted(set(word))
            row={'cell':c['id'],'fineDimension':d,'fineVertexOrder':vs,
                 'orientationRelativeToGeometry':(-1)**(d*(d+1)//2),
                 'parentWord':word,'parentSimplexDimension':len(word)-1,
                 'parentSupport':support,'nondegenerateParentDimension':len(support)-1,
                 'degeneracyMap':[support.index(x) for x in word],
                 'faceRestrictions':[], 'analyticalPayloadInstalled':False}
            index[c['id']]=row; rows.append(row)
    by_vertices={tuple(row['fineVertexOrder']):row for row in rows}
    for row in rows:
        d=row['fineDimension']; vs=row['fineVertexOrder']; width=d+1
        for i in range(width) if d else []:
            target=by_vertices.get(tuple(vs[:i]+vs[i+1:]))
            require(target is not None,'missing shared face')
            deleted=[k*width+i for k in range(r)]
            image=[x for j,x in enumerate(row['parentWord']) if j not in deleted]
            require(image==target['parentWord'],'edgewise face restriction mismatch')
            row['faceRestrictions'].append({'omitFineVertex':i,'face':target['cell'],'deleteParentPositions':deleted,'sign':(-1)**i})
        # Two orders of restricting a codimension-two face must agree on
        # literal parent occurrence positions, not only on displayed labels.
        for i,j in combinations(range(width),2) if d>=2 else []:
            initial=list(range(r*width))
            first=[x for p,x in enumerate(initial) if p%width!=j]
            first=[x for p,x in enumerate(first) if p%(width-1)!=i]
            second=[x for p,x in enumerate(initial) if p%width!=i]
            second=[x for p,x in enumerate(second) if p%(width-1)!=j-1]
            require(first==second,'simplicial face identity fails on occurrence positions')
    return {'scale':r,'cells':rows,'vertexWords':words,
            'fineVertexInterpretation':'a retained parent-nerve comparison history, not a weighted mixture or a single parent chart',
            'parentOrder':[1,2,3,4], 'orientationConvention':'reverse cumulative-coordinate vertex order',
            'structuralRefinementEstablished':True,'analyticalRealizationEstablished':False,
            'full114ChannelEstablished':False,'globalFieldTransportEstablished':False}
