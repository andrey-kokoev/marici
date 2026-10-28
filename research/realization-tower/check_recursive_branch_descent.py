"""Branch-local step/promotion/re-probe using the existing retained line-graph rule.

No assignment of promotion depth to numerical rungs. Different final branch
records are not identified merely because each is a singleton presentation.
"""
import contextlib
import io
import json
from pathlib import Path
import runpy
from unittest.mock import patch
from collections import deque
from check_extended_probe_diagonal import audit

ROOT=Path(__file__).resolve().parents[2]
HOME=Path(__file__).parent


def separation(vertices,edges,left,right):
    if left&right:return 0
    adj={v:set() for v in vertices}
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    queue=deque((v,0) for v in left);seen=set(left)
    while queue:
        v,d=queue.popleft()
        for w in adj[v]-seen:
            if w in right:return d+1
            seen.add(w);queue.append((w,d+1))
    return None


def run_branch(path,promote,branch):
    vertices=[f'b{branch}:p{i}' for i in range(len(path))]
    edges={tuple(sorted((a,b))) for a,b in zip(vertices,vertices[1:])}
    archive={v:{'seed':list(point)} for v,point in zip(vertices,path)}
    support={v:{v} for v in vertices};initial=set(vertices)
    left={vertices[0]};right={vertices[-1]};levels=[];witnesses=[]
    for depth in range(len(path)):
        gap=separation(vertices,edges,left,right)
        levels.append({'depth':depth,'records':len(vertices),'links':len(edges),'probe_separation':gap,'common_records':sorted(left&right)})
        if gap==0:break
        previous_edges=edges.copy();previous_left=left.copy();previous_right=right.copy()
        vertices,edges,witness=promote(vertices,edges,f'b{branch}:level{depth+1}',archive)
        left={v for v in vertices if set(archive[v]['endpoints'])&previous_left}
        right={v for v in vertices if set(archive[v]['endpoints'])&previous_right}
        for v in vertices:support[v]=set().union(*(support[p] for p in archive[v]['endpoints']))
        assert {tuple(archive[v]['endpoints']) for v in vertices}==previous_edges
        for (a,b),w in witness.items():
            assert set(archive[a]['endpoints'])&set(archive[b]['endpoints'])=={w}
        witnesses.append([{'records':[a,b],'shared_previous_record':w} for (a,b),w in sorted(witness.items())])
        assert separation(vertices,edges,left,right)==gap-1
    assert len(vertices)==1 and left==right==set(vertices)
    assert support[vertices[0]]==initial
    return {'path':path,'levels':levels,'final_record':vertices[0],'archive':archive,'adjacency_witnesses':witnesses}


def main():
    # Execute owning checks; capture its one JSON receipt rather than replacing it.
    receipts={}
    def capture(path,text,*args,**kwargs):
        assert path.resolve()==(ROOT/'research/nima/results/retained-line-graph-cycles.json').resolve()
        receipts['owning_rule_regression']=json.loads(text);return len(text)
    with patch.object(Path,'write_text',capture),contextlib.redirect_stdout(io.StringIO()):
        owner=runpy.run_path(str(ROOT/'research/nima/checkers/check_retained_line_graph_cycles.py'))
    reports=[]
    for length in (4,6):
        generated=audit((0,0,0),(length,0,0),length//2)
        paths=generated['shortest_walks']
        assert len(paths)==(36 if length==4 else 400)
        cases=[run_branch(path,owner['promote'],f'{length}-{i}') for i,path in enumerate(paths)]
        assert all([l['probe_separation'] for l in c['levels']]==list(range(length,-1,-1)) for c in cases)
        assert len({c['final_record'] for c in cases})==len(cases)
        reports.append({'original_separation':length,'branches':len(cases),
                        'records_by_depth':[l['records'] for l in cases[0]['levels']],
                        'separation_by_depth':[l['probe_separation'] for l in cases[0]['levels']],
                        'cases':cases})
    # Distinct terminal presentations retain distinct source histories.
    assert reports[0]['cases'][0]['path']!=reports[0]['cases'][1]['path']
    # Disconnected components never acquire a spurious bridge.
    v=['a','b','c','d'];e={('a','b'),('c','d')};archive={x:{'seed':x} for x in v}
    nv,ne,_=owner['promote'](v,e,'control',archive)
    assert len(nv)==2 and not ne
    out={'status':'pass','rule':'Existing retained line-graph promotion on an individual comparison-selected shortest-path branch',
         'dependency':receipts,'experiments':reports,
         'survivor':'Re-probing actual promoted record incidence reduces branch separation by one per promotion, retaining reconstructible ancestry.',
         'limits':['Promotion is an existing candidate generative rule, not an established numerical rung descent.',
                   'This is branch-local, not promotion of the full surrounding lattice or full cell complex.',
                   'The final records from different branches are distinct; common dimensions do not supply cross-branch coherence.',
                   'No particle-role assignment, isotope count, energy, physical clock or full WG filler follows.']}
    target=HOME/'results/recursive-branch-descent-v1.json';target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','experiments':[{k:v for k,v in r.items() if k!='cases'} for r in reports],
                      'disconnected_control':'pass','receipt':str(target)}))


if __name__=='__main__':main()
