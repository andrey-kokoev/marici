# The anti-Hermitian left-cutoff placement channel vanishes by reality and polarization

## Relative ordered operator

Let

\[
\Delta Q_L
=Q_L^T-Q_L^0
\]

be the self-adjoint difference of the Tate and reference Hardy projections. The ordered left-cutoff relative operator is

\[
\boxed{
T_L
=P\Delta Q_L.
}
\]

Its adjoint is

\[
T_L^*
=\Delta Q_LP.
\]

Decompose it into Hermitian and anti-Hermitian parts:

\[
\boxed{
H_L
=
\frac12
(P\Delta Q_L+
\Delta Q_LP),
}
\]

\[
\boxed{
A_L
=
\frac1{2i}
(P\Delta Q_L-
\Delta Q_LP)
=
\frac1{2i}
[P,\Delta Q_L].
}
\]

Both `H_L` and `A_L` are self-adjoint.

## Observer forms

For an observer factor `X_g` at finite regulator, define

\[
t_L(g,h)
=
\operatorname{Tr}
(X_h^*
P\Delta Q_L
X_g),
\]

\[
h_L(g,h)
=
\operatorname{Tr}
(X_h^*H_LX_g),
\]

and

\[
a_L(g,h)
=
\operatorname{Tr}
(X_h^*A_LX_g).
\]

Then

\[
\boxed{
t_L=h_L+ia_L.
}
\]

The forms `h_L` and `a_L` are Hermitian whenever the regulated products are trace class.

## Diagonal identity

For `h=g`, self-adjointness gives

\[
\boxed{
a_L(g,g)
=
\operatorname{Im}t_L(g,g).
}
\]

Thus the diagonal anti-Hermitian placement channel is exactly the imaginary part of the ordered relative regulator.

## Reality of the limiting Weil value

Let

\[
h_g
=g*g^*.
\]

The semilocal Weil distribution is star-compatible:

\[
W_S(h^*)
=
\overline{W_S(h)}.
\]

Since

\[
h_g^*=h_g,
\]

one has

\[
\boxed{
W_S(h_g)
\in
\mathbb R.
}
\]

Equivalently, in the Tate multiplier realization,

\[
W_S(h_g)
=
\langle
\mathcal M_Sg,
A_S\mathcal M_Sg
\rangle
\]

is real because `A_S` is self-adjoint.

## Ordered relative convergence

Assume the exact finite regulator placement has been matched so that the centered ordered relative form satisfies

\[
\boxed{
t_L(g,g)
\longrightarrow
W_S(g*g^*).
}
\]

The universal cutoff terms have already canceled between the Tate and pure reference regulators and are real.

Taking imaginary parts yields

\[
\boxed{
a_L(g,g)
\longrightarrow0
}
\]

for every observer `g` in the common core.

No commutator norm estimate is required for this diagonal conclusion.

## Polarization

Because each `a_L` is Hermitian, the complex polarization identity gives

\[
a_L(g,h)
=
\frac14
\sum_{k=0}^{3}
i^k
a_L
(g+i^kh,
g+i^kh)
\]

up to the chosen inner-product convention.

If diagonal convergence to zero holds for every linear combination `g+i^k h`, then

\[
\boxed{
a_L(g,h)
\longrightarrow0
}
\]

for every observer pair.

On a fixed finite packet, convergence of finitely many polarized entries implies matrix/operator-norm convergence:

\[
\boxed{
\|a_L|_{E_0}\|_{op}
\longrightarrow0.
}
\]

## Eight-leg interpretation

The eight-leg positive feature `Theta_L` has two bounded signed readouts:

\[
\Theta_L^*K_8\Theta_L
=H_L,
\]

\[
\Theta_L^*K_8^{skew}\Theta_L
=A_L.
\]

The result above gives

\[
\boxed{
\langle
\Theta_L(h),
K_8^{skew}
\Theta_L(g)
\rangle
\longrightarrow0.
}
\]

Meanwhile

\[
\boxed{
\langle
\Theta_L(h),
K_8
\Theta_L(g)
\rangle
\longrightarrow
W_S(g*h^*).
}
\]

Thus only the Hermitian readout survives on the `C_34` boundary.

## Reference reality

For the pure nested Hardy reference, the ordered projection-strip trace is real on positive observers after matching orientation, since it is the trace of an exact mismatch projection with a positive observer density.

Therefore subtracting the reference does not introduce a limiting imaginary counterterm. Any finite-regulator imaginary part comes solely from asymmetric observer placement and vanishes in the centered limit by the argument above.

## Scope of the conclusion

The conclusion uses convergence of the **ordered** relative regulator, not merely convergence of its Hermitian part. If only

\[
h_L(g,h)
\to
W_S(g*h^*)
\]

has been proved, reality cannot determine `a_L`.

Thus the exact logical implication is

\[
\boxed{
\text{ordered centered convergence to Hermitian }W_S
\Longrightarrow

a_L\to0.
}
\]

The source Connes trace theorem supplies an ordered scalar limit. What remains is the already isolated conjugation/alignment between that product cutoff and `P Delta Q_L` in the Hardy carrier.

## No trace-norm conclusion

Vanishing matrix coefficients

\[
a_L(g,h)
\to0
\]

on the observer core does not imply

\[
\|A_L\|_1
\to0
\]

or operator-norm convergence on the full Hilbert space.

The statement is exactly what the form-valued `C_34` boundary requires. Stronger operator convergence would need uniform estimates.

## Endpoint terms

Endpoint/winding contributions in the local Tate identity are real on positive observer squares after the star-compatible branch convention is fixed. If a branch convention produces an imaginary endpoint constant, it must be paired with its conjugate orientation before applying this argument.

Thus endpoint reality is part of the orientation normalization, not an extra vanishing estimate.

## Disposition

For the ordered relative product,

\[
\boxed{
\operatorname{Im}
\operatorname{Tr}
(X_g^*P\Delta Q_LX_g)
=
\operatorname{Tr}
\left(
X_g^*
\frac{[P,\Delta Q_L]}{2i}
X_g
\right).
}
\]

Its limit is zero because the centered ordered trace converges to the real Weil value on `g*g*`. Polarization kills every off-diagonal matrix coefficient. Hence the anti-Hermitian eight-leg channel has zero `C_34` boundary readout; no additional boundary current is required.
