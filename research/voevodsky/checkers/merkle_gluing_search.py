"""Bounded discovery of orientation-reversing gluings of affine Q identity faces.
Inputs have only local corners, maps and polynomial proof roots, not vertex IDs
shared across faces. Search is restricted to connected regular simple-edge
polygon surfaces; ambiguity concerns labelled ports, not isomorphism classes.
"""
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
import argparse
import json
from pathlib import Path

from merkle_identity_kernel import Builder, verify as verify_proof
from check_merkle_identity_surface import encode, verify, inverse

DOMAIN=b'marici.face-gluing.v1\0'
def digest(rec): return sha256(DOMAIN+json.dumps(rec,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def polynomial_proof(maps):
    b=Builder(); x=b.var('x'); term=x
    for a,c in maps:
        term=b.term('add',b.term('mul',b.const(a),term),b.const(c))
    proof=b.proof('ring',term,x)
    return b.artifact(['x'],{},proof)

def face_packet(faces):
    """Each face is a list of directed [a,b] maps in its boundary order."""
    objects={}; refs=[]
    for i,maps in enumerate(faces):
        maps=[list(map(str,map(Q,m))) for m in maps]
        proof=polynomial_proof(maps); objects.update(proof['objects'])
        face={'kind':'local-face','occurrence':i,'types':['Q']*len(maps),'maps':maps,'proof':proof['root']}
        ref=digest(face); objects[ref]=face; refs.append(ref)
    root={'kind':'unglued-faces','faces':refs}; key=digest(root); objects[key]=root
    return {'schema':'marici.unglued-faces.v1','root':key,'objects':objects}

def read_faces(packet):
    if set(packet)!={'schema','root','objects'} or packet['schema']!='marici.unglued-faces.v1': raise ValueError('source schema')
    store=packet['objects']
    if len(store)>10000: raise ValueError('source object limit')
    def get(ref):
        if ref not in store or digest(store[ref])!=ref: raise ValueError('source hash mismatch')
        return store[ref]
    root=get(packet['root'])
    if set(root)!={'kind','faces'} or root['kind']!='unglued-faces' or not isinstance(root['faces'],list) or not 1<=len(root['faces'])<=32: raise ValueError('source faces')
    result=[]
    for i,ref in enumerate(root['faces']):
        rec=get(ref)
        if set(rec)!={'kind','occurrence','types','maps','proof'} or rec['kind']!='local-face' or type(rec['occurrence']) is not int or rec['occurrence']!=i: raise ValueError('face occurrence')
        maps=rec['maps']
        if not isinstance(maps,list) or not 3<=len(maps)<=8 or rec['types']!=['Q']*len(maps): raise ValueError('face types/arity')
        for m in maps:
            if not isinstance(m,list) or len(m)!=2 or any(not isinstance(c,str) or len(c)>128 for c in m): raise ValueError('map encoding')
            values=tuple(map(Q,m))
            if not values[0] or list(map(str,values))!=m: raise ValueError('canonical affine isomorphism required')
        actual=verify_proof({'schema':'marici.polynomial-proof-store.v1','root':rec['proof'],'objects':store})
        expected=verify_proof(polynomial_proof(maps))
        if not actual['unconditional'] or (actual['lhs'],actual['rhs'])!=(expected['lhs'],expected['rhs']): raise ValueError('face proof attachment')
        result.append(rec)
    return result

def ports_for(faces): return [(f,j) for f,face in enumerate(faces) for j in range(len(face['maps']))]
def compatible(faces,a,b):
    return a[0]!=b[0] and tuple(map(Q,faces[a[0]]['maps'][a[1]]))==inverse(tuple(map(Q,faces[b[0]]['maps'][b[1]])))

def quotient(faces,pairs):
    ports=ports_for(faces); all_ports=set(ports); used=[]
    for pair in pairs:
        if len(pair)!=2: raise ValueError('pair shape')
        a,b=map(tuple,pair)
        if a not in all_ports or b not in all_ports or not compatible(faces,a,b): raise ValueError('incompatible boundary pairing')
        used.extend((a,b))
    if len(used)!=len(set(used)) or set(used)!=all_ports: raise ValueError('pairing is not a perfect matching')
    parent={p:p for p in ports}
    def find(p):
        while parent[p]!=p: p=parent[p]
        return p
    def union(a,b):
        a,b=find(a),find(b)
        parent[max(a,b)]=min(a,b)
    def end(p): return (p[0],(p[1]+1)%len(faces[p[0]]['maps']))
    for pair in pairs:
        a,b=map(tuple,pair); union(a,end(b)); union(end(a),b)
    labels={p:f'v{find(p)[0]:02}_{find(p)[1]:02}' for p in ports}
    vertices={v:{'type':'Q'} for v in labels.values()}; edges={}; cycles=[]
    for f,face in enumerate(faces):
        cycle=[labels[f,j] for j in range(len(face['maps']))]
        if len(set(cycle))!=len(cycle): raise ValueError('outside simple-polygon grammar')
        cycles.append(cycle)
    for pair in pairs:
        a=tuple(pair[0]); u,v=labels[a],labels[end(a)]
        if u==v: raise ValueError('loop edge outside grammar')
        low,high=sorted((u,v)); key=low+'>'+high
        if key in edges: raise ValueError('parallel edges outside encoder grammar')
        affine=tuple(map(Q,faces[a[0]]['maps'][a[1]]))
        if u!=low: affine=inverse(affine)
        edges[key]={'source':low,'target':high,'map':list(map(str,affine))}
    return {'vertices':vertices,'edges':edges,'faces':cycles}, labels

def certificate(packet,pairs,surface):
    rec={'kind':'gluing-certificate','source':packet['root'],'pairings':pairs,'surface':surface['root'],
         'rule':'inverse-map-pairing; reversed-endpoints; regular-connected-surface'}
    return {'record':rec,'hash':digest(rec)}

def verify_certificate(packet,cert,surface):
    rec=cert['record']
    if cert['hash']!=digest(rec) or set(rec)!={'kind','source','pairings','surface','rule'} or rec['kind']!='gluing-certificate' or rec['rule']!='inverse-map-pairing; reversed-endpoints; regular-connected-surface': raise ValueError('certificate schema/hash')
    if rec['source']!=packet['root'] or rec['surface']!=surface['root']: raise ValueError('certificate endpoint binding')
    faces=read_faces(packet); model,_=quotient(faces,rec['pairings']); rebuilt=encode(model)
    if rebuilt['root']!=surface['root']: raise ValueError('incorrect quotient')
    report=verify(surface)
    if not report['coherent_closed_surface'] or not report['connected']: raise ValueError('not a connected coherent surface')
    return report

def search(packet,max_nodes=10000,max_solutions=2):
    if type(max_nodes) is not int or max_nodes<1 or type(max_solutions) is not int or max_solutions<2: raise ValueError('search budgets')
    faces=read_faces(packet); ports=ports_for(faces)
    candidates={p:[q for q in ports if compatible(faces,p,q)] for p in ports}
    unmatched=[list(p) for p in ports if not candidates[p]]
    solutions=[]; visited=0; limited=False; early=False; rejected=0
    def visit(remaining,pairs):
        nonlocal visited,limited,early,rejected
        if len(solutions)>=max_solutions: early=True; return
        if visited>=max_nodes: limited=True; return
        visited+=1
        if not remaining:
            try:
                model,_=quotient(faces,pairs); surface=encode(model)
                cert=certificate(packet,pairs,surface); report=verify_certificate(packet,cert,surface)
            except ValueError: rejected+=1; return
            solutions.append({'certificate':cert,'surface':surface,'summary':{k:report[k] for k in ('vertices','edges','faces','genus','globally_path_independent')}})
            return
        p=min(remaining,key=lambda p:(len([q for q in candidates[p] if q in remaining]),p))
        for q in candidates[p]:
            if q in remaining:
                visit(remaining-{p,q},pairs+[[list(p),list(q)]])
                if limited or len(solutions)>=max_solutions:
                    if len(solutions)>=max_solutions: early=True
                    return
    visit(set(ports),[])
    if len(solutions)>=2: status='ambiguous'
    elif limited: status='search_limit'
    elif len(solutions)==1: status='unique_labelled_gluing'
    else: status='no_gluing_in_supported_grammar'
    return {'status':status,'exhaustive':not limited and not early,'source_root':packet['root'],
            'visited_nodes':visited,'rejected_complete_pairings':rejected,'unmatched_ports':unmatched,
            'solutions':solutions,'scope':'Labelled local ports; reversed orientation; connected simple-edge regular polygon surfaces. Not uniqueness up to homeomorphism.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('source',type=Path)
    parser.add_argument('--max-nodes',type=int,default=10000); parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    try:
        if args.source.stat().st_size>10_000_000: raise ValueError('source file size limit')
        result=search(json.loads(args.source.read_text(encoding='utf-8')),args.max_nodes)
        text=json.dumps(result,indent=2)
        if args.output: args.output.write_text(text+'\n',encoding='utf-8')
        print(json.dumps({k:v for k,v in result.items() if k!='solutions'},indent=2))
        if result['status']!='unique_labelled_gluing': raise SystemExit(1)
    except (ValueError,KeyError,TypeError,ZeroDivisionError) as error:
        print(json.dumps({'status':'invalid_input','error':str(error)})); raise SystemExit(1)
