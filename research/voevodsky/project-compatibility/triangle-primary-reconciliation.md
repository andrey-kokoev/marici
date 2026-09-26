# Versioned primary-source reconciliation of the measure challenge

## What was retrieved and checked

Retrieved the actual source archives for arXiv:2402.06558v1 and v3, the work cited by our triangle source for the loop measure. Also compared the v3 HTML rendering with the raw TeX. The archive, raw-TeX and HTML hashes are recorded in `triangle-primary-versions.json`; this is not a claim about an unpinned latest revision.

Primary locations in v3 `IR_Divs.tex`:

- lines1073–1093, eq:(3.3): one-loop Gram-measure derivation;
- lines1168–1180, label `eq:Ndne`, eq:(3.11): specific one-loop coefficient;
- lines1262–1269, label `eq:cL`: general-loop coefficient;
- lines4411–4431, label `eq:3s1lInt`, eq:(A.12): explicit triangle integral.

The corresponding v1 one-loop coefficient is at lines1166–1179 under the same `eq:Ndne` label.

URLs: https://arxiv.org/src/2402.06558v1 and https://arxiv.org/src/2402.06558v3 . No owner files or downloaded source formulas were edited.

## The independent challenge is corroborated by a versioned change

The v1 specific coefficient contains

    Vol(external simplex) / Gamma((d-n_e)/2).

The v3 specific ONE-LOOP coefficient instead contains

    Vol(external simplex)^(-1) / Gamma((d-n_e+1)/2).

For three edges and d=3+2epsilon this changes BOTH suspicious features:

- positive external volume becomes inverse external volume;
- Gamma(epsilon) becomes Gamma(epsilon+1/2).

Combining the revised coefficient with the unchanged volume-ratio exponent gives D^(-epsilon) K^(-1/2+epsilon), matching the independent Euclidean Jacobian's external-volume and regulator structure. Its inverse Gamma factor is nonzero at epsilon0.

Thus these are not merely adjustments invented to rescue our calculation. They occur in a later version of the cited primary derivation. We do not infer an author's stated reason or an official erratum from the observed edits alone.

## But the revised source is not internally reconciled

The same v3 document's general-loop coefficient still has Gamma((d-n_s_l-L+l)/2), which gives Gamma(epsilon) for this one-loop triangle. It DOES use inverse external volume. The explicit triangle appendix(A.12) likewise prints Gamma((d-3)/2)=Gamma(epsilon).

Therefore selecting the revised one-loop equation while ignoring the triangle appendix would hide a genuine source conflict. The independent Cartesian Jacobian supports the revised specific one-loop regulator structure, but the printed formulas are not interchangeable as exact normalized definitions.

| Formula | External D power in triangle density | Gamma denominator at d=3+2epsilon |
| --- | --- | --- |
| Primary v1 specific one-loop | 1-epsilon | Gamma(epsilon) |
| Primary v3 specific one-loop(3.11) | -epsilon | Gamma(epsilon+1/2) |
| Primary v3 general formula at L1 | -epsilon | Gamma(epsilon) |
| Primary v3 triangle appendix(A.12) | -epsilon | Gamma(epsilon) |
| Our frozen2408.16386 printed formula | 1-epsilon | Gamma(epsilon) |
| Independent Euclidean measure | -epsilon | Gamma(epsilon+1/2) |

These exponents are insensitive to nonzero dimension-only normalization factors.

## Absolute constants remain a separate gate

If all Vol symbols are interpreted as the same ordinary Euclidean volumes D,K, the revised one-loop coefficient is16/sqrt(pi) times our Cartesian coefficient. This is an external-kinematics-independent discrepancy, unlike the previous extra D factor.

However, the primary text also writes Gram/CM/volume identities without all ordinary Euclidean factors: the raw tetrahedral CM determinant is288K=8 det(Gram), while the text's equations(3.6), (3.8), and(A.10) do not uniformly display those factors. Some prose explicitly says proportionality. It would be unsafe to declare the absolute normalization solved by choosing one displayed equality in isolation.

The structural agreement is established; the literal absolute-normalization dictionary is not. Dimension-only constants cannot reinstate the missing simple zero unless one adds a vanishing or singular regulator-dependent normalization, which would itself require explicit justification.

## Consequence for the earlier local corner result

The prior local theorem remains a theorem for its explicitly specified printed family. Its finite regulator cancellation depended on1/Gamma(epsilon). That cancellation cannot simply be transferred to the revised specific one-loop measure.

Under a common ordinary-volume dictionary, replacing only the measure in the same local candidate integral gives the exact ratio

    mu_old / mu_v3_one_loop
       = (D/3) Gamma(epsilon+1/2)/Gamma(epsilon).

For fixed positive E and hence D>0, this ratio has a simple zero at epsilon0. Thus the old family's finite positive regulator limit corresponds to a regulator pole in the replaced local family, not the same finite observable. This is a diagnostic comparison, NOT an identification of that replacement with the physical continued triangle period.

The primary-source audit therefore strengthens the decision to suspend physical promotion. It also narrows the task: reconcile explicit source definitions and their normalization map, rather than treating an arbitrary completion-order choice as the first missing ingredient.

## Next discriminating work

Freeze a transparent Gram/CM/Euclidean-volume dictionary and compare the specific one-loop derivation with the appendix using a compact nonsingular loop patch. Request the intended convention or correction with exact equation references. Do not silently patch the frozen pilot or proclaim an author's intent from a later formula.

Only after specifying which normalized source object the pilot denotes should its regulator removal and boundary readout be recomputed. Physical analytic continuation, chain transport and the other boundary strata remain open, but they are downstream of this identification.

## Verification boundary

`check_triangle_primary_versions.py` checks the actual raw-TeX volume inversion, Gamma-argument change, and conflicting v3 appendix/general formulas; it also checks homogeneity and the conditional constant ratio algebra. `triangle-primary-versions.json` freezes all source snapshots. These checks establish what the files say, not an author's intended normalization or a physical continuation theorem.
