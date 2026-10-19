# Dispersive/native continuation — iteration 3 of 3

## Result

Certified the **distinct-orbital Slater real-axis dispersive part at E=4**, then
included it in a normalized combined scattering fixture with the **source-
compressed native pair energies**. All **19 checks pass**; source hashes are
current. No finite imaginary-energy extrapolation is used.

This completes a constructive off-center example with all previously declared
channel vertices active. It does not derive physical coupling strengths,
relative native/orbital units, or positron/photon channel identity.

## 1. Fresh state and the remaining weighted integral

Freshly read `native-spinor-pair-adapter.md`. Reload its checked source-bound
adapter receipt, the pair/vector real-axis endpoint receipt and the certified
real-axis orbital density receipt. Retain both native doublets and the full native
pair complement; no source-selected state is substituted for a discarded residual.

For the scalar orbital-record vertex, the real part is

    Re g_A(E+i0)=(1/6) integral rho_1(x)rho_1(y) (x-y)^2
                           Re F(E-x-y;x,y) dxdy,

where

    F(w;x,y)=integral rho_1(t) [(t-x)(t-y)]^2/(w-t+i0) dt.

Direct polynomial division gives a valid identity but can subtract large terms.
This turn evaluates the same integral through a stable small orbital Green block.

## 2. Exact conditional one-body orbital response

Use the alternating-sign gauge h=2I+adjacency, unitarily equivalent to the prior
hopping convention. Its first orthonormal spectral polynomials are

    r_0(t)=1, r_1(t)=t-2, r_2(t)=t^2-4t+3.

Then

    (t-x)(t-y)=r_2(t)+v_1 r_1(t)+v_0,
    v_1=4-x-y, v_0=(x-2)(y-2)+1.

For a,b=0,1,2, the infinite half-line Green entries are

    R_ab(w)=sum_(j=0..min(a,b)) g_1(w)^(|a-b|+1+2j).

Consequently F=v^T R v, with v=(v_0,v_1,1). This is the genuine infinite-volume
orbital response, not a three-site isolated-box resolvent. The exact rational
control checks it against a three-site block with the correct tail Schur term.
Two further rational controls independently compare v^T R v with polynomial
division of the weighted Stieltjes integral.

Set f_m=Re[g_1(w+i0)^m]. The real conditional integrand is

    Re F=(v_0^2+v_1^2+1) f_1
          +2v_1(v_0+1) f_2
          +(2v_0+v_1^2+1) f_3 +2v_1 f_4+f_5.

For 0<=w<=4, f_m=T_m((w-2)/2), with T_m the Chebyshev polynomial. Outside the
band, g_1 is real and its powers are enclosed directly. This removes the last
principal-value variable analytically while retaining branch points and the
Vandermonde orbital records.

## 3. Certified remaining integration

Enclose the polynomial coefficients and all f_m on each rectangle. Chebyshev
bounds use endpoint values plus any included critical points; the critical-point
radicals are themselves enclosed. Cells spanning w=0 or w=4 are split by branch.
All fixed-point products round outward by exact integer floor/ceiling operations.
Square-root density weights and pi use the earlier exact certificates.

Uniform meshes 64,128,256,512 produce valid decreasing-width enclosures. A band-
center control contains the known exact zero at E=6. The final outward-rounded
containing interval is

    Re g_A(4+i0) in [-0.691152,-0.589451].

The error bar is still about 0.102. It is not suppressed by reporting a decimal
midpoint, but it suffices to certify negativity and propagate useful flux bounds.
By spectral reflection, Re g_A(8+i0) is its negative.

Combine this real part with the already certified rho_A(4) to obtain

    g_A(4+i0)=a_A-i b_A, b_A=pi rho_A(4)>0,
    Sigma_A=lambda_A^2 g_A P_s.

This response is not the vector endpoint triple response and was not obtained by
reusing the large-eta complex certificate.

## 4. Replace the arbitrary encounter level by source-compressed energies

The preceding native adapter gives, for the displayed cycle-defect convention,

    epsilon_0=11-2sqrt(6)-sqrt(5),
    epsilon_1=11-2sqrt(6)+sqrt(5).

These are checked against every corresponding source-bound adapter record. They
are the compressed conditional native **pair** energies, approximately 3.864953
and 8.337088. Option 1 uses the second doublet under the same displayed-lift
Hamiltonian; it is not assigned the opposite-lift ground energy.

For an explicit fixture choose relative native/orbital scale one and all cross-
channel lambdas one. These two scale/coupling declarations are not derived from
the source operator or physical observation. The native pullback remains
J Sigma_encounter J^dagger on the retained 100-state pair space; all 96 complement
coordinates are retained and dark only under the chosen vertex.

At E=4 write pair, vector triple and Slater responses as

    g_p=a_p-i b_p, g_v=a_v-i b_v, g_A=a_A-i b_A.

For either native core energy epsilon, the scalar block has

    d_s=4-epsilon-2a_p-a_A, B_s=2b_p+b_A,
    D_s=d_s^2+B_s^2,
    T_2=4b_p^2/D_s,
    T_A=4b_p b_A/D_s,
    R_s=[d_s^2+b_A^2]/D_s.

The vector block has

    d_v=4-epsilon-a_p-a_v,
    D_v=d_v^2+(b_p+b_v)^2,
    T_v=4b_p b_v/D_v,
    R_v=[d_v^2+(b_p-b_v)^2]/D_v.

Both sector sums equal one exactly. For rho=I_4/4, P_2=T_2/4,
P_3=T_A/4+3T_v/4 and survival=R_s/4+3R_v/4. Interval propagation intersects the
exact optical complements and [0,1], without assuming independent extrema can
occur together.

## 5. Certified source-choice sensitivity

Outward-rounded probability enclosures for the declared unit-scale fixture are

| Native doublet option | Two outputs | All three outputs | Survival |
|---:|---|---|---|
| 0 | [0.16916,0.18451] | [0.55997,0.58403] | [0.23776,0.26597] |
| 1 | [0.04070,0.04341] | [0.06484,0.06879] | [0.88780,0.89446] |

The three-output entry sums orthogonal scalar-record and vector sectors. The
exact correlated outcomes sum to one; endpoint sums of independent interval
bounds need not. The triple-flux ranges are disjoint between native choices, as
are their survival ranges, despite the intentionally retained Slater error bar.

Thus selecting an encoding/core energy is consequential. A successful isometry
and covariance check does not remove the native selection or calibration gate.
Where the native adapter requires a nonambient effective output action, this
fixture uses that explicitly declared action rather than claiming the old
ambient output covariance has been repaired automatically.

## 6. Status of this three-turn continuation

Established conditionally and reproducibly:

- Pair and vector-triple off-center real-axis endpoint dispersive certificates.
- A distinct-orbital scalar triple dispersive certificate at E=4.
- Source-bound native pair encodings with all residual coordinates retained.
- Source-compressed pair energies, typed pulled-back self-energies and normalized
  off-center flux with all the declared channels active.

Not established:

- A physical mechanism selecting the doublet, output representation or optional
  cycle-defect operation.
- Relative physical energy/time units or cross-channel coupling strengths.
- Physical conjugate partner or photon-sector identification and reaction ratio.

No physical coupling is admitted by this turn. Normalized conditional amplitudes
are not a substitute for those missing inputs.

## 7. Nonredundant continuation

Use adaptive partitions to tighten the weighted branch-point integral and extend
it across the pair propagating band. Sweep the explicit relative native/orbital
scale and independently allowed couplings to audit parameter identifiability.
A physical coupling claim additionally requires a supplied native interaction
operation or calibration/selection principle, rather than a fitted ratio.

## Reproduction

```sh
python research/voevodsky/checkers/check_slater_real_axis_native.py
```

Receipt: `results/slater_real_axis_native.json`, retaining exact integration
bounds, independent Green-block controls, both source-core energies and complete
conditional flux enclosures.
