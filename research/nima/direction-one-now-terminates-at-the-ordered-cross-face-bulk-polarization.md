# Direction one now terminates at the ordered cross-face bulk polarization

## Reconciled closed stages

The source record already closes more of the finite primewise programme than
the preliminary ledger suggested:

1. moving-seam covariance of the resolved saturated three-port graph;
2. endpoint attachment naturality and rank-two faithfulness;
3. Fourier-orbit and cutoff compatibility;
4. radical descent for the resolved graph;
5. anti-diagonal cancellation of the complete typed external boundary flux.

In particular,

\[
\mathfrak b_\partial^+
-\mathfrak b_\partial^-
+\mathfrak F_B=0.
\]

No additional seam, endpoint, or external-port correction is needed.

## Surviving local datum

Green integration by parts splits as

\[
\langle DK,zK\rangle
=
\mathfrak b_\partial(K;z)
+
\mathfrak b_{\rm bulk}(K;z).
\]

After endpoint cancellation, the remaining phase-sensitive quantity is the
ordered cross-face polarization

\[
\boxed{
\mathcal C_z(K)=\langle DK,zK\rangle.
}
\]

The oriented face difference is

\[
\|x_+\|^2-\|x_-\|^2
=4\operatorname{Re}\mathcal C_z(K).
\]

Diagonal resolved-graph norms do not determine this value. The phase rotation
`DK -> exp(i phi) DK` preserves all diagonal energies and endpoint data while
changing `Re C_z`.

## Relation to the finite target ledger

The ordered polarization supplies the matrix information absent from the
positive direct-sum Gram. In the target Pauli ledger it controls the directed
`sigma_y/sigma_z` data which cannot be reconstructed from the `I/sigma_x`
energies alone.

Thus the four matrix-unit test and the bulk Green test are the same remaining
local problem in two coordinate systems:

\[
\{E_{11},E_{12},E_{21},E_{22}\}
\quad\leftrightarrow\quad
\mathcal C_z(\cdot,\cdot).
\]

## Relation to the homotopy prism

The endpoint and side-boundary terms already sew. The surviving ordered bulk
polarization is therefore the analytic value carried by the top prism/Toda
representative. A higher Green-system equivalence must null-homotope this
ordered form before scalar evaluation; cancelling its scalar real part is not
enough.

## Exact next construction

Expose `C_z` as a continuous sesquilinear form on the complete resolved source
domain and prove:

\[
\mathcal C_z(r,v)=
\mathcal C_z(v,r)=0
\]

for every even-bulk radical vector `r`. Then evaluate its four matrix units on
the rank-two prime endpoint image and compare with the required target table.

No source formula presently supplies this completed ordered polarization.
This is the irreducible local gate for direction one.