# Imperfect-field channel recovery

## Question

Does a unique geometric channel solution imply recovery over the declared field?

## Claim boundary

Take k=F_p(u), with u an indeterminate carrying no temporal interpretation, m=p^e with e>=1, and n=m+3. Assign every triangulation weight u. The construction tests coefficient descent, not source geometry.

Constant weights are locally factorizing and admit triangle factors in k: assign u to triangles incident to one fixed boundary edge and one elsewhere. A channel solution must have a common scale z by flip connectivity, hence z^m=u. The u-adic valuation gives m v_u(z)=1, impossible in k.

The polynomial X^m-u is Eisenstein at u in F_p[u], so is irreducible over k. Adjoining v with v^m=u produces a purely inseparable extension of degree m and restores the solution by assigning v to every channel. Every field extension admitting a solution contains a root of this irreducible polynomial, so this is the minimal root-generated extension. Over an algebraic closure the root is unique, since X^m-u=(X-v)^m, but its scheme multiplicity is m. Unique geometric existence therefore does not imply descent to k.

## Disposition

Exact polynomial checks for m=2,3,4,9 verify the Eisenstein coefficient conditions, zero derivative, Frobenius factorization, and restored reconstruction. The proof establishes minimality; the computations do not infer it from failed root searches. Two checker defects were repaired: unsupported domain-string syntax and failure to reduce a substituted characteristic-two expression modulo p. The final run passes. The unit-only recovery theorem remains unchanged; coefficients with zeros require a different support analysis.
