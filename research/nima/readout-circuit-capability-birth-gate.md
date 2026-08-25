# Readout circuits and capability birth

Owner: `marici.Nima`

## Question

When does failure of observation create a new class, rather than merely break
one coordinate chart or expose an already-declared repair?

Let a source space `S` carry a readout map

\[
O:S\longrightarrow R
\]

and let `B` be the source-derived repair subspace, with

\[
B\subseteq\ker O.
\]

For one frozen map, the observable silent sector is not `ker O` by itself. It is

\[
\mathcal H_O=\ker O/B.
\]

For a family over a coefficient ring `A`, even this is insufficient.  At a
stratum `p`, one must also remove relations already present generically:

\[
K_{\mathfrak p}^{\rm new}
=
\frac{\ker(O\otimes_A k(\mathfrak p))}
{B_{\mathfrak p}+\operatorname{sp}_{\mathfrak p}(K_{\rm gen})}.
\]

Thus a supported birth is measured relative to both declared repairs and the
specialized generic kernel.

This separates three phenomena.

1. **Chart failure.** A selected maximal minor vanishes, but another maximal
   minor is nonzero.  The full map remains injective and `ker O=0`.
2. **Repair circuit.** The readout loses rank, but every new null vector lies
   in `B`.  A silent combination exists, but it is already declared
   equivalent to zero.
3. **Capability birth.** The readout loses rank and
   the specialized kernel contains a vector outside both the repair image and
   the specialized generic relations.

## Route loss versus destructive interference

The same zero result can have two inequivalent lifts.  Factor the readout as

\[
S\xrightarrow{T}R_L\oplus R_R
\xrightarrow{\sigma}R,
\qquad
\sigma(A,B)=A+B.
\]

Then:

- **route loss:** `T(s)=(0,0)`;
- **destructive interference:** `T(s)=(A,-A)` with `A != 0`.

Both satisfy `(sigma circ T)(s)=0`, but only the second carries nonzero route
information.  Its residue is not a third signal and is not added after the
result.  It is the nonzero class in

\[
\ker\sigma=\{(A,-A)\},
\]

forgotten by the sum readout.  In characteristic two the same definition is
used even though `-A=A`; the kernel, rather than the visual sign, is the
invariant object.

For Strominger's determinant,

\[
\det C_{g,d}=C_LL+C_RR,
\]

the route ideal `(L,R)` detects simultaneous constructor loss, while the
Fitting determinant detects both route loss and cancellation after adapter
weighting.  Therefore a Fitting component must be annotated by its lift to
the route space before it is interpreted physically.

The resulting decomposition is a constructible stratification, not generally
a decomposition into closed components.  If `F=C_L L+C_R R` and
`J=(L,R)`, then

\[
\mathfrak D_{\rm route}=V(J),
\qquad
\mathfrak D_{\rm int}=V(F)\cap D(J).
\]

Here `D(J)` means that at least one route survives.  The closure of
`mathfrak D_int` may contain `mathfrak D_route`, so factorization of `F`
alone cannot recover the provenance.  The route map and pairing map must
remain separately typed in the exported matrix packet.

For a minimally dependent set of source columns, the surviving null vector is
the primitive circuit.  In a two-dimensional observation space, three
pairwise independent columns have one such circuit, with coefficients given
by their signed Pluecker coordinates.

## Strominger instance

At `(g,q)=(2,7)`, the transported columns are

\[
v_0=(-6,-8),\qquad v_4=(0,-2),\qquad v_6=(3,1).
\]

Every pair is independent, while

\[
v_0-3v_4+2v_6=0.
\]

Thus `(1,-3,2)` is the unique primitive three-column circuit.  Its novelty is
not established by rank loss alone: it is established only after checking
that it is not in the declared rational-exact/repair sector.

## Kitaev instance

Over `F_2`, the three-column syndrome map

\[
H=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}
\]

has pairwise independent columns and primitive circuit `(1,1,1)`.  Whether
this is a logical class depends on the boundary subspace:

- if `(1,1,1)` is a stabilizer boundary, it is a repair circuit;
- if it is a noncontractible cycle outside the boundary image, it is a
  logical capability.

This is the exact bridge between the magnetic kernel and fault-tolerant
syndrome language.

## Family-level rank discriminant

For a finite free presentation matrix `E` with generic rank `r`, the intrinsic
rank-discriminant is

\[
\mathfrak D=V(I_r(E)),
\]

where `I_r(E)` is the ideal of all generic maximal minors.  One minor
vanishing is only a chart boundary; every maximal minor vanishing is a true
represented-matroid change.

Equivalently, for the observation complex

\[
C_E=[\mathcal M\xrightarrow{E}\mathcal R],
\]

the supported invisible information is the new negative homology after
derived specialization.  Under the usual finite free hypotheses it is
controlled by

\[
\operatorname{Tor}_1^A(\operatorname{coker}E,k(\mathfrak p)).
\]

The checker includes the model

\[
E(t)=\begin{pmatrix}1&0&1\\0&t&t\end{pmatrix}.
\]

Its maximal-minor ideal is `(t)`.  Generic nullity is one, special nullity is
two, and quotienting by the specialized generic relation leaves exactly one
new supported direction.

## Deutsch--Popperian conjecture

Every genuine finite Carrier coefficient birth is a minimally supported
readout circuit in the Fitting rank-discriminant that survives both the
source-derived repair quotient and specialization of generic relations.
Apparent births are Pluecker-chart failures, old generic relations, or circuits
already killed by the repair image.

Additionally, every supported readout zero must be classified as route loss
or pairing-kernel interference.  These have the same displayed result but
different provenance and different successor behavior.

## Falsifiers

- A new class appears while the full readout remains injective.
- A purported physical class lies in the repair image.
- A kernel birth has no minimally dependent circuit support after restriction
  to its active source labels.
- Two legal chart choices disagree on whether the quotient class exists.
- A proposed route-loss explanation has a nonzero lift in route space.
- A proposed interference residue vanishes before the pairing map.

## Next gate

For every known magnetic kernel generator, export:

\[
(\text{active columns},\ \text{readout rank},\ \text{primitive circuit},\
\text{repair-membership}).
\]

The conjecture survives only if the two grade-two exceptions are the only
circuits outside the repair sector, while every determinant-only failure has
zero full kernel.
