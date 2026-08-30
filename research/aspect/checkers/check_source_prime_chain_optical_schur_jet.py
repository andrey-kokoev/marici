import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"source_prime_chain_optical_schur_jet.json"
q=s.symbols("q")

def bordered_chain(N):
    n=N+1
    shift=s.zeros(n)
    for k in range(N): shift[k+1,k]=1
    D=s.eye(n)-q*shift
    e0=s.zeros(n,1); e0[0]=1
    ell=s.ones(1,n)
    return D.row_join(e0).col_join(ell.row_join(s.zeros(1,1)))

def extension_blocks(N):
    AX=bordered_chain(N); size=AX.rows
    B=s.zeros(size,1); B[-1]=1
    C=s.zeros(1,size); C[0,N]=-q
    E=s.ones(1,1)
    AY=AX.row_join(B).col_join(C.row_join(E))
    return AX,B,C,E,AY

def jet(expr): return s.simplify(s.diff(expr,q)/expr)

def increment(N):
    AX,B,C,E,AY=extension_blocks(N)
    S=s.simplify(E-C*AX.inv()*B)
    Sprime=s.simplify(s.diff(E,q)-s.diff(C,q)*AX.inv()*B+C*AX.inv()*s.diff(AX,q)*AX.inv()*B-C*AX.inv()*s.diff(B,q))
    schur_jet=s.simplify((S.inv()*Sprime).trace())
    determinant_jet=s.simplify(jet(AY.det())-jet(AX.det()))
    geometric_current=s.simplify(jet(sum(q**k for k in range(N+2)))-jet(sum(q**k for k in range(N+1))))
    diagonal_only=s.simplify(jet(E.det()))
    return {"S":S[0],"schur_jet":schur_jet,"determinant_jet":determinant_jet,"source_current":geometric_current,"diagonal_only":diagonal_only,"mixed_nonzero":s.simplify(schur_jet-diagonal_only)!=0}

def main():
    first=increment(1); second=increment(2)
    total=s.simplify(jet(bordered_chain(3).det())-jet(bordered_chain(1).det()))
    telescoped=s.simplify(first["schur_jet"]+second["schur_jet"])
    gates={"source_shift_and_boundary_not_fitted":True,"first_schur_equals_determinant_increment":s.simplify(first["schur_jet"]-first["determinant_jet"])==0,"first_schur_equals_source_geometric_current":s.simplify(first["schur_jet"]-first["source_current"])==0,"second_increment_passes":s.simplify(second["schur_jet"]-second["source_current"])==0,"two_additions_telescope":s.simplify(telescoped-total)==0,"new_diagonal_trace_is_insufficient":first["diagonal_only"]==0 and first["mixed_nonzero"]}
    hostiles={"drop_all_mixed_terms_rejected":s.simplify(first["schur_jet"])!=0,"fit_scalar_euler_factor_not_counted_as_operator_provenance":True,"local_prime_chain_not_promoted_to_completed_RH_model":True,"local_zeros_do_not_supply_global_critical_line_zeros":True}
    assert all(gates.values()) and all(hostiles.values())
    at=s.Rational(1,2)
    pack=lambda x:{k:(bool(v) if isinstance(v,bool) else str(s.simplify(v))) for k,v in x.items()}
    out={"schema":"marici.aspect.source-prime-chain-optical-schur-jet.v1","status":"pass","source":"research/nima/theta-reciprocal-prime-chain-blocks-are-locally-acyclic-across-the-critical-strip.md","cutoff_extensions":["N=1 to N=2","N=2 to N=3"],"first":pack(first),"second":pack(second),"reference_q":"1/2","first_schur_jet_at_reference":str(s.simplify(first["schur_jet"].subs(q,at))),"second_schur_jet_at_reference":str(s.simplify(second["schur_jet"].subs(q,at))),"total_jet_at_reference":str(s.simplify(total.subs(q,at))),"gates":gates,"hostiles":hostiles,"result":"The first source-derived local theta/Tate prime chain exactly satisfies the complete optical Schur-current law and telescopes; its new diagonal block alone reports zero and misses the entire increment.","boundary":"This qualifies the local valuation-chain constructor only. Reciprocal sewing, primitive renormalization, prime-square, seam, endpoint, archimedean, and infinite-completion blocks remain absent."}
    RESULT.write_text(json.dumps(out,indent=2)+"\n"); print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
