# Completed local-phase supertrace leaves the endpoint as an unbounded analytic evaluation channel

## Total local phase

For a finite prime set `S`, combine the Euler phase with the archimedean gamma phase:

\[
A_{loc,S}(t)
=
A_\infty(t)+
\sum_{p\in S}
\operatorname{Im}\log(1-p^{-1/2-it}).
\]

Choose

\[
A_\infty(t)
=
\operatorname{Im}
\log\!left(
\pi^{-(1/2+it)/2}
\Gamma((1/2+it)/2)
\rightright)
\]

up to a constant branch. Its derivative is

\[
V_\infty(t)
=
-\frac12\log\pi
+\frac12\operatorname{Re}
\psi(1/4+it/2),
\]

which is the standard gamma/log density in the explicit formula, up to Fourier normalization.

The full smooth local potential is therefore

\[
V_{loc,S}=A_{loc,S}'
=V_\infty+
\sum_{p\in S}(\log p)
\sum_{k\ge1}p^{-k/2}\cos(kt\log p).
\]

The global Weil convention may negate the prime part; that orientation must be fixed when the source explicit formula is attached.

## Supersymmetric extraction

Define

\[
H_{S,+}=D^2+A_{loc,S}^2+V_{loc,S},
\qquad
H_{S,-}=D^2+A_{loc,S}^2-V_{loc,S}.
\]

For a compactly supported smooth spectral observer `chi`, local heat asymptotics give

\[
\boxed{
-\lim_{u\downarrow0}
\sqrt{\pi/u}
\left[
\operatorname{Tr}(M_\chi e^{-uH_{S,+}})
-
\operatorname{Tr}(M_\chi e^{-uH_{S,-}})
\right]
=
\int\chi(t)V_{loc,S}(t)dt.
}
\]

Thus one `2x2` superconnection realizes the gamma density and every active prime-power current on the same carrier. Their nonlinear cross terms in `A_loc,S^2` cancel in the graded coefficient.

## Missing endpoint/pole functional

The completed Weil formula also contains the pole/endpoint contribution. In the multiplicative test normalization this is expressed through Mellin-transform evaluations at off-real spectral parameters corresponding to `s=0` and `s=1`, equivalently shifts by `plus-or-minus i/2` from the critical line.

Schematically, the endpoint form contains terms of the type

\[
\widehat g(i/2),
\qquad
\widehat g(-i/2),
\]

and their polarization. These are analytic evaluations, not integration against a bounded real-axis multiplier.

## Evaluation is unbounded on the ambient spectral L2 space

There is no vector `e_{i/2} in L2(R)` satisfying

\[
\widehat g(i/2)
=
\langle\widehat g,e_{i/2}angle_{L^2(\mathbb R)}
\]

for all analytic test transforms. Point evaluation is not continuous in the bare boundary `L2` norm. One can choose narrow real-axis packets with bounded `L2` norm and arbitrarily large analytic continuation at a fixed off-axis point.

Consequently the endpoint cannot be appended as a bounded rank-one channel to the same unweighted heat carrier.

## Rigged analytic carrier

On a Paley--Wiener space of fixed support, or a Gaussian reproducing-kernel Hilbert space of fixed width, off-axis evaluation is continuous. There exists a reproducing vector `e_{i/2}^{(L)}` or `e_{i/2}^{(u)}` and

\[
\widehat g(i/2)
=
\langle\widehat g,e_{i/2}angle_{PW_L}.
\]

But its norm grows with the support or inverse smoothing scale. For a Paley--Wiener interval of radius `L`, the evaluation norm grows exponentially like

\[
\|e_{i/2}^{(L)}
\|\asymp e^{L/2}
\]

up to polynomial factors. Therefore the endpoint channel is bounded at every finite window but has no uniform bound under global support exhaustion.

This is the same inverse-semigroup growth found in the conjugate-sewing audit.

## Finite-window completed realization

At fixed support or Gaussian width, one can define a completed graded carrier

\[
\mathcal H_{bulk}^{even}
\oplus
\mathcal H_{bulk}^{odd}
\oplus
E_{+1/2}
\oplus
E_{-1/2},
\]

where the two endpoint lines are represented by reproducing kernels. The local gamma--prime current is the renormalized bulk supertrace, and the endpoint is a finite-rank boundary form.

This gives an exact **signed** realization of every source sector at finite regularization. It does not produce a uniform positive Hilbert norm because:

1. the bulk term is a supertrace difference;
2. endpoint evaluation norms diverge under completion;
3. the explicit formula requires cancellation between these pieces before taking the limit.

## Why endpoint completion cannot be orthogonal

If the endpoint lines are added as orthogonal positive summands, their exponentially growing norms survive instead of cancelling the large gamma--prime boundary behavior. The completed source requires a nonorthogonal Green coupling between endpoint evaluations and the bulk phase connection.

The desired boundary condition must therefore produce a Schur complement:

\[
Q_{completed}
=
Q_{bulk}
+
Q_{endpoint}
+
2\operatorname{Re}Q_{cross}.
\]

Its positivity is equivalent to a contractive bound on the cross map. Dropping `Q_cross` or estimating it absolutely destroys the exact endpoint cancellation.

## Relation to Connes--Consani

On their restricted archimedean support window, Connes--Consani obtain precisely such control: the hostile sector is reduced to one Mellin evaluation and bounded by a rank-one correction. Once primes enter, the bulk phase above acquires infinite-rank translation channels, while the endpoint remains finite-dimensional. The missing semilocal theorem must prove that the same boundary Schur complement stays positive.

## Disposition

The completed local `2x2` superconnection succeeds for gamma plus finite primes:

\[
\boxed{
\text{renormalized heat supertrace}
=
\text{gamma phase current}
+
\text{finite-prime von-Mangoldt current}.
}
\]

The endpoint cannot be represented as a uniformly bounded rank-one channel on the ambient boundary `L2` carrier. It requires an analytic rigging whose evaluation norm grows under completion and a nonorthogonal Green coupling to the bulk. Constructing and proving positivity of that Schur complement is now the precise remaining rung-four gate.
