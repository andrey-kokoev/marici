# The Reciprocal Tail Domain Is a Trace Pullback but Dual Times Dual Has No Canonical Green Pairing

## Half-line graph domains

For fixed complex `s`, consider the source tail differential

\[
D_sG=G'+sG.
\]

Its maximal `L2` graph domain on a scale half-line is

\[
\operatorname{Dom}(D_s)=H^1(\mathbb R_+),
\]

because `G` and `D_sG` lie in `L2` exactly when `G` and `G'` do.  Endpoint
evaluation at zero is continuous in the graph norm.  The source solution

\[
G_s(q)=e^{-sq}\int_q^\infty f(v)e^{sv}\,dv
\]

satisfies

\[
D_sG_s=-f,
\qquad
G_s(0)=\int_0^\infty f(v)e^{sv}\,dv.
\]

Thus the scalar zero condition is exactly the additional zero-trace boundary
condition on a source-derived graph-domain state.

## Reciprocal sewing is a pullback

Let `D+` and `D-` be the two oriented half-line graph domains.  Their native
sewing is the trace pullback

\[
D_{\mathrm{sew}}
=
D_+\times_{\mathbb C}D_-
=
\{(G_+,G_-):G_+(0)=G_-(0)\}.
\]

After reversing the negative coordinate, this pullback is canonically
`H1(R)`.  Therefore the archimedean graph-domain problem itself is closed:
the seam is neither an arbitrary boundary condition nor an additional fitted
Hilbert norm.  It is the equalizer of the two continuous trace maps.

Tensoring this construction with the arithmetic test space from the previous
result gives the source test domain

\[
\mathcal D_{\mathrm{test}}
=
\mathcal S_P\widehat\otimes H^1(\mathbb R),
\]

with reciprocal transport, Mellin translation, the doubled differential, and
all continuous arithmetic boundary rows defined before completion.

## The genuine obstruction

The completed theta state need not be test-valued.  It may naturally lie in
the dual extension

\[
\mathcal S_P'\widehat\otimes H^1_{\mathrm{loc}}.
\]

The primitive and augmentation boundary currents also lie in `S_P'`.  There
is no canonical bilinear pairing

\[
\mathcal S_P'\times\mathcal S_P'\longrightarrow\mathbb C.
\]

This is not abstract fussiness.  The constant coefficient row is a continuous
dual functional on `S_P`, but the formal self-pairing of two such rows is
`sum_p 1`, which diverges.  A Riesz map, a regulator, or a chosen pivot norm
can assign a value only by adding structure not yet derived from the source.

Consequently, passing the finite Green identity to completion is legitimate
when one input remains test-valued and the other dual-valued.  It is not yet
legitimate on two independently dual-valued completed states.

## The next categorical object

The missing object is not another maximal differential domain.  It is a
source-derived intermediate space `E` with a continuous pairing

\[
\mathcal S_P\subset E\subset\mathcal S_P',
\qquad
E\times E\longrightarrow\mathbb C,
\]

such that:

1. the completed zero-state belongs to `E`;
2. reciprocal Fourier transport and Mellin translation preserve `E`;
3. endpoint traces and primitive, square, seam, and archimedean currents act
   continuously on `E` in their typed directions;
4. the doubled Green form extends without choosing a divisor-dependent
   regulator;
5. finite Euler cutoffs are dense in the graph topology.

Equivalently, the Green form itself may define a source-native dual pair
`E+ x E-` rather than a self-pairing on one space.  This would fit the two
sector architecture more faithfully: each reciprocal sector supplies the
test direction for the other's boundary current.

## Result

The archimedean completion is no longer obstructed: its correct domain is the
trace pullback of two half-line `H1` domains.  The first real completion
obstruction occurs only after arithmetic dualization.  Two dual-valued
objects have no canonical Green pairing.  The next theorem must derive either
a source-native intermediate dual-pair domain or an explicitly cross-sector
pairing; it may not insert a Hilbert pivot by convenience.

