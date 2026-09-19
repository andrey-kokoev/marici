# The rung-five defect primitive supplies the missing dominant endpoint scale in the reciprocal shell response

## Missing scale

Pure reflected-history overlap has late-shell order

\[
O\!\left(\frac{\Phi(a)^2}{\Lambda(a)^2}\right),
\]

while the completed diagonal reciprocal response requires

\[
\frac{\Phi(a)^2}{\Lambda(a)}.
\]

Therefore a separately sourced endpoint or constitutive component is required.

## Primitive endpoint term

The rung-five Clark-defect primitive at seam `a` is

\[
K_a(q)
=-\frac12|q-a|+\delta_a.
\]

Its `delta_a` coefficient is fixed by the exact identity

\[
\partial_qK_a
=-\frac12\operatorname{sgn}(q-a)+\delta_a'.
\]

It was constructed before Xi-zero specialization and is not normalized from a
shell asymptotic.

Pair the endpoint component against the positive-shell Evans density:

\[
\mathcal E_a^{\rm end}(z)
=\langle\delta_a,\Phi(\cdot)u_+(\cdot;z)\rangle
=\Phi(a)u_+(a;z).
\]

For the stable history,

\[
u_+(a;z)
=-\int_a^\infty e^{z(a-r)}\Phi(r)\,dr
=-\frac{\Phi(a)}{\Lambda(a)}
\left(1+O(\Lambda(a)^{-1})\right),
\]

with the source logarithmic decay rate `Lambda(a)`. Hence

\[
\boxed{
\mathcal E_a^{\rm end}(z)
=-\frac{\Phi(a)^2}{\Lambda(a)}
\left(1+O(\Lambda(a)^{-1})\right).
}
\]

This has exactly the previously missing dominant order.

## Nonlocal primitive part

The `-|q-a|/2` component vanishes at the seam and contributes through an
integrated neighborhood. Under the same Laplace localization its extra factor
`|q-a|` lowers the asymptotic order by at least one inverse decay rate. It does
not alter the leading endpoint coefficient.

## Consequence

The rung-five compensator is not only a formal homotopy. Its singular endpoint
component provides a source-derived candidate for the diagonal constitutive
response that pure reciprocal reflection cannot supply.

The sign is fixed by the orientation of the defect primitive. Reversing the
chain-map output orientation reverses the Green contribution globally; no
primewise fitting is allowed.

## Remaining exact test

Insert the full loaded primitive `K_(k log p)` into the five-port source
codiagonal and compute its contribution to

\[
r_U(z)=CR_{\rm sat}(z).
\]

The required theorem is still vector-valued divisibility

\[
r_U(z)=\tau(z)h_U(z).
\]

The asymptotic calculation closes the missing scale and provenance tests, but
not the exact residual-jet cancellation.