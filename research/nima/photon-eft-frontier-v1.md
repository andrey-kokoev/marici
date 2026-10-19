# Photon EFT continuation — v1 construction checkpoint

**Historical checkpoint:** use the [active v2 frontier](photon-eft-frontier-v2.md). The general degree-five log/window construction proposed below is now completed in its successor packet; this file is not a second live queue.

## Question

What is executable after the photon normalization and primary-source gates, without reopening the disposed C1–C12 inventory or claiming a physical scattering explanation?

## Established input gates

| Gate | Bounded result | Evidence |
|---|---|---|
| N: normalization | T_red=M/(16*pi); at common Born kernel lambda_gamma=16*pi*b, B_std=B_red/(16*pi). Existing reduced coefficients are unchanged. | [Normalization packet](photon-normalization-v1.md) and its checker |
| P: primary-source loop | All four published degree-four log coefficients match physical Bose partial-wave unitarity, including forward-invisible beta12. | [Primary-source packet](photon-primary-loop-v1.md), frozen excerpts and exact checker |
| L: local tensor | Eight explicit local Ward/Bose tensor generators through degree four, retaining every helicity sector. | [Local tensor packet](photon-local-ward-basis-v1.md), exact checker and receipt |
| M: logarithmic tensor | Regular degree-four covariant log representative; every helicity/channel coefficient matched; forward-invisible scale transport retained. | [Loop tensor packet](photon-loop-tensor-v1.md), exact checker and receipt |
| W: window lift | Exact forward Cauchy extension and a derived two-variable analytic difference, with nonunique local matching retained. | [Window lift packet](photon-window-lift-v1.md), exact checker and receipt |
| Q5: cut compatibility | Independent tensor-derived degree-five R2/R3 interference matches the archive; hidden Born F3 affects the forward loop cut. | [Degree-five audit](photon-degree5-cut-v1.md), exact checker and receipt |
| L5: local inventory | Twelve regular covariant generators; forward rank six and a nonzero six-dimensional invisible kernel; independent h5 retained. | [Degree-five local jet](photon-local-degree5-v1.md), exact checker and receipt |
| M5: R-family log/window | Regular odd-degree tensor, exact Cauchy lower polynomial and two-variable analytic difference; all twelve matching directions retained. | [Degree-five log/window packet](photon-degree5-window-v1.md), exact checker and receipt |
| G5: general Born cut | Six bilinear source coordinates, rank-four cut readout and a generally nonzero single-minus loop response. | [General interference packet](photon-general-degree5-cut-v1.md), exact checker and receipt |

The source path N -> P -> L -> M -> W completes **EF-WB4 at its declared finite-order R=s^2 scope**. These are imported-framework mathematical results, not native licensing. Each linked packet carries its scoped controls and receipt; SCC and fresh headless checks accompany the constructed stages. No fresh full-suite pass is claimed after the earlier 180-second timeout.

## EF-WB4 — constructed at the declared scope

**Original candidate, now constructed conditionally:** for the declared R=s^2 Born control, the degree-four photon-loop cut and whole-window forward subtraction admit a covariant Ward/Bose off-forward completion through the retained EFT order, with their analytic matching freedom retained explicitly.

This bounded construction has documented algebraic/analytic arguments and scoped exact controls, not a machine-formalized proof. It is not C13, a newly scored forecast or a physical law. Work in the imported parity-even photon EFT with s+t+u=0, the published upper-rim logarithm, and a fixed declared expansion order in lambda_gamma. Do not identify the photon EFT g2/g3 symbols with the earlier independent Dirac-current coefficients.

### Completed representative and retained freedom

The local/log tensor and its whole-window lift are constructed without rational kinematic poles. The lift includes indispensable lower-degree subtraction terms; its difference from the log representative has a uniformly convergent two-variable series. The off-forward extension is not unique. It preserves all helicities and the local jet coefficients

    g2_gamma, f2_gamma;
    g3_gamma, f3_gamma, h3_gamma;
    g4_gamma, g4prime_gamma, f4_gamma.

Separate the fixed Born control and loop discontinuities from the freely matched local terms at their declared perturbative orders. The loop Phi5 component may vanish at this order without authorizing deletion of the independent local h3_gamma channel.

### Acceptance and strongest falsifiers

1. **Retained tensor identities established:** the local-plus-log construction has algebraic Ward/Bose/Lorentz arguments, supplemented by all-16-helicity and component Ward controls. This is not a machine-formalized proof or an interacting-QFT construction.
2. **Degree-four log/cut matching verified:** all three channel coefficients match the independently checked primary source with normalized Bose factors and the declared logarithm rims. Doubling beta12 still passes forward targets but gives a nonzero off-forward residual. The common-scale shift is a local combination of G4, G4prime and F4, including the forward-invisible term.
3. **Local restriction verified:** the constructed tensor's forward jet has rank five and kernel span(f3_gamma,h3_gamma,g4prime_gamma). Off forward at s=1,t=-16/25,u=-9/25, their (Phi2,Phi5,Phi1) minor is (144/625)*I3. Retain these nonzero directions when completing the loop/window lift; do not set them to zero or confuse jet rank with a fixed-energy helicity-matrix rank.
4. **Window lift and analytic difference derived:** exact forward polynomial-division/rim comparisons fix the visible lower terms. Endpoint-log series prove joint analyticity of the difference for |s|,|t|,|s+t|<tau and determine its retained local jet, including the G4prime scale term. Arbitrary F3/H3/G4prime local additions remain. The unsubtracted massless amplitude is not analytic at the origin.

The original stopping condition (explicit lift with these checks, or a scoped obstruction) is met at the stated mathematical scope. No helicity or invisible term was dropped, normalization fitted, or finite physical matching coefficient predicted.

## Degree-five Born/cut compatibility — verified for the chosen family

The [independent degree-five audit](photon-degree5-cut-v1.md) matches the archived mixed c0*c1 cut against the full crossed Ward/Bose Born tensor for R=r0*s^2+r1*s^3. Use Phi1=a*R(s), Phi2=-a*[R(s)+R(t)+R(u)], Phi3/Phi4 crossed, Phi5=0: thus g2=a*r0, f2=-a*r0, g3=a*r1, f3=-3*a*r1, h3=0 for this chosen family only. Here r0,r1 correspond to the archived polynomial c0,c1; none is a selected physical coefficient or the independent Dirac-current g3.

The normalized physical Bose waves reconstruct D=(37-z^2)/5120, O=-13/1536 and M=-x^2/768, exactly the archived polynomials divided by 16 under the unchanged dictionary. Dropping only the forward-invisible Born F3 term preserves all forward Born data but changes the forward loop D/O coefficients by -1/320 and +1/512. The compatibility test is resolved; generic dimension-ten Born couplings and all-order extrapolations are not.

## Local degree-five tensor inventory — constructed in the regular on-shell ansatz

The eight-generator jet now has explicit G5/G5prime pair-weight extensions and F5=S2*F3, H5=S2*H3. Exact witnesses give coefficient-polynomial rank twelve and forward-jet rank six, with kernel span(f3,h3,g4prime,g5prime,f5,h5). Its six invisible directions remain independent across off-forward/energy comparisons. Deleting h5 leaves forward data unchanged but lowers full rank to eleven; its single-minus control is 138528/390625. This is not an off-shell operator classification or a determination of finite matching.

## Degree-five R-family logarithmic/window representative — constructed

The [regular lift](photon-degree5-window-v1.md) matches all retained helicity/channel coefficients, verifies odd forward crossing C_u=-Gamma(C_s), and derives common-log transport -G5/120+G5prime/320+65*F5/3072. Copying the even sign would create a forbidden forward O scale term 13/768. The degree-five Cauchy division gives lower terms of degrees two, three and four; endpoint-log series derive the two-variable analytic difference, whose remaining series begins at degree six. All twelve finite matching coefficients remain free, including h3/h5 despite this family's zero single-minus loop section.

## General degree-two/degree-three Born interference — constructed

The [general cut inventory](photon-general-degree5-cut-v1.md) removes the R-family ties and projects independent photon g2,f2,g3,f3,h3, preserving the source's physical off-diagonal 2*Phi5 Bose wave. The induced response is pi*Im Phi5=h3*(6*g2+f2)*s^3*t*u/480, generally nonzero. Exact restriction recovers the audited R-family result without fitting normalization.

All six bilinear coordinates g2*g3,g2*f3,g2*h3,f2*g3,f2*f3,f2*h3 remain in the source. Their cut coefficient map has rank four and a two-dimensional kernel; its combinations are not identifications of physical couplings. Interference can be indefinite while the complete Born-wave square remains PSD. This is the quadratic two-photon elastic cut in the stated real parity-even contact stratum, not a full physical IR inventory.

## Next executable construction — general degree-five log/window tensor

Lift all six coupling-coordinate cuts, including the induced single-minus response, into the regular twelve-generator degree-five log/window framework. Verify Ward/Bose identities, every channel/helicity coefficient, exact R-family restriction, common-log transport including the previously absent h5 direction, and the two-variable generated remainder.

Retain the source/readout kernel and all finite matching coefficients; do not quotient away Born directions merely because this cut readout is nonfaithful. Stop at the explicit scoped lift/remainder or a nonzero normalization/crossing/regularity obstruction. This is an unranked bounded mathematical continuation, not selected couplings, native/UV licensing or renewed C12 work.

## Planner projection and disposition

The registered shared low-energy workbench still returns `recommendation: null`, with zero open action cards, ready tasks and blocked tasks: it ranges only over the twelve disposed C1–C12 propositions. Its read-only `--programme low-energy --check` run confirms this. The completed R-family/general Born-cut results and the proposed general log/window construction lie outside that scored inventory; no forecasts, numerical rank or new protocol budget have been invented.

Native preparation, physical matching, exhaustive physical IR inventory and same-scope UV/dispersive assumptions remain separate unearned gates. Missing native authority is not made into an open waiting leaf and does not prevent this explicitly conditional EFT construction. C1–C12 dispositions, exhausted C12 budget and the high-energy pause are unchanged.
