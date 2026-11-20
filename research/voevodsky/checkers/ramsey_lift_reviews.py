"""Replay a local reviewed route. Reviewers judge proof content; replay checks provenance and sequencing."""
from ramsey_lift_execution import inspect_run
from hashlib import sha256
import json

STAGES={
 'lift':['dimension_proof','trace_vs_span','rotation','reflection','duality','domain_coverage'],
 'reduction':['literal_linkages','single_operation','redundancy_witness','equivariance','coordinate_recovery'],
 'prediction':['baseline','survivors_or_cancellations','correction_derivation','predicted_order','source_independence'],
 'threshold':['lower_witness','universal_obstruction','comparison_to_prediction','scope_coverage'],
 'closure':['same_operations','domain_verdict','limitations']}
SPEC=['lift_operation','lift_algorithm','domain','domain_kind','correction_kind','dimension','geometry','rotation','reflection','duality','linkages','single_reduction','baseline','correction_rule','coordinate_rule']

def need(x,s):
    if not x:raise ValueError(s)

def pin(p):return sha256(p.read_bytes()).hexdigest()

def replay(rows,resolve,contract_hash,branches,scope_grants=()):
    routes={}
    for r in rows:
        p=resolve(r['file']);need(pin(p)==r['digest'],'changed review artifact');d=json.loads(p.read_text());k=d['route'];kind=d['action'];need(isinstance(k,str) and k.strip(),'route id')
        if kind=='freeze':
            need(k not in routes and d['contract']==contract_hash and isinstance(d['branch'],str) and d['branch'].strip(),'duplicate or foreign route');need(all(isinstance(d.get(f),str) and d[f].strip() for f in SPEC),'incomplete route specification');need(d['dimension'] in ('4','8') and d['geometry'] in ('trace','span') and d['domain_kind'] in ('pilot','family') and d['correction_kind'] in ('additional','signed'),'scope or geometry');imp=resolve(d['lift_algorithm']);need(pin(imp)==d['implementation_sha256'],'changed implementation');routes[k]=dict(spec=r['digest'],implementation=pin(imp),branch=d['branch'],known_branch=d['branch'] in branches,claim=d['correction_kind'],literal37=False,domain=d['domain'],domain_kind=d['domain_kind'],approved=[],pending=None,state='active',next='lift');continue
        need(k in routes,'unknown route');a=routes[k]
        if kind=='root_review':
            need(any(g=={'spec':a['spec'],'domain':a['domain'],'closure_review':a.get('closure_review')} for g in scope_grants),'external scope decision required');need(a['claim']=='additional' and a['literal37'] and a['state']=='closed_for_declared_domain' and a['domain_kind']=='family' and d['spec']==a['spec'] and d['scope']==a['domain'] and d['closure_review']==a['closure_review'] and d['reviewer'].strip() and d['scope_acceptance'].strip() and d['reason'].strip(),'root requires separate family scope review');a['state']='root_closed_for_declared_domain';continue
        need(a['state']=='active' and d['spec']==a['spec'] and d['stage']==a['next'],'route or stage mismatch');stage=d['stage']
        if kind=='submit':
            need(a['pending'] is None and d['author'].strip() and all(isinstance(d.get(f),str) and d[f].strip() for f in STAGES[stage]),'incomplete submission');ev=resolve(d['evidence']);need(pin(ev)==d['evidence_sha256'],'changed evidence');a['pending']={'digest':r['digest'],'author':d['author']}
            if stage=='prediction':
                t=json.loads(ev.read_text());count=inspect_run(t);need(t['implementation']==a['implementation'] and (a['claim']=='signed' or not t['cancelled']),'implementation or claim mismatch');a['pending']['case37']=sorted(t['input'])==[3,7];a['pending']['literal37']=sorted(t['input'])==[3,7] and len(t['extra'])==2 and not t['cancelled'] and count==23
                need(str(count)==d['predicted_order'],'prediction must come from submitted cells')
        elif kind=='review':
            pending=a['pending'];need(pending and d['submission']==pending['digest'] and d['reviewer'].strip() and d['reviewer']!=pending['author'] and d['reason'].strip(),'review must identify the exact submission and separate reviewer');verdict=d['verdict'];need(verdict in ('accept','revise','refute'),'review verdict');a['pending']=None
            if verdict=='refute':a.update(state='refuted',next=None)
            if verdict=='accept':
                if stage=='prediction':a.update(literal37=pending['literal37'],case37=pending['case37'])
                if stage=='threshold' and a['claim']=='additional' and a['case37']:need(a['literal37'],'literal case needs two distinct additional cells')
                a['approved'].append(stage);i=len(a['approved']);a['next']=list(STAGES)[i] if i<len(STAGES) else None
                if a['next'] is None:a.update(state='closed_for_declared_domain',closure_review=r['digest'])
        else:raise ValueError('unknown action')
    return routes
