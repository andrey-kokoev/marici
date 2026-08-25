# Fiber-orbit lower bound for reverse-lift selectors

## Setting

Let

\[
U:C\to E
\]

be a forgetful projection, and let \(G_e\) be the group of transformations
of the fiber \(F_e=U^{-1}(e)\) that are invisible in the projected packet.
A reverse-lift constructor must select one candidate \(c\in F_e\).

If the orbit

\[
\mathcal O(c)=G_e c
\]

contains \(r\) distinct candidates, the projected packet contains no
distinction among those \(r\) alternatives.

## Information lower bound

Any deterministic selector input capable of choosing every member of the
orbit must have at least \(r\) distinguishable states. In binary encoding it
therefore needs at least

\[
\boxed{\lceil\log_2r\rceil}
\]

bits of additional distinguishing information.

More generally, a selector choosing \(c\) must reduce the invisible symmetry
from \(G_e\) to a subgroup of its stabilizer

\[
\operatorname{Stab}(c)=\{g\in G_e:gc=c\}.
\]

The orbit-stabilizer relation

\[
r=[G_e:\operatorname{Stab}(c)]
\]

measures the minimum number of invisible alternatives the new source data
must separate.

## Authority qualification

This is only an information lower bound. Supplying an arbitrary bit string
does not create authority.

A lawful lift still requires:

1. a named selector constructor;
2. a source authority root for its distinguishing input;
3. an exact map from selector states to fiber candidates;
4. support, resource, epoch, and fault semantics;
5. coherence under the residual stabilizer.

Random choice, software defaults, lexical ordering, or byte-level
canonicalization may satisfy the information count while remaining
unauthorized.

## Smallest witness

For the two-element fiber

\[
\{c_{\mathrm{linear},e},c_{\mathrm{bounded2},f}\},
\]

the invisible swap group has orbit size two. At least one new binary
distinction is necessary. A selector bit can choose a member, but only a
source-authorized declaration that the bit means, for example,
“linear modality at epoch \(e\)” can make the choice operative.

Deleting the selector input restores the swap symmetry and makes compilation
ambiguous. Changing its interpretation while retaining the same bit is a
coherence failure.

## Cross-sector readings

- **Strominger.** Importing one of two core capabilities from the same
  legacy packet needs at least one extra distinction, plus native authority
  for modality, quantity, roots, and epoch. The lower bound exposes why a
  default import policy is a hidden constructor.
- **Kitaev.** If \(r\) physically inequivalent gadgets implement one logical
  operation, compilation needs enough source data to select the gadget
  orbit, followed by an explicit encoding/fault-model proof. Cost ordering
  alone is not authority.
- **Arithmetic/RH.** A scalar kernel with an \(r\)-dimensional family of
  inequivalent labelled lifts cannot canonically select one using scalar
  data. Gauge fixing may encode a representative, but the source must
  authorize the gauge and its transport coherence.
- **Benincasa.** Multiple insertion/contact representatives of one period
  value require an adapter carrying enough source distinctions to select the
  correct quotient class and representative data.

## Finite compiler gate

For a proposed reverse lift:

1. enumerate the relevant finite symmetry orbit;
2. compute its size \(r\);
3. count distinguishable admitted selector states;
4. reject if fewer than \(r\);
5. independently verify authority and semantics of every selector state.

The rejection witness is

\[
\texttt{selector\_distinguishability\_deficit}
\]

with orbit size, available state count, and minimum binary width.

## Durable statement

> Invisible fiber symmetries quantify the minimum new distinction required
> by a reverse lift. Meeting that information bound is necessary but never
> sufficient for authority; the distinguishing data and selector
> constructor must themselves be source-authorized.

