"""Exact rational chain computations for finite bipartite relations."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product


def fixture(restore=False):
    vertices=range(4)
    primitive=[e for e in product(vertices,repeat=2)
               if e[0]!=e[1] and (restore or e!=(0,1))]
    result=[]
    for a,b in product(primitive,repeat=2):
        result.append((('source',('arrow',a[0],b[0])),('target',('arrow',a[1],b[1]))))
    for a,b in product(vertices,repeat=2):
        result.append((('source',('state',a,b)),('target',('state',a,b))))
    return result


def add_scaled(out,vector,scale):
    for key,value in vector.items():
        new=out.get(key,F(0))+scale*value
        if new: out[key]=new
        else: out.pop(key,None)


def apply(columns,vector):
    result={}
    for i,value in vector.items(): add_scaled(result,columns[i],value)
    return result


def rank(columns):
    pivots={}
    for column in columns:
        vector={i:F(value) for i,value in column.items() if value}
        while vector:
            pivot=min(vector)
            if pivot in pivots:
                add_scaled(vector,pivots[pivot],-vector[pivot])
            else:
                scale=vector[pivot]
                pivots[pivot]={i:v/scale for i,v in vector.items()}
                break
    return len(pivots)


def analyze(dimensions,differentials):
    for d in sorted(differentials):
        if d-1 in differentials:
            assert all(not apply(differentials[d-1],column) for column in differentials[d])
    ranks={d:rank(columns) for d,columns in differentials.items()}
    homology={d:n-ranks.get(d,0)-ranks.get(d+1,0) for d,n in dimensions.items()}
    assert all(n>=0 for n in homology.values())
    return ranks,homology


def biclique(ends):
    vertices=sorted({v for edge in ends for v in edge},key=repr)
    vertex_id={v:i for i,v in enumerate(vertices)}
    edge_id={edge:i for i,edge in enumerate(ends)}
    assert len(edge_id)==len(ends), 'simple relation required'
    neighbors=defaultdict(set); adjacency=defaultdict(set)
    for u,v in ends:
        neighbors[u].add(v); adjacency[u].add(v); adjacency[v].add(u)
    unseen=set(vertices); components=[]
    while unseen:
        start=min(unseen,key=repr); todo=[start]; unseen.remove(start); component={start}
        for at in todo:
            for nxt in adjacency[at]:
                if nxt in unseen:
                    unseen.remove(nxt); component.add(nxt); todo.append(nxt)
        components.append(component)
    cells=defaultdict(list)
    for component in components:
        sources=sorted(component & neighbors.keys(),key=repr)
        for p in range(2,len(sources)+1):
            for left in combinations(sources,p):
                common=set.intersection(*(neighbors[u] for u in left))
                for q in range(2,len(common)+1):
                    for right in combinations(sorted(common,key=repr),q):
                        cells[p+q-2].append((left,right))
    labels={d:{cell:i for i,cell in enumerate(rows)} for d,rows in cells.items()}
    differentials={1:[{vertex_id[u]:F(1),vertex_id[v]:F(-1)} for u,v in ends]}
    for d in sorted(cells):
        columns=[]
        for left,right in cells[d]:
            p,q=len(left),len(right)
            if d==2:
                u,w=left; v,z=right
                column={edge_id[u,v]:F(1),edge_id[u,z]:F(-1),edge_id[w,v]:F(-1),edge_id[w,z]:F(1)}
            else:
                column={}
                if p>2:
                    for i in range(p): column[labels[d-1][(left[:i]+left[i+1:],right)]]=F((-1)**i)
                if q>2:
                    for j in range(q): column[labels[d-1][(left,right[:j]+right[j+1:])]]=F((-1)**(p+j))
            columns.append(column)
        differentials[d]=columns
    dimensions={0:len(vertices),1:len(ends),**{d:len(rows) for d,rows in cells.items()}}
    return dimensions,differentials,cells,labels


def dowker(ends, *, include_cells=False):
    # Source simplices are the nonempty subsets of some target neighborhood.
    neighborhoods=defaultdict(set)
    for u,v in ends: neighborhoods[v].add(u)
    faces=defaultdict(set)
    for members in neighborhoods.values():
        ordered=sorted(members,key=repr)
        for n in range(1,len(ordered)+1): faces[n-1].update(combinations(ordered,n))
    cells={d:sorted(rows,key=repr) for d,rows in faces.items()}
    labels={d:{cell:i for i,cell in enumerate(rows)} for d,rows in cells.items()}
    differentials={}
    for d,rows in cells.items():
        if d:
            differentials[d]=[{labels[d-1][cell[:i]+cell[i+1:]]:F((-1)**i)
                               for i in range(d+1)} for cell in rows]
    result=({d:len(rows) for d,rows in cells.items()},differentials)
    return (*result,cells) if include_cells else result
