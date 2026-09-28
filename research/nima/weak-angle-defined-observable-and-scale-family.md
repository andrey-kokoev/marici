# Weak angle: defined observable and corrected boundary evolution

## Observable

Use s_hat_W^2(MZ)=g'^2(MZ)/(g'^2(MZ)+g2^2(MZ)) in the MSbar scheme, with hypercharge convention Q=T3+Y. This differs from the on-shell definition 1-MW^2/MZ^2 and from effective angles extracted from Z-pole asymmetries. Precision comparisons need their respective radiative conversions.

The test below uses MZ=91.1876 GeV and illustrative inverse electromagnetic coupling A=127.95 at MZ. This is an external normalization input. It does not use the low-energy value 137.036 as the electroweak-scale coupling, and does not ingest a weak-angle target or its uncertainty.

## Corrected conditional boundary

At a scale Lambda, adopt the existing common matter-trace normalization after correcting multiplicities:

    alphaY^-1(Lambda)=10*t,
    alpha2^-1(Lambda)=6*t.

The boundary angle is 3/8. The shared coefficient t and the boundary scale require a carrier mechanism. For this diagnostic t is fixed from the supplied electromagnetic normalization; Lambda is varied openly.

## Evolution

Use the one-loop Standard Model coefficients for unrescaled hypercharge, bY=41/6 and b2=-19/6. Assume the Standard Model field content across the entire interval, with no extra thresholds. Set ell=log(Lambda/MZ)/(2*pi). Then

    alphaY^-1(MZ)=10*t+bY*ell,
    alpha2^-1(MZ)=6*t+b2*ell,
    A=16*t+(11/3)*ell,
    t=[A-(11/3)*ell]/16.

Consequently

    s_hat_W^2(MZ)=alpha2^-1(MZ)/A
                 =3/8 - (109/24)*ell/A.

This formula exposes the scale dependence directly.

## Calculated family

| Boundary scale Lambda (GeV) | s_hat_W^2(MZ) |
|---:|---:|
| 91.1876 | 0.375000000 |
| 1e3 | 0.361470837 |
| 1e10 | 0.270414783 |
| 1e13 | 0.231390759 |
| 1e16 | 0.192366736 |
| 1.22e19 | 0.152219344 |

Outcome: the corrected 3/8 boundary evolves into the electroweak-angle neighbourhood for a boundary scale around 1e13 GeV in this approximation. The formerly used Planck-scale boundary yields about 0.1522 under these corrected assumptions. The scale scan is a diagnostic; selecting a scale because its output agrees with observation would calibrate it to that observation.

This supplies a physical mechanism capable of shifting a boundary fraction: scale evolution of the two gauge couplings. It replaces attempts to force a low-energy 3/13 directly from static slot weights. A prediction requires independently fixed Lambda, the kinetic normalization, field content/thresholds, and a precision scheme-matched calculation. The illustrative alpha input is rounded, and no precision experimental fit is performed here.

## Independent strong-coupling constraint

The existing check_neutrino_scale.py infers a roughly 3.4e13 GeV sterile scale from measured neutrino mass and an assumed Yukawa. It records the absolute carrier scale as unresolved. It therefore supplies no independent carrier boundary for this calculation.

Instead extend the common-trace ansatz to SU(3). Its corrected index is 6 across three generations: each Q_L contains two colour triplets, while u_R and d_R contribute one each. The historical value 4.5 omitted the weak multiplicity of Q_L.

Use the additional illustrative input alphaS^-1(MZ)=8.5 and b3=-7. The boundary is (alphaY^-1,alpha2^-1,alpha3^-1)=(10t,6t,6t). The electromagnetic sum A and strong inverse S obey

    A=16t+(11/3)ell,
    S=6t-7ell,
    ell=(3A-8S)/67.

With A=127.95, S=8.5, MZ=91.1876 GeV this yields Lambda=6.66445717e14 GeV, t=6.916542289, and the independent output s_hat_W^2(MZ)=0.207667213. This lies well below the electroweak value near 0.231. Conversely the previously promising Lambda=1e13 GeV predicts alphaS=0.070934864 instead of the illustrative input 1/8.5, approximately 0.11765.

Outcome: the common matter-trace boundary plus one-loop Standard Model evolution fails the joint three-coupling diagnostic. Choosing a scale to match the weak angle alone hides the strong-sector mismatch. No precision significance is assigned to this rounded-input, one-loop calculation. Extra thresholds, a different kinetic boundary, or additional fields would define further hypotheses requiring independently specified content.

Exact trace arithmetic and floating-point running identities are checked in research/nima/checkers/check_three_gauge_common_trace_boundary.py. The weak angle is never an input to that test.

## Existing extra matter and common-correction tests

The repository's sterile right-handed neutrinos have Y=0 and trivial SU(2), SU(3) representations. Their one-loop gauge beta contributions vanish. They do not change the three-coupling result in this approximation; Yukawa-dependent effects at higher orders are a separate calculation.

A common correction along the boundary vector (10,6,6) is absorbed by the fitted shared coefficient t. It leaves both the inferred scale and weak-angle output unchanged. A common multiplicative boundary factor likewise just redefines t. Degenerate complete SU(5) multiplets supply one-loop threshold shifts proportional to (5/3,1,1) in the unrescaled hypercharge convention, also parallel to that vector. They give the same zero-change result in this diagnostic.

More generally let (D_Y,D_2,D_3) be additive shifts in inverse couplings at MZ. After refitting the same electromagnetic and strong inputs, the weak-angle change is

    delta s_hat_W^2 = [-23 D_Y/134 +111 D_2/134 -109 D_3/201]/A.

This is an exact linear response of the one-loop boundary equations with externally supplied threshold shifts. Physical thresholds can also depend on the solved boundary scale; that dependence would have to be included in a specified model. The coefficients identify which sector-dependent corrections can affect the mismatch. Corrections parallel to the common boundary vector cancel identically.

Outcome: the existing sterile-neutrino proposal and a universal carrier normalization do not repair this one-loop branch. A repair requires independently specified sector-dependent kinetic terms or nonuniversal thresholds, including their representations and masses. No such new spectrum is selected by this test.

Checker: research/nima/checkers/check_gauge_threshold_repair.py. Singlet indices and the refit/cancellation identities pass. No output artifacts are written.

## Existing sector-dependent Gram rule

The historical check_gauge_couplings.py postulates g_i^2 proportional to C_i/lambda_i with lambda=(12,4,4). Retaining this postulate while correcting matter counts to C=(10,6,6) makes the inverse boundary proportional to (6/5,2/3,2/3), or (9/5,1,1).

Using the same EM and strong inputs, the resulting scale is 1.495609e14 GeV and weak angle 0.200542274. The script also labels its U1 running GUT-normalized while building C_Y from ordinary hypercharges. If its numerical boundary is instead assigned to the GUT-normalized coupling g1 and converted via g1^2=(5/3)gY^2, the physical inverse boundary becomes (3,1,1). That reading yields scale 1.13687892e10 GeV and weak angle 0.155317661.

These readings are distinct ansatz choices, not two physical answers produced by a consistent convention change. A consistent generator rescaling also rescales its trace and kinetic normalization. The diagnostic exposes the historical ambiguity without selecting the convention that approaches a target.

Outcome: neither corrected reading of the existing sector-dependent rule repairs the joint coupling mismatch. The tested branches are common matter trace (0.207667), ordinary-hypercharge C/lambda (0.200542), and historically assigned GUT-normalized C/lambda (0.155318). All values are one-loop diagnostic outputs from rounded EM and strong inputs. No remaining tested rule establishes a weak-angle prediction near 0.231.

Checker: research/nima/checkers/check_sector_gram_gauge_boundary.py. Corrected indices, convention conversion, boundary sums and running identities pass.

## Verification

research/nima/checkers/check_weak_angle_scale_family.py checks the running and normalization identities and prints the family. It writes no artifacts. The historical check_gauge_couplings.py used inconsistent matter multiplicities and a different boundary ansatz C_i/lambda_i, with GUT-normalized U(1) running. This calculation is an explicitly separate corrected common-trace branch; it is not a rerun of that historical prediction.
