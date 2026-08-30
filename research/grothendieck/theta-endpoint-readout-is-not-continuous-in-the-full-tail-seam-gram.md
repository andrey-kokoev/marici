# Theta endpoint readout is not continuous in the full tail--seam Gram

## Setup

For the continuous coefficient model, the full tail--seam synthesis has the
exact energy

\[
 \lVert Uc\rVert^2
 =C\int_{\mathbb R}
   |\widehat c(\xi)|^2|\widehat\Phi(\xi)|^2\,d\xi.
\]

The spectral endpoint that supplies the scalar transform is

\[
 L(c)=G_c(0)=\int_{\mathbb R}c(p)\Phi(p)\,dp.
\]

With compatible Fourier normalization and
`y=chat conjugate(Phihat)`, Parseval gives

\[
 \lVert Uc\rVert^2=C\lVert y\rVert_2^2,
 \qquad
 L(c)=C'\int_{\mathbb R}y(\xi)\,d\xi.
\]

## Exact unboundedness witness

Assume `Phihat` is continuous and nonzero on every compact interval, as in
the analytic nonvanishing source regime used for faithfulness.  Put

\[
 y_N(\xi)=\frac{\mathbf1_{[-N,N]}(\xi)}{\sqrt{2N}},
 \qquad
 \widehat c_N=\frac{y_N}{\overline{\widehat\Phi}}.
\]

For each finite `N`, `c_N` is an admitted `L2` packet because the reciprocal
of `Phihat` is bounded on `[-N,N]`.  But

\[
 \lVert Uc_N\rVert^2=C,
 \qquad
 |L(c_N)|=|C'|\sqrt{2N}\longrightarrow\infty.
\]

Therefore

The functional \(L\) is not continuous in the full tail--seam Gram norm.

## Meaning

The zero-to-boundary-state bridge uses the condition `G_s(0)=0`.  That
condition is not defined continuously on the completion of the bulk
tail--seam state alone.  The scalar endpoint cannot be reconstructed after
completion by a bounded trace map.

The completed object must retain an endpoint port explicitly:

\[
 U_{\rm boundary}c=(Gc,Hc,L(c)),
\]

or use a source-derived rigging whose topology already contains `L` as a
continuous boundary functional.  Merely adjoining `L` to the norm by hand is
not enough; its normalization and Green-current incidence must come from the
theta/Tate boundary system.

## Relation to the constructor-generated topology

Valuation cylinders repair loss of discrete arithmetic type, but they do not
by themselves repair this global spectral trace.  The operational topology
must therefore contain two independently sourced kinds of ports:

1. prime-valuation/Fock constructors, which prevent arithmetic type erasure;
2. endpoint and modular-current ports, which prevent loss of non-`L2`
   boundary data.

This is a second axis, not another valuation projector.

## Honest obstruction

The source-derived rank-two differential system exists on finite packets,
and its native doubled bulk is positive.  Yet its defining spectral boundary
condition does not survive the bulk Gram completion automatically.  The next
theorem must construct the augmented boundary-bearing topology and prove the
full Green identity there.
