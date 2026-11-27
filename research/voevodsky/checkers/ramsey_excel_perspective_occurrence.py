"""Partial two-perspective receipt on the literal width-seven edge 147--247."""
from itertools import combinations
from pathlib import Path
import json
from two_perspective_gate import template, gaps

D=Path(__file__).resolve().parents[1]/'results'

def run():
    rows={s for s in combinations(range(1,8),3) if min(s[1]-s[0],s[2]-s[1])>=2}
    a,b=(1,4,7),(2,4,7)
    near=lambda s,t:sum(abs(i-j) for i,j in zip(s,t))==1
    squares=sorted((c,d) for c in rows-{a,b} for d in rows-{a,b,c} if near(a,c) and near(b,d) and near(c,d));assert squares==[((1,4,6),(2,4,6)),((1,5,7),(2,5,7))]
    r=template();e='width-seven row 147, column marks 2:B and 1:R; witnessed swap to 247. See ramsey_excel_perspective_occurrence.py.'
    def record(k,n,v):r[k][n]=dict(status='recorded',result=v,evidence=e)
    for n,v in dict(carrier='row 147 with a witnessed first-red swap',marks='labeled B at 2 and R at 1; N marks not supplied',X='reverse the ordered endpoint reading, without editing the row',readout='physical row and ordered (column,color) labels',compare='literal equality of row and ordered marks').items():record('frozen',n,v)
    marks=[(2,'B'),(1,'R')];state=lambda m:dict(row=a,marks=m)
    for n,m in [('I',marks),('X',marks[::-1]),('XX',marks[::-1][::-1])]:record('readings',n,state(m))
    record('comparisons','I:X','same row; marks reversed');record('comparisons','I:XX','same row and same ordered marks')
    r['square_completions']=squares;r['limitation']='Treating the other square direction as NN would require selecting and typing a pair. Neither selection nor typing follows from the mere existence of a commuting square.';assert list(gaps(r));(D/'ramsey_excel_perspective_occurrence.json').write_text(json.dumps(r,indent=2)+'\n')

if __name__=='__main__':run()
