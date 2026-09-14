# One endpoint probe reduces the augmented core problem to the bulk

## Input

The source identity fixes the heat-remainder endpoint coefficient as

\[
\alpha_h=e^{h/4}-1>0.
\]

The minimal endpoint graph completion is

\[
\mathcal H_E
\cong
\mathcal H_{\mathrm{ord}}
\oplus
\mathbb C_E.
\]

Every odd heat probe has zero endpoint coordinate, so its closure lies in the first summand.

## Core reduction theorem

Let \(\mathcal V_{\mathrm{odd}}\) be the odd heat-polynomial probe space and let \(e_E=(0,1)\) be the pure endpoint vector. Define

\[
\mathcal V_E
=
\mathcal V_{\mathrm{odd}}
+
\mathbb C e_E.
\]

Then

\[
\overline{\mathcal V_E}^{\mathcal H_E}
=
\mathcal H_E
\]

if and only if

\[
\overline{\mathcal V_{\mathrm{odd}}}^{\mathcal H_{\mathrm{ord}}}
=
\mathcal H_{\mathrm{ord}}.
\]

Indeed, the two summands are independent. Odd probes can approximate only the bulk coordinate, while \(e_E\) spans the entire endpoint coordinate. One endpoint probe is both necessary and sufficient to repair this particular codimension-one defect.

## Positivity reduction

For a split form

\[
q_E(f,z)
=
q_{\mathrm{bulk}}(f)
+
\alpha_h|z|^2,
\]

endpoint positivity is automatic because \(\alpha_h>0\). Therefore

\[
q_E\geq0
\]

if and only if

\[
q_{\mathrm{bulk}}\geq0.
\]

The endpoint sector is now correctly retained and no longer invisible, but it contributes no missing positivity to the bulk.

## Möbius interpretation

The decomposition has the same operational shape as the channel-bundle splitting:

- the endpoint vector is a globally retained invariant coordinate;
- odd transverse probes occupy the sign-changing sector;
- deleting the invariant coordinate loses information;
- adjoining it repairs typing but does not prove transverse positivity.

This is an analogy of decompositions, not an identification of the analytic graph carrier with the topological Möbius bundle.

## Disposition

The endpoint-blindness gate is repaired by a minimal one-dimensional augmentation. The remaining analytic question is now cleanly isolated:

> Are odd heat-polynomial probes a graph-norm form core for the closable gamma-plus-prime bulk form on \(\mathcal H_{\mathrm{ord}}\)?

That question requires a common closable bulk form and differentiated tail estimates; ordinary Schwartz or \(L^2\) density is insufficient.

## Verification

```text
python research/voevodsky/checkers/check_endpoint_augmented_odd_core_reduction.py
```

The checker verifies the direct-sum rank statement in bulk dimensions one through eight and the split positivity equivalence.

Artifacts:

- `research/voevodsky/checkers/check_endpoint_augmented_odd_core_reduction.py`
- `research/voevodsky/results/endpoint_augmented_odd_core_reduction.json`
