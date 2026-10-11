# Retained differences become observable at a second interface

## Question

Can two retained geometric states with the same first readout respond differently at another interface already present in the source?

Yes. No new selector, phase defect, or particle interpretation is needed.

## Readout contract

Use the same real vector d as input to each selected local interface. For triangle t, read

```text
A_t d = D_t conjugate(L_t) d,
```

where L_t is its actual retained local projector and D_t is the phase registration reconstructed from its generated mode.

This compares two local readouts of the same retained input. It is not the sequential operation A_second A_first d, and it does not identify the pair of readouts with the final collective return N. Both the input and the two outputs must remain available.

## Exact distinguishing example

Take the electron boundary states

```text
front = (1/3,1/3,1/3,0),
back  = (0,0,0,1).
```

Their spatial vectors are (1,1,-1)/3 and -(1,1,-1). The AB interface reads zero for both.

The existing AC interface lies on a different face. Its front readout is

```text
(1/45 - sqrt(-3)/15,
 2/45,
 -1/45 - sqrt(-3)/15).
```

Its back readout is minus three times that nonzero vector. Thus the first interface's equality is not equality of the retained states.

## General result, not just this pair

Each real local readout has rank two and forgets the normal direction of its face. Two interfaces on different faces have different normal kernels; their intersection is zero.

The checker audits all 66 pairs of existing interfaces:

- 12 pairs on the same face have joint real rank two.
- 54 pairs on different faces have joint real rank three.

Relative to AB, its two other same-face interfaces remain blind to its normal. Each of the nine interfaces on the other three faces detects it.

Consequently two different-face readouts reconstruct any real input vector d, not just distinguish the example above.

## Explicit reconstruction

For two selected interfaces A_1,A_2 and their outputs z_1,z_2, let

```text
M = Re(A_1* A_1 + A_2* A_2),
d = M^(-1) Re(A_1* z_1 + A_2* z_2).
```

For AB and AC the exact matrix is

```text
M = [[8/15, 0,    7/15],
     [0,    8/15, 2/5 ],
     [7/15, 2/5,  14/15]].
```

It is invertible. The checker verifies the inverse on a real basis and recovers all 455 denominator-12 tetrahedral grid points. Barycentric coordinates are recovered by λ_i=(1+POINTS[i]·d)/4.

This result is for real geometric inputs. Two complex rank-one readouts cannot recover an arbitrary three-component complex state. Among triples of source interfaces, 216 have complex rank three; the four triples lying entirely on one face have rank two.

## Why retention matters operationally

If only the first output is kept, the example's two states both become the same stored zero. Feeding that zero into a second projector cannot distinguish them. The checker verifies this negative control.

If the original direction is retained, the second interface can access the difference and reconstruct it jointly with the first output. Retention therefore preserves an experimentally distinguishable possibility within this readout model, rather than just an unused label.

This is the key distinction:

```text
same first readout ≠ interchangeable inputs to every subsequent interface.
```

It provides a concrete operational role for the retained direction complex. It does not supply a measurement dynamics or prove that access to the second interface occurs automatically; the operation being tested is explicitly a second read of the retained input.

## Verification

```text
python research/voevodsky/checkers/check_second_interface_observability.py
```

Thirteen exact checks pass. `results/second_interface_observability.json` records both example outputs, the inverse, all pair ranks, all triple complex ranks, and source/checker hashes. The source is unchanged.
