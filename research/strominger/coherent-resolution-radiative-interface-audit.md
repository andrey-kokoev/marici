# Coherent Resolution to radiative phase space: typed interface audit

## Disposition

**Obstructed at named missing arrows.** The source defines a Coherent **Construction** Law and enough combinatorics to reconstruct a candidate cellular resolution, but it does not define a complete Coherent Resolution chain complex, its admissible quotient, or a map from that complex to radiative phase space. Consequently no CR cycle, boundary, or secondary class currently descends to a soft charge, flux, or memory observable.

## 1. Exact meaning and authority of CR

The authoritative local source is `research/nima/coherent-construction-bridge-atlas.md`. It defines

\[
\Gamma_n=\sum_{h\in\mathcal H_n}\epsilon_h\mathcal C_h,
\qquad \Phi_Z(C)=CZ,
\qquad
\Omega_{n,2,4}=\sum_h\epsilon_h(\Phi_Z)_*\omega_{\mathcal C_h}.
\]

This is called the **Coherent Construction Law**, not a Coherent Resolution. The maximal resolution recoverable without adding unsupported structure is:

- degree 0: history cells / positive-root intervals;
- degree 1: endpoint covers and cluster flips;
- degree 2: commuting squares and associahedral pentagons;
- candidate differentials: cellular boundaries and, on interval functions, the Möbius operator
  \(\Box_d=\Delta_u\Delta_v\);
- filtrations: external cutoff `n`, root interval length, and the AF/Wedderburn shell tower.

The source does not give one graded complex containing all these objects, signs for all boundary maps, a proof that square/pentagon relations are null in the physically weighted canonical-form complex, compatible homotopies, or an admissible quotient. The amplituhedron pushforward and selected-center radial map are candidates, but the latter explicitly changes multiplication.

## 2. Required radiative target

A typed target would have to declare at least:

\[
\Gamma_{\rm rad}=\{C_{AB}(u,z,\bar z),\;N_{AB}=\partial_uC_{AB}\}/\text{gauge},
\]

Bondi cuts `u=const`, helicity polarization, sphere smearing `f(z,\bar z)` or `Y^A`, and the radiative symplectic pairing (up to the frozen convention)

\[
\Omega_{\mathcal I^+}(\delta_1C,\delta_2C)
\propto
\int_{\mathcal I^+}du\,d^2z\,
(\delta_1C^{AB}\delta_2N_{AB}-\delta_2C^{AB}\delta_1N_{AB}).
\]

It must also fix BMS charge normalization and a frequency transform with an `omega -> 0` prescription. These fields are absent from the CR source.

## 3. Arrow-by-arrow audit

| Proposed arrow | Disposition | Named obstruction |
|---|---|---|
| CR generators -> shear/news modes | obstructed | no history/root/flip-to-`C_AB,N_AB` map or helicity assignment |
| CR differential -> charge flux | obstructed | no chain identity `F d_CR = d_BMS F`, Bondi cuts, or normalization |
| CR cycles -> leading/subleading soft charges | obstructed | no `omega -> 0` limit, smearing field, or hard-leg Ward action |
| CR boundaries -> gauge equivalence | obstructed | no proof that square/pentagon or Möbius-exact data map to Bondi gauge directions |
| CR secondary classes -> memory | obstructed | no transgression to `Delta C_AB`, integrated news, or spin-memory contour |
| canonical weights -> radiative symplectic form | naive map falsified | tested kernel is non-Hermitian and non-normal; its linear scalar weights cannot equal an antisymmetric phase-space two-form |

Thus descent cannot merely be unproved at the last step: the generator map needed to state descent is missing.

## 4. Kernel/image and quotient treatment

The NNMHV source exactly shows that insertion changes a rank-one transport image to the newly inserted null-edge spinor, while reflow varies the kernel line at fixed image. This is genuine kernel/image data in projective matrix transport. It is not yet the radical or gauge kernel of `Omega_{I+}`. No source map sends these lines to the zero-frequency soft radical, Bondi gauge orbits, or a hard-radiative quotient.

Accordingly:

- insertion/reflow do not induce leading/subleading soft factors;
- simple-root updates do not define normalized BMS charge flux;
- their integrated cutoff relation is not a memory observable;
- history order, cutoff `n`, and deformation `t` remain combinatorial/refinement parameters, not physical time.

## 5. Exact residual and independence checks

The boundary update changes the signed exchange residual by

\[
-\frac{16831310196814032984532666}
{13806319031175469878522007124844375}\ne0.
\]

This residual is independent of any radiative interpretation and remains a cluster-weight defect. Calling it flux would require the missing typed arrow and normalization, not a relabeling.

The audit separately checks that history order is not Bondi time, `t` is not Bondi time, `n` is not a Bondi cut, the exchange defect is not a BMS flux, and the two-channel split is not radiative polarization.

## 6. Minimal repair contract

A future bridge must supply a map `F` on generators and verify:

1. `F d_CR = d_rad F` with explicit signs;
2. invariance under square/pentagon homotopies;
3. descent through the declared CR quotient and Bondi gauge quotient;
4. compatibility with `Omega_{I+}`;
5. a normalized `omega -> 0` limit producing the leading or subleading Ward action;
6. an integrated cut-to-cut identity equal to a named memory observable.

Until then every proposed bridge is obstructed, except the naive canonical-weight/symplectic identification, which is falsified.

## Evidence

- `research/strominger/checkers/coherent_resolution_radiative_interface_audit.py`
- `research/strominger/results/coherent_resolution_radiative_interface_audit.json`
- `research/nima/coherent-construction-bridge-atlas.md`
- `research/strominger/soft-bms-memory-conventions.md`
- `research/strominger/subleading-triangle-conventions.md`
