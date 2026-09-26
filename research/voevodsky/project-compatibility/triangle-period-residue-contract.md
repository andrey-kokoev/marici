# Sector pilot: total-energy residue versus the three-site cosmological period

## Hostile-audit warning: physical measure identification is challenged

`triangle-measure-audit.md` independently derives the ordinary Euclidean loop Jacobian and finds that the literal printed measure used below differs by16D/(3sqrt(pi))*Gamma((d-2)/2)/Gamma((d-3)/2). It has scaling degree d+4 instead of d and contains an epsilon0 zero absent from the ordinary loop measure. The conditional calculations below remain calculations of their stated printed family; their physical promotion is blocked until the external normalization/volume convention is reconciled. Source validation is now a concrete measure-identification problem, not just a request to choose a completion order.

`triangle-primary-reconciliation.md` now corroborates the challenge with versioned primary TeX: arXiv:2402.06558v1's specific coefficient has positive external volume and Gamma(epsilon), while v3 eq:(3.11) changes these to inverse volume and Gamma(epsilon+1/2). The same v3 appendix(A.12) still prints Gamma(epsilon), so this is not a fully reconciled source packet. Structural agreement with the independent Jacobian is established for the revised specific formula; absolute constants and conflicting formulas remain open. No silent replacement of the frozen pilot is authorized.

Two further traversal steps now fix the ordinary-volume dictionary and transport the period explicitly. `triangle-volume-dictionary.md` gives signedCM2=16D, CM3=288K and an exact Cartesian/distance-coordinate patch integral2. `triangle-measure-transport.md` defines the Euclidean-measure benchmark G on the same localized candidate chain and proves P_old=R*G, R=H/(3sqrt(pi))*Gamma(epsilon+1/2)/Gamma(epsilon). Its regulator-first boundary has a nonzero1/epsilon pole, not the old finite limit. The transported joint coefficient is epsilon*E^(2-epsilon)*G→pi/(2a) integral chi(x,0)/(x+b) dx. No physical subtraction or cycle prescription follows from this comparison.

`triangle-cartesian-pole.md` now confirms the Euclidean pole independently in line-normal Cartesian coordinates, without the old normalization or joint theorem. `triangle-readout-jet.md` then proves the old finite boundary P0 retains the pole coefficient but not a finite part: if P=RG, G=A/epsilon+B+..., then B=(3/H)(P1+2log(2)P0). A normalization shift can leave P0 fixed while changing B. This is a data-sufficiency theorem, not a choice of physical subtraction scheme or a calculation of B.

## Choice and status

Select the one-loop three-site edge-weight twisted period in arXiv:2408.16386v2, equation eq:Triangle, as the FIRST compatibility pilot. This freezes a source interface and a concrete missing diagram; it does not certify residue/interchange, an E=0 chain, an amplitude interpretation, or a completion topology. Those unresolved fields keep the pilot-contract leaf active.

Alternatives inspected: cyclic permutation of the same six-term source has an explicit orientation-preserving action, but by itself does not test the singular completion boundary. Immediate scattering-amplitude identification is rejected because the existing typing audit supplies neither an independently normalized target amplitude nor a comparison map. The period-residue problem directly exposes the source-to-readout completion gap without either shortcut.

## Primary source and independent physical prescription

- `temp/arxiv-2408.16386-source/sections/applications.tex`, lines204–260: eq:Triangle, six simplex terms, one common oriented Gamma, explicit q_G=E=sum X_i and denominators.
- Applications source SHA256: `3e92460fe2e34dc21a537c784dab3b2fbcd9b7cfee9e7372f06971b50d8b6f9b`, freshly matched to the frozen certificate.
- `sections/method.tex`, lines1–88: distinguishes site-energy integration from the edge-weight period; defines the twisted pairing integral_Gamma u phi, u=kappa0 K^gamma, gamma=(d-n_s-L)/2, external-volume normalization, and K vanishing on the integration boundary.
- `research/benincasa/cyclic_q_assembly_certificate.md`: source assembly and generic oriented-chain perimeter. It does not supply E=0 specialization.

The prescribed probe is integration against this source chain, NOT a freely chosen functional, not our finite Boolean observer, and not yet a detector probability or scattering amplitude. The primitive operation to test is total-energy residue/specialization. The coefficient object retains the twist and normalization, rather than silently replacing the physical form by its rational denominator.

## Typed contract

1. **Source:** the displayed six-term rational form and labelled denominators; retain the common measure, kappa0, K^gamma, regulator and oriented chain.
2. **Already available constructor:** formal E-residue of the rational prefactor at generic integration coordinates. Its extension to the full twisted coefficient family is an obligation, not an assumption.
3. **Existing readout:** P(E)=integral over Gamma_E of u_E phi_E on the source's generic admissible parameter domain.
4. **Candidate boundary test:** integration against a source-derived specialized relative chain Gamma_0, in the correctly specialized coefficient system. Gamma_0 has NOT been supplied.
5. **Desired compatibility:** residue of P(E) equals the boundary period of the appropriately specialized/residual form, with an explicit witness accounting for endpoint/vanishing-cycle terms when nonzero. This is not asserted true.
6. **Transported test:** if the residual form constructor is well-defined, composing its boundary integration test with that constructor must be identified with the independently sourced parameter-residue readout. Defining the latter to be the former is prohibited.

An analytic chart may use X3=E-X1-X2 with X1,X2 fixed. This does NOT choose a physical continuation path, sheet or boundary-value prescription: E=0 is not reached inside generic positive external energies. These data must be sourced separately.

## Missing fields and admission gates

- continuation path/branch and regulator regime;
- whether the full normalized twisted period is meromorphic in E with the required pole order, or needs a different regularized boundary object;
- specialization/nearby-cycle map for the actual relative chain and local coefficients;
- endpoint trivialization OR explicitly retained endpoint contributions;
- residue/integration interchange with domain and regularization hypotheses;
- the actual completed chain/coefficient topology and any uniform estimate needed to justify extension.

Do not manufacture a norm or topology to make interchange true. Do not infer any of these from a finite formal residue, generic cyclic covariance, or the presence of the factor1/E. In particular kappa0 and K^gamma may carry parameter dependence and must not be discarded.

The older `check_total_energy_period_residue_interchange.py` is a hard-coded missing-arrow census, not a source-sensitive proof or an analytic counterexample to this physical period. Its missing-map diagnosis is useful; absence of a supplied map does not itself prove this particular period has no such map.

## Fresh severe test: fixed chain still does not suffice

On the same oriented interval0≤y≤1, for E>0, take

    f(E,y)=1/E + 1/(E+y)^2.

The exact primitive is y/E - 1/(E+y), hence

    integral_0^1 f(E,y)dy = 2/E - 1/(E+1).

The generic formal integrand residue is1, so its integral is1; the integrated function has residue2. The moving pole y=-E collides with the endpoint y=0. Thus even a fixed chain and an explicit simple generic E pole do not justify automatic interchange. With f=1/E alone, both orders give1.

`check_period_residue_boundary.py` verifies the primitive, period, residues and mismatch using exact sparse rational-polynomial identities over Fraction; no floating-point integration or installed algebra system. It records all source hashes and verifies that they remain unchanged. This counterexample falsifies the unrestricted structural implication, NOT the cosmological period itself.

Receipt: `period-residue-boundary.json`; reproduce:

    python research/voevodsky/project-compatibility/check_period_residue_boundary.py

## Boundary-observation refinement

`endpoint-observation-completion.md` derives the hostile control's missing endpoint functional from its own kernel: E f_E dy = dy + E/(E+y)^2 dy converges against continuous tests to dy+delta_0. The blow-up y=Et fixes the extra mass at1. A modulus-of-continuity estimate controls the pairing; bounded Lipschitz tests admit a uniform O(sqrt(E)) bound. Total-variation convergence fails, with distance tending to2. Exact kernel/mass/blow-up identities and rational bound samples pass the extended checker; the general convergence estimate is a written proof, not an Agda theorem.

This repairs the model's observation law but does not supply the triangle's physical topology or boundary object. It sharpens the physical gate: derive a source-compatible common-domain description and prove vanishing boundary mass under applicable control, OR retain the actual generated boundary contribution. An ordinary Laurent residue is not assumed for arbitrary test-weighted or twisted periods.

## Actual source normalization and degeneration

`triangle-normalization-degeneration.md` audits the printed external-volume factor inside c_(d,n_e,L), not only the named kappa0 formula. Literally, for d=3+2epsilon, kappa0=C(d)*D^(1-epsilon). On the reduced chart X3=E-X1-X2, exact Cayley–Menger algebra gives D=E(E-2X1)(E-2X2)(2X1+2X2-E)/16. Its prefactor kappa0/E consequently has local order E^(-epsilon) under the stated generic/branch conditions, not automatically a simple pole.

Exact internal Gram degeneration gives K|E0=-B^2/144 and a transverse positivity identity. Real nonnegative-volume limiting support is restricted to B=0; generic fixed-coordinate coefficient asymptotics do not control its integration.

Continuing along this reduced family and continuing energies with spatial invariants fixed are different source parameter maps. The latter keeps D fixed. Their physical choice and the printed normalization are now explicit owner-input gates; no period asymptotic or physical continuation is inferred from these polynomial checks.

## Conditional transverse-density result

`triangle-transverse-density.md` retains the actual product y_e dy_e measure and derives the local coordinate C=sqrt(H F)z. The positive Jacobian is sqrt(H F)/(16a^2), and K=H F(1-z^2)/(576a^2). With the literal printed normalization, the combined H power is exactly1, leaving H/E rather than the fixed-coordinate E^(-epsilon) estimate. Exact derivative/exponent checks pass.

For the candidate real representative, all remaining source denominators are positive on the limiting noncollinear stratum. On compact patches F>0, a written dominated-convergence proof at fixed Re(epsilon)>-1/2 gives a finite local period limit with an explicit beta factor. Thus this patch cannot supply a1/E divergence under those hypotheses. This is neither the full physical period nor a proof of meromorphicity, cycle transport or regulator removal.

## Execution and handoff

The collinear audit in `triangle-collinear-obstruction.md` now identifies paired denominator collisions: q3/q23 on0<x<a and q3/q31 on-b<x<0. The E0-first density has nonzero leading order w^(epsilon-2), requiring Re(epsilon)>1 for absolute integrability on compact interior x intervals. This prevents extending the regular-patch dominated-convergence argument toward epsilon0 without additional control; it does not disprove regularized periods. Fifty-four exact rational leading-jet fixtures pass.

The joint scaling in `triangle-joint-profile.md` now derives E^2 A_E→W on0<x<a away from its singularity. Its denominator D3=A+B*lambda-2sqrt(A B lambda)z vanishes at lambda=A/B,z=1. The limiting coefficient profile is absolutely integrable for0<Re(epsilon)<1 and matches the previous large-lambda collinear coefficient. The joint-profile calculation alone gives the formal density power E^(epsilon-1), not an integrated asymptotic. Exact checks pass27 collision/overlap and144 additional jet fixtures.

`triangle-moving-collision-limit.md` now proves a conditional localized integrated limit: E^(1-epsilon) P_chi(E) converges to the source-derived profile pairing for0<Re(epsilon)<1. Exact finite-E geometry locates w_star=v^2(a-x)^2/d^2,z=1; recentering yields a uniform integrable majorant controlling the moving collision and rescaled tail. The boundary functional depends only on chi(x,0) and is nonzero for positive boundary tests at real regulator in the strip. The proof is written analysis;24 exact center and480 height/Heron fixtures verify its geometric arithmetic.

`triangle-regulator-coefficient.md` now extracts the local profile divergence I_x(epsilon)=pi/[2a(x+b)epsilon]+O(1), uniformly on compact0<x<a. Fresh inspection of the printed normalization gives C(d)/epsilon→16/9 and L/epsilon→1/(6a), producing the finite sequential coefficient (4pi*b*(a+b)/3) integral chi(x,0)/(x+b) dx. Exact checks cover27 coefficient fixtures and162 completed-square identities. This takes the E^(1-epsilon)-normalized energy limit FIRST; it does not identify a regulator-first residue. At fixed positive epsilon, E*P_chi instead tends to zero.

`triangle-limit-order.md` now derives the regulator-first finite-E observable independently, retaining all six terms at the exact collision. Its local Mellin coefficient is2pi*s_c*t_c/d; keeping the finite-E angular term is essential. The same observable E*P_chi has iterated limits B_chi=(4pi*b*(a+b)/3) integral chi(x,0)/(x+b) dx when the regulator is removed first, and0 when E is taken first. Thus positive boundary tests give a genuine local completion-order obstruction under the stated candidate-representative assumptions. Twenty-four exact finite-E and nine limiting-coefficient fixtures pass; analytic arguments remain written proofs.

`triangle-joint-corner.md` now supplies the missing uniform argument: recentered coefficients extend smoothly to E0, the local Mellin remainder is uniform, and the complementary tail has a regulator-uniform bound. Consequently E^(1-epsilon)P_chi=B_chi+O(E+epsilon) for small positive parameters. Along epsilon*log(E_ref/E)→c, the same E*P_chi tends to exp(-c)B_chi, realizing the full interval from0 toB_chi for positive boundary tests. This is a written conditional local theorem, not a conclusion from iterated limits or a machine-formalized analytic proof. `check_triangle_pilot_closure.py` reruns all seven exact-checker dependencies.

The local completion must retain this corner parameter or use a source-prescribed approach; no desired value is selected by fiat. After the independent measure challenge and versioned-source comparison, the dictionary and compact-patch test are now supplied. The Cartesian pole check is now independently confirmed and frozen. The next priority is the physical readout contract: inspect explicit source finite-observable/subtraction constructions to distinguish a regulated period, pole coefficient, finite part, normalized pole or finite combination. If finite-part transport is intended, retain the regulator first jet and the normalization second coefficient. Further opposite-interval, endpoint and infinity calculations are deferred rather than treated as the most productive next step. The physical source parameter map, normalization and regulator/energy approach remain active owner-evidence gates; this result is not the global physical period or an amplitude identification.

Source-owner request to marici.Benincasa, copied as a coordination request to marici.Nima: identify the source-derived continuation/relative chain specialization, twist/normalization regime, endpoint datum and actual topology, or confirm which are still open in the intended source packet. Cite source locations or admitted results rather than propose a target-defined functional. No owner artifact edits requested. Source-owner reply/adoption is not presumed.

The owner-input branch is active alongside local analysis. Failure of naive interchange is branch-local and does not terminate the project programme.
