# Corridor Suspension Cocycle and the Graded Reflection-Lift Gate

## Record

Date: 2026-08-15

Status: proved integral classification of the suspension-valued reflection
required by entry225. The class is the nonzero element of
(H^1(C_2;\mathbb Z_{\rm sign})\cong\mathbb Z/2). This does not construct
the wall-supported geometric correspondence or the literal entry143 map. No
graph admission is claimed.

## The graded reflection equation

Reflection exchanges the ordinary and shifted corridor boundaries. Let
(ain\mathbb Z) be the degree carried by the forward exchange. Because
reflection acts on the shift lattice by sign, the cocycle equation is
\[
a+r(a)=a-a=0.
\]
Thus every integer is a cocycle. Changing the grading trivialization on one
boundary changes (a) by
\[
b-r(b)=2b.
\]
Consequently
\[
H^1(C_2;\mathbb Z_{\rm sign})
=\mathbb Z/2.
\]

The required exchange (P\leftrightarrow P[1]) has (a=1), hence is the
nonzero class. The reverse exchange has degree (-1), so their composite has
degree zero and reflection still squares to the identity. But the odd class
cannot be removed by any integral change of boundary grading.

## Geometric consequence

An ordinary reflection pullback has degree cocycle zero. It therefore cannot
realize the entry225 exchange even after replacing a dualizing line by an
ungraded two-term wall complex. The wall correspondence must additionally
carry a graded lift of the reflection action groupoid whose forward and
reverse arrows have degrees (+1) and (-1).

This is not the physical endpoint parity (p_{\partial,Q}). It is a local
grading obstruction attached to the corridor reflection. Identifying the two
would be circular: the physical class is defined only after the pointed
endpoint/(Q) mapping fiber exists.

## Minimal next datum

The smallest viable geometry now has two inseparable parts:

1. a wall-supported two-term relative-dualizing/excess triangle restricting
   to (P) and (P[1]);
2. a graded reflection-groupoid lift carrying the odd suspension cocycle and
   compatible with endpoint Beck--Chevalley maps.

Only after both are mapped to literal entry143 normal/Cech rows can the
endpoint connector and generic-(Q) equations be assembled.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_corridor_suspension_cocycle.rs`

The checker verifies the cocycle equation, the Smith factor `[2]`, the
nontrivial odd class, and cancellation of forward/reverse degrees.

SHA-256:
`6fdc921b506f910088c7aec32fcb7b483901cd91b6baa6ecd080a8496ecd0f37`

Fresh `rustfmt --check`, warnings-denied optimized compilation, runtime
assertions, and JSON output passed. Native PowerShell was used only because
the user-site structured-command surface cannot access this repository or
invoke `rustc`.

## Outcome contract

~~~json
{
  "claim": "The suspension-valued corridor reflection is the nonzero integral class in H1(C2;Z_sign)=Z/2; it cannot be realized by an ordinary degree-zero geometric reflection or removed by an integral regrading.",
  "status": "proved_scoped_corridor_suspension_cocycle",
  "scope": "integral grading local system on the two-boundary reflection action groupoid",
  "smith": [2],
  "required_cocycle": 1,
  "required_class_mod_2": 1,
  "ordinary_reflection_class": 0,
  "not_identified_with": "physical p_partial_Q",
  "minimal_additional_datum": "a graded reflection-action-groupoid lift with odd suspension cocycle, coupled to the wall-supported two-term excess triangle",
  "unconstructed": [
    "wall-supported excess triangle",
    "literal entry143 realization",
    "endpoint connector cells",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_corridor_suspension_cocycle.rs",
  "checker_sha256": "6fdc921b506f910088c7aec32fcb7b483901cd91b6baa6ecd080a8496ecd0f37"
}
~~~
