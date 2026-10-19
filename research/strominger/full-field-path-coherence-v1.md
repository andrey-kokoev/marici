# Lifting the path-dependent coefficient frame to all 36 amplitudes

## Native witness

Used the contact-witnessed pair of open native paths ending at the same P
chart at origin 3, with relative five-coefficient permutation
`H=[1,4,0,2,3]`. Its order is five. Absolute history is not identified or reset.

## Full-fiber construction

For the previously constructed geometric isometric embedding B: C^5 -> C^36,
let E=BB*. Define

```
U_H = B H B* + (I-E).
```

This transports the embedded coefficients by H and leaves their orthogonal
31-dimensional complement unchanged. Exact native-metric checks give

```
U_H* U_H = I
U_H B = B H
U_H^5 = I.
```

The lift obeys the permutation composition law. Identity on the complement
is an explicit extension choice, not a unique consequence of the source.
This constructs an endpoint comparison in the P field, not the individual
species-changing PN/NE transport maps along the two paths.

## Fixed projectors fail—and the alignment obstruction is general

The constructed U_H does not commute with any of the native L,G,N matrices.
For alignment G this failure is not repairable merely by choosing another B
within the tested geometric equivariance hypothesis.

The native P alignment G is exactly the average of the twelve proper
tetrahedral actions on its 36-component field. The five-coefficient domain is
being modelled as four permuted vertex scalars plus one fixed context scalar.
Its corresponding average is

```
Q = diag(J_4/4, 1).
```

Any A4-equivariant embedding must obey `G B=B Q`. If a full-field U also obeyed
`UB=BH` and preserved fixed G, then

```
B(QH-HQ)=0.
```

But QH-HQ is explicitly nonzero. Thus an injective B cannot satisfy all these
conditions. This is a conditional algebraic obstruction for the specified
vertex/context representation and fixed-G hypothesis, not a prohibition on
other coefficient interpretations or field models.

The proper tetrahedral coefficient permutations together with H generate a
60-element group (A5). This is an algebraic coefficient-comparison group;
it is not established as an isometry group of T or a physical spatial symmetry.

## Frame-covariant alternative

Set `X_new=U_H X_old U_H*` for X=L,G,N. All full-matrix checks then pass:

```
X_new U_H = U_H X_old
G_new L_new = N_new.
```

This retains the same metric and projector algebra in a different component
frame. It need not mean a change of the physical operator, provided the field
basis and geometric readouts are transformed consistently. The constructed
frame can mix spatial patches; it has not been identified with a native local
geometric frame change.

## Disposition

A norm-preserving 36-amplitude realization of the observed endpoint five-cycle
exists. It requires frame-covariant component operators for this geometric
binding, rather than treating the fixed native matrices as unchanged under
all path comparisons. The obstruction explains why geometry and origin alone
were insufficient to label the coefficient state.

The remaining task is to derive the individual PN/NE field connections and
geometric readouts that produce this comparison, or revise the vertex/context
binding hypothesis. A freely chosen endpoint lift is not that derivation.

```sh
python research/strominger/checkers/check_full_field_path_coherence.py
```

Evidence: `results/full-field-path-coherence/verification.json`.
Production/viewer unchanged.
