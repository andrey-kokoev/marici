# An NE candidate from N's existing relative-sector modes

## The missing two-dimensional source is already present

The native neutron local projector has rank three: one selected mode in each
of three rotating sectors. Alignment keeps their common mode. The difference

```
C_N = L_N - N_N
```

is an exact rank-two metric-orthogonal projector onto the relative-sector
modes. These are not two additional copies of the baryon return. They are
already independent directions inside the original 36-coordinate N field.

Choose the normalized real contrast basis on sector amplitudes:

```
(1,-1,0)/sqrt(2),  (1,1,-2)/sqrt(6).
```

Multiplying these amplitudes by the actual normalized native sector mode gives
a 36-by-2 frame K. Exact checks establish `Ksharp K=I` and `K Ksharp=C_N`.

## Native geometric and electron symmetries match

The actual cyclic permutation of the three N sectors acts on K as a real
120-degree rotation. A specific retained order-three action V in the electron's
native 24-element dictionary was selected, and an exact unitary W constructed
with `VW=W R_C3`. No arbitrary nonnative electron action was substituted.

Let J be the native electron return frame and define

```
S = J W Ksharp.
```

Then, exactly,

```
S Ssharp = N_E
Ssharp S = L_N - N_N
S R_C3 = (J V J*) S.
```

Thus the two native N contrast modes map isometrically onto the entire native
E return doublet. The common N return is untouched by this readout: `S N_N=0`.

## Native five-coefficient NE test

The native N active slots are [1,2,3], E's ordered active slots are [3,2,4],
and NE is the permutation [0,4,2,3,1]. On the ordered active triples, NE is a
reflection. Its exact two-dimensional contrast matrix is retained.

A candidate binding identifies active-window contrast coordinates with the
three-sector contrast coordinates in the stated basis. After including the
reflection in the E binding, the checker proves

```
S B_N = B_E Pi_NE
```

for all five input coordinates. Both sides represent a rank-two part; the
common active coefficient and two complementary slots are not represented by
this return-sector binding. Identifying the window's coefficient cycle with
the belt's spatial sector rotation is still an explicit ansatz, not a derived
geometric identity. The successful test is stronger than rank matching but
does not select that ansatz uniquely.

## Lossless channel exchange, with explicit dynamics caveat

The partial isometry extends to a metric-unitary involution on the direct sum
of the N and E raw fields (36+8 channels):

```
T = [[I-C_N, Ssharp],
     [S,     I-N_E]].
```

The checked partial-isometry identities prove T squared is identity. If the
E channel starts at zero, this transfers N's contrast component while retaining
its common return and all other source components. It does not clone data.
A direct-sum field exchange is not by itself a physical particle-creation rule.

This candidate deliberately relaxes the earlier return-intertwining requirement:
it converts modes rejected by N's alignment into E return modes. Under the
existing defect operator `H=2I-L-G`, the source contrast has eigenvalue 1 and
the target return has eigenvalue 0. The exchange therefore does not conserve
that defect measure. A physical interpretation needs a justified dynamics,
work or reservoir term; none is invented here.

## Disposition

A concrete NE **contrast-sector** candidate now uses existing native data,
reaches the full E return doublet, respects a native C3 action, and passes the
five-slot NE reversal test under an explicit binding ansatz. Full five-slot
binding, the connection to the independently constructed global PN map, path
coherence and physical dynamics remain open.

```sh
python research/strominger/checkers/check_neutron_contrast_electron_transport.py
```

Evidence: `results/neutron-contrast-electron-transport/verification.json`.
Production/viewer unchanged.
