"""Owner-local conjecture workbench. Standard library; run without -O."""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations
import json
from math import lcm
from pathlib import Path

HOME=Path(__file__).resolve().parents[1]; ROOT=HOME.parent.parent
CONTRACT=HOME/'contracts/ramsey-relational-lift-conjecture-net.v1.json'
HISTORY=HOME/'results/ramsey-relational-lift-attempts.jsonl'
RECEIPT=HOME/'results/ramsey-relational-lift-check.json'

from ramsey_lift_reviews import replay, STAGES, SPEC
JOURNAL=HOME/'results/ramsey-relational-lift-route-events.jsonl'

def route_rows():return [json.loads(l) for l in JOURNAL.read_text().splitlines() if l.strip()] if JOURNAL.exists() else []

GRANTS=HOME/'contracts/ramsey-relational-lift-scope-grants.json'
def priors(c,*targets):return {n['id']:n['criterion'] for n in c['conjectures'] if n['kind']=='tested_prior' and set(n['applies_to']).intersection(targets)}

def check_prior_response(c,d):
    for k in priors(c,'cells',d['branch']):
        response=d.get('prior_response',{}).get(k,{})
        demand(response.get('relation') in ('respects','different_scope','challenges') and str(response.get('reason','')).strip(),f'give scoped response to {k}')

def routes(c,rows):
    for r in rows:
        d=json.loads(evidence(r['file']).read_text());
        if d['action']=='freeze':check_prior_response(c,d)
    return replay(rows,evidence,digest(CONTRACT),{n['id'] for n in c['conjectures'] if n['kind']=='candidate'},json.loads(GRANTS.read_text())['grants'])

def dashboard(rs):
    result={}
    for rid,r in rs.items():
        nodes={'cells':'frozen',r['branch']:'in review'}
        for s,n in [('lift',r['branch']),('reduction','quotient'),('prediction','readout'),('threshold','threshold'),('closure','scoped-closure')]:
            if s in r['approved']:nodes[n]='accepted on this route'
        if r['state']=='refuted':nodes[r['branch']]='route refuted'
        result[rid]={'nodes':nodes,'next':r['next'],'action':('review submission' if r['pending'] else 'submit evidence') if r['next'] else r['state']}
    return result

def demand(x,msg):
    if not x: raise ValueError(msg)

def digest(p):return sha256(p.read_bytes()).hexdigest()

def evidence(path):
    p=(ROOT/path).resolve();demand(p.is_relative_to(ROOT) and p.is_file(),f'invalid evidence: {path}');return p

def pilots():
    # Fourier column rank: the complex exponential columns with frequencies
    # +/-N/l,+/-N/k are orthogonal; changing a conjugate pair to cos/sin is invertible.
    n=lcm(3,7);rank=len({f%n for f in (n//3,-n//3,n//7,-n//7)})
    sites={(i%3,i%7) for i in range(n)};demand((len(sites),rank)==(21,4),'clock')
    demand(len(sites)<23,'cardinality')
    a={(0,2),(0,3),(1,2)};b=a|{(1,3)}
    def ok(v,e):return all(0<sum(p in e for p in combinations(t,2))<3 for t in combinations(range(v),3))
    def moves(e,root):return {m for m in range(16) if m>>root&1 and ok(5,e|{(i,4) for i in range(4) if m>>i&1})}
    demand(ok(4,a) and ok(4,b) and moves(a,0)==moves(b,0)==set() and 10 in moves(a,1)-moves(b,1),'reroot')
    return {'clock37':['++',{'positions':len(sites),'fourier_rank':rank}],'cardinality':['-+',{'max_quotient':21,'threshold_control':23}],'reroot':['-+',{'distinguishing_red_mask':10}]}

def history(nodes):
    entries=[json.loads(line) for line in HISTORY.read_text().splitlines() if line.strip()] if HISTORY.exists() else []
    ids=set()
    for r in entries:
        demand(r['id'] not in ids and r['node'] in nodes and r['outcome'] in ('++','-+','+-','--') and r['summary'].strip(),'invalid attempt');ids.add(r['id']);demand(digest(evidence(r['evidence']))==r['sha256'],'attempt evidence changed')
    return entries

def evaluate(c):
    nodes={n['id']:n for n in c['conjectures']};demand(len(nodes)==len(c['conjectures']),'duplicate node');demand(c['objective']['outcome'] is None,'root requires separate closure review');p=pilots();used=set();vis=set();active=set()
    def visit(k):
        demand(k in nodes and k not in active,'unknown dependency or cycle: '+k)
        if k in vis:return
        active.add(k);n=nodes[k];demand(n['claim'].strip() and n['criterion'].strip(),'empty claim/criterion')
        for d in n['requires']+n.get('any_of',[]):visit(d)
        if 'test' in n:
            t=n['test'];demand(t not in used and p[t][0]==n['outcome'],'test/outcome mismatch');used.add(t)
        elif n['kind']=='tested_prior':
            path,pin=c['prior_sources'][n['source']];demand(digest(evidence(path))==pin,'changed prior source');demand(n['outcome'] in ('++','-+') and n['verification'] and n['locator'] and n['applies_to'] and all(t in nodes and t!=k for t in n['applies_to']),'invalid scoped prior')
        else:demand(n['outcome'] is None,'reviewed verifier required for new verdict')
        vis.add(k);active.remove(k)
    for k in nodes:visit(k)
    demand(used==set(p),'missing controls');passed={k for k,n in nodes.items() if n['outcome']=='++'}
    ready=[k for k,n in nodes.items() if n['outcome'] is None and set(n['requires'])<=passed and ('any_of' not in n or bool(set(n['any_of'])&passed))];demand(c['next'] in ready,'blocked next action')
    rs=routes(c,route_rows());closed=[r['domain'] for r in rs.values() if r['state']=='root_closed_for_declared_domain']
    return {'imported_priors':{n['id']:n['verification'] for n in nodes.values() if n['kind']=='tested_prior'},'routes':rs,'route_frontier':dashboard(rs),'scope_grants_sha256':digest(GRANTS),'execution_engine_sha256':digest(Path(__file__).with_name('ramsey_lift_execution.py')),'review_engine_sha256':digest(Path(__file__).with_name('ramsey_lift_reviews.py')),'journal_sha256':digest(JOURNAL) if JOURNAL.exists() else None,'closed_scopes':closed,'id':c['id'],'revision':c['revision'],'contract_sha256':digest(CONTRACT),'checker_sha256':digest(Path(__file__)),'evidence_sha256':{f:digest(evidence(f)) for f in c['evidence']},'root':'closed_for_listed_scopes' if closed else 'open','node_count':len(nodes),'checked':p,'ready':ready,'priority':c['next'],'attempt_count':len(history(nodes)),'history_sha256':digest(HISTORY) if HISTORY.exists() else None}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('action',choices=['check','snapshot','verify','frontier','show','record','route-event','route-schema']);ap.add_argument('--node');ap.add_argument('--outcome',choices=['++','-+','+-','--']);ap.add_argument('--summary');ap.add_argument('--evidence');args=ap.parse_args();c=json.loads(CONTRACT.read_text());nodes={n['id']:n for n in c['conjectures']};res=evaluate(c)
    if args.action=='route-schema':res={'freeze_fields':SPEC,'submission_fields':STAGES}
    if args.action=='route-event':
        f=evidence(args.evidence);row={'file':f.relative_to(ROOT).as_posix(),'digest':digest(f)};routes(c,route_rows()+[row]);JOURNAL.parent.mkdir(exist_ok=True)
        with JOURNAL.open('a',encoding='utf8') as out:out.write(json.dumps(row)+'\n')
        print('Route event recorded.');return
    if args.action=='record':
        demand(args.node in nodes and args.outcome and args.summary and args.summary.strip() and args.evidence,'record requires node, outcome, summary, evidence');f=evidence(args.evidence);t=datetime.now(timezone.utc).isoformat();r=dict(id=t,node=args.node,outcome=args.outcome,summary=args.summary,evidence=f.relative_to(ROOT).as_posix(),sha256=digest(f),revision=c['revision']);HISTORY.parent.mkdir(exist_ok=True)
        with HISTORY.open('a',encoding='utf8') as out:out.write(json.dumps(r)+'\n')
        print('Attempt recorded; formal verdict unchanged.');return
    if args.action=='show':
        scoped={k:v for k,v in res['route_frontier'].items() if args.node in v['nodes']};demand(args.node in nodes or scoped,'unknown node');res={'node':nodes.get(args.node,{'id':args.node,'kind':'novel branch'}),'tested_constraints':priors(c,args.node),'scoped_progress':scoped,'history':[r for r in history(nodes) if r['node']==args.node]}
    if args.action=='frontier':res={'new_route_priority':c['next'],'active_route_actions':res['route_frontier'],'new_route_work_cards':[{'id':k,'test':nodes[k]['criterion'],'tested_constraints':priors(c,k)} for k in res['ready']]}
    if args.action=='snapshot':RECEIPT.parent.mkdir(exist_ok=True);RECEIPT.write_text(json.dumps(res,indent=2)+'\n')
    if args.action=='verify':demand(res==json.loads(RECEIPT.read_text()),'receipt drift; review changes before snapshot')
    print(json.dumps(res,indent=2))
if __name__=='__main__':main()
