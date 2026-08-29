# Three-system defect pairing and the first interaction holonomy

## Question

What changes when three tiny-tail systems are paired, and which closure effects exist only at three-system level?

## Claim boundary

For completed systems \(A_j:H_j\to K_j\), first pass to their finite defect spaces

\[
\mathsf K_j=\ker A_j,\qquad
\mathsf C_j=\operatorname{coker}A_j.
\]

After the invertible bulk complements are eliminated, every finite-rank interaction is controlled by a reduced defect matrix

\[
D:\bigoplus_{j=1}^3\mathsf K_j
\longrightarrow
\bigoplus_{j=1}^3\mathsf C_j.
\]

The coupled system can be invertible only if total defect dimensions match and \(D\) is invertible. This is the universal three-system gate.

### Charge-balance obstruction

The total Fredholm index is

\[
\operatorname{ind}(A_1\oplus A_2\oplus A_3)
=
\sum_{j=1}^3\operatorname{ind}A_j.
\]

Compact interactions preserve this sum. Three unit charges chosen only from \(+1\) and \(-1\) can never sum to zero. Therefore three same-size singly charged systems cannot close by compact pairing alone.

The minimal charge-balanced triples have forms such as

\[
(+1,-1,0),\qquad
(+1,+1,-2),\qquad
(-1,-1,+2).
\]

Alternatively, each subsystem may have index zero but retain one kernel and one cokernel; then the total charge vanishes while a three-by-three defect pairing is still required.

### Perfect-matching criterion

Construct a bipartite graph whose left vertices are kernel defect lines and whose right vertices are cokernel defect lines. An authorized interaction arrow contributes an edge exactly when its induced defect coefficient is nonzero.

A necessary condition for closure is a perfect matching. For generic coefficients it is also sufficient: the determinant of \(D\) contains one monomial for each perfect matching. If symmetry or signs make all matching monomials cancel, the graph is combinatorially adequate but the typed pairing still fails.

This turns constructor synthesis into a finite incidence problem before analytic conditioning is considered.

### Directed triangle

Assume each system has one kernel and one cokernel and only cyclic cross-arrows are admitted:

\[
D_{\triangle}
=
\begin{pmatrix}
0&0&c_{31}\\
c_{12}&0&0\\
0&c_{23}&0
\end{pmatrix}.
\]

Then

\[
\det D_{\triangle}=c_{12}c_{23}c_{31}.
\]

All three defects are paired exactly when every edge of the directed cycle is nonzero. Deleting any one arrow restores a one-dimensional kernel and cokernel.

This is the first interaction architecture whose closure depends on a loop rather than a single bridge.

### The first gauge-invariant holonomy

Rephase the three defect frames by nonzero scalars \(g_1,g_2,g_3\). Edge coefficients transform as

\[
c_{ij}\longmapsto g_jc_{ij}g_i^{-1}.
\]

Individual edge phases are frame-dependent. Around the triangle, however,

\[
\Omega=c_{31}c_{23}c_{12}
\]

transforms by conjugation; in the scalar case it is invariant. A two-system bridge has no corresponding independent loop invariant because its single phase can be absorbed into endpoint frames.

Thus three-system pairing creates the first genuine interaction holonomy:

- additive lens: the loop records a summed cocycle or total defect;
- determinant-line lens: it records a product magnitude and phase;
- ordered noncommutative lens: it records the conjugacy class of the ordered product.

This is where the coefficient lens first changes not only readout but the law of composition.

### Symmetric versus skew pairing

For a real symmetric triangle interaction

\[
D_{\mathrm{sym}}
=
\begin{pmatrix}
0&a&c\\
a&0&b\\
c&b&0
\end{pmatrix},
\qquad
\det D_{\mathrm{sym}}=2abc.
\]

All three modes are gapped when \(abc\ne0\). For equal couplings \(a=b=c=\varepsilon\), the eigenvalues are

\[
2\varepsilon,-\varepsilon,-\varepsilon.
\]

The common mode separates from a two-dimensional differential sector.

For a real skew-symmetric pairing

\[
D_{\mathrm{skew}}^T=-D_{\mathrm{skew}},
\]

every three-by-three determinant vanishes. At least one zero mode survives. Hence an odd number of real defects cannot be fully paired by a purely antisymmetric interaction. Closure then requires a fourth mode, a diagonal term, complexification, or a change of coefficient lens.

This is a decisive three-system falsifier invisible in the two-system case.

### Scalar shadows

Under cyclic symmetry, pass to the three Fourier modes of the system label:

\[
x_0=x_1+x_2+x_3,
\]

and two nontrivial cyclic-character modes \(x_\omega,x_{\omega^2}\). A scalar sum sees only \(x_0\). It can therefore report perfect common-mode coherence while the two-dimensional differential sector contains a kernel, phase frustration, or nontrivial holonomy.

Three-system scalar agreement is consequently even less informative than two-system equality comparison. At least two independent relational ports are required to reconstruct arbitrary labelled amplitudes; a loop-holonomy port is additionally required when ordered composition matters.

### Conditioning and completion

Finite closure requires \(\det D_X\ne0\). Completion-stable closure requires the smallest singular value to obey

\[
\inf_X\sigma_{\min}(D_X)>0
\]

along with uniform bounds on the bulk inverses.

A nonzero loop product alone is insufficient: one edge may tend to zero while another diverges, leaving the determinant fixed but the condition number unbounded. The correct certificate is the full singular-value profile in the source-derived defect metrics.

### Prediction for three reciprocal or cutoff systems

If three theta/Tate subsystems are composed, the new datum is not a third copy of the tiny tail. It is the ordered triangle of incidence maps. The audit should ask:

1. do the three defect charges balance?
2. does the authorized arrow graph admit a perfect matching?
3. is the interaction symmetric, skew, sesquilinear, or ordered?
4. what loop holonomy survives changes of local source frame?
5. do all singular values remain uniformly positive?

A nontrivial loop phase with correct local edges is a new global sector, not a local inconsistency.

## Disposition

Three-system pairing introduces two structures absent from the two-system problem: a perfect-matching condition across a defect network and a gauge-invariant loop holonomy. It also exposes an odd-dimensional obstruction: purely real skew pairing cannot gap three defect modes.

The most promising finite model is the directed three-cycle. It isolates one coefficient per incidence edge, makes arrow deletion maximally diagnostic, and separates scalar, determinant-phase, and ordered-holonomy lenses. If the programme's missing coherencer is genuinely compositional rather than merely corrective, its first unmistakable signature should appear as this three-system loop invariant.