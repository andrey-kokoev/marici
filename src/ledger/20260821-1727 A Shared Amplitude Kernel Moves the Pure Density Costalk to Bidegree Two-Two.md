# 1727 — A Shared Amplitude Kernel Moves the Pure Density Costalk to Bidegree Two-Two

## Nontransverse rank-drop test

Take two singular amplitude maps with a common kernel:

\[
f_\varepsilon=\operatorname{diag}(1,\varepsilon),
\qquad
g_\eta=\operatorname{diag}(1,\eta).
\]

Their composite is

\[
g_\eta f_\varepsilon
=\operatorname{diag}(1,\varepsilon\eta).
\]

## Multi-Rees packet

For \(|u\rangle=(a,b)^T\), the direct density is

\[
\boxed{
\rho_{\varepsilon,\eta}
=
\begin{pmatrix}
a^2&\varepsilon\eta ab\\
\varepsilon\eta ab&\varepsilon^2\eta^2b^2
\end{pmatrix}.
}
\]

The common-kernel amplitude has bidegree \((1,1)\).  Consequently the
image–kernel density term also has bidegree \((1,1)\), while the pure kernel
density has bidegree \((2,2)\).

Iterated specialization gives the same packet.  No classes occur at
\((2,0)\) or \((0,2)\); inserting them would double-count the shared kernel.

## Diagonal specialization

On \(\varepsilon=\eta=t\), the cross term begins at ordinary order two and the
pure kernel costalk at order four:

\[
\rho_t=
\begin{pmatrix}
a^2&t^2ab\\t^2ab&t^4b^2
\end{pmatrix}.
\]

Thus a first- or second-grade-only audit can miss the pure supported quantum
kernel under repeated nontransverse readout.

## Narrow result

The existing labelled multi-Rees calculus resolves the shared-kernel
intersection without excess Tor.  The essential requirement is preserving
the full multivaluation before diagonal specialization.  No new Cut carrier
stratum appears.

## Durable artifacts

- `research/benincasa/checkers/shared_kernel_multirees_hermitian.rs`
- `research/benincasa/results/shared-kernel-multirees-hermitian.json`
- `research/benincasa/shared-kernel-multirees-hermitian.md`

## Next falsifier

Test a length-three chain of shared-kernel singular maps.  Determine whether
the pure density costalk always occurs at twice the summed amplitude valuation,
or whether repeated derived intersections generate an independent extension.
