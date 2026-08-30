# Joint trace surjectivity reduces to a contractive overlap correction

## Local lifts are not enough

Let the complete boundary space be the Hilbert sum

\[
\mathcal H_{\partial}
=
\bigoplus_{j\in J}\mathcal H_j,
\]

where \(j\) ranges over wall, endpoint, prime, square, connected,
archimedean, and response strata after horizontal descent.

Suppose each coordinate trace

\[
\Gamma_j:\operatorname{Dom}A_{\max}\to\mathcal H_j
\]

has a bounded local lift

\[
R_j:\mathcal H_j\to\operatorname{Dom}A_{\max},
\qquad
\Gamma_jR_j=I.
\]

The naive assembled lift is

\[
R_0b=\sum_jR_jb_j.
\]

It need not be a right inverse for the joint trace because a lift for one
stratum can generate traces in another.

## Overlap matrix

Define the block overlap operator

\[
K=\Gamma R_0-I
\]

on \(\mathcal H_{\partial}\). Its blocks are

\[
K_{ij}
=
\Gamma_iR_j-\delta_{ij}I.
\]

Then

\[
\Gamma R_0=I+K.
\]

If \(I+K\) is invertible, the corrected joint lift is exactly

\[
R=R_0(I+K)^{-1},
\]

and

\[
\Gamma R=I.
\]

Thus joint trace surjectivity is a boundary overlap problem, not a collection
of independent local extension theorems.

## Contractive sufficient condition

A clean sufficient condition is

\[
\|K\|\le1-\delta_{\mathrm{tr}}
\]

for some \(\delta_{\mathrm{tr}}>0\). Then the Neumann inverse exists and

\[
\|(I+K)^{-1}\|
\le
\frac1{\delta_{\mathrm{tr}}}.
\]

Consequently,

\[
\|R\|
\le
\frac{\|R_0\|}{\delta_{\mathrm{tr}}}.
\]

This gives the uniformly bounded right inverse required by the complete
boundary-triple theorem.

The sign is important: the exact obstruction is \(-1\in\sigma(K)\).
Contractivity is stronger than necessary but converts the source audit into a
falsifiable uniform margin.

## Schur elimination by strata

The overlap system should be eliminated in source order:

1. positive theta endpoint port;
2. wall--jump observer frame;
3. primitive and square prime histories;
4. connected Schatten stratum;
5. archimedean determinant line;
6. horizontal Fourier response equalizer.

At each stage, the new coordinate is corrected against the already fixed
ones. If the corresponding diagonal Green block is coercive, the correction
is a Schur return.

The final right inverse is a product of triangular corrections. Therefore
cellwise invertibility is insufficient: the composite and its inverse must
remain uniformly bounded.

## Relation to the five margins

The overlap matrix decomposes according to the same coherent and disagreement
modes as the global Green system.

- Prime and analytic observability control local lift norms.
- Glue transversality controls seam overlap.
- Diagonal observability prevents a common trace mode from disappearing.
- Mixed cancellation controls the terminal off-diagonal blocks.

These margins do not automatically prove \(\|K\|<1\). The source must derive a
comparison between the overlap operator and the complete Green Gram. But the
decomposition shows where each block estimate belongs.

The trace margin is upstream logically: if \(-1\) enters the overlap spectrum,
the declared Green carrier omits a deficiency direction and the later five
margins are being measured on the wrong boundary quotient.

## Prime-diagonal simplification

If twisted Mellin equivariance proves exact prime diagonality, then the
prime-sector part of \(K\) is a direct sum

\[
K_{\mathrm{prime}}
=
\bigoplus_p K_p.
\]

Uniform invertibility becomes

\[
\inf_p
\sigma_{\min}(I+K_p)>0.
\]

This avoids a full cross-prime Schur estimate. Without exact equivariance,
entrywise local bounds do not control the assembled overlap operator.

## Horizontal descent qualification

The Fourier orbit presentations must first descend to the horizontal
equalizer. Building \(R_0\) on the orbit direct sum creates four copies of
each physical trace and can make \(I+K\) appear singular for a purely
representational reason.

The correct order is:

\[
\text{local orbit lifts}
\longrightarrow
\text{intertwining proof}
\longrightarrow
\text{horizontal descent}
\longrightarrow
\text{joint overlap inversion}.
\]

## Completion theorem

For cutoffs \(X\), let

\[
K_X=\Gamma_XR_{0,X}-I.
\]

A sufficient completion package is:

\[
\sup_X\|R_{0,X}\|<\infty,
\qquad
\sup_X\|K_X\|\le1-\delta,
\]

together with strong graph convergence of \(R_{0,X}\), \(\Gamma_X\), and
\(K_X\) on the declared stratified carrier.

Then

\[
R_X=R_{0,X}(I+K_X)^{-1}
\]

is uniformly bounded, and its limit is a right inverse for the completed
trace.

Finite surjectivity without the uniform spectral gap permits approximate
boundary vectors whose minimal lift norm diverges.

## Minimal hostiles

1. Every \(\Gamma_j\) is onto, but two local lifts create equal and opposite
   cross-traces, so \(-1\in\sigma(K)\).
2. Every finite \(I+K_X\) is invertible, but its smallest singular value tends
   to zero.
3. Prime-diagonal blocks are controlled while coherent off-prime overlap
   creates an approximate \(-1\)-eigenvector.
4. The orbit direct sum fails although the horizontal equalizer passes.
5. The corrected traces are onto, but the triangular correction maps are not
   uniformly bi-bounded.

## Verdict

The complete trace theorem now has an explicit constructive target. Build
source-local lifts, compute their typed overlap matrix, and invert the single
boundary operator \(I+K\).

The earliest missing calculation is the finite overlap matrix for the
wall--endpoint--prime packet. If its normalized norm is strictly below one in
the source metric, the same Neumann correction yields the first genuine joint
right inverse. The remaining strata can then be added by controlled Schur
steps.
