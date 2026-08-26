# Bounded Resistance Does Not Imply Uniform State Observability

For a weighted graph with vacuum anchor \(a\), two coercivity constants answer
different questions.

The resistance radius

\[
R_* = \max_v R_{\mathrm{eff}}(a,v)
\]

controls pointwise deviation:

\[
\max_v|u(v)-u(a)|^2\le R_*\mathcal E(u).
\]

The smallest eigenvalue \(\lambda_a\) of the grounded Laplacian controls the
full state norm:

\[
\sum_{v\ne a}|u(v)-u(a)|^2
\le \lambda_a^{-1}\mathcal E(u).
\]

A uniform grounded spectral gap implies a uniform resistance bound because
each diagonal entry of the inverse grounded Laplacian is at most
\(\lambda_a^{-1}\). The converse is false in growing dimension.

## Exact star-family separation

Take a unit-conductance star with \(m\) leaves and choose one leaf as the
vacuum anchor. Every other leaf is at resistance distance two from the anchor,
so

\[
R_*=2
\]

for every \(m\). The grounded Laplacian has smallest eigenvalue

\[
\lambda_m=
\frac{m+1-\sqrt{(m+1)^2-4}}2,
\]

which tends to zero like \((m+1)^{-1}\).

Thus any scalar normalization with \(2\mathcal E(u)<1\) remains pointwise
nonzero at every vertex uniformly in \(m\). Nevertheless the global anchored
\(\ell^2\) state can carry arbitrarily large norm at fixed energy. The vector
equal to \(c\) on every unanchored vertex has

\[
\mathcal E=c^2,
\qquad
\|u-u(a)\|_2^2=mc^2.
\]

Pointwise unit closure and state observability are therefore inequivalent.

## Theta/Tate consequence

The resistance theorem can prove that a scalar normalization never vanishes
without proving that the full tail state is observable or that its completion
has a uniform lower frame bound. Conversely, demanding a grounded spectral
gap may be unnecessarily strong if the RH-bearing arrow needs only scalar
nonvanishing.

The correct type depends on the claim:

- scalar Tate section nonvanishing: resistance-radius control may suffice;
- full tail-plus-seam state reconstruction: require a global observability or
  grounded spectral-gap theorem;
- physical actuation: still requires an authorized lift beyond either
  mathematical inequality.

This recovers the earlier distinction between feature faithfulness and state
observability in a purely Carrier-geometric model.

## Falsifiers

- A bounded resistance radius is reported as a uniform \(\ell^2\) Poincare
  constant.
- Grounded spectral-gap collapse is reported as a scalar zero.
- A state-observability theorem is demanded when only scalar nonvanishing is
  claimed.
- Growing vertex count is omitted from the norm comparison.
- A scalar anchor is treated as a full-state measurement port.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to type whether the effective-resistance compiler also
solves the earlier observability problem.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The exact star family proves it does not: scalar unit closure survives
uniformly while global state observability collapses with dimension.
