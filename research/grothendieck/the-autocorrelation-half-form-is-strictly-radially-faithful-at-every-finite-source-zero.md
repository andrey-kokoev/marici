# The autocorrelation half-form is strictly radially faithful at every finite-source zero

## The half-form

Let

\[
P(w)=\sum_{j=0}^n a_jw^j
\]

be a nonzero polynomial with real coefficients. Define its autocorrelation
coefficients

\[
C_k=\sum_{j=0}^{n-k}a_ja_{j+k}
\]

and analytic half-form

\[
A(w)=\frac{C_0}{2}+\sum_{k=1}^n C_kw^k.
\]

On the unit circle,

\[
2\operatorname{Re}A(e^{i\theta})
=|P(e^{i\theta})|^2.
\]

Therefore `Re A` is nonnegative on the boundary. By the Poisson formula and
the strong minimum principle,

\[
\operatorname{Re}A(w)>0
\qquad (|w|<1).
\]

No positivity assumption on the individual coefficients is needed.

## The oriented current at a zero

Define

\[
J(w)=\sum_{k=1}^n C_k(w^k-w^{-k}).
\]

The full reciprocal autocorrelation is

\[
P(w)P(w^{-1})
=C_0+sum_{k=1}^nC_k(w^k+w^{-k}).
\]

At a nonzero root of `P`, this expression vanishes. Consequently,

\[
J(w)=2A(w)
\qquad (P(w)=0).
\]

If the root lies outside the disk, the same identity written in the reciprocal
chart gives

\[
J(w)=-2A(w^{-1}).
\]

It follows that every nonzero root satisfies the exact trichotomy

\[
\begin{aligned}
|w|<1 &\Longrightarrow \operatorname{Re}J(w)>0,\\
|w|=1 &\Longrightarrow \operatorname{Re}J(w)=0,\\
|w|>1 &\Longrightarrow \operatorname{Re}J(w)<0.
\end{aligned}
\]

Thus the normal quadrature of the oriented autocorrelation current is strictly
faithful to radial displacement at every finite-source zero.

## Meaning for the programme

The proposed hostile—an off-seam zero with accidentally tangential current—
cannot exist for any finite real source packet. The failure to find it was not
numerical luck.

This closes the faithfulness half of the revised gate. For finite packets,

\[
P(w)=0
\quad\text{and}\quad
\operatorname{Re}J(w)=0
\quad\Longrightarrow\quad
|w|=1.
\]

The remaining burden is solely the polarization half: derive from completed
theta boundary conditions that a zero-state has zero normal current.

## Infinite-source boundary

The theorem does not yet establish the theta result. Passing to the completed
infinite source requires:

1. convergence of the autocorrelation coefficients or a source-native
   distributional replacement;
2. boundary values defining a positive-real half-form;
3. compatibility of truncations with the completed modular seam;
4. no loss of the strict sign through a nonuniform limit;
5. an independent zero-state law eliminating the normal current.

The first four are completion questions. The fifth is the remaining
RH-bearing constructor. But the earlier two-part uncertainty has collapsed:
once polarization is proved, radial faithfulness is already universal.

