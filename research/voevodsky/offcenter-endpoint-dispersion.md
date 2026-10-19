# Dispersive/native continuation — iteration 1 of 3

## Native-adapter follow-up

`native-spinor-pair-adapter.md` supplies a source-bound conditional 100x4 pair
encoding with 99 exact checks. It retains all complementary coordinates and
exposes doublet/output covariance choices; no physical coupling is inferred.

## Result

Certified **real-axis retarded dispersive parts** of the pair and vector-triple
endpoint channels at E=2 and E=4, with corresponding off-center flux bounds in an
explicit endpoint-only submodel. All **37 checks pass** and source hashes are
current. No finite imaginary-energy parameter is used.

The scalar Slater-record triple response is different and remains open. Native
and physical coupling are not inferred from the successful continuum calculation.

## 1. Fresh state and separation of obligations

Freshly read the preceding energy-response continuation and reload its checked
receipt and the earlier center-energy response. Retain the same free half-line
operators and endpoint measures; do not replace the Slater measure by a product
measure or the native core by a newly relabelled particle space.

The prior complex responses at E+8i are not used as boundary values. Only the
certified real-axis densities are reused for imaginary parts.

## 2. Analytically remove one spectral variable

The one-body endpoint response is

    g_1(z)=[z-2-sqrt((z-2)^2-4)]/2,

with the branch asymptotic to 1/z and negative imaginary part in the upper
half-plane. Its real boundary value r(w) is

    r(w)=(w-2)/2,                       0<=w<=4,
    r(w)=[w-2-sign(w-2)sqrt((w-2)^2-4)]/2, otherwise.

It is continuous, bounded by one in magnitude, increasing inside the band and
decreasing outside. Its exact minimum -1 and maximum +1 occur at w=0 and w=4.

Integrating the last variable of the genuine energy-sum spectral measure gives

    Re g_2(E+i0)=integral rho_1(x) r(E-x) dx,
    Re g_3(E+i0)=integral rho_1(x)rho_1(y) r(E-x-y) dxdy.

The bounded one-body response permits dominated passage to the boundary after
this integration. There is no remaining principal-value singularity; the
square-root branch points are retained, not numerically crossed by a finite-box
pole or a finite-eta extrapolation.

## 3. Actual error certificates at branch points

Partition the remaining energy variables with meshes 128,256,512. Enclose each
square-root density weight as in the preceding continuum checker. For each
response argument interval, enclose r using its endpoints and any included
extrema at 0 or 4. This handles cells straddling a branch point exactly.

Integer square roots give endpoint radical bounds. Signed interval products and
rational Machin pi bounds give lower/upper integral sums. Response endpoints are
rounded outward to a 10^-10 rational grid before flux propagation. Decimal views
are not used in the calculations.

Checks include decreasing enclosure widths, pair/triple reflection and an
independent overlap with the previously certified pair real part at E=6. The
pair real part at E=4 vanishes exactly by spectral reflection; its box integral
contains zero before that symmetry identity is used.

Outward-rounded containing ranges are

| Energy | Re g_2 | Re g_3, vector endpoint |
|---:|---|---|
| 2 | [-0.5186765,-0.5137028] | [-0.3340323,-0.3277503] |
| 4 | 0 exactly | [-0.4258880,-0.4150841] |

The triple real parts at E=10 and E=8 are respectively their negatives by
reflection about 6. Pair reflection is about 4. These are genuine real-axis
retarded dispersive values, unlike the preceding large-eta certificates.

## 4. Off-center optical flux in an explicitly restricted fixture

Choose H_core=6I_4 and unit input/two-output/vector-triple couplings, but set
**lambda_A=0**. This is the endpoint-only submodel, not the full combined
Slater-record fixture. The unresolved Slater real part is neither dropped from
an active vertex nor assigned the vector endpoint value.

Write

    g_pair=a_p-i b_p, g_vector3=a_v-i b_v,
    b_p=pi rho_2(E), b_v=pi rho_3(E).

For scalar input coupled to input pair and two-output fibers,

    d_s=E-6-2a_p,
    T_s=4b_p^2/[d_s^2+4b_p^2],
    R_s=d_s^2/[d_s^2+4b_p^2].

For vector input coupled to input pair and vector triple fibers,

    d_v=E-6-a_p-a_v,
    T_v=4b_p b_v/[d_v^2+(b_p+b_v)^2],
    R_v=[d_v^2+(b_p-b_v)^2]/[d_v^2+(b_p+b_v)^2].

Both sector sums equal one algebraically. Certified intervals contain these
identities, and intersecting complementary ranges improves bounds without
assuming independently extremal response values are simultaneous.

For unpolarized rho=I_4/4, P_2=T_s/4, P_3=3T_v/4 and survival=R_s/4+3R_v/4.
Outward-rounded probability enclosures are

| Energy | Two outputs | Vector three outputs | Survival |
|---:|---|---|---|
| 2 | [0.0143657,0.0148514] | [0.0054528,0.0058478] | [0.9793009,0.9801814] |
| 4 | [0.1043365,0.1050497] | [0.2400205,0.2507008] | [0.6442496,0.6556429] |

The exact correlated probabilities sum to one. They are incoming energy-fiber
fluxes in a declared fixture, not captured or initially retained probabilities,
and not physical branching fractions.

## 5. Native/physical coupling remains a distinct gate

A continuum response determines what a *specified* attachment sees. It does not
choose that attachment, identify the conjugate representation partner physically,
or set its work/energy scale. No source-bound native full-spinor core map is
constructed by the integrals above.

The next native step should explicitly reuse a retained source-cycle-compatible
spinor encoding and test its tensor/conjugate pair map against the encounter
projectors and covariance. Any choice between the available native doublets,
operation-energy coefficients or orbital attachment records must remain visible.
An admitted mathematical adapter would still not prove physical positron/photon
identity or derive empirical coupling constants.

## 6. Nonredundant continuation

For the Slater real part, integrate the last variable with its polynomial
Vandermonde factors retained. Express it through the first three one-body orbital
resolvent entries or polynomially weighted g_1 moments, and certify the remaining
branch-point integrals. Then restore lambda_A in the off-center scalar scattering
block. In parallel, construct and audit a source-bound native spinor-pair adapter
rather than silently reusing the scalar eleven-state port generator.

## Reproduction

```sh
python research/voevodsky/checkers/check_offcenter_endpoint_dispersion.py
```

Receipt: `results/offcenter_endpoint_dispersion.json`, with exact signed continuum
bounds, mesh controls, real-axis responses and restricted-fixture flux enclosures.
