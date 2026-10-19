# Fixed native projection: maximal full-band discrepancy despite a good low window

[Contract](contracts/native-projection-full-band-obstruction.v1.json) · [exact support checker](check_native_projection_full_band_obstruction.py) · [receipt](results/native-projection-full-band-obstruction.v1.json)

## Result

The fixed eight-state projection retains the native ground, two negative-axis endpoint fits, and the exact symmetric preparation sector. Its [low-window comparison](NATIVE-PROJECTION-ON-SHELL-ERROR.md) remains valid. It is nevertheless **not a uniformly accurate full-band scattering surrogate** under the same conditional three-chain laws and canonical common flux frame:

```
max_(0<E<4) ||S_hat_n(E)-S_hat_r(E)|| = 2.
```

This is the largest possible difference of two unitary matrices. A phase-opposition energy exists strictly inside

```
39/100 < E_* < 2/5
```

in stored K units. At the explicit rational energy E=2/5 the norm error is already **greater than 199/100**. These are exact algebra/continuity results, not estimates of a sampled maximum. The multiplication-operator norm on the common free energy-profile space is also 2, because continuity gives positive-measure neighborhoods approaching the maximum.

The discrepancy still annihilates the symmetric sector. Pure belt or carrier-sum scattering remains exactly reproduced throughout the open band. This obstruction concerns this fixed projection/contact/frame, not every eight-state model or every reduction.

## 1. Pole-free bracket and exact phase crossing

Use the preceding certificate's antisymmetric cores A_n (dimension six), A_r (dimension three), inherited metrics G_n,G_r and common port seed u_j. Define the normalized real compliance

```
m_j(E)=<u_j,(A_j-E)^(-1)u_j>/<u_j,u_j>.
```

Unlike the earlier low window, the present bracket is above a closed-core eigenvalue. No positivity of m_j is assumed. The checker certifies the weighted inertias at **both** bracket endpoints:

| Core | inertia of G_j(A_j-E) at each endpoint |
|---|---|
| Native antisymmetric | (5 positive,1 negative,0 zero) |
| Reduced antisymmetric | (2 positive,1 negative,0 zero) |

For a self-adjoint finite matrix, identical negative counts and no endpoint zeros exclude any eigenvalue between the endpoints. Thus both compliances are real analytic on the entire closed bracket. An apparent sign crossing across a pole would not be a valid witness; the no-pole check is essential.

Let

```
Gamma^2=E(4-E),
a_j=1+(E/2)m_j, b_j=(Gamma/2)m_j,
D_j=a_j^2+b_j^2=1+E m_j+E m_j^2,
W(E)=a_n a_r+b_n b_r
    =1+(E/2)(m_n+m_r)+E m_n m_r.
```

For every real m_j and 0<E<4,

```
D_j=E(m_j+1/2)^2+1-E/4 > 0.
```

The canonical scalar scattering phase is `s_j=(a_j+i b_j)/(a_j-i b_j)`. Algebra gives

```
s_n+s_r=2W/[(a_n-i b_n)(a_r-i b_r)],
d^2(E):=|s_n-s_r|^2
       =E(4-E)(m_n-m_r)^2/(D_n D_r),
4-d^2(E)=4W(E)^2/(D_n D_r).
```

The checker verifies the last identity as an exact multivariate polynomial identity, independently of its endpoint evaluations. It computes

```
W(39/100)>0,    W(2/5)<0.
```

Continuity and the intermediate value theorem therefore give E_* in the pole-free bracket with W(E_*)=0. At that energy, `s_n=-s_r` and `d(E_*)=2`. The exact symmetric block is common to both models, so their full matrix difference is `(s_n-s_r)Q_a` and also has norm 2. Unitarity supplies the global upper bound 2.

At E=2/5, Gamma=6/5 is rational. The checker independently constructs both exact complex phases, verifies unit modulus, replays their squared difference and proves

```
d^2(2/5) > (199/100)^2.
```

The source endpoint-wave convention multiplies both outgoing matrices by the same energy-dependent phase -exp(2ik); all norm and common-effect comparisons survive that common unitary factor. No fitted on-shell rotation is used.

## 2. An operational relative-phase witness, not just a global phase

A pure carrier-difference input has only one output channel sector: an opposite scalar phase alone is not an intensity distinction. To give a genuine common-effect witness, use orthonormal common-flux vectors v_s (the belt input) and v_a (the carrier difference), and the coherent input

```
v=(v_s+v_a)/sqrt(2).
```

The symmetric outgoing vector z_s=S_hat_n v_s=S_hat_r v_s is common, unit norm and orthogonal to v_a. The two monochromatic outgoing vectors are

```
y_j=(z_s+s_j v_a)/sqrt(2).
```

For the **same** mathematical effect `A(E)=|y_n(E)><y_n(E)|`,

```
p_n=1,
p_r=|<y_n,y_r>|^2=1-d^2(E)/4,
p_n-p_r=d^2(E)/4.
```

Thus at E=2/5 the probability gap is greater than **39601/40000**. At E_* the two monochromatic outputs are orthogonal and this ideal effect distinguishes them perfectly. This is a declared phase-coherent model preparation/readout, not a licensed physical instrument or branching fraction.

Monochromatic states are not normalized packets. For normalized scalar profiles g supported sufficiently near E_*, take the common incoming free profile `f(E)=g(E)v` and the same energy-diagonal effect A(E). Then

```
p_n-p_r=integral |g(E)|^2 d^2(E)/4 dE.
```

Continuity makes this arbitrarily close to one. This proves the existence of normalized packets with arbitrarily accurate discrimination, without claiming that a normalized packet attains the monochromatic perfect value. The low-window alpha_in/12 outgoing-error theorem is unaffected: this bracket lies outside its 0<E<=1/64 domain.

## Verification boundary and next work

The receipt binds a freshly replayed preceding certificate and exact pole counts, sign checks, polynomial identity, rational witness phases and squared gap. The intermediate value, continuity, operator-norm and packet consequences are documented analysis, not machine-formalized theorems. Numerical exploration helped locate the bracket but contributes no proof evidence.

C1–C12, their scoped dispositions and budgets are unchanged. No high-energy cycle is spent; no historical owner receipt is refreshed, and ancestor drift remains explicit. No native full bound count is inherited by the reduced core. The next distinct question is whether the missing antisymmetric spectral/phase structure explains the obstruction and what retained enrichment would repair it, rather than merely enlarging the already disproved uniform full-band claim.

```sh
python -S research/scattering/low-energy/check_native_projection_full_band_obstruction.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_native_projection_full_band_obstruction.py
```
