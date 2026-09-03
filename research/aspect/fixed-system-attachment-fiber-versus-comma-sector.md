# Fixed-system attachment fiber versus comma sector

## Question

For a fixed original system \(S\), should its instrument sector be the strict fiber of the forgetful functor or the comma category \((S\downarrow U)\)?

## Claim boundary

This packet compares the two constructions for a Grothendieck fibration of attachments. It does not identify a source-to-target map with physical evolution or claim that every comma object is a physical realization of \(S\).

## Strict fiber

Let

\[
U:\mathcal S_{\rm inst}\to\mathcal S
\]

be the projection from the Grothendieck construction of

\[
\operatorname{Att}:\mathcal S^{op}\to\mathbf{Cat}.
\]

The strict fiber \(U^{-1}(S)\) has:

- objects \((S,D)\) with \(D\in\operatorname{Att}(S)\);
- morphisms over \(\operatorname{id}_S\).

For the strict Grothendieck construction, this fiber is exactly \(\operatorname{Att}(S)\). It classifies decorations that preserve the underlying system.

## Comma category

An object of \((S\downarrow U)\) is

\[
((T,E),a:S\to T).
\]

It may have \(T\ne S\). Hence it classifies an attached target together with a base-system map from \(S\), not merely an attachment on \(S\).

A morphism from \(((T,E),a)\) to \(((T',E'),a')\) is a total-category map \(h:(T,E)\to(T',E')\) satisfying

\[
U(h)\,a=a'.
\]

This construction is appropriate when a source interface into a changed carrier matters. The arrow \(a\) has no physical-time meaning without a separately supplied physical process map.

## Pullback comparison

Because \(U\) is a fibration with chosen pullbacks, define

\[
K:(S\downarrow U)\to\operatorname{Att}(S),
\qquad
K((T,E),a)=a^*E.
\]

There is also a fully faithful inclusion

\[
J:\operatorname{Att}(S)\to(S\downarrow U),
\qquad
J(D)=((S,D),\operatorname{id}_S).
\]

Chosen reindexing gives

\[
KJ=\operatorname{id}.
\]

Moreover,

\[
\operatorname{Hom}_{(S\downarrow U)}(J(D),((T,E),a))
\cong
\operatorname{Hom}_{\operatorname{Att}(S)}(D,a^*E).
\]

Thus

\[
J\dashv K.
\]

The fiber is a reflective subcategory of the comma sector. The right adjoint \(K\) returns the attachment data visible after pulling the target back to \(S\).

There is no general reverse adjunction: a comma morphism from \(((T,E),a)\) to \(J(D)\) would require a base map \(T\to S\) retracting or otherwise cohering with \(a\).

## Finite witness

For the base poset \(S_0\to S_1\), with two discrete attachments over each base object, the fiber over \(S_0\) has two objects. The comma category \((S_0\downarrow U)\) has four: two over \(S_0\) and two attached targets over \(S_1\).

Exhaustive hom-set comparison verifies \(J\dashv K\). Treating the comma category as the strict fiber fails the cardinality check \(4\ne2\).

## Disposition

Use \(\operatorname{Att}(S)\) or the strict fiber for instrumentation that leaves \(S\) unchanged. Use \((S\downarrow U)\) when the mathematical object includes a map from \(S\) into a possibly changed attached target. The pullback right adjoint relates them but does not identify them.
