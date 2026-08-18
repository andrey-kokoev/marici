---
id: 484
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Restored Minus Conormal Residue Is Exact Below Resonance

## Record

Status: source-typed minus-endpoint completion of Entry 483.

Entry 483 shows that the universal quartic factor must be restored before a
conormal identity is compared with the odd resonance lattice. Put

[
c=b+1,
qquad
g=a^3c(2-c).
]

Restoring the frozen factor (a^4) and dividing by the declared minus normal
(c) gives

[
a^4rac{g}{c}
=
a^7(2-c).
]

Therefore the minus conormal residue is

[
oxed{
operatorname{Res}_{c=0}(a^4g)=2a^7.
}
]

## Degreewise typing

The residue lies in bidegree

[
(I,J)=(7,0),
]

whereas the odd resonance lies in

[
(I,J)=(7,1).
]

Using Entry 460's source-derived boundary assignment,

[
B(I,J)=
left(
leftlfloorrac I2ightfloor,
leftlfloorrac I2ightfloor+J
ight),
]

one obtains

[
B(7,0)=(3,3),
qquad
B(7,1)=(3,4).
]

Thus the restored residue is regular in its own lattice and sits exactly one
minus-incidence step below the resonance. It cannot be identified with the
resonance class by bare evaluation.

## Exactness

For the degreewise operator

[
D_b=a(1-cpartial_c),
]

the scalar into target degree ((I,J)) is (1-J). At ((7,0)),

[
1-J=1.
]

Hence the incoming block

[
D_b:(6,0)longrightarrow(7,0)
]

is a unit map, and

[
oxed{
2a^7
in
operatorname{im}D_b.
}
]

The restored minus conormal residue is therefore exact in the complete
degreewise exceptional complex. It creates no endpoint-supported odd class.

## Combined boundary result

Entry 483 makes the plus-boundary cancellation regular by restoring the
universal quartic factor. The present calculation shows that the independently
typed minus residue lands in an exact block. Together they remove the
endpoint obstruction to separating the extensive conjugate-(L_2) tail from
the reduced odd resonance line.

This is a boundary-complex result. It does not yet prove that the global
specialization morphism has no interior kernel or cokernel arising from the
quartic tail.

## Classification

- plus endpoint: typed cancellation in the ((7,1)) lattice;
- minus endpoint: exact restored residue in ((7,0));
- odd resonance: distinct reduced class in ((7,1));
- new carrier datum: none.

## Next falsifier

Construct the global specialization map from the complete orbit-completed
weighted-Rees exact cokernel to the extended resonant object. Compute its
kernel and cokernel away from the endpoints. Any remaining extensive residual
must be classified as interior quartic-tail coefficient data rather than
boundary support.

## Evidence

- `research/benincasa/marici-gm/src/bin/soft_axis_minus_quartic_restoration.rs`;
- Entries 460, 469, and 481--483.
