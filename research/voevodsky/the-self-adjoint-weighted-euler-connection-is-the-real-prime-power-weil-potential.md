# The self-adjoint weighted Euler connection is the real prime-power Weil potential

## Correction to the raw derivative construction

The Euler contratower note conjugated

\[
D=-i\partial_s
\]

between weighted Hilbert spaces. On a nonconstant weighted space

\[
L^2(\mathbb R,w(s)ds),
\]

this raw derivative is not symmetric. The correct self-adjoint first-order operator on a smooth core is

\[
\boxed{
D_w=-i\left(\partial_s+\frac12\partial_s\log w\right).
}
\]

Indeed multiplication by `w^(1/2)` conjugates `D_w` to the ordinary self-adjoint momentum on unweighted `L2`.

## Prime transition and weight change

Let

\[
m_q(s)=1-q^{-1/2-is}
\]

and let the unitary transition be

\[
U_qf=m_qf.
\]

The weights satisfy

\[
w_{S\cup\{q\}}
=
\frac{w_S}{|m_q|^2}.
\]

Therefore

\[
\partial_s\log w_{S\cup\{q\}}
=
\partial_s\log w_S
-\partial_s\log|m_q|^2.
\]

## Exact self-adjoint connection

A direct calculation gives

\[
\begin{aligned}
U_q^{-1}D_{w_{S\cup\{q\}}}U_q
&=D_{w_S}
-i\frac{m_q'}{m_q}
+\frac{i}{2}\partial_s\log|m_q|^2\\
&=D_{w_S}
+
\operatorname{Im}\frac{m_q'}{m_q}.
\end{aligned}
\]

Thus the unitary gauge transformation automatically cancels the real logarithmic-amplitude derivative and retains only the real phase derivative:

\[
\boxed{
U_q^{-1}D_{w_{S\cup\{q\}}}U_q
=D_{w_S}+V_q,
\qquad
V_q=\operatorname{Im}(m_q'/m_q).
}
\]

The correction `V_q` is a real multiplication operator, as required for a self-adjoint connection.

## Prime-power expansion

Put

\[
r=q^{-1/2},
\qquad
\ell=\log q.
\]

Since

\[
\frac{m_q'}{m_q}
=
 i\ell\frac{re^{-is\ell}}{1-re^{-is\ell}},
\]

we obtain

\[
\boxed{
V_q(s)
=
\ell\operatorname{Re}
\frac{re^{-is\ell}}{1-re^{-is\ell}}
=
(\log q)
\sum_{k\ge1}q^{-k/2}\cos(ks\log q).
}
\]

This is exactly one copy of the real prime-power Weil potential. The earlier primal-plus-contra expression gave twice this value because it summed the two orientations explicitly. The self-adjoint weighted connection performs the pairing internally and fixes the factor of two.

## Cumulative flat connection

For

\[
M_S=
\prod_{p\in S}m_p,
\qquad
w_S=w_\emptyset|M_S|^{-2},
\]

the cumulative unitary `U_S=M_S` satisfies

\[
\boxed{
U_S^{-1}D_{w_S}U_S
=D_{w_\emptyset}+V_S,
}
\]

where

\[
V_S(s)
=
\operatorname{Im}\partial_s\log M_S(s)
=
\sum_{p\in S}(\log p)
\sum_{k\ge1}p^{-k/2}\cos(ks\log p).
\]

Since scalar Euler factors commute, this connection remains flat under adjoining primes in either order.

## Archimedean completion has the same form

Let the base weight contain the archimedean local factor,

\[
w_\emptyset(s)=|E_\infty(s)|^2.
\]

Then

\[
D_{w_\emptyset}
=-i\partial_s
-\frac{i}{2}\partial_s\log|E_\infty|^2.
\]

After conjugating to unweighted `L2`, the corresponding phase connection is the real derivative of the archimedean scattering phase. Its explicit expression contains the digamma/log terms appearing in the archimedean Weil distribution.

Therefore gamma and primes are naturally the same kind of object:

\[
\boxed{
\text{local Weil terms}
=
\text{phase connections of local-factor Hilbert metrics}.
}
\]

The endpoint/pole contribution remains a boundary term because it is not represented by a unitary local factor on the critical line.

## Candidate completed operator

On the common unweighted spectral carrier, define formally

\[
\mathscr D_S
=D_0+V_\infty+V_S,
\]

where `D_0=-i partial_s`, `V_infinity` is the archimedean phase connection, and `V_S` is the finite-prime potential above. This is symmetric on a natural smooth core because every `V` is real.

Its square is positive:

\[
\mathscr D_S^2\succeq0.
\]

But the Weil functional is linear in the phase connection, not its square. Therefore positivity of `mathscr D_S^2` alone does not prove Weil positivity. One needs a relative trace or supersymmetric difference extracting the linear term

\[
\mathscr D_S^2-D_0^2
=
D_0V+VD_0+V^2,
\]

while canceling the unwanted `V^2` and derivative pieces through the contra-sector and endpoint boundary condition.

## Precise rung-four target

The `2x2` tower should use the Dirac pair

\[
\mathscr D_S^+=D_0+V,
\qquad
\mathscr D_S^-=D_0-V,
\]

or an equivalent graded connection. Their squared difference is

\[
(\mathscr D_S^+)^2-(\mathscr D_S^-)^2
=2(D_0V+VD_0),
\]

so the quadratic `V^2` term cancels. A compressed graded trace could then yield the linear local Weil current plus boundary terms.

The missing identity is now concrete:

\[
W_S(f)

=
c\operatorname{Str}
\left(\vartheta_S(f)
[(\mathscr D_S^+)^2-(\mathscr D_S^-)^2]
P_S
\right)
+E_{endpoint}(f),
\]

with domains, trace-class properties, and the constant `c` derived from the source.

## Disposition

After correcting the derivative for the changing Hilbert metric, the Euler tower produces a canonical self-adjoint connection whose potential is exactly the real von-Mangoldt prime-power series:

\[
\boxed{
V_S(s)=
\sum_{p\in S}
(\log p)
\sum_{k\ge1}p^{-k/2}\cos(ks\log p).
}
\]

This is stronger than the raw complex logarithmic derivative: the primal/contragredient pairing and reality are built into unitarity. The remaining construction is a graded compressed-trace identity cancelling `V^2` and retaining the linear phase connection together with the endpoint term.
