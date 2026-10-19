# C12 attempt 1: exact threshold kernel and a uniform-bound proof draft

[Open C12](contracts/low-energy-scattering-conjectures.v5.json) · [exact kernel checker](check_pentachoron_threshold_kernel.py) · [kernel receipt](results/pentachoron-threshold-kernel.v1.json)

[Attempt record](contracts/pentachoron-threshold-attempt1.v1.json) · [remaining-review workbench](../../conjecture_net/LOW-ENERGY-WORKBENCH.md)

**Protocol accounting:** one of the two focused effort units has been used. The exact threshold-kernel test passes. The uniform argument below is a proof draft pending the remaining review unit; C12 is still open. This does not consume or renew the separate high-energy protocol.

## 1. Fresh finite facts

The checker freshly replays the ground certificate and reads the same hash-pinned symbolic matrices. Let A=H_O-theta I, G=ker A, D=G intersect ker P, and V be the exact four-column ground basis. It checks:

- A is PSD, dim G=4, dim D=2, and P is an orthogonal rank-two projector.
- J, two independent columns of P, is a basis of ran P.
- The four-by-two matrix V*J has rank two. Therefore V* restricted to ran P is injective. V need not be an orthonormal basis for this conclusion.
- H_C-theta I has rank twenty. A computed exact inverse satisfies both inverse identities.

These facts are stronger than a scan or a sampled determinant. No explicit matrix entries for sqrt(A) are needed.

## 2. Exact kernel argument

Define Q=sqrt(A), the unique PSD square root, and

```
M0 = [[-2Q-2P,       2P],
      [    2P, theta I-H_C-2P]].
```

If M0(u,chi)=0, the first row says `Q u+P(u-chi)=0`. Since V*Q=0, multiplication by V* gives `V*P(u-chi)=0`. Injectivity on ran P forces `P(u-chi)=0`. Hence Q u=0, so u belongs to G. The second row now reduces to `(H_C-theta I)chi=0`; its exact inverse forces chi=0. Thus P u=0 and u belongs to D.

Conversely every (d,0), d in D, is in the kernel. Consequently

```
ker M0 = D direct-sum {0},   dim ker M0=2.
```

There is no additional bright or invisible/core threshold kernel. M0 is Hermitian. On N=(D direct-sum {0}) orthogonal-complement, dimension 38, its restriction N0 is therefore invertible. This is the dark-reduced invertibility needed for C12, not invertibility of the unreduced forty-state block.

The criterion genuinely uses both finite hypotheses: rank-two ground/contact pairing and invertibility of H_C-theta I. Hermiticity or positivity alone is insufficient. Controls reject dependent pairing columns and an invalid core inverse.

## 3. Uniform small-k argument — pending review

Let delta>0 be the smallest positive eigenvalue of A. Its positivity follows from finite dimensionality and the exact ground/PSD certificate; no numerical value of the gap is required. For E=theta+k^2, 0<k^2<delta, put G0 for the orthogonal projector onto G and C0=I-G0. In coefficient boundary variables the full outgoing block is

```
M(k) = [[2 i k G0 - 2 sqrt(A|C0-k^2 I) C0 - 2P, 2P],
        [                                           2P, (theta+k^2)I-H_C-2P]].
```

The dark sector reduces this block for every such k: H_O spectral functions preserve D, P annihilates D on both sides, and the core coordinate of its projector is zero. Its dark restriction is 2ik I_D. The complementary block N(k) acts on the fixed space N and tends to N0.

For lambda>=delta,

```
0 <= sqrt(lambda)-sqrt(lambda-k^2)
   = k^2 / (sqrt(lambda)+sqrt(lambda-k^2))
   <= k^2/sqrt(delta).
```

Thus, for k<=1,

```
||N(k)-N0|| <= 2k+(1+2/sqrt(delta))k^2 <= L k,
L = 3+2/sqrt(delta).
```

Set a=||N0^(-1)|| and choose

```
k0 = min(1/2, sqrt(delta)/2, 1/(4aL)).
```

A Neumann bound yields `||N(k)^(-1)||<=2a` for 0<k<k0. In particular the full M(k) is invertible there: its other summand is the invertible dark block 2ik I_D. No eliminated-core inverse or uncontrolled real-pole exception is being assumed.

Below the first excitation all four ground channels have the same velocity 2k. The incoming/outgoing unit-flux factors cancel in the ground transmission map, giving

```
T(k)b = 2ik G0 [M(k)^(-1)(b,0)]_lead,    b in B=G orthogonal-minus D.
```

Hence `||T(k)|B||<=4a k`. The independent dark certificate gives `T(k)|D=I_D`, and the reducing decomposition excludes B-to-D transfer. Therefore with C=4a,

```
||T(k)-Q_D||<=Ck.
```

Continuity in the source convention gives R=T-I_G, so

```
||R(k)+(I_G-Q_D)||=||T(k)-Q_D||<=Ck.
```

The constants are mathematically specified finite positive quantities. C12 is existential; a decimal estimate of a or delta is not needed. A claim of explicit numerical optimal constants would require a different certificate.

## 4. Conditional packet consequence — pending review

For an energy-normalized ground profile f=f_D+f_B supported in (theta,theta+epsilon), epsilon<k0^2, the orthogonal reducing sectors give

```
P_trans = ||f_D||_L2^2 + integral ||T(E)f_B(E)||^2 dE.
```

Consequently `0<=P_trans-||f_D||_L2^2<=C^2 epsilon`. This uses squared transmission, the source energy normalization and the common ground-channel velocity; it is not a capture or locally loaded-core claim.

## 5. Remaining review gate

Independently re-read the source junction/flux convention and check the positive-square-root kernel argument, fixed reducing complement, uniform inverse bound, ground flux-factor cancellation and packet measure. Replay both finite certificates. Either accept the complete scoped proof, expose a concrete defect/counterexample, or record inconclusive within the one remaining effort unit. No automatic verdict follows from the kernel receipt alone.

```sh
python research/scattering/low-energy/check_pentachoron_threshold_kernel.py --check
```
