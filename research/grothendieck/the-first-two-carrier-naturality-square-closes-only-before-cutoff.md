# The first two-carrier naturality square closes only before cutoff

## Question

The circle heat carrier and logarithmic tail carrier cannot be identified.
Can they nevertheless be joined by a source-derived dagger correspondence,
and does its first Fourier–Poisson naturality square survive finite cutoff?

## The smallest typed fragment

Retain four distinct objects:

- the circle carrier (C_{\mathrm{circ}}), with winding labels and heat
  preparation;
- the logarithmic carrier (C_{\log}), with the coordinate (q=\log n),
  translation, and tail/head resolvents;
- the rigged boundary object (B);
- the observer family (O), carrying primitive, square, seam, connected,
  and archimedean seminorms.

The vertical arrows are correspondences

\[
i_{\mathrm{circ}}:C_{\mathrm{circ}}\rightsquigarrow B,
\qquad
i_{\log}:C_{\log}\rightsquigarrow B.
\]

Their daggers retain the reverse boundary incidences.  They are not inverses
and do not identify the carrier generators.

At finite label support, let (S_X) be the typed incidence that sends the
circle winding label (n) to the log label (q_n=\log n).  For a circle
spectral preparation with diagonal coefficients (h_n), define the log-side
multiplication operator by the same labelled coefficients:

\[
H_X=\operatorname{diag}(h_n)_{n\in X},
\qquad
M_X=\operatorname{diag}(h_n)_{n\in X}.
\]

Then the first naturality square is exact:

\[
S_XH_X=M_XS_X.
\]

Taking adjoints gives the dagger square

\[
H_X^*S_X^*=S_X^*M_X^*.
\]

This is a genuine correspondence statement.  It says that the same labelled
heat coefficient is seen in the logarithmic chart as multiplication.  It
does not say that the circle Laplacian is logarithmic translation.

## Scale covariance rather than generator identification

Writing the heat scale as (t=e^{2q}), multiplicative scale transport

\[
t\longmapsto e^{2a}t
\]

becomes translation

\[
q\longmapsto q+a.
\]

Thus the source comparison relates circle metric dilation to log translation.
It does not relate additive heat time to log translation.  The earlier
bounded-intertwiner no-go is therefore respected.

Reciprocal Fourier–Poisson sewing acts by

\[
t\longmapsto t^{-1},
\qquad
q\longmapsto-q,
\]

after the modular half-density is retained.  This is the candidate global
two-cell between the two presentations.

## First Beck–Chevalley anomaly

Finite Euler cutoff is not a source subobject of the restricted adelic theta
carrier.  Replacing every omitted unramified vector changes infinitely many
local factors.  Consequently global Fourier–Poisson sewing has no
source-authorized finite-cutoff endomorphism.

The obstruction is already visible on the archimedean lattice comb.  Let

\[
\Delta_N=\sum_{|n|\le N}\delta_n.
\]

Its Fourier transform is the trigonometric polynomial

\[
\widehat\Delta_N(\xi)
=
\sum_{|n|\le N}e^{-2\pi i n\xi},
\]

not another finite lattice-supported comb.  Hence the finite source span is
not preserved by Fourier transport.

If (P_X) denotes cutoff projection and (F) the global Fourier operation,
the missing Beck–Chevalley square has residual

\[
\mathfrak A_X=P_XF(I-P_X).
\]

The exact finite model in the accompanying checker has

\[
\operatorname{rank}\mathfrak A_X=1.
\]

The rank is only a minimal witness.  In the actual lattice source, the
residual is the entire omitted Fourier tail.  Call it the Poisson cutoff
leakage anomaly.

## Categorical consequence

The smallest valid dagger fragment therefore has two different layers.

First, finite labelled preparation and log-chart multiplication satisfy an
exact naturality square, together with its adjoint.  Cutoff bonding also
commutes with this diagonal labelled square.

Second, the Fourier–Poisson coherence cell lives only on the completed global
source.  It cannot be compiled from finite Euler cells.  Finite cutoffs may be
diagnostic projections after global sewing, but they are not horizontal
objects on which the Poisson cell closes.

The desired completed two-cell must therefore be constructed in this order:

1. form the full restricted theta source;
2. apply Fourier–Poisson sewing globally;
3. map both presentations into the rigged boundary correspondence;
4. test the full pro-Gram observer family;
5. only then project to Euler diagnostics.

## Scope

The labelled naturality and dagger squares are exact.  The Poisson cutoff
leakage is an exact typing obstruction.  No completed operator-valued
Fourier–Poisson two-cell, common-kernel theorem, or RH conclusion is proved.

## Result

The first two-carrier correspondence exists on labelled preparations without
identifying the carriers.  Its Fourier–Poisson Beck–Chevalley square cannot
exist at finite Euler cutoff: Fourier transport leaks outside every truncated
source object.  The categorical attack must therefore construct one global
completion-level coherence cell and regard cutoffs only as projections of
that cell.
