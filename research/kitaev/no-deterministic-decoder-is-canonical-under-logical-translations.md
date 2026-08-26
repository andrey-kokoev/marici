# No Deterministic Decoder Is Canonical Under Logical Translations

Let (T_s\) be the syndrome fiber modulo local repairs. From the preceding
packet, (T_s) is a torsor over the logical group (H_1). Thus (H_1) acts
freely and transitively:

\[
h:T_s\to T_s,
\qquad
t\longmapsto t+h.
\]

Every logical translation leaves the local syndrome (s) unchanged.

Suppose a deterministic decoder were canonical under all logical translations.
Its selected class (D(s)\in T_s) would have to satisfy

\[
D(s)+h=D(s)
\]

for every (h\in H_1\), because the input syndrome is fixed by the symmetry.
But a torsor action is free, so this equality forces (h=0). Therefore:

If (H_1\ne0), no deterministic decoder origin is invariant under the full
logical translation symmetry.

This is a symmetry obstruction, not a computational limitation.

## Exact four-class witness

For

\[
H_1=\mathbf F_2^2,
\]

the four logical classes are

\[
(0,0),(1,0),(0,1),(1,1).
\]

Translation by ((1,0)) exchanges the first pair with the second pair, while
translation by ((0,1)) exchanges the two rows. No class is fixed by both
nontrivial generators, or even by either generator individually.

Thus the smallest torus cannot have a deterministic decoder that is
simultaneously invariant under both logical loop translations and depends
only on syndrome.

## What can choose an origin

A reference class (r\in T_s) identifies the torsor with its group:

\[
T_s\longrightarrow H_1,
\qquad
t\longmapsto t-r.
\]

This selects an origin, but it breaks the translation symmetry. The reference
may come from:

- a declared vacuum or tensor unit;
- a boundary anchor;
- a geometric metric and tie-breaking frame;
- a noise prior and loss function;
- a previous-round logical-state estimate;
- an external control register.

Each is explanatory only when its origin and transport law are derived from
the source. Calling the chosen section canonical does not remove its symmetry
breaking.

## Randomized and coherent alternatives

The uniform probability distribution on a finite torsor is translation
invariant. Hence a randomized rule can preserve the symmetry, but it does not
select a preferred logical correction and generally randomizes the logical
state.

A coherent superposition over correction classes is a different quantum
operation. It requires an actuator, ancilla, and uncomputation analysis; it is
not a deterministic classical decoder hidden inside the syndrome.

## Naturality statement

More categorically, there is no natural transformation assigning a point to
every nontrivial (H)-torsor. Any torsor automorphism must preserve a natural
point, while translations provide fixed-point-free automorphisms. A pointed
torsor admits such a choice precisely because the point is added structure.

This distinguishes:

\[
\text{abstract distinction}
\ne
\text{canonical frame}
\ne
\text{implemented correction}.
\]

## Authority boundary and falsifiers

The theorem forbids a symmetry-invariant deterministic origin. It does not
forbid useful decoders that deliberately use geometry, priors, or references.
Nor does it prove that all logical translations are physical symmetries in a
particular implementation; that must be checked from the Hamiltonian and
boundary conditions.

Falsifiers are:

- claiming a torsor has a canonical zero without a reference;
- using a minimum-weight tie breaker while calling logical translations
  unbroken;
- presenting the uniform randomized decoder as logical-state preserving;
- treating a coherent correction superposition as a classical section;
- applying the no-go when boundaries or source data already point the torsor;
- inferring physical symmetry solely from abstract homology action.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to turn decoder nonselection into a symmetry no-go theorem.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. A nontrivial logical torsor has no translation-invariant deterministic
origin; every practical decoder must expose its symmetry-breaking reference.
