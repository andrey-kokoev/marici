# Uniform sewing descent is an authorized quasidiagonality gate

## Question

What exact operator property upgrades fixed-observer leakage convergence to
uniform compatibility of completed sewing with the cutoff family?

## Two leakage directions

Assume first that completed sewing is an endomorphism \(F:H\to H\) of one
common completed carrier and that \(P_n\) are the source-authorized finite-rank
cutoff projections. Relative to

\[
H=P_nH\oplus(I-P_n)H,
\]

the commutator has block form

\[
[P_n,F]
=
\begin{pmatrix}
0&P_nF(I-P_n)\\
-(I-P_n)FP_n&0
\end{pmatrix}.
\]

The upper-right block is incoming leakage from omitted source states into the
visible diagnostic. The lower-left block is outgoing leakage from visible
states into the omitted complement.

Because their domains and ranges are orthogonal,

\[
\lVert[P_n,F]\rVert
=
\max\left(
\lVert P_nF(I-P_n)\rVert,
\lVert(I-P_n)FP_n\rVert
\right).
\]

Therefore uniform two-sided descent is equivalent to

\[
\lVert[P_n,F]\rVert\longrightarrow0.
\]

## Correct name and authority boundary

With \(P_n\to I\) strongly and each \(P_n\) finite-rank, this is a
quasidiagonal approximation of \(F\). The programme needs more than abstract
quasidiagonality: the projections must be the actual source-authorized cutoff
filtration. Existence of a convenient unrelated filtration does not establish
descent for Euler diagnostics.

If forward and reverse sewing inhabit different carriers, the commutator is
not typed. One must instead retain the two off-diagonal naturality residuals
between the corresponding source and target projections. Only after a common
carrier is constructed may they be compressed into one commutator.

## Hostile shift

The backward shift has one unit edge crossing every standard cutoff. Hence
both the moving-boundary obstruction and the commutator norm remain one. Every
fixed observer is eventually reconciled, but the authorized filtration is not
quasidiagonal for that shift.

This shows why pointwise convergence could not finish the argument.

## Consequence for Fourier–Tate sewing

The next source theorem is now exact. Construct the completed common carrier
and prove one of:

1. the authorized cutoff projections asymptotically commute with sewing;
2. the two directed leakage blocks obey a stronger summable domination law;
3. the nonvanishing commutator converges to a separately typed boundary
   operator that must remain in the completed object.

The third outcome is not failure if the boundary operator is source-derived.
It means strict descent is the wrong target and the lax defect survives as a
physical port.

## DPC verdict

Uniform strictification is neither a vague compactness hope nor a consequence
of fixed-observer convergence. It is the authorized quasidiagonality gate
above.

Finite falsifier: one cutoff with a persistent unit crossing edge disproves
any claimed decay estimate for that filtration.

## Verification

The checker `check_authorized_quasidiagonality_gate.py` verifies the exact
commutator block identity on a finite hostile shift and a positive reducing
filtration fixture.

