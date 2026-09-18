# Exact support theorem for the NNMHV (2,3) component

Write the generalized invariant with anchor `r`, pair `a<b`,

\[
L=\langle\xi|x_{ra}\widetilde x_{ab},\qquad
R=\langle\xi|x_{rb}\widetilde x_{ba}.
\]

Since `x_rb=x_ra+x_ab`, `x_ba=-x_ab`, and `x_ab \widetilde x_ab=x_ab^2 I`,

\[
L+R=-x_{ab}^2\langle\xi|.
\]

For an ordinary invariant (`r=n`), the coefficient of `eta_j` vanishes for `j<a`. Hence an outer invariant can contain `eta_2` only when `a_1=2`.

For a right-nested inner invariant, `a_2\ge b_1\ge4`, so both `eta_2` and `eta_3` coefficients vanish. Its `(2,3)` wedge is zero.

For a left-nested inner invariant the anchor is `r=a_1=2`. For `2\le j<a_2`,

\[
q_j^{\rm inner}=x_{a_2b_2}^2\langle\xi_{\rm inner}j\rangle.
\]

The outer pair is `(2,b_1)`, and its coefficients for `j<b_1` are

\[
q_j^{\rm outer}=\langle\xi_{\rm inner}j\rangle,
\qquad
\langle\xi_{\rm inner}|=\langle n|x_{nb_1}\widetilde x_{b_1 2}.
\]

If `a_2>3`, both labels 2 and 3 lie below `a_2`, so the two coefficient rows are proportional and

\[
q_2^{\rm outer}q_3^{\rm inner}-q_3^{\rm outer}q_2^{\rm inner}=0.
\]

The only generic nonzero case is therefore

\[
\boxed{\text{left-nested},\quad a_1=2,\quad a_2=3.}
\]

Its histories are indexed by

\[
5\le b_2\le b_1\le n-1,
\]

so their number is

\[
\sum_{b_1=5}^{n-1}(b_1-4)=\frac{(n-5)(n-4)}2.
\]

For each supported history the exact normalized summand is

\[
T_n(b_1,b_2)=
\frac{K_{2b_1}K_{b_1 2;3b_2}^{0;2b_1}}{\langle23\rangle^4}
\left(q^{\rm outer}_2q^{\rm inner}_3-q^{\rm outer}_3q^{\rm inner}_2\right)^4,
\]

including the transported upper endpoint when `b_2=b_1`. Thus

\[
\widehat C_{23}(n)=\sum_{5\le b_2\le b_1\le n-1}T_n(b_1,b_2).
\]
