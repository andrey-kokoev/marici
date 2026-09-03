# GL(2,Z) covariance

## Question

Do general monomial coordinate changes act solely by determinant in every realization?

## Claim boundary

They do for de Rham, Betti, Tate, character-residue, and oriented boundary realizations. For

`u'=u^a v^b`, `v'=u^c v^d`,

the wedge and every free-lattice realization are multiplied by `ad-bc`.

Integral Milnor K2 has a correction:

`{u',v'}=(ad-bc){u,v}+ac{u,u}+bd{v,v}`.

Here `{x,x}=-{x,-1}` and `2{x,-1}=0`, so the diagonal terms are 2-torsion. They vanish after rationalization and under dlog, period, and secondary-valuation comparisons, but cannot be silently deleted integrally. For example, the determinant-one shear `u'=uv`, `v'=v` gives `{uv,v}={u,v}+{v,v}`.

## Disposition

The primitive free obstruction obeys exact determinant covariance. Integral Milnor lifts may differ by regulator-invisible 2-torsion. The next leaf determines whether these diagonal corrections vanish in the actual function field and whether localization boundaries detect them.

## Verification

- `research/voevodsky/check_cosmology_GL2Z_covariance.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
