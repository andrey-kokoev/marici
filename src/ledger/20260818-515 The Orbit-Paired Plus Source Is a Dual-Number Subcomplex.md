# The Orbit-Paired Plus Source Is a Dual-Number Subcomplex

The generator-filtered complex of Entry 514 admits a source-level deck
diagonalization.  For a labelled monomial `a^i b^j` in the minus lattice,
let `x_-` and `x_+` denote its two orbit-labelled copies.  The plus
eigenvector is

\[
x_-+\tau(-1)^i x_+,
\]

where

\[
\tau_p=(-1)^{e_b},\qquad
\tau_q=(-1)^{e_b+1}.
\]

The deck involution fixes `u`, acts on scalar coefficients by `a -> -a`,
and acts on the gradient frames with characters `(-,+,+)`.  Consequently
the eigenspace decomposition is `R=Q[u]/(u^2)`-linear.

The executable checker forms every plus eigenvector before applying the
differential.  Its scalar image is deck invariant, its gradient image is
invariant after including the frame characters, and its `u`-multiple
remains invariant.  The verified plus source ranks over `R` are

\[
\begin{array}{c|rrrr}
D&12&16&20&24\\\hline
\operatorname{rank}_R A_D^+&226&530&962&1522.
\end{array}
\]

Thus the plus sector is an actual dual-number subcomplex, not a projection
of target rows after column admission.  The next computation may now build
the finite matrices of this plus complex and compute its genuine middle
homology and derived specialization.

## Evidence

- `research/benincasa/check_soft_axis_labelled_total_truncation.py`
- Entries 514 and 105.
