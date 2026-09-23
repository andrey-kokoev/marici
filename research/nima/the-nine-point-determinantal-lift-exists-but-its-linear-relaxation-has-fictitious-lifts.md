# The nine-point determinantal lift exists, but its linear relaxation has fictitious lifts

The first `n>8` test is exact. For positive moment-curve external data `Z_j=(1,j,...,j^5)` at nine points, `ker Z^T` has dimension three, with the three shifted length-seven binomial vectors as an explicit independent basis. A fixed target source representative `C` has a six-parameter fibre

    C(T)=C+T K,    T=[a0 a1 a2; b0 b1 b2].

Its 36 ordered rank-two minors are NOT affine in those six variables. Nevertheless each becomes affine after introducing the three quadratic coordinates

    q01=a0*b1-a1*b0,
    q02=a0*b2-a2*b0,
    q12=a1*b2-a2*b1.

The checker symbolically verifies ALL 36 exact identities of the form

    Delta_ij(C(T)) = base_ij + linear_ij(T)
                      + sum_(p<r) q_pr*(K_pi*K_rj-K_pj*K_ri).

Thus the positive fixed-target fibre is represented exactly by **36 affine halfspaces in nine lifted coordinates, intersected with three quadratic graph equations**. This is a reusable semialgebraic certificate format, not an arbitrary-nine-point positive-cell compiler.

The graph equations are indispensable. For the fixed source with first row all ones and second row `(1,1,2,3,4,5,6,7,8)`, its target has a real strictly positive lift at `b1=1/10000`, with minimum source minor `1/10000`. But at `T=0`, setting independent `q01=1/10000`, `q02=q12=0` makes ALL 36 affine lifted minor inequalities strictly positive while violating `q01=a0*b1-a1*b0`. This point is a **fictitious lifted witness**. Since the same target independently HAS a real positive lift, this example demonstrates certificate unsoundness of the linear RELAXATION, not a false target-membership verdict in this particular case.

The earlier curved eight-point slice persists: varying only `a0=a,b1=b` gives `Delta12=a*b+7a+b`. The extra hidden direction at nine points does not remove the determinant term. At ten points `ker Z^T` has dimension four: its six proposed `q` coordinates also satisfy the first pure quadratic Plücker relation `q01*q23-q02*q13+q03*q12=0`, independently verified symbolically. That relation alone is weaker than coupling `q` to the actual `T`; all graph equations remain essential.

The algebraic lifting formula extends to EVERY `n>=8` for rank-two sources: put `r=n-6`, let `K` span `ker Z^T`, and introduce `binomial(r,2)` coordinates `q_pr`. All `binomial(n,2)` ordered source minors become affine in the `2r` entries of `T` and the `q_pr`, while exact realizability is the quadratic graph `q_pr=a_p*b_r-a_r*b_p`. **The polynomial degree remains two at arbitrary n** because a rank-two minor is bilinear in its two source rows; only the number and coherence of coordinates grow. The n=9 executable test checks a nontrivial instance of this general determinant identity.

This supplies a concrete `n>8` path: use source-bound determinantal graph certificates and verify polynomial realizability before positivity or pushforward. A subsequent seven-label zero-padded source-cell candidate has exact full image rank, but another strictly positive target has certified minimum source support AT LEAST eight. See `a-nine-point-positive-target-requires-at-least-eight-source-labels.md`. The next discriminating step is an eight-/nine-support candidate with exact image rank and source-form residues in this carrier. Neither the current carrier nor a linear relaxation establishes history-to-cell matching, global coverage, or the analytic `n^-2` completion law.

Run `uv run --with sympy python research/nima/checkers/check_nine_point_determinantal_fibre.py`. Artifact: `research/nima/results/nine-point-determinantal-fibre.json`.
