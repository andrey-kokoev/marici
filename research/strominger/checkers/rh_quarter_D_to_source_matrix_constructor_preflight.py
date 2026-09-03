import contextlib,io,inspect,json,runpy
from pathlib import Path
base=Path(__file__).parents[1]
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py')))
boundary=json.loads((base/'results'/'rh_quarter_source_generator_size_boundary.json').read_text())
callables={n:str(inspect.signature(v)) for n,v in g.items() if callable(v) and not n.startswith('_')}
builder_names=[n for n in callables if any(x in n.lower() for x in ['source_matrix','build_matrix','transfer_matrix','hurwitz_matrix_family'])]
q9=g['Q'](9);d9=g['D'](9,0)
checks={'source_boundary_audit_passed':boundary['status']=='passed','Q_and_D_generators_exposed':{'Q','D'}<=set(callables),'Q9_and_D9_nonempty':bool(q9) and bool(d9),'no_parameterized_source_matrix_builder_exposed':not builder_names}
r={'schema':'marici.strominger.rh_quarter_D_to_source_matrix_constructor_preflight.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'The D-family backend can generate Q and D polynomials at size nine, but exposes no parameterized assembly map producing source matrices A_k,B_k,C_k or proving their terminal-minor formula.','Q_signature':callables.get('Q'),'D_signature':callables.get('D'),'Q9_degree':len(q9)-1,'D9_degree':len(d9)-1,'candidate_builder_names':builder_names,'required_missing_typed_object':'A source-derived build_source_matrices(k) map from Q,D data to A_k,B_k,C_k with labelled rows and columns and a proved source-term identity.','acceptance_test':'At k=8 reproduce the retained A,B,C exactly; at k=9 produce dimensionally valid matrices; verify every source-term determinant identity before running Hall flow.','checks':checks};(base/'results'/'rh_quarter_D_to_source_matrix_constructor_preflight.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r,indent=2))
