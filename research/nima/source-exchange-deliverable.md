# Source-to-exchange deliverable: conditional chain, explicit remaining gates

## Verdict after ten iterations

The immediate adapter exists as an executable CONDITIONAL source-labelled
experiment. The stronger objective of deriving the selected physical instrument
and its absolute coupling from the native source remains open. No passing test
in this packet is permission to promote that stronger claim.

The concrete chain is

    actual shared-leg matrices and comparison witnesses
      -> declared trace-to-quadrature preparation
      -> boundary-validated addressed exchange events
      ->16 conserved anchors +137 mismatches, covariance and history
      -> conditional oscillator/homodyne measurement.

The adapter retains original source matrices, reference, witness chains and
preparation gain. Its independent record memory is an explicit instrument
attachment, not a relabelled native composite value.

## Deliverables and evidence

| Component | Implementation / account |
|---|---|
| Reusable compiler | `checkers/labelled_exchange_experiment.py` |
| Native state through detector | [End-to-end audit](source-exchange-end-to-end-audit.md) |
| Physical preparation/readout assumptions | [Oscillator instrument](exchange-oscillator-preparation-and-measurement.md) |
| Calibration and phase/loss hostiles | [Detector contract](exchange-detector-calibration-and-identifiability.md) |
| Reset and energy accounting | [Resource ledger](exchange-preparation-reset-resource-ledger.md) |
| Consolidated acceptance and test design | `checkers/check_source_exchange_deliverable.py` |

The final checker freshly executes the resource audit, which freshly executes
the end-to-end audit and all eight supporting checkers. Source witness and
matrix calculations use exact rational arithmetic where specified; numerical
exchange, covariance and detector checks use tolerance1e-10.

## Five success criteria, without weakening their meaning

1. **State:** a specific map from actual matrix responses to prepared record
   quadratures is checked. It requires a declared trace readout, preparation
   gain, vacuum carrier and independently attached record modes. It is not a
   faithful replacement of all native source data; provenance remains retained.
2. **Operation:** witness boundaries, addressed event concatenation and tested
   reference relabelling commute with the adapter. Native shared-leg operator
   factorization is rejected by all109 rooted rectangle tests. The adapter is
   deliberately not advertised as that stronger compositional representation.
3. **Observable:** coherent preparation, difference-mode pulse and phase-referenced
   quadrature readout have explicit Hamiltonian and detector contracts. Standard
   bosonic mechanics and its measurement rule are supplied, not source-derived.
4. **Normalization:** calibrated detector parameters and a chosen preparation
   scale are separated from1/137. The relative share does not fix an absolute
   coupling; it even occurs in raw vacuum mismatch variances. Physical standards,
   source-selected gain and a current/field action remain missing.
5. **Discriminator:** signed two-pulse echo and first-port rectangle distinguish
   specified coherent alternatives under a stable, independently monitored phase
   reference. Phase jumps and loss/preparation ambiguity are explicit controls.

## Finite-sample falsifying tests

The last iteration adds a conservative statistical design using the actual
native-seeded detector moments. This is an analytic conditional bound, not
experimental validation or a fitted confidence claim.

Let M=E[y_reference]-b>0, and let v denote the variances from the declared detector
model. Assume independent, identically prepared shots and independent dark and
reference batches, with fixed phase/gain statistics and no unmodelled drift.

For the echo, use D=mean(signal)-mean(dark). Its expectation is +M or -M for
exchange and quarter-turn. With n shots in each batch, Chebyshev gives

    P(wrong sign) <= (max(v_exchange,v_quarter_turn)+v_dark)/(n*M^2).

For the rectangle, use

    D=mean(signal)-(mean(reference)+mean(dark))/2.

Its expectation is -M/2 for exchange and +M/2 for the flat-identity alternative.
With n shots in each independent batch,

    P(wrong sign) <= [4*max(v_rectangle,v_reference)+v_reference+v_dark]/(n*M^2).

At the DECLARED fixture parameters,638 shots per signal/dark batch for echo,
and3138 shots per signal/reference/dark batch for rectangle, bound the error
by.001 per test under either specified hypothesis. These are not familywise
bounds or guarantees against parameter misspecification. In particular a pi
phase-reference jump still defeats the echo discrimination assumption. Each
shot must satisfy the full preparation/reset contract; record-only reset fails.

## What has been ruled out

- Identifying the old exchange mean law with the new family-mean relaxation.
- Treating all current shared-leg trace composites as exchange-closed records.
- Treating native boundary-response witnesses as freely writable amplitudes.
- Factoring the137 exchanges through invertible shared primitive-leg operators
  on the same state space.
- Inferring interaction strength from a normalized variance fraction.
- Calling record-only reset a fresh zero-carrier preparation, or calling ideal
  exchange energy conservation a complete apparatus resource budget.

Each obstruction has a bounded stated scope. Nonlinear readouts, enlarged
intermediate state spaces, other source representations and higher transported
witness actions have not been globally excluded.

## Remaining constructor, not another generic feedback law

To advance the stronger objective, supply an independently justified native
source-to-instrument action, or a concrete calibrated apparatus contract, that
selects the attached memory, preparation gain, addressed pulse and phase standard.
A physical coupling claim additionally needs a charge/current observable and its
field action with independently fixed kinetic/interaction normalization.

The conditional compiler can then test that input against its existing state,
composition, reference, measurement and resource hostiles. It cannot select its
own assumptions simply by passing them. Another abstract feedback proposal or
normalization by137 would not close this gate.

## Reproduction

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_source_exchange_deliverable.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-source-exchange-deliverable

Machine acceptance: `results/source-exchange-deliverable.json`. It explicitly
sets `objective_complete` to false while marking the bounded conditional tests
passed. No experimental data or absolute electromagnetic constant is claimed.
