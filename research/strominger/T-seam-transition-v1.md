# Explicit role/index and coefficient-reference seam

## Candidate occurrence transition

For a native reference at absolute origin r, define

```
J_r(role,i) = (opposite role, 2r+2-i).
```

It pairs C_r with M_(r+2), M_r with C_(r+2), and C_(r+1) with M_(r+1).
The C0/M2 abstract seam now has an explicit transition carrying role and index,
rather than equating their occurrences.

At fixed r, J_r squared is identity. It is covariant under translating every
index and the origin together. Composition at successive reflection centers
satisfies J_(r+1) J_r = index translation by +2 with role restored. Thus the
family does not justify resetting origins or declaring a finite phase period.

All 24 saved hydrogen markings, at origins 0..10 (264 cases), pass the
context-aware reversed local frame audit.

## The missing coefficient-reference distinction

Use two five-coordinate reference bases:

```
Incoming: C0 M0 C1 M1 C2
Outgoing: M0 C1 M1 C2 M2
```

J maps the first set bijectively onto the second. In their displayed orders,
the coefficient basis transition is

```
Q = [4,3,2,1,0].
```

In particular, the coefficient at incoming C0 is carried to outgoing M2. No
new sixth amplitude is supplied and no missing slot is set to zero. Applying
the reverse reference transition recovers the original five independent
coefficients exactly.

This replaces the earlier attempted fixed-basis geometric identification with
an explicit direction-dependent reference basis. It remains a chosen chart
law; it is not a proof that six independent physical amplitudes reduce to five.

## Native dual maps recovered

Invert the original edge map, then change its reference basis with Q:

```
Q NE^-1 Q = PN
Q PN^-1 Q = NE
```

Both equalities hold exactly for the supplied native five-slot maps. Therefore
old E->N->P, expressed in the outgoing dual basis, uses exactly the native
new P->N->E coefficient permutations—not merely arbitrary inverse matrices.
Symbolic independent coefficient labels verify the full two-step traces in all
264 cases. Combined with the context-aware reader transformation, both local
frames and coefficient maps have compatible reversal conventions.

## Relation to the T model

This supplies a candidate seam transition for the abstract a=[C0~M2] reference
class and resolves its five-slot bookkeeping. It supports the already tested
reversal action fixing a and exchanging b/c. It does not yet derive an order-three
physical rotation, identify a barycentric coordinate with the integer origin,
or glue all assembly loops consistently. The proposed a=R,b=M,c=C naming remains
a model interpretation rather than a consequence of the permutation identities.

Native image-channel dimensions and the twelve-sector electron dictionary
still require a separate common-object construction. The occupied-support
contraction permission remains an additional rule; this reference transition
does not itself remove occupied N support.

Production/viewer unchanged.

```sh
node research/strominger/checkers/check_T_seam_transition.mjs
```

Evidence: `results/T-seam-transition/verification.json`.
