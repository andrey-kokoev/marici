"""Audit whether an exchange involution preserves unequal occurrence coefficient data."""
import json
import sympy as sp
c31,c23=sp.symbols('c31 c23')
v=sp.Matrix([c31,c23]); swap=sp.Matrix([[0,1],[1,0]])
residual=sp.simplify(swap*v-v)
assert residual==sp.Matrix([c23-c31,c31-c23])
assert sp.solve(list(residual),(c31,c23))=={c31:c23}
print(json.dumps({'schema':'marici.nima.qg12-source-occurrence-exchange.v1','status':'passed','source_condition':'c31 != c23 (frozen source audit)','exchange_residual':[str(x) for x in residual],'exchange_preserves_ordered_coefficient_data_iff':'c31=c23','sum_is_exchange_invariant':True,'sum_invariance_constructs_summand_involution':False,'bold_conjecture':'the source-sewn sum canonically exchanges its two occurrence summands','disposition':'falsified for the frozen unequal occurrence classes','residual_conjecture':'equivariance can only be attached to a separately constructed specialization of the unsplit total; it does not descend from occurrence exchange'},sort_keys=True))
