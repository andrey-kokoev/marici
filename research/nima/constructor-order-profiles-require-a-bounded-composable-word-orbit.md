# Constructor order profiles require a bounded composable-word orbit

## Order-profile category

Attach to every typed constructor

[
S:E_{-delta}^{A}longrightarrow E_{-ho_S(delta)}^{B}
]

a monotone order profile (ho_S). Only profiles of composable arrows may be
combined. For a typed composite (Tcirc S),

[
ho_{Tcirc S}(delta)
le
ho_T(ho_S(delta)),
]

with the inequality reversed if the frozen rung convention orders larger
indices as stronger rather than weaker spaces.

The completion question is therefore about the action of the typed constructor
semigroupoid on order parameters, not about nine isolated continuity proofs.

## Two closure regimes

A common fixed rung exists if there is a compatible family
(delta_A), one for each object type, such that every admitted arrow
(S:A	o B) satisfies

[
ho_S(delta_A)ledelta_B.
]

A weaker bounded-orbit regime starts from (delta_0) and requires

[
sup_{winmathcal W_{mathrm{adm}}}ho_w(delta_0)<infty
]

over the constructor words actually admitted by typing and completion.

The object-indexed version matters: grade doubling is not necessarily an
endomorphism of one rung. A single scalar (delta_*) can falsely reject a
valid family of grade-indexed spaces.

## Affine profile test

Suppose a generator has

[
ho_S(delta)=a_Sdelta+b_S,
qquad a_S,b_Sge0.
]

For an endomorphism on one object, a finite invariant rung can satisfy

[
a_Sdelta_*+b_Sledelta_*.
]

Hence:

- if (a_S<1), it suffices that
  [
  delta_*gerac{b_S}{1-a_S};
  ]
- if (a_S=1), positive drift (b_S>0) forbids a fixed rung;
- if (a_S>1), no positive fixed rung exists when (b_Sge0), unless
  iteration is not admitted or the object index changes the comparison.

Thus the additive hostile (deltamapstodelta+1) and multiplicative hostile
(deltamapsto2delta) are exact endomorphism obstructions.

## Adams typing correction

Grade-doubling Adams transport naturally relates different object types:

[
A_2:E_{-delta}^{(k)}
longrightarrow
E_{-ho_{A_2,k}(delta)}^{(2k)}.
]

Repeated Adams operations produce grades (k,2k,4k,ldots). There are three
legitimate outcomes:

1. the source admits only bounded Adams depth in the first-edge constructor;
2. grade-indexed rung choices (delta_k) absorb the doubling;
3. the full inductive/projective topology admits all finite grades and proves
   continuity of the unbounded order orbit.

Calling (ho(delta)=2delta) unstable before deciding which outcome is
source-typed would conflate an endomorphism with a grade-changing arrow.

## Cycle criterion

The strongest finite falsifiers are typed cycles. If a constructor word
(w:A	o A) returns to the same object and

[
ho_w(delta)>delta
]

for every admissible (delta), repeated traversal escapes every fixed rung.
Acyclic grade growth can be handled by object-indexed spaces; positive drift
around a genuine constructor cycle cannot.

Therefore the first calculation should be on cycle profiles, paralleling the
earlier holonomy audit.

## Matrix and tropical compilation

For affine profiles, composition obeys

[
(a_T,b_T)circ(a_S,b_S)
=
(a_Ta_S,;a_Tb_S+b_T).
]

Each admitted word can therefore be compiled exactly. The finite audit should
record:

- source and target object types;
- profile pair ((a_S,b_S));
- whether iteration is typed;
- every fundamental constructor cycle;
- its composite profile;
- a common object-indexed invariant region or a declared limit-topology proof.

This is a one-dimensional affine holonomy representation of the constructor
category.

## Frontier

The names and types of the nine operations must be frozen from the source
before assigning profiles. The immediate executable packet is not nine guessed
numbers. It is a typed profile table with unknown entries, followed by source
derivation of each entry and exact cycle compilation.

The decisive theorem is:

> Every admitted constructor cycle has a nonexpanding order profile on one
> common object-indexed region, or the declared projective/inductive topology
> proves continuity of its full orbit.

Only then does generatorwise continuity lift to a completion-stable common
domain.
