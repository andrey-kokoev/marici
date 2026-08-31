# Reduced-ratio grade order makes the projective cycle port reciprocal-equivariant

## Question

Can the greedy forest order be derived from the ordered theta-pair arithmetic and made compatible with reciprocal exchange?

## Claim boundary

Yes. In each rational ratio block, reduce the ordered pair to a primitive pair times one common grade. Order edges by a Cantor-diagonal combination of shell ordinal and common grade. Reciprocal exchange preserves both indices, translates the endpoint graph, and therefore carries the greedy forest and chord port isomorphically to the opposite ratio block.

## Primitive ratio coordinates

Write the positive rational ratio in lowest terms as

\[
\frac mn=\frac ba,
\qquad
\gcd(a,b)=1.
\]

Then every ordered pair in this block has a unique common grade \(g\ge1\):

\[
n=ga,
\qquad
m=gb.
\]

For the \(j\)-th consecutive-prime shell \((p_j,q_j)\), the translated edge is

\[
e_{j,g}^{a,b}
=
[\log(gap_j),\log(gaq_j)].
\]

The half-density amplitude is

\[
(nm)^{-1/2}
=
\frac1{g\sqrt{ab}}.
\]

## Source-derived edge order

Order \((j,g)\in\mathbb N^2\) by total grade

\[
\Gamma(j,g)=j+g,
\]

then by \(j\), then by \(g\). Every initial grade cutoff is finite, and every edge appears after finitely many predecessors. This is a source-derived order from consecutive-prime shell ordinal and common theta dilation grade; it does not inspect response values, Xi zeros, or desired inverses.

Use this order in the greedy forest construction for every reduced ratio block.

## Reciprocal graph isomorphism

Reciprocal exchange sends

\[
(n,m)=(ga,gb)
\longmapsto
(gb,ga)
\]

and therefore

\[
D=\log(b/a)
\longmapsto-D.
\]

The reflected edge is

\[
e_{j,g}^{b,a}
=
[\log(gbp_j),\log(gbq_j)].
\]

It is the original edge translated by the fixed logarithmic displacement:

\[
e_{j,g}^{b,a}
=e_{j,g}^{a,b}+\log\frac ba.
\]

Translation preserves endpoint equality, paths, connected components, and cycles. Since reciprocal exchange also preserves the ordering pair \((j,g)\), greedy admission or rejection agrees edge by edge. Thus

\[
e_{j,g}^{a,b}\in T_D
\quad\Longleftrightarrow\quad
 e_{j,g}^{b,a}\in T_{-D}.
\]

## Chord-port intertwining

Let \(R_D\) exchange the ordered labels and identify translated endpoints, and let \(R_D^Z\) carry each chord coordinate to its reflected chord. The common amplitude is unchanged because \(nm\) is symmetric. Hence

\[
Z_{-D}R_D
=
R_D^ZZ_D.
\]

With symmetric projective grade

\[
W(j,g,a,b)
=W(j,g,b,a),
\]

the reflection maps source and chord seminorms isometrically. The completed cycle observer is therefore reciprocal-equivariant without fitting a phase or coefficient.

## Cutoff compatibility

A total-grade cutoff \(\Gamma(j,g)\le N\) is finite and reflection-stable. Greedy forests, chord sets, common histories, and reciprocal maps all restrict to the same cutoff square. Passing to the projective limit preserves the intertwining identity.

## Canonicality boundary

The total-grade order is canonical only relative to three already declared choices:

1. the natural ordering of consecutive-prime shells;
2. reduced positive integer ratio coordinates \((a,b)\);
3. common dilation grade \(g\).

It is not yet an exposed G4 interface field. Another source-authorized order could yield a coherently equivalent forest, but that equivalence must be constructed rather than assumed.

## G4 consequence

A common-history architecture can retain a projective cycle port that respects reciprocal exchange and uses no post hoc observer selection. G4 still must expose whether it adopts this order, the invariant cycle space, or retained labels.

## Disposition

The projective cycle observer now has a source-derived reciprocal-equivariant ordering and reflection law. Its remaining obstruction is architectural authority: the current G4 witness does not declare any cycle port, forest order, or invariant cycle quotient. No RH conclusion is authorized.
