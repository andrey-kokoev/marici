"""Residue census for unsplit leading sewn-wall forms in the X1-soft chart."""
import json
import sympy as sp
a,xi,k,p=sp.symbols('a xi k p'); s=p*sp.sqrt(5-4*k)
w1=-(a+p)/(2*p*(a-p)**2*(a+3*p)*(a**2+(4*k-5)*p**2))
w2=-1/(16*p**3*(k-1)*(xi+1)*(k+xi))
w3=-1/(64*p**4*(xi+1)*(k-xi))
def residues(f,var,points): return {label:sp.factor(sp.residue(f,var,point)) for label,point in points}
r1=residues(w1,a,[('a=p',p),('a=-3p',-3*p),('a=+s',s),('a=-s',-s)])
r2=residues(w2,xi,[('xi=-1',-1),('xi=-k',-k)])
r3=residues(w3,xi,[('xi=-1',-1),('xi=k',k)])
assert all(v!=0 for v in [*r1.values(),*r2.values(),*r3.values()])
assert sp.simplify(sum(r1.values()))==0
assert sp.simplify(sum(r2.values()))==0
assert sp.simplify(sum(r3.values()))==0
out={name:{q:str(v) for q,v in rs.items()} for name,rs in [('q_g1',r1),('q_g2',r2),('q_g3',r3)]}
print(json.dumps({'schema':'marici.nima.unsplit-wall-leading-residues.v1','status':'passed','oriented_leading_coefficients':{'q_g1':str(w1),'q_g2':str(w2),'q_g3':str(w3)},'grades':{'q_g1':-1,'q_g2':-2,'q_g3':-1},'residues':out,'componentwise_residue_sums_zero':True,'cross_component_cancellation_defined':False,'claim_boundary':'generic separated poles; no gluing/pushforward map or epsilon normalization'},sort_keys=True))
