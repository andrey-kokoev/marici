# The endpoint pair is the harmonic cokernel of the shifted Laplacian and Green identity fixes the cross term

## Endpoint differential complex

On the finite support interval

\[
I_L=[-L,L],
\]

consider the shifted Laplacian

\[
P=
\partial_x^2-\frac14.
\]

Its homogeneous equation has the two solutions

\[
e_+(x)=e^{x/2},
\qquad
e_-(x)=e^{-x/2}.
\]

These are exactly the Paley--Wiener reproducing vectors for evaluation at the completed endpoints `plus-or-minus i/2`.

For the maximal operator

\[
P_{max}:H^2(I_L)\to L^2(I_L),
\]

and a minimal realization obtained by imposing both function and derivative boundary conditions, the adjoint cokernel is

\[
\boxed{
\ker P_{max}^*
=
\operatorname{span}\{e_+,e_-\}.
}
\]

Thus the endpoint pair is not an externally appended coordinate system. It is the harmonic cokernel of the local bulk differential operator.

## Endpoint evaluations as cokernel coordinates

For `g in L2(I_L)`, define

\[
a(g)=\langle g,e_+\rangle
=
\widehat g(i/2),
\]

\[
b(g)=\langle g,e_-\rangle
=
\widehat g(-i/2).
\]

Hence the endpoint quotient map is

\[
\beta_L:L^2(I_L)\to\mathbb C^2,
\qquad
\beta_Lg=(a(g),b(g)).
\]

Its kernel is

\[
\ker\beta_L
=
\overline{\operatorname{ran}P_{min}}.
\]

Consequently there is an exact Hilbert-complex segment

\[
H^2_0(I_L)
\xrightarrow{P_{min}}
L^2(I_L)
\xrightarrow{\beta_L}
\mathbb C^2.
\]

This is a non-tautological arithmetic endpoint model: the endpoint coordinates are selected by the shifts `plus-or-minus 1/2` in `P`, not chosen after the fact.

## Parity splitting

The harmonic cokernel decomposes as

\[
\ker P^*
=
\operatorname{span}\{\cosh(x/2)\}
\oplus
\operatorname{span}\{\sinh(x/2)\}.
\]

These are exactly the positive even and negative odd endpoint channels of the swap form

\[
J_{end}=P_{even}-P_{odd}.
\]

Thus the forbidden odd endpoint direction is the odd harmonic mode of `P`.

## Green boundary form

For smooth `h,u`, integration by parts gives

\[
\langle Ph,u\rangle
-
\langle h,Pu\rangle
=
\left[
h'\bar u-h\bar u'
\right]_{-L}^{L}.
\]

If `u` is one of `e_plus,e_minus`, then `Pu=0`, so

\[
\boxed{
\langle Ph,e_\pm\rangle
=
\left[
h'e_\pm-h e_\pm'
\right]_{-L}^{L}.
}
\]

Therefore endpoint evaluation of a bulk exact vector is precisely a boundary Wronskian. This fixes the endpoint--bulk cross term canonically; it is not a free Schur parameter.

For the odd mode `u_odd=sinh(x/2)`, one obtains

\[
\boxed{
\langle Ph,\sinh(x/2)\rangle
=
\left[
h'\sinh(x/2)
-\frac12h\cosh(x/2)
\right]_{-L}^{L}.
}
\]

The exponentially growing odd endpoint functional is therefore identical to an exponentially weighted Robin boundary trace of the bulk primitive `h`.

## Energy identity

Taking `u=h` in Green's formula gives

\[
-\langle Ph,h\rangle
=
\int_{-L}^{L}
\left(|h'|^2+\frac14|h|^2\right)dx
-
\left[h'\bar h\right]_{-L}^{L}.
\]

The positive bulk energy is

\[
\mathcal E_L(h)=
\int_{-L}^{L}
\left(|h'|^2+\frac14|h|^2\right)dx.
\]

Endpoint terms and their cross coupling occur together in the Robin boundary form. Treating the endpoint as an orthogonal summand discards exactly the term required by Green's identity.

## Factorization

The shifted Laplacian factors as

\[
-P=
(-\partial_x+\tfrac12)
(\partial_x+\tfrac12)
=
(\partial_x+\tfrac12)^*
(\partial_x+\tfrac12)
\]

modulo boundary domains. Thus

\[
\mathcal E_L(h)
=
\|(\partial_x+\tfrac12)h\|^2
+
\text{boundary correction}.
\]

Choosing the Robin boundary condition

\[
h'+\frac12h=0
\]

at the appropriate orientation kills one exponential mode; the opposite Robin choice kills the reciprocal mode. Retaining both orientations gives the `2x2` endpoint complex.

## Candidate sewing to the local superconnection

The spectral superconnection uses

\[
D_t=-i\partial_t
\]

and Euler--gamma phase `A_loc,S(t)`. Under Fourier transform, `D_t` becomes multiplication by the physical coordinate `x`, while multiplication by prime exponentials becomes translation by `k log p`.

The endpoint operator `P=partial_x^2-1/4` acts on this same physical log-coordinate carrier. Therefore a candidate completed complex is

\[
H^2_0(I_L)
\xrightarrow{P}
L^2(I_L)
\xrightarrow{\mathcal D_{loc,S}}
\mathcal H_{graded,S}
\xrightarrow{\beta_L}
\mathbb C^{1,1}.
\]

This display is only a candidate until the middle arrows are typed on common domains, but the endpoint map and its cross form are exact.

## Relation to Suzuki's cokernel

Suzuki's minimal completion retains `ker L*` as an abstract signed harmonic boundary. The present differential complex gives a concrete two-dimensional local harmonic boundary:

\[
\ker P^*
=
\operatorname{span}\{e^{x/2},e^{-x/2}\}.
\]

An intertwiner between Suzuki's cokernel and this endpoint space would need to send the functional-equation even/odd decomposition to `cosh/sinh`. This is now a precise operator equation rather than a spectral analogy.

## What remains

The construction identifies the endpoint boundary and fixes its Green cross term, but it does not yet show that the gamma--prime phase operator factors through `P` with the required domain. The decisive identity would be an intertwining relation

\[
PT_S=T_S\mathscr D_{loc,S}
\]

up to a trace-class remainder whose boundary trace is the completed Weil form.

If such `T_S` is an isometry or contraction compatible with prime enlargement, Green's energy identity would turn the completed form into a positive bulk norm. Without this intertwiner, positivity remains unproved.

## Disposition

The negative endpoint channel has now been embedded canonically into a bulk differential complex:

\[
\boxed{
\text{endpoint pair}
=
\ker(\partial_x^2-\tfrac14)^*
=
\operatorname{span}\{e^{x/2},e^{-x/2}\}.
}
\]

Green's identity uniquely supplies the nonorthogonal endpoint--bulk coupling as a Wronskian boundary form. The remaining rung-four gate is the construction of a source-derived intertwiner from the gamma--prime superconnection into this shifted-Laplacian energy complex.
