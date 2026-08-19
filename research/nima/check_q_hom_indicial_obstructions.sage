import json
from sage.misc.sage_eval import sage_eval

ROOT = "/mnt/c/Users/andrey/src/marici/research/benincasa"
R.<u,v> = PolynomialRing(QQ)
F = FractionField(R)
Q = -u^4+4*u^3*v-4*u^3-4*u^2*v+4*u^2-8*u*v-4*v^2+16*u+16*v-16
D = -4+12*u-6*u*v+4*v-9*u^2+4*u^2*v-v^2
H = -2-3*u+2*u*v+v-u^2*v+u^3
a9 = json.load(open(ROOT+"/bivariate_soft_gram_connection.json"))
a3 = json.load(open(ROOT+"/marked-wall-quotient-connection.json"))

def parse(x):
    if isinstance(x,(int,Integer)): return F(x)
    return F(sage_eval(str(x).replace("^","**"),locals={"u":u,"v":v,"D":D,"H":H}))

def A3(axis):
    z=F(0); d=a3[axis]
    return [[parse(d["alpha"]),z,z],[parse(d["beta1"]),parse(d["gamma1"]),z],[parse(d["beta2"]),z,parse(d["gamma2"])]]

def audit(label,K,u0,v0):
    v1=K((-Q.derivative(u)/Q.derivative(v))(u=u0,v=v0))
    L=LaurentSeriesRing(K,'t',default_prec=4); t=L.gen(); uu=L(u0)+t; vv=L(v0)+L(v1)*t
    def residue(entries): return matrix(K,[[parse(x)(uu,vv)[-1] for x in row] for row in entries])
    R9=residue(a9["connection_u"])+v1*residue(a9["connection_v"])
    R3=residue(A3("u"))+v1*residue(A3("v"))
    T=identity_matrix(K,3).tensor_product(R9)-R3.transpose().tensor_product(identity_matrix(K,9))
    cp=T.charpoly(); roots=[n for n in range(-20,21) if cp(K(n))==0]
    return {"label":label,"R9_charpoly":str(factor(R9.charpoly())),"R3_charpoly":str(factor(R3.charpoly())),"Hom_charpoly":str(factor(cp)),"integer_roots":roots}

S.<z> = PolynomialRing(QQ)
KD.<wd> = NumberField(z^2-44*z+100)
KH.<wh> = NumberField(3*z^2-6*z+1)
records=[
    audit("Q_cap_D",KD,KD(4),wd),
    audit("Q_cap_H",KH,wh,KH(2)-wh/2),
    audit("Q_cap_u_plus_v_minus_2",QQ,QQ(8)/5,QQ(2)/5),
]
print(json.dumps({"schema":"marici.nima.q_hom_indicial_obstructions.v1","records":records},indent=2))
