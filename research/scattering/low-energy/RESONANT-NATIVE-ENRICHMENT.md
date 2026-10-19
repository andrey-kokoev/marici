# One retained enrichment repairs the fixed projection's full-band obstruction

[Contract](contracts/resonant-native-enrichment.v1.json) · [exact checker](check_resonant_native_enrichment.py) · [receipt](results/resonant-native-enrichment.v1.json)

## Result

A **nine-state core (three visible plus six native hidden coordinates)** replaces the eight-state projection's maximal full-band error 2 by the rigorous bound

```
||S_hat_native(E)-S_hat_9(E)|| <= 1/4,     0<E<4.
```

This is the same supplied conditional three-chain model and canonical common flux frame, in stored K units. It is an analytic full-band bound backed by exact polynomial interval positivity, not a sampled maximum. It is not full native identity or a physical energy calibration.

The enrichment preserves:

- both full-visible negative-axis endpoint fits z=-1,-2;
- the native ground, visible direction and metric norm, hence the conditional Householder threshold limit;
- the full exact five-dimensional symmetric core sector and its two-dimensional lead sector;
- positivity of the inherited metric and nonnegativity of the core, with inertia (8 positive,0 negative,1 zero).

It also exactly matches the **positive-band response at E=2/5**, where the preceding eight-state model had error greater than 199/100. The new antisymmetric error has a double zero there. The old eight-state obstruction and its receipt remain valid for that old model; they are not overwritten.

For any normalized common incoming free profile on the entire open band, let alpha_in be the norm of its carrier-difference component. The outgoing norm error is at most **alpha_in/4**; any common bounded effect 0<=A<=I has probability discrepancy at most **alpha_in/2**. These are conditional free-profile comparisons, not full joint-state dynamics or newly supplied physical detectors.

Nine is minimal **within fixed-native hidden orthogonal endpoint projections with full-band error strictly below 2**. This is not a minimum among arbitrary fitted realizations.

## 1. Source-derived construction and exact retention

Let W_8 be the preceding five-dimensional hidden trial space. Add the columns of the single real positive-energy snapshot

```
X=(K_QQ-(2/5)I)^(-1)K_QP,
W_9=span(W_8,columns(X)).
```

The hidden rank increases by exactly one, from five to six. With a canonical basis W, use exactly the previous native-metric orthogonal construction:

```
H_W=W*H_Q W, L_W=H_W^(-1)W*H_Q,
E_9=diag(I3,W), L_9=diag(I3,L_W),
K_9=L_9 K E_9, H_9=E_9*H_native E_9.
```

The checker verifies the isometry, orthogonal compression and nested embedding `E_9(L_9 E_8)=E_8`. Ground preservation and symmetric-sector intertwining follow from containment and are also checked directly. The residual still has rank one: the improvement is controlled approximation, not an invariant reduction of all eleven states.

At z=-1,-2,2/5 the actual hidden solutions lie in W_9. The checker verifies both native/reduced hidden inverses exist and the lifted solutions and full-visible self-energies agree. At the positive point this implies equality of open scattering responses, since contact/lead terms are identical and the full open matrices are invertible by visible cyclicity. No positive-definite Galerkin-error sign is assumed at E=2/5.

On the antisymmetric sector, the nested trial spaces have dimensions three, four and six for the old projection, enrichment and source. Below the native gap, positive Galerkin ordering gives

```
0<m_8(E)<=m_9(E)<=m_native(E).
```

Thus the preceding 0<E<=1/64 low-window envelope also holds for the enriched core: its compliance discrepancy decreases, and its contact denominator modulus increases with positive m. The full-band 1/4 bound is proved separately below.

## 2. The missing closed-core in-band pole count is repaired

Exact weighted inertias of A_j-4I on the antisymmetric sectors give:

| Core | Antisymmetric dimension | Eigenvalues in (0,4) | Eigenvalues above 4 |
|---|---:|---:|---:|
| Native | 6 | 3 | 3 |
| Old eight-state | 3 | 2 | 1 |
| Enriched nine-state | 4 | 3 | 1 |

All antisymmetric cores are strictly positive and none has eigenvalue 4. Each is cyclic from its single port, so these eigenvalues are simple compliance poles with nonzero port residues. The enrichment restores the **count of closed-core in-band poles** missing from the old model. This is useful spectral structure, not an identification of complex scattering resonances or a count of bound states of the coupled infinite-chain operator. No native full bound count or preparation weight is automatically inherited.

## 3. Denominator-cleared full-band certificate

For each antisymmetric core A with inherited metric G and port u, compute real field polynomials

```
m(E)=n(E)/q(E),   q(E)=det(EI-A).
```

The exact Faddeev/adjugate recurrence verifies the matrix polynomial identity and Cayley–Hamilton endpoint. Coprimality of n,q is checked algebraically; the representation is not a numerical fit.

Write the native pair as n_n,q_n and enriched pair as n_9,q_9. Set

```
D_j=q_j^2+E q_j n_j+E n_j^2,
P=n_n q_9-n_9 q_n,
N=E(4-E)P^2,       D=D_native D_9.
```

The scalar contact formula then gives throughout the open band, including closed-core poles by continuity,

```
|s_native-s_9|^2=N/D.
```

There are no spurious zero denominators: `D_j=(q_j+E n_j/2)^2+E(4-E)n_j^2/4`, and coprimality prevents simultaneous real zeros of q_j,n_j. Thus D_j>0 for 0<E<4, even where a bare compliance has a pole. The source and enriched models have the identical symmetric scattering block, so this is the full flux-frame norm error squared.

The checker forms the degree-18 polynomial

```
B(E)=D(E)-16N(E)
```

and certifies B>=0 on all of [0,4]. Exact Bernstein coefficients are nonnegative after dyadic subdivision into just five cells:

```
[0,1/4], [1/4,1/2], [1/2,1], [1,2], [2,4].
```

A Bernstein polynomial is a nonnegative combination of nonnegative basis functions on its cell. This gives N/D<=1/16 throughout the open band and proves the uniform norm bound 1/4. The receipt stores the field polynomials and subdivision trace; no grid interpolation or floating-point eigenvalue estimate is used.

P is nonzero, of degree seven. Its zeros at -1,-2,2/5 have exact multiplicity two; the last gives quadratic local coefficient-error order near the repaired witness. The remaining mismatch is explicit, not erased by the full-band upper bound. The bound 1/4 is certified, not asserted to be the optimal supremum. An exact rational witness at E=39/10 gives norm error >9/50, so the current worst-case bracket is (9/50,1/4].

## 4. Minimality and packet consequence

The earlier positive Galerkin energy-error argument forces every hidden orthogonal endpoint trial space to contain the rank-five negative-axis snapshot span. Below five hidden coordinates, exact endpoints are impossible. At exactly five the space is uniquely the old eight-state trial space, up to basis, and has full-band error 2 by its independent obstruction certificate. This six-hidden construction has full-band error at most 1/4<2. Therefore nine total core coordinates are minimal for **endpoint preservation plus submaximal full-band error within this native orthogonal class**. No arbitrary-realization minimum or physical operation licensing follows.

In the common free, flux-whitened energy representation, the S-matrix difference is scalar on the fixed carrier-difference projector Q_a and zero on Q_s. For any normalized incoming profile f, multiplication and integration give

```
||(S_hat_native-S_hat_9)f|| <= ||Q_a f||/4.
```

Both outgoing profiles have norm one by the same conditional scattering unitarity. Cauchy–Schwarz therefore gives common-effect probability error at most `||Q_a f||/2`. As before, the common source endpoint phase -exp(2ik) does not alter the comparison.

## Verification boundary and next question

Finite field algebra, source binding, interpolation, nesting, cyclicity, inertias, coprimality, polynomial recurrences, exact multiplicities and Bernstein subdivisions are replayed. Galerkin ordering, threshold/packet consequences and the class-minimality argument are documented analysis, not machine-formalized proofs. Tests include deliberately wrong polynomial signs, too-small bounds, denominator cancellations and scope promotions.

C1–C12 and their budgets are unchanged, no high-energy cycle is spent, and historical ancestor drift is preserved without reissuing owner receipts. The next distinct target is to certify a sharper worst-case band error or compare this full-band accuracy against the remaining two omitted antisymmetric directions; neither a full native identity nor physical channel admission is established.

```sh
python -S research/scattering/low-energy/check_resonant_native_enrichment.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_resonant_native_enrichment.py
```
