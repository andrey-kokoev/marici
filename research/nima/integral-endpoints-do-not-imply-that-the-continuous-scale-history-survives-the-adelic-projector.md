# Integral endpoints do not imply that the continuous scale history survives the adelic projector

## Two different parameters

The first Adams history runs through logarithmic scales

\[
t\in[\log p,2\log p].
\]

Its analytic states are reciprocal windows

\[
W_t(q)=H(q+t)-H(q-t).
\]

The adelic vacuum bridge, by contrast, is diagonal on additive characters

\[
\chi_r,
\qquad
r\in\mathbb Q,
\]

and retains exactly the integer indices:

\[
K_f\chi_r
=
\begin{cases}
e^{-\pi r^2}\chi_r,&r\in\mathbb Z,\\
0,&r\notin\mathbb Z.
\end{cases}
\]

The scale parameter \(t\) is not the adelic character index \(r\).

## Endpoint integrality is insufficient

At the endpoints,

\[
e^{\log p}=p,
\qquad
e^{2\log p}=p^2,
\]

so the primitive and square labels are integers.

For an interior point

\[
t=(1-\theta)\log p+\theta\,2\log p,
\qquad
0<\theta<1,
\]

the exponential scale is

\[
e^t=p^{1+\theta}.
\]

This is generally neither an integer nor a rational number.

Therefore the continuous scale-path history does not define a path inside the integral character sector merely because its endpoints are \(p\) and \(p^2\).

## No direct kernel-intersection theorem yet

The expression

\[
\ker K_f\cap\mathcal V_{\mathrm{mix}}
\]

is meaningful only after a source map places the mixed history in the adelic character space.

No such intertwiner has yet been constructed. The comoving window history lives in an archimedean translation/dilation representation, while \(K_f\) acts on periodized adelic additive characters.

Thus the ideal bridge is a candidate, not yet a typed operation on the first Adams history.

## Required dilation intertwiner

Let \(\mathcal U_t\) denote the source dilation or translation representation generating \(W_t\). Let \(\mathcal K_\tau\) denote the modular adelic Gaussian family.

The missing comparison has the schematic form

\[
\mathfrak I\mathcal U_t
\Longrightarrow
\mathcal M_t\mathfrak I,
\]

where:

- \(\mathfrak I\) maps the scale-history carrier into an adelic or Mellin module;
- \(\mathcal M_t\) is the corresponding modular action on the adelic vacuum family;
- the comparison is source-derived from Tate dilation and Poisson sewing.

At \(t=\log p\) and \(2\log p\), it must recover the integral prime and prime-square endpoint maps.

## Fixed-vacuum sandwich does not commute with scale propagation

The operator \(K_f=K_1\) is tied to the self-dual Gaussian scale. Dilation changes the real Gaussian and produces the family \(K_\tau\).

Therefore one should not assume

\[
K_f\mathcal U_t=\mathcal U_tK_f.
\]

The correct relation is likely covariant and moves the heat/modular parameter. Freezing \(K_f\) along the entire history may break the source dilation law.

## Two possible source-correct routes

### Endpoint sandwich

Apply the adelic vacuum only after the continuous Green/Stokes history has produced typed endpoint and mixed blocks. This needs no claim that interior scales are integral, but it must prove that the resulting endpoint operator acts on the surviving integral sector.

### Moving-vacuum history

Transport the adelic Gaussian family along the scale path and sandwich fiberwise:

\[
K_{\tau(t)}^{1/2}
R_t
K_{\tau(t)}^{1/2}.
\]

This respects modular dilation but introduces a determinant-line transport problem between different trace-class fibers.

Neither route is currently derived for \(B_{\alpha,p}\).

## Minimal hostile

A proposed intertwiner sends the endpoint labels \(p,p^2\) correctly but maps every interior scale \(p^{1+\theta}\) to a nonintegral rational character. The adelic projector annihilates almost the entire path. Endpoint scalar checks pass while the Green history is destroyed.

Another hostile freezes the self-dual vacuum at every \(t\), producing trace-class operators that fail the modular covariance square.

## Consequence for determinant typing

The existence of a canonical nuclear bridge does not authorize composing it with every source operator. One must prove composability in the category:

\[
\text{scale history}
\to
\text{typed endpoint block}
\to
\text{adelic integral sector}
\to
\text{nuclear sandwich}.
\]

At present, only the last arrow is constructed.

## Current frontier

The next irreducible theorem is an archimedean-scale-to-adelic-modular intertwiner for the two-chart history.

Until that theorem exists, the conservative determinant route is endpoint-first:

1. complete the rigged Green/Stokes history;
2. form the oriented primitive-to-square endpoint block;
3. prove that block preserves the adelic integral sector;
4. only then apply the canonical vacuum sandwich.

Endpoint integrality alone does not prove history integrality.
