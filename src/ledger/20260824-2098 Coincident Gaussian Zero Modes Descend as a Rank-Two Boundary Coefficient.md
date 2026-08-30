# 2098 — Coincident Gaussian Zero Modes Descend as a Rank-Two Boundary Coefficient

## Question

Entry 2096 forced two occurrence-resolved Rees normals at a simultaneous
two-mode zero.  Test whether their two rank-one boundary coefficients glue
canonically when the degenerate source admits symplectic mode mixing.

## Frozen exact transition

Use mode-major coordinates \((q_1,p_1,q_2,p_2)\) and the passive symplectic
rotation

\[
S=
\begin{pmatrix}
c&0&s&0\\
0&c&0&s\\
-s&0&c&0\\
0&-s&0&c
\end{pmatrix},
\qquad
c=\frac35,
\quad s=\frac45.
\]

It is orthogonal and symplectic.  At the coincident zero, take

\[
h_0=\operatorname{diag}(0,1,0,1).
\]

Then

\[
Sh_0S^T=h_0.
\]

Thus \(S\) is an actual source stabilizer, not a change to the physical
quadratic source.

## Boundary coefficients

In one labelled frame, the two first Rees coefficients are

\[
B_1=\frac12E_{q_1q_1},
\qquad
B_2=\frac12E_{q_2q_2}.
\]

Under the source stabilizer,

\[
B_i\longmapsto B_i'=SB_iS^T.
\]

The exact rational audit gives

\[
B_1'\ne B_1,
\qquad
B_2'\ne B_2,
\]

while

\[
\boxed{B_1'+B_2'=B_1+B_2.}
\]

Therefore the individual rank-one lines are frame-dependent at the coincident
degeneracy, even though they transform covariantly away from it.  Their sum is
the canonical coefficient on the two-dimensional soft \(q\)-plane.

## Narrow result

\[
\boxed{
\text{At coincident zero modes, the multi-Rees coefficients descend as a
rank-two associated bundle, not as two canonically split lines.}
}
\]

The labelled normal geometry remains necessary: it constructs the two local
grades and their transition.  But the enhanced source stabilizer prevents a
canonical splitting on the deepest stratum.

This is coefficient descent over an existing Carrier intersection.  No new
Carrier incidence is required.  The correct datum is

\[
\text{resolved normal cone}
+\text{stabilizer representation}
\longrightarrow
\text{unsplit boundary coefficient bundle}.
\]

## Next falsifier

Replace the passive constant stabilizer by a genuinely coupled positive
two-mode quadratic family approaching the coincident corner.  Derive its
spectral projectors and connection before taking the limit.  Test whether the
rank-two boundary bundle has nontrivial holonomy around the frequency-collision
locus.  Trivial holonomy closes the Gaussian descent locally; nontrivial
holonomy would be sector-specific coefficient transport, not automatically a
new Carrier cell.

## Durable evidence

- `research/benincasa/checkers/two_mode_gaussian_rees_descent.py`
- `research/benincasa/checkers/results/two-mode-gaussian-rees-descent.json`
- Ledger allocation: `seqclaim-ebf975933d2458c20073af66`

