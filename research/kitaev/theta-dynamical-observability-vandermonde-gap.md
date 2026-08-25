# Scalar dynamics can observe finite theta packets but clustered modes destroy uniformity

Owner: `marici.Kitaev`

## Bounded question

Can source dynamics reduce the discrete-port rank cost by making one scalar
output observable over time, and can that observability remain uniform as
arithmetic modes cluster?

## Finite diagonal theorem

Let a finite labelled coefficient state evolve by

\[
\dot c=Ac,
\qquad
A=\operatorname{diag}(\lambda_1,\ldots,\lambda_N),
\]

and let the scalar output be

\[
y=Jc,
\qquad J=(j_1,\ldots,j_N).
\]

The (N\)-step derivative observability matrix is

\[
\mathcal O_N=
\begin{pmatrix}
J\\JA\\ \vdots\\ JA^{N-1}
\end{pmatrix}
=V(\lambda_1,\ldots,\lambda_N)\operatorname{diag}(j_1,\ldots,j_N).
\]

Therefore

\[
\det\mathcal O_N
=\left(\prod_jj_j\right)
\left(\prod_{a<b}(\lambda_b-\lambda_a)\right).
\]

One scalar output observes the full finite state exactly when every modal
overlap is nonzero and the eigenvalues are distinct.

This does not contradict the instantaneous rank theorem. The resource has
moved from simultaneous output rows to (N\) time derivatives or samples and
to a source-derived evolution law.

## Degenerate modes

For a general generator, the PBH criterion requires

\[
\ker(\lambda I-A)\cap\ker J=0
\]

for every eigenvalue. If an eigenspace has geometric multiplicity (m\), at
least (m\) independent scalar output rows are necessary on that block. Hence

\[
r\ge\max_\lambda\dim\ker(\lambda I-A)
\]

is the dynamical output-rank lower bound.

For a repeated diagonal eigenvalue and one scalar row, a nonzero vector inside
that eigenspace can always be chosen orthogonal to (J\), giving the minimal
PBH witness.

## Clustered-mode completion collapse

Distinctness at every finite cutoff is not uniform separation. For three
modes (0,\delta,2\delta\),

\[
\det\mathcal O_3
=2\delta^3j_1j_2j_3.
\]

With bounded nonzero modal overlaps, the observation matrices remain
invertible for every \(\delta>0\), while their smallest singular values tend
to zero as \(\delta\to0\). The finite derivative reconstruction becomes
arbitrarily ill-conditioned.

Logarithmically adjacent arithmetic labels therefore reproduce the completion
obstruction even in the dynamical formulation. A uniform theorem needs a
spectral-gap estimate, a weighted time horizon growing with inverse spacing,
or a different source norm.

## Relation to the seam germ

The complete time/germ signal can be faithful even though one instantaneous
endpoint value is not. Its finite translate faithfulness is the continuous
analogue of the Vandermonde observability theorem. The full jet tower records
successive dynamical moments; it is not a single instantaneous rank-one
measurement.

For the actual theta programme, a matrix (A_X\) acting on the labelled
coefficient module has not yet been supplied with proof that its output orbit
equals the source seam germ. The theorem is therefore a compiler criterion,
not an instantiated theta dynamics claim.

## Hostile fixtures

1. Distinct modes and nonzero overlaps: observable with one scalar row.
2. One zero overlap: the corresponding eigenvector is invisible.
3. Repeated eigenvalue: a PBH vector survives inside the degenerate block.
4. Distinct but clustered modes: every finite matrix has full rank while the
   observability constant collapses.
5. Fitted dynamics: choosing eigenvalues from desired label separation lacks
   source authority.
6. Infinite time/jet access: mathematical faithfulness does not imply a finite
   executable instrument.

## Disposition

Dynamics can reduce simultaneous discrete-port dimension from (N\) to the
maximum geometric multiplicity, even to one at a simple spectrum. It pays with
temporal/jet depth and spectral conditioning. Without a source-derived
coefficient generator and a uniform gap/Gramian theorem, this does not repair
theta completion stability.

## Claim strength

Exact finite-dimensional observability theorem and clustered-spectrum
completion obstruction. No source-derived theta coefficient dynamics or
physical instrument is claimed.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_dynamical_observability.py`.
The result is written to
`research/kitaev/results/theta-dynamical-observability.json`.
