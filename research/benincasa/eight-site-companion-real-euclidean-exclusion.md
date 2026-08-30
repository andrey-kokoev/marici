# Eight-site companion discriminants miss the real-Euclidean routing cone

## Frozen question

After imposing the source base relations, the 36 cyclic orbit representatives (288 labelled occurrences) of rank-four C8 walls reduce to four patterns:

| pattern | orbit count |
|---|---:|
| surviving edge 1, free even edges | 21 |
| surviving edge 8, free odd edges | 7 |
| surviving edge 6, free odd edges | 6 |
| surviving edge 4, free odd edges | 2 |

The universal linear factors were already excluded from the real-Euclidean routing cone. This audit asks whether the remaining companion Jacobian factor can vanish together with the four cover equations when all five retained edge squares are strictly positive and the full C8 routing Gram matrix is positive semidefinite.

## Reduction

Write the retained edge squares as

\[
A=a^2,\quad B=b^2,\quad C=c^2,\quad D=d^2,\quad Z=z^2.
\]

The deck-even substitution halves the polynomial degrees without changing real feasibility. Two patterns are directly `unsat` in exact QF_NRA:

\[
B_8=\varnothing,\qquad B_6=\varnothing.
\]

For family A, eliminate the linearly occurring \(C,D\), then solve the remaining linear equations for \(A,Z\). For \(B_4\), eliminate \(D\), then solve linearly for \(A,C,Z\). In both cases the final cover equation is quadratic in \(B\).

Its discriminant factors as

\[
\Delta_A
=196k^2(7k+6)^2D_A(k,l)^2F_A(k,l)G_A(k,l),
\]

and

\[
\Delta_{B_4}
=-8k^2(7k+6)^2D_{B_4}(k,l)^2F_{B_4}(k,l)G_{B_4}(k,l).
\]

The complete factors are serialized in the result packet. Exact QF_NRA sign tests on the C8 PSD polygon prove

\[
\Delta_A<0,
\qquad
\Delta_{B_4}<0.
\]

The same tests prove that neither discriminant vanishes on the PSD polygon. Since the potentially exceptional linear-solve denominators \(D_A,D_{B_4}\) occur squared in the discriminants, their zero loci also miss that polygon. No denominator branch was discarded.

## Narrow result

\[
\boxed{
\text{None of the 36 source-base-reduced C8 companion-wall orbits meets the generic real-Euclidean routing cone.}
}
\]

Together with the prior linear-factor exclusion, all 288 labelled occurrences are dormant for a continuation that retains real nonnegative edge squares and positive-semidefinite C8 routing geometry.

This does **not** exclude activation after complexifying the routing variables, and it does not identify a physical Leray pairing in the complex domain.

## Durable artifacts

- `marici-gm/src/bin/eight_site_base_reduced_companion_models.rs`
- `results/eight-site-base-reduced-companion-models.json`
- `checkers/eight_site_companion_feasibility.py`
- `checkers/eight_site_companion_nlsat.py`
- `checkers/eight_site_companion_boundary_ideals.py`
- `checkers/eight_site_companion_rational_reduction.py`
- `checkers/eight_site_companion_discriminant_sign.py`
- `checkers/eight_site_companion_exceptional_compatibility.py`
- `results/eight-site-companion-discriminant-sign.json`
