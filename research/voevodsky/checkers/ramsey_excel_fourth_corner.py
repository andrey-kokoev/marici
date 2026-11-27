"""Can independent table swaps construct the fourth *whole* graph support from three?"""
from itertools import combinations,product
from collections import Counter
from ramsey_retention_slice import decode,check,D,CAT
import json,sys
P=D.parent/'ramsey_excel_fourth_corner_protocol.json';R=D.parent/'ramsey_excel_fourth_corner.json'
rule=dict(law='In cyclic order A,B,C,D, independent swaps on disjoint table blocks give 1_A+1_C=1_B+1_D coordinatewise. Supply three corners and predict D=A+C-B. Require binary outputs and exact fourth support. This tests coordinate copies (including duplicated or constant columns), not arbitrary functions of the two swap bits.',scope='Enumerate all terminal-width-reaching independent two-swap squares at widths 7 and 8. On all seven 17-cores and 191 22-cores enumerate all recolorable squares. Supply square, cyclic order and three graph rows as extra inputs. Use both consistent orientations, count only extensions passing a whole graph check. Report seed-only and full-row fits; test the other pairings as a relabeling control. No claim to select the graph square.')
def eq(s,j):return int(bool(s>>j&1))
def run():
    assert json.loads(P.read_text())==rule;report=[]
    for k,n in [(6,17),(7,22)]:
        width=k+1;rows={frozenset(c) for c in combinations(range(1,width+1),3) if min(c[1]-c[0],c[2]-c[1])>=2};faces=set()
        for s in rows:
            moves=[frozenset([i,i+1]) for i in range(1,width) if s^set([i,i+1]) in rows];
            for t,u in combinations(moves,2):
                corners=[s,s^t,s^t^u,s^u];
                if t&u or corners[2] not in rows or not any(width in c for c in corners):continue
                assert all((p in corners[0])+(p in corners[2])==(p in corners[1])+(p in corners[3]) for p in range(1,width+1));faces.add(frozenset(corners))
        stats=Counter();hist=Counter();example=None
        for ix,line in enumerate((CAT/f'r3{k}_{n}.g6').read_text().splitlines(),1):
            a=decode(line);cycles=set();adj=[{j for j in range(n) if j!=i and not v>>j&1 and not v&a[j]} for i,v in enumerate(a)]
            for i in range(n):
                for j in adj[i]:
                    for h in adj[j]-{i}:
                        for l in (adj[h]&adj[i])-{j}:
                            c=(i,j,h,l);cycles.add(min(t[p:]+t[:p] for t in (c,c[::-1]) for p in range(4)))
            for c in sorted(cycles):
                for d in (2,3):
                    S=[];G=a.copy()+[0]*5
                    for i in range(4):
                        x,y=c[i],c[(i+1)%4];s=(1<<x)|(1<<y)|(a[c[(i+d)%4]]&~(a[x]|a[y]));S.append(s);G[n+i]=s|1<<(n+4);G[-1]|=1<<(n+i)
                        for j in range(n):G[j]|=((s>>j)&1)<<(n+i)
                    stats['tested']+=1
                    if not check(G,(1<<(n+5))-1,3,k+1):continue
                    stats['legal']+=1;bad=[j for j in range(n) if eq(S[0],j)+eq(S[2],j)!=eq(S[1],j)+eq(S[3],j)];stats['anchors_exact']+=not(set(bad)&set(c));stats['whole_exact']+=not bad;hist[len(bad)]+=1
                    stats['any_pairing_exact']+=any(all(eq(S[0],j)+eq(S[h],j)==sum(eq(S[t],j) for t in range(1,4) if t!=h) for j in range(n)) for h in (1,2,3))
                    if bad and example is None:example=dict(record=ix,square=c,failed_column=bad[0],actual_bits=[eq(s,bad[0]) for s in S],wrong_columns=bad)
        report.append(dict(step=[n,n+5],new_table_squares=len(faces),counts=dict(stats),wrong_column_histogram=dict(hist),example=example));print(report[-1])
    R.write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':
    if sys.argv[1]=='freeze':
        text=json.dumps(rule,indent=2)+'\n';assert not P.exists() or P.read_text()==text;P.write_text(text)
    else:run()
