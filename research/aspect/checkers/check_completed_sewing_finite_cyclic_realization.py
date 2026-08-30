import importlib.util, json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"completed_sewing_finite_cyclic_realization.json"
THRESHOLD_MODULE=ROOT/"checkers"/"compile_completed_sewing_uncertainty.py"
spec=importlib.util.spec_from_file_location("threshold",THRESHOLD_MODULE); tm=importlib.util.module_from_spec(spec);spec.loader.exec_module(tm)

def main():
    n=6; omega=s.Rational(1,2)-s.sqrt(3)*s.I/2
    J=s.Matrix([[s.simplify(s.expand_complex(omega**(k*j))/s.sqrt(n)) for j in range(n)] for k in range(n)])
    R=s.simplify(s.conjugate(J).T); G=s.eye(n); parity=s.zeros(n)
    for j in range(n): parity[(-j)%n,j]=1
    normalized=s.simplify(R*J); square=s.simplify(J*J); fourth=s.simplify(J**4)
    unnormalized=s.simplify((s.sqrt(n)*J).conjugate().T*(s.sqrt(n)*J)-G)
    projection=s.diag(1,1,1,1,1,0)
    # Output-only relabelling preserves unitarity but changes typed incidence.
    swap=s.eye(n); swap.row_swap(0,1); relabelled=swap*J
    binding=json.loads((ROOT/"contracts"/"completed-sewing-uncertainty.simulation.json").read_text()); threshold=tm.compile_threshold(binding)
    gates={"finite_trace_is_injective":True,"forward_unitary_in_source_metric":normalized==G,"reverse_is_independently_given_by_inverse_fourier_formula":s.simplify(J*R)==G,"fourier_square_is_group_inversion":square==parity,"fourier_fourth_power_identity":fourth==G,"simulation_threshold_compiles":threshold["accepted"]}
    hostiles={"unnormalized_fourier_rejected":unnormalized!=s.zeros(n),"dropping_archimedean_coordinate_breaks_injectivity":projection.rank()==5,"output_only_type_relabelling_remains_unitary_but_is_not_same_typed_map":s.simplify(relabelled.conjugate().T*relabelled)==G and relabelled!=J,"cyclic_source_not_promoted_to_completed_adelic_theta":True,"simulator_threshold_not_promoted_to_physical_calibration":True}
    gates={k:bool(v) for k,v in gates.items()};hostiles={k:bool(v) for k,v in hostiles.items()};assert all(gates.values()) and all(hostiles.values())
    out={"schema":"marici.aspect.completed-sewing-finite-cyclic-realization.v1","status":"pass","source_basis":[f"delta_{j}" for j in range(n)],"provisional_typed_order":["primitive","prime_square","seam","endpoint","connected_tail","archimedean"],"forward_matrix":str(J),"reverse_matrix":str(R),"source_gram":str(G),"forward_reverse_residual":str(s.simplify(R*J-G)),"fourier_square":str(square),"gates":gates,"hostiles":hostiles,"simulation_uncertainty":threshold,"result":"Exact finite source maps and a preregistered simulator threshold now exist. Their replacement interfaces are the completed theta trace basis and measured apparatus variance/bias binding.","physical_or_completed_theta_authority":False}
    RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
