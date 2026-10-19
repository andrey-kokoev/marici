# Constructive three-hidden-state interpolant — exact endpoint fit, wrong threshold

[Contract](contracts/three-hidden-native-interpolant.v1.json) · [exact checker](check_three_hidden_native_interpolant.py) · [receipt](results/three-hidden-native-interpolant.v1.json)

## Result

There **is** a constant, positive six-state model with three visible and three hidden coordinates that matches the native eleven-state core's full visible effective operator **and visible closed-core resolvent** at z=-1,-2 exactly, in stored K units. It even keeps K_PP unchanged.

Together with the [preceding two-point lower bound](SCALAR-C-NATIVE-COMPARISON.md), this proves that **three hidden coordinates are minimal for exact interpolation at those two points** in the declared constant full-visible class. It does not say that three hidden coordinates realize the complete native dynamics; the source's exact hidden realization has eight.

The follow-up preservation tests fail in useful ways: this interpolant is strictly positive and **loses the native zero mode**. With the same conditional three-chain attachment its coefficient limit is I3, not the native Householder limit. Endpoint interpolation is therefore not a certificate of low-energy fidelity.

C1–C12 remain unchanged. This is a supplied approximation model, not a source-forced interaction, physical identification, new live conjecture or renewed protocol.

## Construction without matrix square roots

Let H_P be the native visible metric and write

```
N_s=K_PQ(sI+K_QQ)^(-1)K_QP,   s=1,2.
```

The preceding source audit proves positive hidden energy and rank-three coupling. Thus N_1,N_2 are positive definite in H_P. Define

```
R_1=N_1^(-1), R_2=N_2^(-1),
G=R_2-R_1,
T=2R_1-R_2,
H_h=H_P G,
A_h=G^(-1)T,       B_h=G^(-1),       C_h=I3.
```

The hidden coordinates are new fitted coordinates, not three selected coordinates in the native eight-dimensional hidden space. The checker proves directly over Q(sqrt(151)) that H_P G and H_P T are symmetric positive definite. Hence H_h is a positive metric, A_h is H_h-self-adjoint and positive, and B_h,C_h are metric adjoints:

```
H_h B_h=H_P,       H_h A_h=H_P T.
```

Set

```
K6 = [[K_PP, I3],
      [G^(-1), G^(-1)T]],
H6 = diag(H_P,H_h).
```

The full H6 K6 is checked symmetric with inertia (6 positive,0 negative,0 zero). Positivity of this full core is a verified property of this source-specific construction, not an automatic inference from positivity of its diagonal blocks. No floating eigensolver or unrecorded basis whitening is used.

## Exact interpolation

The fitted negative-axis self-energy is

```
N_tilde(s)=C_h(sI+A_h)^(-1)B_h=(sG+T)^(-1).
```

By construction `G+T=R_1` and `2G+T=R_2`, so `N_tilde(1)=N_1` and `N_tilde(2)=N_2`. With K_PP retained,

```
K6_eff(-s)=K_PP-N_tilde(s)=K_native_eff(-s),   s=1,2.
```

Both full cores are nonnegative and these z values are negative, so their resolvents exist. The checker independently inverts both full matrices and verifies equality of the entire 3x3 visible resolvent compression at both points. This is stronger than matching one output ratio or one preparation.

After metric whitening, K6 belongs to the constant Hermitian three-hidden class. The old lower bound rules out every two-or-fewer-hidden candidate, even with arbitrary constant visible-block refitting. Consequently this construction attains the minimum hidden dimension for **this two-point objective**, not for all-energy response or source-operation correspondence.

## Preservation tests: why the model is not a faithful replacement

1. **Zero mode:** the native core has a simple visible zero mode. K6 has rank six and no kernel. Their spectra cannot be intertwined as whole-core dynamics.
2. **A third point:** at z=-3 the native negative self-energy minus N_tilde(3) is nonzero; its visible-metric Gram inertia is (2 positive,0 negative,1 zero). Endpoint fitting did not make the rational responses identical.
3. **Lower threshold, with an explicit additional lead assumption:** attach the same three supplied leads, visible projector P and coefficient convention as in C11. In the fitted metric,

```
M6(k)=E I-K6+(eta-1)P,   E=2-2cos(k), eta=exp(ik),
S6(k)=I3-i(2sin(k))[M6(k)^(-1)]_PP.
```

At k=0 the full matrix is -K6 and is invertible. Analytic inversion yields a bounded inverse near zero and therefore `S6_hat(k)=I3+O(k)`. No singular hidden-block inverse or sampled finite k is needed.

For the native core, C11 instead gives `S0=I3-2ww*` after whitening, with ||w||=1. In the same coefficient convention and any fixed shared visible metric frame,

```
lim_(k->0) ||S6_hat(k)-S_native_hat(k)|| = ||I3-S0|| = 2.
```

The common endpoint phase does not remove the two different native eigenvalue signs. This is a coefficient-operator limit, not a per-preparation probability bound or flux assignment at zero velocity. No quantitative positive-band window or reaction branching prediction is supplied here.

## Scope and next distinct task

This gives a constructive answer beyond the scalar-C obstruction: a larger constant passive realization can fit both prescribed data points exactly. It also supplies a concrete counterexample to inferring threshold dynamics from off-band interpolation.

The candidate does not automatically inherit the native source's five bound modes, retained weights, wave-operator receipts or physical labels. Its three-chain attachment is a conditional test fixture, not a newly selected law. Historical native-adapter hash drift is unchanged; no owner receipt is reissued or all-ancestor freshness claimed.

Next, impose the native zero-mode/visible-projection constraint together with the endpoint data, for example via a source-derived positive projection that retains the ground vector. A fit with another arbitrary extra point alone would not address the observed threshold failure. Preparation/readout-specific approximations remain a separate option.

The checker replays finite field inverses, full-core and metric inertias, endpoint resolvent identities and non-preservation witnesses. The minimality deduction and analytic threshold expansion are documented mathematics, not machine-formalized analysis.

```sh
python -S research/scattering/low-energy/check_three_hidden_native_interpolant.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_three_hidden_native_interpolant.py
```
