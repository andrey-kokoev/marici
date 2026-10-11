"""Unified bounded verification gateway; trusted-session polynomial proof cache.
Cache entries never replace current-input integrity and closure validation.
No persistent cache file is trusted or loaded.
"""
from collections import OrderedDict
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import argparse
import json

from merkle_identity_kernel import Kernel, digest as proof_digest
from check_merkle_identity_surface import verify as verify_surface
from merkle_gluing_search import read_faces, verify_certificate
from merkle_cone_filler import verify as verify_filler
from merkle_witness_transport import verify as verify_transport

VERSION=sha256(Path(__file__).with_name('merkle_identity_kernel.py').read_bytes()+Path(__file__).read_bytes()).hexdigest()

def guard(value,depth=0,budget=None):
    if budget is None: budget=[200000]
    budget[0]-=1
    if depth>96 or budget[0]<0: raise ValueError('input nesting/item budget')
    if isinstance(value,dict):
        if len(value)>10000 or any(not isinstance(k,str) for k in value): raise ValueError('object/key budget')
        for key,item in value.items():
            if len(key)>4096: raise ValueError('key length')
            guard(item,depth+1,budget)
    elif isinstance(value,list):
        if len(value)>10000: raise ValueError('array budget')
        for item in value: guard(item,depth+1,budget)
    elif isinstance(value,str):
        if len(value)>4096: raise ValueError('string length')
    elif type(value) is int:
        if value.bit_length()>64: raise ValueError('integer size')
    elif value is not None and type(value) is not bool: raise ValueError('unsupported JSON scalar')

def strict_loads(text):
    if len(text.encode('utf-8'))>10_000_000: raise ValueError('file size limit')
    def pairs(items):
        result={}
        for key,value in items:
            if key in result: raise ValueError('duplicate JSON key')
            result[key]=value
        return result
    def bad_constant(value): raise ValueError('nonfinite JSON number')
    result=json.loads(text,object_pairs_hook=pairs,parse_constant=bad_constant)
    guard(result); return result

def polynomial_preflight(artifact):
    """Rehash every supplied object, then check reachable DAG depth/references.
    Even a full cache hit requires the current referenced objects to be present.
    """
    store=artifact['objects']
    if not isinstance(store,dict) or len(store)>10000: raise ValueError('object count')
    for key,rec in store.items():
        if not isinstance(rec,dict) or proof_digest(rec)!=key: raise ValueError('object hash mismatch')
    active=set(); heights={}
    def visit(ref,depth=0):
        if not isinstance(ref,str) or ref not in store: raise ValueError('missing dependency')
        if depth>96: raise ValueError('dependency depth limit')
        if ref in active: raise ValueError('cyclic dependency')
        if ref in heights: return heights[ref]
        active.add(ref); rec=store[ref]; kind=rec.get('kind')
        if kind=='judgment': children=[rec['context'],rec['proof']]
        elif kind=='context': children=[r for pair in rec['assumptions'].values() for r in pair]
        elif kind=='proof': children=[rec['lhs'],rec['rhs']]+rec.get('premises',[])
        elif kind=='term': children=rec.get('args',[])
        else: raise ValueError('unsupported reachable record kind')
        height=1+max((visit(child,depth+1) for child in children),default=0)
        if height>96: raise ValueError('dependency height limit')
        active.remove(ref); heights[ref]=height; return height
    visit(artifact['root'])
    return len(heights)

class VerifiedCache:
    """Bounded trusted in-process cache, scoped to implementation + context."""
    def __init__(self,limit=20000,namespace=VERSION):
        self.limit=limit; self.namespace=namespace; self.entries=OrderedDict(); self.hits=0; self.misses=0
    def get(self,key):
        key=(self.namespace,)+key
        if key not in self.entries: self.misses+=1; return None
        self.hits+=1; self.entries.move_to_end(key); return deepcopy(self.entries[key])
    def put(self,key,value):
        key=(self.namespace,)+key; self.entries[key]=deepcopy(value); self.entries.move_to_end(key)
        while len(self.entries)>self.limit: self.entries.popitem(last=False)

class CachedKernel(Kernel):
    def __init__(self,artifact,cache):
        self.cache=cache
        self.context_key=artifact['objects'][artifact['root']]['context']
        super().__init__(artifact)
    def term(self,key,depth=0):
        if key in self.terms: return super().term(key,depth)
        cached=self.cache.get((self.context_key,'term',key))
        if cached is not None:
            self.terms[key]=cached; return cached
        result=super().term(key,depth); self.cache.put((self.context_key,'term',key),result); return result
    def proof(self,key,depth=0):
        if key in self.proofs: return super().proof(key,depth)
        cached=self.cache.get((self.context_key,'proof',key))
        if cached is not None:
            self.proofs[key]=cached; return cached
        result=super().proof(key,depth); self.cache.put((self.context_key,'proof',key),result); return result

def verify(artifact,cache=None,require_global=False,require_unconditional=False):
    guard(artifact)
    if not isinstance(artifact,dict): raise ValueError('artifact object required')
    schema=artifact.get('schema'); cache=cache if cache is not None else VerifiedCache()
    before=(cache.hits,cache.misses); reachable=None
    if schema=='marici.polynomial-proof-store.v1':
        reachable=polynomial_preflight(artifact); result=CachedKernel(artifact,cache).verify()
    elif schema=='marici.identity-surface-store.v1':
        if set(artifact)!={'schema','root','objects'}: raise ValueError('surface envelope')
        result=verify_surface(artifact)
        if not result['coherent_closed_surface']: raise ValueError('surface not locally coherent and closed')
    elif schema=='marici.cone-filler-store.v1': result=verify_filler(artifact)
    elif schema=='marici.witness-transport-store.v1': result=verify_transport(artifact)
    elif schema=='marici.unglued-faces.v1':
        faces=read_faces(artifact); result={'verified':True,'face_count':len(faces),'gluing':'not supplied or inferred'}
    elif schema=='marici.gluing-proof-bundle.v1':
        if set(artifact)!={'schema','source','certificate','surface'}: raise ValueError('gluing envelope')
        result=verify_certificate(artifact['source'],artifact['certificate'],artifact['surface'])
    else: raise ValueError('unsupported artifact schema')
    if require_global and result.get('globally_path_independent') is not True: raise ValueError('global path-independence policy not satisfied or not applicable')
    if require_unconditional and result.get('unconditional') is not True: raise ValueError('unconditional proof policy not satisfied or not applicable')
    return {'accepted':True,'schema':schema,'result':result,'reachable_objects':reachable,
            'cache_hits':cache.hits-before[0],'cache_misses':cache.misses-before[1],
            'cache_scope':'Trusted process only; polynomial terms/proofs; context and implementation bound. Integrity is always rechecked.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('artifact',type=Path)
    parser.add_argument('--require-global',action='store_true'); parser.add_argument('--require-unconditional',action='store_true'); args=parser.parse_args()
    try:
        if args.artifact.stat().st_size>10_000_000: raise ValueError('file size limit')
        artifact=strict_loads(args.artifact.read_text(encoding='utf-8'))
        print(json.dumps(verify(artifact,require_global=args.require_global,require_unconditional=args.require_unconditional),indent=2))
    except (ValueError,KeyError,TypeError,ZeroDivisionError,RecursionError,AttributeError,OverflowError) as error:
        print(json.dumps({'accepted':False,'error':str(error)})); raise SystemExit(1)
