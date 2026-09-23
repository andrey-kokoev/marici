# The four-pair branch Jacobian factors through the quadratic derivative

## Question

Which exact part of the nine-point four-pair source-to-target Jacobian produces the two-sheet branch structure, and can its trace be reduced without selecting a square-root branch?

## Claim boundary

For a target with a regular four-dimensional retained-eight source fibre, each of four paired-minor equations is affine in `(a,b,c,d,q)`, with `q=ad-bc`. Write them as `M x + v q + k=0`, where `x=(a,b,c,d)`, and solve `x(q)=-M^{-1}(v q+k)`. Define the graph polynomial `P(q)=q-a(q)d(q)+b(q)c(q)`.

The ACTUAL four-by-four Jacobian of the paired minors along the source fibre is `M+v grad(ad-bc)`. The matrix determinant lemma and `x'(q)=-M^{-1}v` give the **exact identity**

    det(d paired minors / dx) = det(M) P'(q).

A checker expands all four exact paired minors for the certified rational minimum-eight target and verifies this identity as a polynomial in `q` OFF the graph locus, with `det(M) != 0`; it rejects the opposite sign. Consequently graph-root collisions are precisely the source-fibre pair-constraint transversality failure on this regular chart. This is a source-fibre Jacobian factorization, not an identification of the complete eight-dimensional target Jacobian with `P'` without the remaining ambient-coordinate factors.

For any rational source-form density represented over the resulting separable quadratic field as `F(q)=H(q)/P'(q)`, reduce `H` modulo `P` to `h0+h1 q`. With leading coefficient `A` of `P`, the exact BOTH-sheet trace is

    F(q+) + F(q-) = h1/A.

This is a universal algebraic trace reduction; no square-root sign or real-positivity selector occurs. The formal-symbol checker tests the identity and rejects a positive-sheet-only substitution. It makes the next task specific: compute `H` from the labelled eight-column source residue and full source-to-target coordinate Jacobian as rational functions of GENERAL target Pluecker coordinates, then compare `h1/A` with a COMPLETE sourced psi super-five-bracket component and its pole residues. The two already-certified rational sample traces and one algebraic fixed-target trace do not determine that global `H`.

## Disposition

The exact fibre factor and abstract trace rule are established; global target form and complete source-history comparison remain open. No nine-point general triangulation or analytic completion follows.

Check: `research/nima/checkers/check_nine_point_trace_derivative_reduction.py`; result: `research/nima/results/nine-point-trace-derivative-reduction.json`.
