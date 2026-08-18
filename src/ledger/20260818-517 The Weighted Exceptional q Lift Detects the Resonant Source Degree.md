# The Weighted Exceptional q Lift Detects the Resonant Source Degree

Work on the Newton-adapted blowup `Bl_(u,a^2)` with

\[
\nu(a)=1,\qquad \nu(u)=2,
\]

and write `f=a^i b^j`.  Away from `b=+-1`, the leading terms of
`L_1=b+1-u` and `L_2=a+-u/2` are `b+1` and `a`.  Hence

\[
m_0=a^{i+e_b}b^j(b+1)^{e_a}.
\]

For the labelled `q` operator, the leading principal coefficient is

\[
(C_q)_0=(i-s_b)a^{i+e_b-1}b^j(b+1)^{e_a},
\]

where `e_b=2-s_b`.  Therefore the equal-valuation terms in the first
component of the full lift reduce to

\[
\begin{aligned}
(\widehat H_q)_{a,0}
&=-\frac32m_0+\frac a4(C_q)_0\\
&=\frac{i-s_b-6}{4}
a^{i+e_b}b^j(b+1)^{e_a}.
\end{aligned}
\]

Thus the generic exceptional order jumps exactly when

\[
\boxed{i=s_b+6.}
\]

For `s_b=1` this is the previously observed odd resonance degree `i=7`;
for `s_b=0` it is `i=6`.  The cancellation is source-derived from the
labelled coefficient `C_q`; it is invisible in an unlabelled gradient
span or in a generic minimum-of-valuations table.

The other generic leading components are

\[
(\widehat H_q)_{u,0}
=\frac{u}{2}(i-s_b)
a^{i+e_b-1}b^j(b+1)^{e_a},
\]

and, for the `p` operator,

\[
(C_p)_0=
a^{i+e_b}b^{j-1}(b+1)^{e_a-1}
\bigl[-j(b+1)+s_a b\bigr],
\]

with `(Hhat_p)_b=3m/2`.  These formulas must be restricted separately at
the endpoints.  At `b=-1`, `L_1=-u`, so sectors with `e_a=2` vanish modulo
`u^2` and sectors with `e_a=1` acquire an extra exceptional factor `u`.
At `b=1`, `L_1=2-u` remains a unit but `c=1-b^2` vanishes, changing the
gradient rank.

The next chart calculation must therefore retain the resonant `q` source
degree as a separate exceptional summand and glue it with the two endpoint
complexes; a single generic residual bundle is not flat across these
strata.
