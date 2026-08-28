# A single normal holonomy cannot generate physical flavor mixing: WP943

## Question

Can WP942's boundaryless route derive a proper phenomenologically viable
`physical16` family when one source-selected Wilson holonomy is the complete
family-space constructor?

## Single-holonomy grammar

Let `W` be the unitary Wilson holonomy acting on the three-dimensional family
space.  Admit the strongest coefficient-independent single-source grammar in
which both Yukawa sectors are functions of the same normal operator:

\[
Y_u=f_u(W),
\qquad
Y_d=f_d(W),
\]

for polynomial, analytic, or continuous functional calculi on the finite
spectrum of `W`.  The functions may differ and may select nondegenerate mass
spectra.

Because `W` is normal, the spectral theorem diagonalizes every function of
`W` in the same family basis.  Therefore

\[
H_u=Y_uY_u^\dagger,
\qquad
H_d=Y_dY_d^\dagger
\]

belong to one commutative functional calculus and obey

\[
[H_u,H_d]=0.
\]

All commutator invariants vanish, including

\[
\operatorname{Im}\operatorname{Tr}[H_u,H_d]^3=0.
\]

For nondegenerate spectra the left diagonalizing bases coincide, so the CKM
matrix is diagonal up to phases and permutations.  Degeneracies enlarge the
unphysical stabilizer but do not produce a faithful measured mixing pattern.

## Exact witness and repair cost

Take

\[
W=\operatorname{diag}(1,-1,i),
\]

with two distinct polynomials for the Yukawa sectors.  Their exact Grams are
diagonal and commute, regardless of the polynomial coefficients.

A genuinely mixed comparator is

\[
H_u=\operatorname{diag}(1,2,4),
\qquad
H_d=
\begin{pmatrix}
2&1&i\\
1&3&1\\
-i&1&5
\end{pmatrix}.
\]

The leading principal minors of `H_d` are `2,5,20`, so it is positive
definite, while

\[
\operatorname{Tr}[H_u,H_d]^3=-36i.
\]

Thus a viable CP-odd family requires a second source object not contained in
the functional calculus of `W`.  Merely assigning arbitrary independent
Yukawa matrices at a marked point would restore the full flavor fiber and
select nothing.

## Groupoid and time typing

The Wilson phase is relational under the boundaryless gauge groupoid.  No
absolute phase is inferred.  The theorem concerns simultaneous functional
calculus and quotient descent; it does not use temporal or causal ordering.

## Classification

A single selected holonomy is a source-derived spectral selector and basis
rigidifier, but its image lies in the commuting locus of `physical16`.  That
proper locus is experimentally excluded by nontrivial CKM mixing and CP
violation.  Hence the simplest boundaryless route descends, but descends to
the wrong physical family.

The smallest exact falsifier is the nonzero comparator invariant `-36i`.
The next constructor must supply at least two noncommuting, source-related
family operators with their relative orientation fixed independently of the
measured CKM data.  It must also derive the radius/threshold map and a
calibrated holonomy-sensitive instrument.  Algebraic span of two operators is
not executable control; the operations and ports must be physically typed.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp943_single_holonomy_physical16_commuting_no_go.py

Generated result:
`research/flavor/results/wp943_single_holonomy_physical16_commuting_no_go.json`.
