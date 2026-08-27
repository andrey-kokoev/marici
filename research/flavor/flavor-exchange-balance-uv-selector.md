# Exchange-balance UV selector: WP676

## Deutschian candidate explanation

The simplest hard-to-vary explanation of protected vertex balance is an exact
exchange of the two parity partners. For the species mass matrix

\[
\mathcal M=
\begin{pmatrix}
M_A&yJ_n\\
zJ_n&M_B
\end{pmatrix},
\]

invariance under \(A\leftrightarrow B\) forces

\[
M_A=M_B,
\qquad
y=z.
\]

This selects a proper subspace of the internal mass-block parameter space. It also
saturates the exact fixed-product erosion minimum

\[
y^4+z^4\geq2(yz)^2.
\]

## Why this is not yet a flavor selector

On the selected subspace, the product \(p=y^2\) remains free. The matched
coefficient

\[
c=-\frac{p}{M}
\]

still ranges continuously. Exchange removes reciprocal imbalance but fixes
neither the low-energy coefficient nor a proper physical16 family. It is a UV
factorization-fiber selector and backreaction minimizer, not a numerical
flavor selector.

## Pole-basis correction

Exact exchange also means the bare labels are not physical pole labels after
the frame background is inserted. For one generator eigenvalue \(j\), the
balanced mass block has eigenvalues

\[
M-yj,
\qquad
M+yj.
\]

Therefore WP674's abstract \(A\to B+n\) cascade cannot simply reuse the bare
exchange labels. The physical pole transitions and angular response must be
recomputed after diagonalizing the complete frame background. This is a basis
typing issue, not a claim that all cascades close.

## Disposition

WP681 corrects the authority of this statement. The independently typed
entrance and exit currents break (A\leftrightarrow B), so the exchange is not
a symmetry of the complete source grammar. It is an internal-block rigidifier
and erosion minimizer conditional on an unadmitted exchange of external source
objects, not a genuine source selector. Moreover, the balanced frame
fluctuation is diagonal in the pole basis and closes the proposed cross-pole
cascade exactly.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp676_exchange_balance_uv_selector.py

Generated result: results/wp676_exchange_balance_uv_selector.json.
