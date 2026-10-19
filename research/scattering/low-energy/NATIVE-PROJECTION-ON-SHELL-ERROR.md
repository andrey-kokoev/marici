# Native projection: a certified on-shell window and outgoing-packet error

[Contract](contracts/native-projection-on-shell-error.v1.json) · [exact support checker](check_native_projection_on_shell_error.py) · [receipt](results/native-projection-on-shell-error.v1.json)

## Result — a different comparison from finite-time Duhamel

For the fixed native eleven-state core and its [eight-state orthogonal projection](GROUND-PRESERVING-NATIVE-PROJECTION.md), attach the **same conditional three-chain laws** in the same visible-coordinate frame. Write S_hat for canonical flux-whitened scattering matrices. In stored K energy units,

```
||S_hat_n(E)-S_hat_r(E)|| <= (2/3)sqrt(E),    0<E<=1/64.
```

The source endpoint-wave convention has actual outgoing amplitudes b=-exp(2ik)S a. This is the same unitary multiplication for both models: it preserves the profile norm difference and conjugates a common outgoing effect equally. Their matrix difference annihilates the belt/carrier-sum sector exactly throughout the open band, not merely at threshold. It is a scalar times the carrier-difference projector Q_a=I-Q_s. The bound is conditional and narrow-window: 1/64 is not a physical energy scale or a full-band guarantee.

For a normalized common incoming **free, energy-normalized** profile f in L2((0,epsilon),C3,dE), define

```
alpha_in=||Q_a f||,       0<epsilon<=1/64.
```

The outgoing free profiles satisfy

```
||(S_hat_n-S_hat_r)f|| <= (2/3)sqrt(epsilon) alpha_in,
|p_n(A)-p_r(A)| <= (4/3)sqrt(epsilon) alpha_in,    0<=A<=I.
```

At epsilon=1/64 these are respectively **alpha_in/12** and **alpha_in/6**. A is the same specified bounded effect on the common outgoing free-profile Hilbert space; it is not a supplied physical detector. Incoming pure belt or carrier-sum profiles have alpha_in=0; a carrier difference has alpha_in=1, and either normalized single carrier with a common scalar envelope has alpha_in^2=1/2. These weights are not branching fractions.

This compares scattering operators on the common free lead space. It does **not** compare two entire coupled states with the same embedded finite-time initial condition. The earlier [Duhamel certificate](NATIVE-PROJECTION-TIME-ERROR.md) does that different job. No t-to-infinity limit of its growing bound is used here.

## 1. Exact sector reduction and regularity

The preceding projection and time-error certificates establish the exact five-dimensional symmetric core sector and its reducing two-dimensional visible sector. The checker also constructs the complementary cyclic sectors directly from the carrier-difference seed u=e_1-e_2:

- native antisymmetric core: dimension six;
- reduced antisymmetric core: dimension three;
- inherited metrics positive, with exact compression/isometry and port identities;
- K_a,n > (1/8)I and K_a,r > (1/4)I in their respective metrics.

The full visible cyclic dimensions are independently checked as eleven and eight. Consequently the real-band boundary matrix

```
M(k)=E(k)I-K+(exp(ik)-1)P,   E(k)=2-2cos(k), 0<k<pi
```

is invertible for either core: a null vector would have zero port projection by the positive imaginary-part identity, then be an invisible core eigenvector, contradicting cyclicity. The identical finite contacts give the usual unitary conditional scattering matrices. Finite-dimensional attachments to the free chains give the common free scattering space; this invokes the same stationary chain framework as the native model, not a new physical interaction.

Exact symmetric intertwining and contact invariance show that the full S-matrix difference is supported only on Q_a. The equal carrier port weights imply that Q_s and Q_a commute with the port whitening; hence these are the same orthogonal projectors in the common flux frame. No on-shell frame fitting is performed.

## 2. Scalar compliance and the Galerkin sign

In either antisymmetric core let

```
m_j(E)=<u_j,(K_a,j-E)^(-1)u_j>/<u_j,u_j>,   j=n,r.
```

The seed norm and port normalization are preserved. The reduced operator is the actual native-metric orthogonal compression, not an arbitrary interpolant. For E below the native antisymmetric gap, positive Galerkin energy error therefore gives

```
delta(E)=m_n(E)-m_r(E) >= 0.
```

This is the same positive energy-error argument as endpoint minimality, now applied to the full antisymmetric core with positive K_a,n-E. Its source/projection identities and its E=0 instance are replayed exactly. It is not a claim that the errors of arbitrary fitted models have this sign.

Let m_n0=m_n(0), m_r0=m_r(0). Positivity and the certified gap g=1/8 yield, throughout 0<=E<=1/64=g/8,

```
m_n(E) <= m_n0/(1-E/g) <= (8/7)m_n0,
m_r(E) >= m_r0,
0 <= delta(E) <= D := (8/7)m_n0-m_r0 < 1/3.
```

The first inequality follows from the positive spectral representation of (K_a,n-E)^(-1); the second follows from monotonicity of a positive resolvent below its spectrum. The final inequality is checked over Q(sqrt(151)), not from sampled energies. For orientation only, m_n0 is about 1.90935, m_r0 about 1.86853, and D about 0.313584. The receipt stores exact field values.

## 3. Contact denominators do not amplify this error

Put w=exp(ik), beta=w-1=-E/2+i sin(k), and Gamma=2sin(k)=sqrt(E(4-E)). On the single antisymmetric channel the rank-one resolvent formula gives

```
s_j(E)=1+i Gamma m_j(E)/(1-beta m_j(E)),
s_n(E)-s_r(E)
 = i Gamma delta(E)/[(1-beta m_n(E))(1-beta m_r(E))].
```

Since each m_j(E)>0 in the window,

```
Re(1-beta m_j)=1+(E/2)m_j >= 1.
```

Both denominators thus have modulus at least one. It follows that

```
|s_n-s_r| <= Gamma delta(E) <= 2sqrt(E)D < (2/3)sqrt(E).
```

With exact equality on the symmetric sector, this is the full common-flux-frame operator bound. Multiplication by this pointwise scalar envelope, followed by integration in dE, proves the outgoing-packet norm bound. Unitarity normalizes both outgoing profiles; Cauchy–Schwarz bounds any common-effect probability difference by twice their norm distance. This is an analytic argument, not a numerical positive-band scan or an inference from off-band endpoint agreement.

## 4. The remaining error really has square-root order

The checker verifies exactly

```
delta0=m_n0-m_r0 > 0.
```

The scalar formula, beta=O(sqrt(E)) and Gamma=2sqrt(E)+O(E^(3/2)) then give

```
S_hat_n(E)-S_hat_r(E)=2i delta0 sqrt(E) Q_a+O(E).
```

Thus the antisymmetric pointwise norm error has sharp square-root order in energy. Ground/Householder preservation does not give an O(E) coefficient-error estimate. The leading coefficient is phase-coherent and frame-specific; it is not itself an intensity branching ratio. The exact value of 2delta0 is stored separately from the conservative uniform envelope 2/3.

## Verification and remaining gates

The checker freshly replays the parent certificates and verifies cyclic dimensions, weighted self-adjointness/coercivity, antisymmetric Galerkin embedding and port normalization, m_j0, the E=0 energy-error identity and the exact envelope inequality. Negative controls refuse a zero leading error, an altered envelope, enlarged scope and physical admission. Tests exercise rational squared packet bounds and scope/preparation guards. The spectral inequalities, rank-one contact formula and scattering/packet consequences above are documented mathematics, not machine-formalized analysis.

No full-band accuracy, reduced bound-sector count, physical species, energy calibration, source-operation licensing or detector map is inferred. C1–C12 and their budgets are unchanged; no high-energy cycle is run. The historical ancestor mismatch is preserved rather than refreshed. The next distinct comparison is to tighten or extend the window with the actual scalar rational compliances, or test whether a substantial discrepancy elsewhere in the open band prevents a global approximation claim.

```sh
python -S research/scattering/low-energy/check_native_projection_on_shell_error.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_native_projection_on_shell_error.py
```
