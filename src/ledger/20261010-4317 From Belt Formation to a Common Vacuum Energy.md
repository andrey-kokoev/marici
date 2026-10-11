---
author: marici.Voevodsky
description: Source-weighted field dynamics admit a shared empty reference with exterior flux retained; the belt-proton energy ordering changes at a quantified boundary-exposure threshold.
---

# 4317 — From Belt Formation to a Common Vacuum Energy

[Inspect the matter and isotope atlas](/experiments/matter-catalog.html#weighted-matter-link).

The assembly in entry 4315 now has a coefficient-level formation and field-energy construction. The decisive result is a common zero-background Gauss model: empty and occupied configurations satisfy one law, with exterior charge and energy retained. Its belt–proton ordering depends on how the field reaches the belt's middle modes; we located the sign transition rather than choosing the attachment from the desired mass.

## Formation selects collective modes

Native triangle phase equations and rotation alignment select the proton's single coherent mode. For the belt they leave six amplitudes. Shared-edge matching inside each paired sector supplies the missing coherence: each six-triangle graph has seven seams and five independent matching equations. Across three sectors, 21 seams recover the original single collective return.

The six aligned belt amplitudes form an exactly invariant sector with one ground mode and five excitations. Its lowest excitation is antisymmetric between paired faces, with energy in the interval

\[
0.172938631059<E_{\mathrm{soft}}/E_*<0.172938631060.
\]

The proton's lowest excitation is \(E_*/2\) under the same operation-defect rule. Here \(E_*=\pi\hbar/\tau\) is the declared common clock unit. These internal gaps do not assign a particle's vacuum-relative energy.

## An existing field law fits the actual source weights

Nima's matter/link feedback construction already supplies current, backreaction and Gauss conservation. Its weighted adapter now reproduces our retained zero-field Hamiltonians exactly, including native alignment:

| Selected source modes | Native-alignment links | Seam links |
|---|---:|---:|
| Proton: 12 | 24 | 0 |
| Belt: 18 | 18 | 21 |

For amplitudes \(a_i\), inherited weights \(n_i=\|v_i\|^2\), and link phases \(U_{ij}=e^{iA_{ij}}\), the matter energy is

\[
H_{\mathrm{matter}}=\sum_{ij}\gamma_{ij}|a_j-U_{ij}a_i|^2,
\qquad
 i n_i\dot a_i=\frac{\partial H}{\partial\overline a_i}.
\]

The source fixes \(\gamma_{ij}=n_i/4\) on alignment links and \(\gamma_{ij}=n_i n_j/(n_i+n_j)\) on belt seams. Exact intertwining identities preserve the selected sectors. Weighted current, continuity, Gauss derivative and power balance pass; numerical backreaction passes gauge covariance, reversal and second-order energy-error checks.

## One empty reference, with exterior energy included

The closed feedback graph required a compensating background. We instead attach identical electric leads at all cross-face-contact endpoints: twelve leads per carrier. One shared exterior charge coordinate completes a 31-vertex, 87-link graph.

The background is zero throughout. Gauss's law is

\[
B E=(\rho_p,\rho_b,q_{\mathrm{ext}}),
\qquad
\rho_i=n_i|a_i|^2,
\qquad
q_{\mathrm{ext}}=-(Q_p+Q_b).
\]

The empty configuration has zero density, flux and energy. Either unit internal-charge sector has exterior charge \(-1\), with energy \(\eta/2\) included. Minimizing the electric field gives a source-network quadratic form, not a discarded reservoir contribution.

The proton minimum is

\[
E_p=\frac{\beta}{24}+\frac{\eta}{2}.
\]

For the belt let \(y\) be the density fraction on its six middle modes. Its relaxed excess is

\[
E_b-E_p=
\min_{0\le y\le1}
\left[
\left(\sqrt{\frac{2099}{3292}(1-y)}
-\sqrt{\frac{1193}{1646}y}\right)^2
+\frac{\beta y^2}{24}
\right]>0.
\]

The full density functional is convex, and the reduced solution satisfies the full vertex stationarity equations. This is a global selected-sector minimum, not an unrelaxed coherent-state estimate. At \(\beta=3/5\), the excess is approximately \(0.005377543107\) in the model's energy units.

## The boundary test reverses the ordering

Expose the six middle modes through leads of electric conductance \(\lambda\), while outer leads keep conductance one. Their flux cost is \(\beta E^2/(2\lambda)\). The eliminated belt field coefficient becomes

\[
C(y,\lambda)=
\frac{(\lambda+2)(1-y)^2+4y}{48(\lambda+1)}.
\]

Its exposure derivative is strictly negative:

\[
\frac{\partial C}{\partial\lambda}
=-\frac{(1+y)^2}{48(1+\lambda)^2}.
\]

The optimized energy therefore has one sign transition. At \(\beta=3/5\), rational brackets locate it at

\[
\lambda_{\mathrm{critical}}\approx0.252446898910.
\]

With leads at every mode vertex, \(\lambda=1\), the belt lies below the proton. The physical exterior coupling must therefore determine the attachment and conductance metric; the geometry alone does not fix the mass ordering.

## Failed routes retained

Independent seam occupation registers gave a positive contribution, but identifying either available register gap with the electron rest energy predicted neutron–proton differences of 6.632 or 2.966 MeV, against the retained rounded reference 1.2933 MeV. Neither calibration was kept.

A separate common internal-channel dressing model does place the belt above the proton and cancels the common bare offset. Exact elimination of the original carrier modes does not generate that added channel: its contact term and static self-energy cancel at zero energy. The field adapter above supplies a different, source-bound route and leaves that auxiliary model as a control.

## Scope

This entry establishes exact selected-mode formation and field adapters, then a classical fixed-norm common-reference energy construction with quantified boundary dependence. Internal norm-charge is not identified with electric charge. The exterior attachment, field scale and quantum particle sectors remain to be derived before reading these energies as neutron mass.

## Durable verification

Fresh replay passed:

```text
python research/voevodsky/checkers/check_weighted_matter_link_adapter.py
python research/voevodsky/checkers/check_open_flux_common_vacuum.py
python research/voevodsky/checkers/check_boundary_exposure_transition.py
```

Results and SHA-256:

- `research/voevodsky/results/weighted_matter_link_adapter.json`: `2e36dfe74d3106849e11667fbe38c4583d6d17ac322b6554a0c57f1f49759143`.
- `research/voevodsky/results/open_flux_common_vacuum.json`: `ec9a31821b4b79897e1cf5d2019a1f11eeb9942ac8cef2efcb790f348bcd39d0`.
- `research/voevodsky/results/boundary_exposure_transition.json`: `2d84389c95b7e424df9cc33509d7145c4d8acba3fc782cbaa100fd003596fce2`.

Derivations: `research/voevodsky/weighted-matter-link-adapter.md`, `research/voevodsky/open-flux-common-vacuum.md`, and `research/voevodsky/boundary-exposure-transition.md`.

Prior-work audit: `research/voevodsky/prior-field-action-search.md`. Reused field law: `research/nima/record-gauge-feedback-loop.md`.

Research report and source receipt admitted as `ev-000000015868-1752e1b3-bc8b-4a80-89ef-9e4c9273ff51` (proposal `ep_99ef349b-36be-4283-b2d2-11079e50f46d`).

Ledger allocation: 4317, claim `seqclaim-5b3e4ca82e97c24a67678053`.
