# Gauge and radiative closure of the FDM-2 mediator (WP91)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Admitted source and quotient claim

This packet audits only the proposed WP90 source. It does not promote that
model to an observed UV completion. Take

\[
Q_L\sim(3,2,1/6),\quad H\sim(1,2,1/2),\quad
d_R,D_L,D_R\sim(3,1,-1/3),\quad S\sim(1,1,0).
\]

Then every WP90 mediator vertex has zero total hypercharge and contracts to
an `SU(3)c x SU(2)L` singlet. The new fermions form a vectorlike pair, so their
left-handed anomaly contributions cancel. No generation-basis reference or
texture chart is introduced.

## CP-allowed counterterm space

For `S=x+i y` with CP `y -> -y`, the complete real, gauge- and CP-invariant
renormalizable scalar basis is

\[
\{x^i y^{2j}: i+2j\leq4\}.
\]

It contains nine monomials (eight after discarding the constant). The compact
three-square form used in WP90 is therefore not closed under generic allowed
counterterms. Its exact coordinates `4/5 +/- 3i/5` require renormalized
coefficient conditions at a declared scale; neither CP nor gauge symmetry
protects those numbers.

This is not a failure of the qualitative selector. At either WP90 vacuum the
exact scalar Hessian is

\[
\operatorname{Hess}V=\operatorname{diag}(306/25,144/25).
\]

It is positive definite with smallest eigenvalue `144/25`. By the implicit
function theorem, sufficiently small CP-preserving coefficient perturbations
retain a conjugate pair of nearby strict local minima with nonzero `y`.
Continuity likewise retains the nonzero commutator determinant in a
sufficiently small neighborhood. Thus the proper physical16 attribute
`J != 0` is locally robust, while the numerical vacuum coordinate and the
magnitude of `J` are not source predictions without extra renormalization
data or a protecting symmetry.

## Classification and falsifier

The proposed source remains a **selector** of the CP-broken union and not a
texture rigidifier. Its Schur-complement readout descends to weak-basis
invariants. The smallest exact radiative-closure falsifier is the allowed
counterterm `epsilon*x`: it preserves gauge symmetry and CP but shifts the
stationarity equation at `(4/5,+/-3/5)` by `epsilon`, so the advertised exact
vacuum coordinates cease to be stationary for every nonzero `epsilon`.

The surviving instrument gate is physical rather than algebraic: establish a
real singlet/vectorlike-quark sector and a finite-temperature quench/reset
whose effective potential stays in the CP-broken basin. Collider bounds,
threshold matching, nucleation, and bath errors remain untyped.

Verification: `uv run --with sympy python
research/flavor/checkers/wp91_fdm2_gauge_radiative_closure.py`.
