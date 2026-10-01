"""Complete the local biclique comparison chain complex of the137-slot fixture."""
from biclique_complex import analyze, apply, biclique, fixture

ends=fixture()
dimensions,differentials,cells,labels=biclique(ends)
ranks,homology=analyze(dimensions,differentials)
assert dimensions=={0:64,1:137,2:672,3:1304,4:1074,5:416,6:64}
assert ranks=={1:47,2:90,3:582,4:722,5:352,6:64}
assert homology=={0:17,1:0,2:0,3:0,4:0,5:0,6:0}
assert sum((-1)**d*n for d,n in dimensions.items())==17
mixed=next(i for i,(left,right) in enumerate(cells[4]) if len(left)==len(right)==3)
bad=dict(differentials[4][mixed])
left,right=cells[4][mixed]
bad[labels[3][(left,right[1:])]]*=-1
assert apply(differentials[3],bad)
print('degree | cells | boundary rank | homology dimension')
for d in sorted(dimensions): print(f'{d:6} | {dimensions[d]:5} | {ranks.get(d,0):13} | {homology[d]:18}')
print('All consecutive boundary composites vanish exactly; mixed-face sign corruption is detected.')
print('d4 fills all722 previous kernel directions; all positive-degree rational homology vanishes.')
print(f'All complete bipartite blocks enumerated; maximum cell dimension={max(cells)}.')
