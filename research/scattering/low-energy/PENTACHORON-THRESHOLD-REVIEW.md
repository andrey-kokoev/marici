# C12 final review: established for the fixed contact model

This is the second and final effort unit of the original C12 protocol. The [attempt-1 proof draft](PENTACHORON-THRESHOLD-PROOF.md) is preserved as historical evidence. This review accepts the complete scoped amplitude assertion and its packet corollary, not a general pentachoron scattering or physical-production claim.

## 1. Source conventions checked afresh

Sections 3–5 of [the autonomous contact source](../high-energy/pentachoron_autonomous_contact_note.md) give the quadratic form, derivative jump, core equation, outgoing square-root branch, velocities and unit-flux readout. At epsilon=ell=hbar=kappa=1, the actual boundary matrix is

```
[[2iK(E)-2P, 2P], [2P, E-H_C-2P]].
```

The signs in the draft agree with this full system. Open ground momentum is k and closed momenta are `i sqrt(lambda-k^2)`, where lambda is a positive eigenvalue of H_O-theta I. Thus their contribution is **minus** twice that positive square root, not an incoming/advanced branch. Both contact diagonals remain present. No finite-core elimination or fitted contact coefficient is used.

## 2. Exact kernel and fixed complement checked

The ground and kernel checkers are replayed freshly by the review checker. They establish the PSD/ground certificate, full-rank ground pairing on ran P, and a two-sided exact inverse of H_C-theta I. Multiplying the first threshold row by V* forces P(u-chi)=0; then u belongs to G and the second row forces chi=0. Thus the kernel is exactly `(D,0)`.

M0 is Hermitian, so its restriction N0 to the fixed orthogonal complement N is bijective. This is not the false assertion that the unreduced forty-state threshold matrix is invertible. The projector diag(Q_D,0) commutes with M(k) on both sides: spectral functions of H_O preserve D, and P annihilates D on both sides. Therefore N is the same reducing complement for all sufficiently small k, despite M(k) not being Hermitian for positive k.

## 3. Uniform inverse estimate checked

The exact finite-dimensional PSD certificate implies a strictly positive gap delta between theta and the remaining sixteen native modes. Its decimal value is unnecessary. The spectral theorem and the rationalized scalar identity give

```
||sqrt(A|C0)-sqrt(A|C0-k^2 I)|| <= k^2/sqrt(delta)
```

for 0<k^2<delta. Orthogonal compression cannot increase operator norm. Including the ground 2ik term and the core k^2 shift gives

```
||N(k)-N0|| <= 2k+(1+2/sqrt(delta))k^2 <= Lk,
L=3+2/sqrt(delta),   k<=1.
```

Let `a=||N0^-1||>0`, `k0=min(1/2,sqrt(delta)/2,1/(4aL))`. Then `a||N(k)-N0||<1/4`, so the Neumann series gives `||N(k)^-1||<=4a/3<=2a`. The dark block is 2ik I_D, also invertible for k>0. Hence the complete outgoing response is well-defined throughout 0<k<k0, not just along a sequence or away from unrecorded exceptions.

The constants are explicit mathematical expressions in the source matrices. Existential C12 does not require their numerical evaluation or optimality. The review checker verifies the rational Neumann margin; the spectral theorem/norm argument is a documented mathematical proof, not machine-formalized functional analysis.

## 4. Flux factors and amplitude bounds checked

For an incoming ground coefficient b, unit-flux preparation supplies b/sqrt(v), with v=2k. The boundary right-hand side is `2ik b/sqrt(v)`, while outgoing ground readout multiplies the contact value by sqrt(v). The **same scalar** v appears for all four ground modes, so

```
T(k)b = 2ik G0 [M(k)^-1(b,0)]_lead.
```

For b in B, the source lies in N, giving `||T(k)b||<=4ak||b||`. The reducing complement makes its ground output orthogonal to D. For d in D the exact free solution is T(k)d=d, R(k)d=0, with no core component. Consequently, with C=4a,

```
||T(k)-Q_D|| <= Ck.
```

Continuity gives R=T-I_G in exactly the source's one-side-incidence convention, so `R+(I_G-Q_D)=T-Q_D`. This proves the second claimed uniform bound with the same C. No limit was inferred merely from unitarity, and the dark sector has not been discarded.

## 5. Packet statement checked

C12 uses energy-normalized incoming asymptotic profiles: `integral ||f(E)||^2 dE=1`. The source's stationary 1/sqrt(v) normalization is consistent with this measure. If one instead starts with a momentum-normalized g(k), the conversion is `f(E)=g(k)/sqrt(2k)`, because dE=2k dk; no extra velocity factor belongs in the stated energy integral.

The two reducing output sectors are orthogonal even for coherent input profiles. Thus

```
P_trans = ||Q_D f||_L2^2 + integral ||T(E)(I_G-Q_D)f(E)||^2 dE.
```

On the declared support, k^2=E-theta<epsilon. The second term lies between zero and C^2 epsilon. This proves the stated packet inequality uniformly over profiles and phases, not just the source's four-mode incoherent numerical example. It concerns incoming asymptotic packets, not locally prepared bound overlap, capture or permanent connected occupation.

## 6. Verdict and authority boundary

**C12 is established within its fixed conditional mathematical model.** The local result is recorded in the v6 successor; C1–C11, their outcomes, models and edges remain unchanged. The protocol ends with two units used, zero remaining, and no renewal.

The exact certificate checkers verify finite hypotheses and refusal controls. This review supplies the analytic argument; it is not an Agda/Rzk formalization, an external human peer review or an independently calibrated physical measurement. No species, dimensional scale, detector, 2gamma/3gamma process, branching ratio or complete programme coverage is admitted. The separate high-energy execution budget is untouched.

## Replay

```sh
python research/scattering/low-energy/check_pentachoron_threshold_review.py --check
```
