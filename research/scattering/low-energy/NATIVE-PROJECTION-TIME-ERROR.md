# Native eight-state projection: a preparation-sensitive finite-time error bound

[Contract](contracts/native-projection-time-error.v1.json) · [exact support checker](check_native_projection_time_error.py) · [receipt](results/native-projection-time-error.v1.json)

## Result and comparison domain

For the [eight-state native projection](GROUND-PRESERVING-NATIVE-PROJECTION.md), the residual norm is now certified in the inherited metrics. Let J denote its isometric embedding into the eleven-state native core, or its extension by the identity on the **same supplied three-chain leads**. Let U_n(t),U_r(t) be the corresponding unitary evolutions and let

```
alpha=||(I-Pi_sym)psi||.
```

Pi_sym is the reducing exact preparation sector: five core dimensions and, when leads are attached, the belt/carrier-sum two-dimensional port subspace on every lead site. Operator J* denotes the Hilbert-space adjoint (L on the core), not an unweighted transpose; stars inside explicit metric-matrix formulas denote conjugate transposes. For every reduced initial state psi and every real t,

```
||U_n(t)J psi-J U_r(t)psi|| <= alpha min(2,3|t|).
```

This compares **the same embedded initial preparation**, not two different incoming wave-operator states. Time is in the source's stored K / conditional chain convention with hbar=1, not calibrated seconds. The bound is nontrivial for short times and exact for alpha=0 at all times. It does not prove uniformly small long-time error or an asymptotic S-matrix bound.

For a normalized preparation, two useful consequences are

```
P_native(omitted core directions at time t) <= alpha^2 min(1,9t^2),
|p_native(A,t)-p_reduced(J* A J,t)|
    <= min(1,2 alpha min(2,3|t|)),       0<=A<=I.
```

The first quantity is probability in the three omitted native core directions, not total occupation of leads or permanent capture. The second uses a mathematically specified common effect, not a newly identified physical detector.

For example, |t|<=1/30 guarantees state error <=alpha/10 and omitted-core probability <=alpha^2/100. These are rigorous conditional tolerances, not empirical fit errors.

## Exact inherited-metric residual norm

Use the unchanged source projection data E,L,K_r,H_r, with `L E=I`, `E*H_n E=H_r`, and `K_r=L K E`. Define

```
R=K E-E K_r,
R_sharp=H_r^(-1) R* H_n,
D=R_sharp R,
tau=trace(D).
```

R has rank one. Whitened D is positive semidefinite of rank one, so its only nonzero eigenvalue is tau and

```
||R||^2=tau.
```

The checker computes tau exactly in Q(sqrt(151)), verifies weighted adjoints/Gram identities and certifies

```
4 < tau < 9,       hence 2 < ||R|| < 3.
```

Thus 3 is a certified integer upper bound, not an unweighted Euclidean norm estimate. The certificate also stores the exact rank-one factor and norm-squared field value for independent replay.

## Why the same bound applies with infinite chains

The native and reduced conditional lead/contact Hamiltonians have blocks

```
H_n=[[K+P_n,-V_n],[-V_n*,H_D]],
H_r_full=[[K_r+P_r,-V_r],[-V_r*,H_D]],
J=diag(E,I_leads).
```

V inserts the three endpoint lead coordinates into the visible core. The source embedding retains those coordinates exactly, so

```
P_n E=E P_r, E V_r=V_n, V_n* E=V_r*.
```

The identical free lead blocks cancel as well. Consequently

```
H_n J-J H_r_full=diag(R,0_leads)
```

as a rectangular map. Its rank and norm are exactly those of R. All these chain Hamiltonians are bounded self-adjoint: the free chain is bounded and the core/contact blocks are finite. There is no unbounded point-trace argument here and no infinite-lead cutoff. This does not transfer to a different lead law without a new residual calculation.

## Reducing projector and named preparations

The checker freshly constructs the symmetric core subspace from belt and carrier-sum seeds, pulls it into reduced coordinates and forms its metric-orthogonal projector P_s. It verifies

```
P_s^2=P_s, P_s*=P_s (in H_r),
[K_r,P_s]=[P_r,P_s]=0, R P_s=0.
```

On the three visible coordinates the corresponding projector is

```
Q_s=[[1,0,0],[0,1/2,1/2],[0,1/2,1/2]].
```

The carrier weights are equal. The checker verifies both contact intertwinings `P_s V_r=V_r Q_s` and `V_r* P_s=Q_s V_r*`. With identical leads this proves that Pi_sym=P_s on the core and Q_s on every lead site commutes with H_r_full. The corresponding native sector is exactly intertwined, as established by the preceding projection certificate.

For normalized initially central model preparations, the exact alpha-squared values are:

| Preparation in native visible coordinates | alpha^2 |
|---|---:|
| Belt character | 0 |
| Sum of the two carrier characters | 0 |
| Difference of the two carrier characters | 1 |
| Either single carrier character | 1/2 |

Normalization uses the full inherited metric, not raw coefficient counting. These are preparation weights in an error estimate, not reaction branching fractions. General lead preparations use the same Q_s decomposition sitewise.

## Duhamel proof and observable consequences

The rectangular unitary Duhamel identity is

```
U_n(t)J-J U_r(t)
  = -i integral_0^t U_n(t-s) (H_n J-J H_r_full) U_r(s) ds.
```

The residual annihilates Pi_sym and that projector commutes with U_r(s). Unitarity therefore bounds the integral by `3|t| alpha`. Exact intertwining on Pi_sym and the triangle inequality give the complementary cap `2alpha`, proving the displayed state bound. Negative t follows by the same argument with absolute time.

For the omitted-space projection `Q_omit=I-JJ*`, the reduced comparison state is annihilated. Squaring the state-error estimate gives the short-time leakage bound. Moreover the exact symmetric evolution never enters that omitted space, while the remaining native component has norm alpha. This improves the trivial cap to alpha^2 and gives `alpha^2 min(1,9t^2)`.

For any positive contraction A and normalized states, Cauchy–Schwarz gives expectation difference at most twice their norm distance. Probabilities also differ by at most one. The reduced effect is exactly J* A J, so the two displayed probabilities have a defined common meaning; no empirical detector map is inferred.

## Boundaries and next distinct task

This replaces an unquantified rank-one mismatch with an explicit finite-time, preparation-dependent certificate. It does not erase the nonzero residual, prove full native identity, inherit the native full bound-mode counts for the reduced model, or take t to infinity to obtain a scattering bound. Arbitrary native initial states with omitted components require additional initial-projection error accounting.

A separate on-shell energy-window error contract is the next useful test. The exact symmetric sector and the regular antisymmetric threshold block offer a route; the present Duhamel estimate alone is not that argument.

Exact finite algebra and norm inequalities are replayed where stated. Duhamel, unitarity and their consequences are documented analysis, not machine-formalized proofs or numerical time-integration evidence. C1–C12 and source-owner results are unchanged, C12 is not renewed, no high-energy cycle is executed, and the historical ancestor warning remains explicit.

```sh
python -S research/scattering/low-energy/check_native_projection_time_error.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_native_projection_time_error.py
```
