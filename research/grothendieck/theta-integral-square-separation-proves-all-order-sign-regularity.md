# Integral square separation proves all-order sign regularity

## Bounded question

Is the discrete conjecture of packet 111 true at every order, or does a later
faithful winding tuple eventually reproduce the continuous collision?

## Mode-adjunction recurrence

Recall

\[
 P_r(y_1,\ldots,y_r)
 =\sum_{j=0}^r(-1)^{r-j}2^j(2r-2j+1)!!\,e_j(y_1,\ldots,y_r).
\]

Write `Y=(y_1,...,y_(r-1))` and let

\[
 \mathcal E_Y=\sum_{i=1}^{r-1}y_i\partial_{y_i}
\]

be the Euler operator.  Splitting
`e_j(Y,y_r)=e_j(Y)+y_re_(j-1)(Y)` gives the exact recurrence

\[
 \boxed{
 P_r(Y,y_r)
 =\bigl(2y_r-(2r+1)\bigr)P_{r-1}(Y)
 +2\mathcal E_YP_{r-1}(Y).}
\]

Using `partial_i P_(r-1)=2P_(r-2)(Y without y_i)`, this becomes

\[
 P_r(Y,y_r)
 =\bigl(2y_r-(2r+1)\bigr)P_{r-1}(Y)
 +4\sum_{i=1}^{r-1}y_iP_{r-2}(Y\setminus y_i).
\]

## Induction on distinct integral winding modes

Let

\[
 y_i=\pi t n_i^2,
 \qquad
 t\ge1,
 \qquad
 1\le n_1<\cdots<n_r.
\]

Distinctness implies `n_r>=r`.  Therefore

\[
 2y_r-(2r+1)
 \ge2\pi r^2-(2r+1)
 >6r^2-(2r+1)>0.
\]

The base cases are

\[
 P_0=1,
 \qquad P_1(y_1)=2y_1-3>0.
\]

Assume the theorem for all smaller orders and all faithful subsets.  Every
`P_(r-1)(Y)` and every deletion minor `P_(r-2)(Y without y_i)` in the
recurrence is positive.  Their coefficients are positive as well.  Hence

\[
 \boxed{
 P_r(\pi tn_1^2,\ldots,\pi tn_r^2)>0}
\]

for every order `r`.

## All-order theorem

Restoring the positive row and column factors and the fixed Vandermonde
orientation yields:

> **Integral completed-circle sign-regularity theorem.** For every `r>=1`,
> every `1<=t_1<...<t_r`, and every distinct positive winding labels
> `1<=n_1<...<n_r`, the evaluation determinant of
> `b(t,n^2)` has the canonical nonzero sign.

Equivalently, the completed circle spectral family is a discrete extended
complete Chebyshev system of every finite order on the authorized integral
spectrum.

The proof uses no finite census and no limiting assumption.  Its mathematical
force comes from the quadratic separation law `n_r^2>=r^2`, which dominates
the linear rank cost `2r+1` in the adjunction recurrence.

## Explanation

The continuum carrier permits arbitrarily many nearly coincident modes near
the completion fold, and it fails at order seven.  The arithmetic source does
not.  Each additional independent winding label must occupy a new square, so
the spectral separation accelerates faster than the obstruction grows:

\[
 \boxed{
 \text{rank cost }O(r)
 \quad<\quad
 \text{integral-square separation }O(r^2).}
\]

This is a hard-to-vary Explanation for why integrality becomes dynamically
protective only after several coupled modes are present.  Low orders cannot
distinguish the discrete source from its continuum relaxation; order seven is
the first level at which the distinction becomes visible.

## RH boundary

This theorem proves all-order sign regularity of the **labelled spectral
kernel** `b(t,n^2)`.  It does not yet prove that the summed Riemann kernel
`Phi(u)=sum_n b(e^(2u),n^2)` is a Pólya-frequency kernel of infinite order, nor
that its cosine transform has only real zeros.  Infinite positive summation
can lose strict finite-rank information unless the summation map is shown to
preserve the relevant variation-diminishing class.

The next gate is therefore precise:

> Does source-authorized summation over the integral winding labels preserve
> the all-order sign regularity strongly enough to put `Phi` in the required
> Schoenberg/Pólya class?

The smallest falsifier is a finite positive sum of authorized winding columns
whose translation kernel has a wrongly oriented minor.  The theorem here
forbids blaming such failure on the labelled carrier; it would locate the
obstruction exactly at scalar aggregation.

## Supersession

Packet 110 remains the exact continuous-relaxation falsifier. Packet 111
proved faithful order seven. This packet proves the discrete conjecture at all
orders and supersedes its conjectural status.
