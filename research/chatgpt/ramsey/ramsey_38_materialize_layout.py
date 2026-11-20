"""Extract and replay the six-bit 27-address core/core and border decoder."""
from itertools import combinations
from pathlib import Path
import json
from ramsey_38_layout_recognition import find,sign
from ramsey_38_incidence_core_lift import independent
cols=find(27,sign,8,10);order=[c[r] for r in range(3) for c in cols];old=set(order);order+=sorted(set(range(27))-old)
L=[j|((1^((j&1)*(j>>1&1)))<<3)|(((j&1)*(j>>2))<<4)|(((j>>1&1)*(j>>2))<<5) for j in range(8)];table={};borders=[];A=[0]*27
for j in range(27):
    bm=0
    for i in range(j):
        s=sign(order[i],order[j]);key=f'{i//8},{j//8},{L[i%8]^L[j%8]}'
        if j<24:assert table.setdefault(key,int(s))==s;v=table[key]
        else:v=int(s);bm|=v<<i
        if v:A[i]|=1<<j;A[j]|=1<<i
    if j>=24:borders.append(bm)
ss=independent(A);assert all(r in ss for r in A) and max(map(int.bit_count,ss))==7
Path(__file__).with_name('ramsey_38_cell_6bit_27_from_catalogue.json').write_text(json.dumps(dict(source='record 1499',order=order,labels=L,core_decoder=table,border_masks=borders,rows=A),indent=2));print('verified 27; remaining addresses',order[-3:])
