# Full Seam Rank Does Not Imply Uniform Transversality

Let (K=\ker Q), let (R:K\to Z) be the operative residual, and let
(H:K\to Y) be the authorized seam observation. After the finite kernel gate

\[
\ker(H|_K)\subseteq\ker(R|_K),
\]

define the quotient lower-frame bound

\[
\beta(H,R)=
\inf_{x\in K,\ Rx\ne0}
\frac{\|Hx\|}{\|Rx\|}.
\]

The sharp restricted domination constant is

\[
C_{K}=\beta(H,R)^{-1}.
\]

At each finite cutoff, sufficient restricted rank is equivalent to
(\beta_N>0). Completion-stable repair requires the strictly stronger bound

\[
\inf_N\beta_N>0.
\]

## Full-rank hostile

Take (K=\mathbb R^2), (R=I), and

\[
H_\varepsilon=
\begin{pmatrix}
1&0\\
1&\varepsilon
\end{pmatrix}.
\]

For every (\varepsilon>0), (H_\varepsilon) has rank two and both row norms
remain bounded above and below. Yet for (x=e_2),

\[
\|H_\varepsilon x\|=\varepsilon,
\qquad
\|Rx\|=1,
\]

so (\beta(H_\varepsilon,R)\le\varepsilon) and the domination constant is at
least (1/\varepsilon). The rows become asymptotically collinear. Rank remains
complete while transversality collapses.

Adding the independently aligned row ((0,1)) gives

\[
\|H_\varepsilon^{\mathrm{full}}x\|^2
=x_1^2+(x_1+\varepsilon x_2)^2+x_2^2
\ge\|x\|^2,
\]

so the residual is uniformly dominated with constant at most one. Again, that
row is admissible only if source-authorized.

## Why principal angles alone are insufficient

For every finite (\varepsilon>0), the row space of (H_\varepsilon) is all
of (K^*), exactly the same space as the residual rows. Subspace principal
angles are therefore zero even while the lower-frame bound collapses. The
completion invariant is the smallest generalized singular value, not merely
row-space incidence.

Thus the compiler hierarchy is:

\[
\text{kernel inclusion}
\;<\;
\text{finite quotient rank}
\;<\;
\text{uniform quotient frame bound}.
\]

## Falsifiers

- Every cutoff has full seam rank but (\beta_N\to0).
- Row spaces coincide while the smallest singular value collapses.
- Individual row norms are bounded but rows become collinear.
- A repair row is selected after seeing the hostile rather than derived from
  the frozen constructor family.
- A cutoff-dependent basis change hides divergent condition numbers.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
9/10. Restricted rank, lower-frame bound, row norms, and domination constant
were frozen. Nearly collinear bounded rows were the hostile.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Full rank and even equality of row spaces were separated from uniform
repair. The exact completion datum is the generalized lower-frame bound, not a
principal-angle or rank certificate.
