# The Even-Veronese Endpoint Carries a Commuting Metaplectic Pair

## The spectator is another control module

Write the endpoint algebra as

\[
\mathcal C=\mathbb C[u,v]_{\mathrm{even}}.
\]

Each spinor coordinate supplies its own metaplectic triple:

\[
E_u=\frac{u^2}{2},\quad F_u=-\frac{\partial_u^2}{2},\quad
H_u=u\partial_u+\frac12,
\]

and the analogous operators \(E_v,F_v,H_v\). Each triple obeys the `sl2`
relations and has Casimir \(-3/4\). Every operator in the \(u\)-triple
commutes with every operator in the \(v\)-triple.

Thus the native control algebra is

\[
\mathfrak{sl}_2^{(u)}\oplus\mathfrak{sl}_2^{(v)}.
\]

The exponent of \(v\) is spectator multiplicity only relative to the chosen
\(u\)-action. Without a preferred spinor axis, it is itself dynamical under
the second commuting action.

## Parity decomposition

Because the algebra contains monomials of even total degree, it decomposes as

\[
\mathcal C=
(M_u^{\rm even}\otimes M_v^{\rm even})
\oplus
(M_u^{\rm odd}\otimes M_v^{\rm odd}).
\]

Both summands are preserved by the commuting metaplectic pair. The spinor
exchange \(u\leftrightarrow v\) swaps the two `sl2` factors while preserving
each total-parity summand.

This is the first source-native six-control system in the comparison:

```text
three u-controls + three v-controls.
```

It must not be conflated with the earlier six interchange squares, which are
three controls tested across two directed stage arrows. One is a generator
count; the other is a coherence-test count.

## Implication for reciprocal sewing

If reciprocal sewing exchanges the two spinor axes, it should implement the
outer automorphism

\[
\mathfrak{sl}_2^{(u)}\leftrightarrow
\mathfrak{sl}_2^{(v)}.
\]

Then the correct invariant and anti-invariant controls are the diagonal and
relative triples

\[
E_\pm=E_u\pm E_v,qquad
F_\pm=F_u\pm F_v,qquad
H_\pm=H_u\pm H_v.
\]

The plus triple is sewing-even and the minus triple is sewing-odd. This gives
a precise algebraic location for a relative seam channel without inventing a
new generator.

## Scope and next gate

The spinor exchange is canonical on the abstract conic, but it has not yet
been identified with theta reciprocal sewing. The next source test must derive
the map from the completed theta boundary data and check whether it exchanges,
fixes, or mixes the two metaplectic factors.

The claim fails if cross-commutators are nonzero, either Casimir changes, the
even algebra is not preserved, or the source sewing does not act by the
proposed factor exchange.
