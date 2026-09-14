# The Euler contratower commutator constructs the full prime-power Weil current

## Finite-place Hilbert tower

For a finite set of primes `S`, define the Euler multiplier

\[
M_S(s)=
\prod_{p\in S}m_p(s),
\qquad
m_p(s)=L_p(1/2+is)^{-1}
=1-p^{-1/2-is}.
\]

Let the weighted spectral carrier be

\[
\mathcal H_S=
L^2\!\left(\mathbb R,|E_\infty(s)M_S(s)^{-1}|^2ds\right).
\]

This matches the weighted Hardy--Titchmarsh normalization in the semilocal Sonin construction: adding a prime multiplies the entire-function weight by `L_p` and multiplies vectors by `L_p^{-1}`.

For `q notin S`, define

\[
U_{S,q}:\mathcal H_S\longrightarrow\mathcal H_{S\cup\{q\}},
\qquad
(U_{S,q}f)(s)=m_q(s)f(s).
\]

Then

\[
\begin{aligned}
\|U_{S,q}f\|_{S\cup\{q\}}^2
&=
\int |m_qf|^2
|E_\infty M_S^{-1}m_q^{-1}|^2ds\\
&=
\int |f|^2|E_\infty M_S^{-1}|^2ds\\
&=
\|f\|_S^2.
\end{aligned}
\]

Hence

\[
\boxed{U_{S,q}\text{ is unitary}.}
\]

The prime tower is therefore realized exactly, not conjecturally, at the Hilbert-carrier level.

## Contratower

Let

\[
\overline{\mathcal H}_S
\]

be the conjugate Hilbert space. The contragredient transition is

\[
\bar U_{S,q}\bar f
=
\overline{U_{S,q}f},
\]

which is multiplication by `bar(m_q)` on boundary values. The primal and contragredient transitions form the square

\[
\begin{matrix}
\mathcal H_S&\xrightarrow{U_{S,q}}&\mathcal H_{S\cup\{q\}}\\
\downarrow J_S&&\downarrow J_{S\cup\{q\}}\\
\overline{\mathcal H}_S&\xrightarrow{\bar U_{S,q}}&
\overline{\mathcal H}_{S\cup\{q\}},
\end{matrix}
\]

and this square commutes by construction.

## Prime-squared tower

Tensoring gives the unitary transition

\[
U_{S,q}^{(2)}
=
U_{S,q}\otimes\bar U_{S,q}

:
\mathcal H_S\widehat\otimes\overline{\mathcal H}_S
\longrightarrow
\mathcal H_{S\cup\{q\}}
\widehat\otimes
\overline{\mathcal H}_{S\cup\{q\}}.
\]

Expanding

\[
m_q\bar m_q
=(1-r_qe^{-is\ell_q})(1-r_qe^{is\ell_q}),
\qquad
r_q=q^{-1/2},
\quad
\ell_q=\log q,
\]

retains the four sectors

\[
1,

e^{-is\ell_q},

e^{is\ell_q},

1.
\]

When multiplied by the old product, these generate old--old, old--new, new--old, and new--new polarization. No orthogonal prime splitting occurs.

## Spectral derivative as a connection

Let

\[
D=-i\frac{d}{ds}
\]

on a common smooth core. Direct differentiation gives

\[
U_{S,q}^{-1}DU_{S,q}
=D+a_q,
\]

where

\[
\boxed{
a_q(s)=-i\frac{m_q'(s)}{m_q(s)}.}
\]

Since

\[
m_q(s)=1-r_qe^{-is\ell_q},
\]

we obtain

\[
\boxed{
a_q(s)
=
\ell_q
\frac{r_qe^{-is\ell_q}}
     {1-r_qe^{-is\ell_q}}
=
\ell_q\sum_{k\ge1}
r_q^ke^{-iks\ell_q}.}
\]

Thus one commutator with the Euler transition produces the entire prime-power tower with exactly the von Mangoldt weights

\[
(\log q)q^{-k/2}.
\]

This constructs the previously missing logarithmic operation:

\[
\boxed{
U_{S,q}^{-1}[D,U_{S,q}]
=
-i\partial_s\log m_q.
}
\]

## Paired real Weil current

The contratower contributes

\[
\bar a_q(s)
=
\ell_q\sum_{k\ge1}r_q^ke^{iks\ell_q}.
\]

Adding the two orientations gives

\[
\boxed{
a_q(s)+\bar a_q(s)
=
2(\log q)
\sum_{k\ge1}q^{-k/2}
\cos(ks\log q).}
\]

Up to the global explicit-formula sign and Fourier normalization, this is exactly the real prime-power Weil current.

Therefore the primal/contragredient square does more than preserve Euler products: its differentiated connection produces the additive logarithmic prime distribution.

## Flat tower connection

For the cumulative transition

\[
U_S=M_S,
\]

one has

\[
U_S^{-1}DU_S
=D+A_S,
\qquad
A_S=-i\partial_s\log M_S
=
\sum_{p\in S}a_p.
\]

If primes are added in either order,

\[
U_{S\cup\{p\},q}U_{S,p}
=
U_{S\cup\{q\},p}U_{S,q},
\]

because the scalar Euler multipliers commute. The connection increments also commute and add. Thus the prime tower has zero discrete curvature:

\[
\delta_pa_q-\delta_qa_p+[a_p,a_q]=0.
\]

This supplies the exact rung transition coherence for the prime-power current.

## What remains before rung-four positivity

The construction now provides:

1. unitary prime transitions;
2. unitary contragredient transitions;
3. coherent tensor-square transitions retaining mixed polarization;
4. the complete finite-place logarithmic prime-power current as a derivative commutator.

What it does not provide is positivity of the trace after inserting the connection. The multiplication operator

\[
a_q+\bar a_q
\]

changes sign with `s`, and the global Weil convention places the prime contribution with the hostile sign. A commutator identity constructs the correct current but does not make it a positive operator.

The next required cell is a compressed Green identity

\[
W_S(f*g^*)
=
\operatorname{Tr}
\bigl(\vartheta_S(g)P_S\vartheta_S(g)^*\bigr)
-E_S(g),
\]

where the commutator connection `A_S+bar A_S` is included inside the same trace and the remainder is controlled uniformly under `S -> S union {q}`.

## Disposition

The proposed `2x2` tower can be constructed exactly through the semilocal Euler multipliers. Most importantly,

\[
\boxed{
\text{prime tower connection}
+
\text{contratower connection}
=
\text{full real von-Mangoldt prime-power current}.
}
\]

This closes the earlier “one derivative short” algebraic gap. The remaining obstruction is no longer production of the Weil prime weights; it is proving that the completed compressed trace containing this signed connection is positive after endpoint--gamma completion.
