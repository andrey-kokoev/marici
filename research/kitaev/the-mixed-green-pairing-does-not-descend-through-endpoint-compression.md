# The mixed Green pairing does not descend through endpoint compression

## Question

Does the reciprocal mixed Green pairing descend through the local scalar
endpoint traces, or must the tail functions remain present until relational
sewing?

## Source graph domains

For fixed \(s\), let

\[
D_sG=G'+sG
\]

on the half-line graph domain

\[
\mathcal D_s=H^1(\mathbb R_+).
\]

Endpoint evaluation

\[
\tau_0(G)=G(0)
\]

is continuous. Its kernel is

\[
\mathcal D_s^0
=
\{G\in H^1(\mathbb R_+):G(0)=0\}.
\]

The reciprocal side has its own oriented graph domain and endpoint trace.

## Mixed Green pairing

Before scalar endpoint compression, the natural cross-sector bulk contains
the sesquilinear pairing

\[
\beta(G_+,G_-)
=
\int_0^\infty
G_+(q)\overline{G_-(q)}\,dq.
\]

This pairing is continuous on the \(L^2\) components of the graph domains.

For it to descend through the two endpoint maps, the relational descent
theorem requires

\[
\beta(\ker\tau_0,\mathcal D_-)=0
\]

and

\[
\beta(\mathcal D_+,\ker\tau_0)=0.
\]

Both conditions fail.

## Exact source-admissible witness

Choose any nonzero

\[
h\in C_c^\infty(0,\infty).
\]

Then

\[
h(0)=0.
\]

For the plus source flow, define

\[
f_+=-(h'+s_+h).
\]

For the reciprocal flow, define

\[
f_-=-(h'+s_-h).
\]

Both forcings are compactly supported smooth source functions, and the
corresponding decaying tail solutions are

\[
G_+=h,
\qquad
G_-=h.
\]

Their endpoint traces vanish:

\[
\tau_0(G_+)=\tau_0(G_-)=0.
\]

But

\[
\beta(G_+,G_-)
=
\int_0^\infty|h(q)|^2\,dq
>0.
\]

Thus the mixed Green pairing is nonzero on the product of the two local trace
kernels.

This is a source-range witness, not merely an arbitrary ambient Sobolev
vector.

## Consequence

No pairing on the two scalar endpoint values can reconstruct the mixed Green
bulk. In particular, there is no function

\[
\overline\beta:\mathbb C\times\mathbb C\longrightarrow\mathbb C
\]

such that

\[
\beta(G_+,G_-)
=
\overline\beta(G_+(0),G_-(0))
\]

for all source-admissible tails.

The endpoint scalar is a boundary observation of the tail state. It is not a
quotient sufficient statistic for reciprocal Green sewing.

## Trace pullback remains valid

This does not invalidate the reciprocal trace pullback

\[
\mathcal D_{\rm sew}
=
\mathcal D_+\times_{\mathbb C}\mathcal D_-.
\]

The pullback retains the full pair of tail functions while imposing equality
of their endpoint traces. The witness \((h,h)\) belongs to this sewn carrier.

What fails is the later compression

\[
\mathcal D_{\rm sew}\longrightarrow\mathbb C
\]

that remembers only the common endpoint.

Thus local trace sewing is compatible with the relational form; scalar
endpoint totalization is not.

## Architecture verdict

The order must be:

1. retain each half-line graph state;
2. impose the endpoint equalizer;
3. form the cross-sector Green or signed-kernel relation;
4. quotient only the radical of the complete relation;
5. take scalar endpoint or determinant readouts afterward.

Quotienting to the endpoint line before step three destroys a nondegenerate
infinite-dimensional interior tail subspace.

This is a concrete theta instance of relational-first completion.

## Relation to the physical alternating polarization

The physical mixed-sheet numerator is an alternating combination of several
cross products and becomes a reflection coboundary. The present witness
proves non-descent of the underlying mixed Green pairing through endpoint
compression.

It does not by itself prove that the full alternating physical combination
is nonzero on the same diagonal witness; antisymmetry can cancel special
choices. The next audit must apply the complete alternating numerator to
independent zero-trace source tails before imposing the reflection-fixed
relation.

This qualification prevents replacing the physical source combination by one
convenient mixed product.

## Completion implication

The endpoint trace has infinite-dimensional kernel at every finite cutoff and
after graph completion. This is not a small singular-value phenomenon. It is
an exact structural kernel.

Any completion that retains only endpoint values loses the mixed relation
before arithmetic dualization even begins. Adding primitive or square scalar
currents later cannot reconstruct an arbitrary lost tail pairing unless a
source theorem shows those currents are jointly faithful on the trace kernel.

No such theorem is currently pinned.

## Minimal falsifier certificate

A descent claim is rejected by the packet:

    {
      "code": "mixed_green_pairing_not_endpoint_descending",
      "plus_trace": 0,
      "minus_trace": 0,
      "plus_source": "-(h' + s_plus h)",
      "minus_source": "-(h' + s_minus h)",
      "mixed_pairing": "||h||_2^2 > 0",
      "source_admissible": true
    }

## Disposition

The finite kernel test is decisive for the basic mixed Green form: it does
not descend through scalar endpoint compression. The full tail carrier must
survive until reciprocal relational sewing.

The remaining sharper calculation is the same test for the complete
alternating physical polarization and its transverse-jet quotient.

## Claim boundary

This packet proves non-descent for the natural mixed \(L^2\) Green pairing on
the source graph domains. It does not yet establish non-descent of every
alternating or reflection-reduced physical combination.
