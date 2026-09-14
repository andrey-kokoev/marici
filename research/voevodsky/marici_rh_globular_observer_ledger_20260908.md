# RH globular observer ledger

Date: 2026-09-08

## Purpose

This ledger retypes the current Marici/RH constructions according to Nima's observer-tower rules. It prevents parallel observer lists, target rank, higher coherence, diagnostics, positivity, and completion from being conflated.

## Six nodes

1. **Global source node** — the restricted-product theta/Tate preparation.
2. **Theta source node** — the completed packet `(C,U,V)`, its full Fourier history, and `xi=C+U+V`.
3. **Relative-null node** — the derived zero fiber of `xi`, retaining `A=U-V`.
4. **Completed sewing node** — global Fourier–Poisson sewing before diagnostic cutoff.
5. **Endpoint/conductor node** — the six `D_k`, 24 framed source maps, conductor residue, and P24 diagnostics.
6. **Green/work node** — the Hermitian response, positive bulk, and boundary-work defect.

These are different objects. Equal scalar coordinates or matching dimensions do not identify them.

## Rungs

### Rung 0: source incidences and observations

Established:

- global source to theta packet;
- Xi relative-null fiber;
- algebraically faithful full Fourier observer on the translated-theta source;
- 24 local framed maps into six endpoint targets;
- the source-current identity on the Green response.

Open or restricted:

- one common-source incidence from the global theta source to the endpoint/conductor source;
- a common completed domain with uniform observer margin;
- independent positive-cone admission.

### Rung 1: comparisons of observations

Established:

- global Fourier sewing before cutoff;
- the bordered Xi/endpoint incidence at target level.

Falsified:

- strict finite-cutoff Fourier Beck–Chevalley; its leakage has rank one.

### Rung 2: coherence of comparison paths

Established only diagnostically:

- the endpoint P24 class detects a nontrivial endpoint translation.

Missing:

- a completed coherence cell comparing the relative-null route with the endpoint-observer route.

### Rung 3: promotion back to the RH parent problem

Missing:

- a source-authorized promotion identifying the boundary of the completed coherence cell with the Green boundary-work defect `D_bw`.

Without this promotion, P24 and six-normal residuals diagnose the endpoint child tower but do not constrain the parent theta-zero state.

## Residual discipline

| Residual | Required action |
|---|---|
| presentation redundancy | quotient |
| observer invisibility | prove joint faithfulness |
| local transition anomaly | trivialize before descent |
| arithmetic approximation | bound and converge |
| substantive Green residual | preserve and prove positive |

The finite Fourier leakage is a transition/approximation cell, not presentation gauge and not itself a zeta zero. The P24 class is a diagnostic coherence residual, not a null equation. The Green residual is the signal needed for confinement and must not be discarded in the name of coherence.

## Current frontier

SCC compilation order corrects the earlier two-step frontier. The first missing typed object is a source-authorized map from the frozen global theta/Tate preparation to the marked endpoint/conormal preparation, together with a joint-acquisition capability for theta/Fourier and endpoint observers on that same preparation.

Its acceptance test is:

1. all endpoint ports are typed on the same preparation as the theta observer;
2. the map commutes with the established theta and endpoint restrictions;
3. each component has a source evidence locator independent of target-rank data.

The common completion domain, relative-null/endpoint coherence, and boundary-work promotion are downstream. Higher-rung cells cannot repair the missing level-zero leg.

## Machine audit

```sh
python research/voevodsky/check_marici_rh_globular_observer_ledger_20260908.py \
  --output research/voevodsky/marici_rh_globular_observer_ledger_certificate_20260908.json
```

The checker validates six nodes, fourteen cells, globular boundary levels, residual dispositions, and the two-item active frontier in 56 assertions.
