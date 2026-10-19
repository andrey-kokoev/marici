# Native positive projection: endpoint fit and ground/threshold preservation

[Contract](contracts/ground-preserving-native-projection.v1.json) · [exact checker](check_ground_preserving_native_projection.py) · [receipt](results/ground-preserving-native-projection.v1.json)

## Constructive result

The preceding [three-hidden fitted model](THREE-HIDDEN-NATIVE-INTERPOLANT.md) matched the two negative-axis data points but lost the native zero mode. A **source-derived orthogonal compression** now succeeds at both requirements:

- **8 core coordinates: 3 visible plus 5 hidden**, instead of the source's 11;
- positive inherited metric and nonnegative core with inertia (7 positive,0 negative,1 zero);
- exact full-visible effective operators and visible closed-core resolvents at z=-1,-2;
- the same simple ground vector, its visible component and total metric norm;
- the same conditional three-chain Householder coefficient limit as C11;
- exact retention/intertwining of the five-dimensional belt/carrier-sum cyclic sector.

It is not an invariant realization of the whole native core. The third-point error and the full-core intertwining residual are nonzero. This is a new conditional reduction of the fixed K, not a new physical interaction or a change to C1–C12.

## Native-metric construction

Partition the fixed K with the same three visible coordinates P and eight hidden coordinates Q. Let H_P,H_Q be their positive source metrics. Define the hidden snapshots

```
X_s=(sI+K_QQ)^(-1)K_QP,   s=1,2,
Wspace=span(columns(X_1),columns(X_2)).
```

The checker obtains rank five over Q(sqrt(151)). The hidden part of the native ground vector is **already in this span**; explicitly requesting it adds no dimension. This containment is source-specific, not a general consequence of fitting two spectral points.

Choose an exact echelon-normalized basis W for that span, and set

```
H_w=W* H_Q W,
L_w=H_w^(-1) W* H_Q,
A_r=L_w K_QQ W, B_r=L_w K_QP, C_r=K_PQ W,
K_r=[[K_PP,C_r],[B_r,A_r]], H_r=diag(H_P,H_w).
```

The native embedding and its metric adjoint are

```
E=diag(I3,W), L=diag(I3,L_w),
L E=I8, E* H_native E=H_r, K_r=L K E.
```

The visible projector commutes through the embedding: `P_native E=E P_r`. Direct weighted congruence checks give positive H_r, positive hidden A_r and core inertia (7,0,1). Thus positivity is inherited from the actual source, not fitted with a changed direct block. The hidden basis lives inside the native hidden space; unlike the three-hidden fit, these are not abstract fitted coordinates.

## Endpoint preservation and the precise minimum

At either endpoint, X_s lies in Wspace. Write `Y_s=L_w X_s`. Exact identities give

```
W Y_s=X_s, (sI+A_r)Y_s=B_r,
C_r(sI+A_r)^(-1)B_r=K_PQ(sI+K_QQ)^(-1)K_QP.
```

Consequently the full visible effective operators coincide. Both nonnegative full cores have regular negative-axis resolvents, and direct inversions additionally verify equality of their entire visible resolvent compressions at both points.

Five is minimal **within this orthogonal projection class**, not among arbitrary fitted models. To see this, consider any hidden trial subspace with its metric-orthogonal Galerkin solve. In whitened notation, put

```
A_s=sI+K_QQ > 0,
X_s=A_s^(-1)B, X_trial=Galerkin_solution,
N_s=B*X_s, N_trial=B*X_trial.
```

Galerkin orthogonality gives the matrix energy-error identity

```
N_s-N_trial=(X_s-X_trial)* A_s (X_s-X_trial).
```

For full matrix equality at s=1 and 2, positive definiteness forces every column of both X_s into the trial subspace. That subspace must therefore contain their rank-five span. The new construction attains it. The earlier three-hidden fit remains minimal in the **larger arbitrary-realization class**; it is not such a native orthogonal projection. Nor is five claimed minimal among all arbitrary ground-preserving fits.

## Ground, threshold and preparation structure

Let v span the native kernel and `v_r=L v`. The checker verifies

```
E v_r=v, K_r v_r=0,
v_r* H_r v_r=v* H_native v,
(v_r)_P=v_P != 0.
```

Positivity and the single native zero mode exclude additional compressed zero modes. Equivalently this is also confirmed by full weighted inertia. The inherited ground is still lead-visible.

Under the **same declared** positive three-chain attachment, the compressed boundary matrix has the C11 form

```
M_r(k)=E(k)I-K_r+(exp(ik)-1)P_r,
S_r(k)=I3-i(2sin(k))[M_r(k)^(-1)]_PP.
```

The simple-kernel Schur argument applies in the inherited positive metric. The complementary core block is invertible and the port projection is nonzero. It yields `S_r_hat(k)=S0+O(k)`, with exactly the native metric Householder matrix determined by v_P. Unlike the three-hidden fit, the coefficient limit gap is zero. This is a limiting statement, not an explicit uniform error constant or nonzero flux assignment at k=0.

There is a stronger preparation-specific result. Generate the native cyclic subspace from the belt vector and the sum of the two carrier characters. It has dimension five and lies entirely in Ran(E). Its reduced copy satisfies `K E=E K_r` on that subspace, and the visible projector preserves it. Thus its closed-core unitary dynamics and resolvent responses are exactly retained, not just matched at two points. With the same identical lead laws, its two-dimensional visible lead sector remains reducing and the same intertwining extends to that conditional coupled sector. This does not identify these geometric preparations with photon multiplicities or classify the reduced model's entire bound sector.

## What is still approximate

The global residual `R=K E-E K_r` is nonzero. At z=-3 the native negative self-energy minus the compressed one is also nonzero. Its positive error is independently checked by the native-metric energy-error identity. The certificate records ranks and inertias instead of concealing the mismatch behind exact endpoint tests.

Neither an all-energy identity nor an error bound for every positive-band packet is inferred. The original C2/C5 full-model counts and weights are not automatically assigned to this new eight-state core. The construction is a conditional approximation, not source-operation licensing or a calibrated physical model. Historical ancestor drift is preserved and no source-owner receipt is reissued.

The next executable step is to bound the residual-driven error away from the exactly retained preparation sector, for instance using the unitary Duhamel estimate for the common conditional lead model. Matching another arbitrary point is not a substitute for a controlled domain/preparation error contract.

## Verification boundary

The checker replays exact field identities, ranks, source/metric bindings, full endpoint inverses, ground preservation and preparation-sector intertwining. The universal Galerkin minimality, time-evolution consequence and analytic threshold expansion are documented arguments, not machine-formalized analysis. All energy coordinates are in stored K units. C12's exhausted budget is not renewed and no high-energy cycle is executed.

```sh
python -S research/scattering/low-energy/check_ground_preserving_native_projection.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_ground_preserving_native_projection.py
```
