"""Sparse algebraic transport across one Fourier--Motzkin elimination.
No optimizer, projected dictionary construction, or source-engine import.
Rows are (normal, upper); the caller must establish their statement validity.
"""
from fractions import Fraction as Q

def transport(rows,weights,index,allow_nonnegative_repair=False):
 if not rows or not 0<=index<len(rows[0][0]):raise ValueError('INVALID_ELIMINATION')
 rows=[(tuple(map(Q,a)),Q(b)) for a,b in rows];weights=list(map(Q,weights));d=len(rows[0][0])
 if len(weights)!=len(rows) or any(w<0 for w in weights) or any(len(a)!=d for a,b in rows):raise ValueError('INVALID_PROOF')
 original=sum(w!=0 for w in weights);imbalance=sum(w*a[index] for w,(a,b) in zip(weights,rows));repair=None
 if imbalance:
  if not allow_nonnegative_repair or imbalance<0:raise ValueError('UNBALANCED_RETIRED_NORMAL')
  required=tuple(Q(-int(j==index)) for j in range(d))
  matches=[i for i,(a,b) in enumerate(rows) if a==required and b==0]
  if not matches:raise ValueError('MISSING_ZERO_BOUND_NONNEGATIVITY_ROW')
  i=matches[0];weights[i]+=imbalance;repair={'row':i,'weight':str(imbalance)}
 positive=[[i,w*a[index]] for i,(w,(a,b)) in enumerate(zip(weights,rows)) if w and a[index]>0]
 negative=[[i,-w*a[index]] for i,(w,(a,b)) in enumerate(zip(weights,rows)) if w and a[index]<0]
 terms=[{'kind':'zero','row':i,'weight':str(w)} for i,(w,(a,b)) in enumerate(zip(weights,rows)) if w and a[index]==0]
 assert sum(v for i,v in positive)==sum(v for i,v in negative)
 p=n=0
 while p<len(positive) and n<len(negative):
  mass=min(positive[p][1],negative[n][1]);assert mass>0
  terms.append({'kind':'pair','positive':positive[p][0],'negative':negative[n][0],'weight':str(mass)})
  positive[p][1]-=mass;negative[n][1]-=mass
  if positive[p][1]==0:p+=1
  if negative[n][1]==0:n+=1
 assert p==len(positive) and n==len(negative)
 normalized=sum(w!=0 for w in weights);bound=normalized-(1 if positive else 0)
 assert len(terms)<=bound and len(terms)<=original
 return {'retired_position':index,'repair':repair,'terms':terms,'counts':{'input_nonzero':original,'normalized_nonzero':normalized,'positive_nonzero':len(positive),'negative_nonzero':len(negative),'projected_nonzero':len(terms)}}

def expand(rows,index,terms):
 """Reverse a supported projected proof by substituting its row recipes."""
 out=[Q(0)]*len(rows)
 for term in terms:
  w=Q(term['weight'])
  if w<0:raise ValueError('NEGATIVE_MULTIPLIER')
  if term['kind']=='zero':
   i=term['row']
   if rows[i][0][index]!=0:raise ValueError('NOT_A_ZERO_ROW')
   out[i]+=w
  elif term['kind']=='pair':
   i=term['positive'];j=term['negative'];a=rows[i][0][index];b=rows[j][0][index]
   if not a>0>b:raise ValueError('INVALID_PAIR_SIGNS')
   out[i]+=w/a;out[j]-=w/b
  else:raise ValueError('UNSUPPORTED_PROOF_ROW')
 return out
