"""Content-addressed exact source-word certificates for rank26 seed generators."""
from __future__ import annotations
from fractions import Fraction
import hashlib,json
from pathlib import Path
def _norm(x):
 if isinstance(x,Fraction):return [x.numerator,x.denominator]
 if isinstance(x,dict):return [[str(k),_norm(v)] for k,v in sorted(x.items(),key=lambda z:str(z[0]))]
 if isinstance(x,(list,tuple)):return [_norm(v) for v in x]
 return x
def digest(x):return hashlib.sha256(json.dumps(_norm(x),separators=(',',':')).encode()).hexdigest()
def make(descriptor,origins,rows,target,columns,coefficients,generator_path):
 word=[{'basis_index':i,'numerator':a.numerator,'denominator':a.denominator} for i,a in enumerate(coefficients) if a]
 gp=Path(generator_path);parts=gp.parts;rel='/'.join(parts[parts.index('research'):])
 cert={'schema':'marici.voevodsky.exact-source-certificate.v1','replay_mode':'generator_recompute','canonical_target_id':'target:'+digest(descriptor),'descriptor':_norm(descriptor),'source_basis':_norm(origins),'source_basis_digest':digest(origins),'row_digests':[digest(r) for r in rows],'matrix_digest':digest(rows),'equation_columns_digest':digest(columns),'equation_count':len(columns),'target_digest':digest(target),'sparse_word':word,'generator':{'path':rel,'source_digest':hashlib.sha256(gp.read_bytes()).hexdigest()}}
 assert replay(cert,origins,rows,target,columns,coefficients)
 return cert
def replay(cert,origins,rows,target,columns,coefficients):
 if cert['source_basis_digest']!=digest(origins) or cert['matrix_digest']!=digest(rows) or cert['target_digest']!=digest(target) or cert['equation_columns_digest']!=digest(columns):return False
 decoded=[Fraction(0) for _ in origins]
 for t in cert['sparse_word']:decoded[t['basis_index']]=Fraction(t['numerator'],t['denominator'])
 if decoded!=list(coefficients):return False
 recon={}
 for a,row in zip(decoded,rows):
  for k,v in row.items():recon[k]=recon.get(k,Fraction(0))+a*v
 return {k:v for k,v in recon.items() if v}==target
