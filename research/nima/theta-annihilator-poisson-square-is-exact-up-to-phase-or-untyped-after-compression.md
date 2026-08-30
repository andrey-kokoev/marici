# Theta annihilator–Poisson square is exact up to phase or untyped after compression

## Status

Exact metaplectic covariance theorem and typing no-go. On the full Schwartz
source, Fourier transport intertwines the Gaussian annihilation operator with
itself up to the canonical quarter-turn phase. Hence the annihilator–Poisson
commutator square has zero residual.

After compression to lattice values alone, the annihilator is not defined
because it also requires derivative samples. A nonzero residual cannot be
claimed from that mistyped square. It can arise only after constructing an
enlarged boundary port and computing its explicit compression defect.

## Fourier covariance of the annihilator

Use the Fourier convention

\[
(\mathcal Ff)(\xi)
=\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,dx.
\]

Then

\[
\mathcal F\partial_x\mathcal F^{-1}=2\pi i\xi,
\]

and

\[
\mathcal F x\mathcal F^{-1}=\frac{i}{2\pi}\partial_\xi.
\]

For

\[
a=\partial_x+2\pi x,
\]

we obtain

\[
\mathcal Fa\mathcal F^{-1}
=i(\partial_\xi+2\pi\xi)
=ia.
\]

Equivalently,

\[
\mathcal Fa=ia\mathcal F.
\]

The twisted commutator

\[
\mathfrak C=\mathcal Fa-ia\mathcal F
\]

vanishes identically on the Schwartz core.

## Consequence for a faithful transported boundary object

Suppose a boundary constructor (C\) retains enough information to transport
both Fourier transform and the annihilator. Write

\[
U_C C=C\mathcal F,
\qquad
a_C C=Ca.
\]

Then

\[
U_Ca_CC
=C\mathcal Fa
=iCa\mathcal F
=ia_CU_CC.
\]

On the generated boundary object,

\[
U_Ca_C=ia_CU_C.
\]

Thus every faithful functorial lift inherits the zero twisted residual. Exact
metaplectic transport cannot create the desired mixed arithmetic current.

## Value sampling does not carry the annihilator

Let the value-sampling map be

\[
S_0f=(f(n))_{n\in\mathbb Z}.
\]

The sampled annihilator is

\[
(S_0af)_n=f'(n)+2\pi nf(n).
\]

It is not determined by (S_0f\). Two Schwartz functions may agree at every
integer and have different derivative samples. Therefore no operator (A_0\)
on the value sequence alone can satisfy

\[
A_0S_0=S_0a
\]

on the full Schwartz source.

The square formed from Fourier transport, (a), and value sampling is not a
noncommuting square. One of its arrows is absent.

## Minimal jet-sampling repair

Adjoin the derivative port

\[
S_1f=((f(n),f'(n)))_{n\in\mathbb Z}.
\]

On this first-jet boundary, the annihilator readout is the declared row

\[
(v_n,d_n)
\longmapsto
d_n+2\pi nv_n.
\]

But Fourier transport of (S_1f\) is not determined by independent termwise
rotation of these pairs. Fourier transform mixes all lattice samples through
the global source. A boundary Fourier constructor must therefore be built on a
rigged sequence space with its Poisson bonding law.

If that constructor is faithful to the Schwartz relation, its twisted
annihilator square again has zero residual. If it is compressed, the missing
information must be represented by an additional boundary defect port.

## Termwise vacuum identity

For the Gaussian vacuum (g\),

\[
ag=0.
\]

After translation,

\[
aT_ng=2\pi nT_ng.
\]

This identity holds separately for every label. Multiplying each translated
atom by an arbitrary coefficient leaves the same termwise relation. Therefore
it cannot constrain cancellation between distinct labels after scalar
aggregation.

Dilation of the relation generates higher label moments but no inter-label
coupling. This agrees with the earlier Vandermonde-observability no-go.

## Where a genuine residual could live

A nonzero mixed residual can occur only if a boundary constructor fails to be a
faithful intertwiner for a source-derived reason. Candidate locations are:

- the derivative-comb distribution created by moving (a) across sampling;
- a half-comb or endpoint restriction that breaks odd-current cancellation;
- a domain defect between additive Schwartz transport and multiplicative Tate
  completion;
- a renormalized infinite-label boundary term;
- a marked incidence port absent from value sampling.

Such a residual must be constructed and typed independently. It cannot be
defined as the difference of two arrows when one arrow does not exist.

## Finite falsifier

Choose a nonzero Schwartz function (h\) satisfying

\[
h(n)=0
\]

for every integer while (h'(n_0)\neq0\) at some integer (n_0\). Then

\[
S_0h=0,
\qquad
S_0ah\neq0.
\]

This is the exact kernel witness proving that the annihilator does not descend
through value sampling.

For any proposed enlarged boundary constructor, the finite transport
falsifier is instead the twisted square

\[
U_Ca_C-ia_CU_C.
\]

If it vanishes, the constructor adds no annihilator mismatch. If it is nonzero,
every component must be traced to a declared boundary or compression channel.

## Consequence

The Gaussian annihilation law supplies exact source provenance and a positive
oscillator energy. Poisson/Fourier transport carries it coherently but does not
turn it into an orientation current. The next RH-bearing object cannot be the
full-source annihilator commutator. It must be a source-authorized boundary
defect created at a specific lossy crossing, with the discarded jet or marked
port retained explicitly.
