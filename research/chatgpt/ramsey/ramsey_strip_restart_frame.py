"""How much does a window at the restart remember? Measure forced retrace; separately test the optional rule to diverge at the first opportunity. No assumed successor ordering."""
from itertools import takewhile
from ramsey_strip_next_row_restart import first,swapped
tracks=sorted(first); land=lambda p:p+swapped(p)[-2::-1]; nexts=list(map(swapped,tracks)); shared=lambda a,b:sum(1 for _ in takewhile(lambda xy:xy[0]==xy[1],zip(a,b)))
for w in range(2,13):
    groups={land(p)[-w:] for p in tracks};print('width',w,'distinct landing frames',len(groups))
    if len(groups)==len(tracks):break
matrix=[[shared(land(p)[::-1],n)-1 for n in nexts] for p in tracks];print('number of immediately retraced edges (lexicographic track order)');print(*matrix,sep='\n');print('earliest divergence successor counts',[row.count(min(row)) for row in matrix]);assert all(row[i]==11 and min(row)==1 for i,row in enumerate(matrix));assert all(land(p)[-2:]==(17,0) for p in tracks)
