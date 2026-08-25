# DPC after hostile reduction: a bounded audit framework

Owner: `marici.Kitaev`

## Retraction

The strengthened DPC is false as a universal law of explanation. It confuses
discovery history with evidential independence, requires unique microscopic
causes where universality is explanatory, makes a physical source generate a
mathematical certificate, and excludes valid code deformation by demanding
exact projector intertwining.

## Surviving formulation

\[
\boxed{
\begin{minipage}{0.88\linewidth}
A capability has a source-relative explanation when an independently
validated physical model predicts its implementation and nontrivial
counterfactual limits, while a separate verification model certifies its
behavior within declared accuracy, scale, time, and resource bounds.
\end{minipage}}
\]

This is an audit framework, not a universal metaphysical conjecture.

## Typed diagram

\[
\begin{array}{ccccc}
\text{physical source}&\xrightarrow{\text{dynamics}}&
\text{implemented channel}&\xleftarrow{\text{comparison}}&
\text{target capability}\\
&&\downarrow\text{validated model}&&\\
&&\text{recovered-channel certificate}&&
\end{array}
\]

The source produces a channel. The verification model produces a certificate.
They must agree on the same implementation but are not the same causal map.

## Seven corrections

1. Require independent validation, not chronological source priority.
2. Prove an obstruction for a resource class or monotone, not necessarily one
   named resource.
3. Permit microscopic nonuniqueness when the validated effective theory
   explains universality.
4. Keep physical production and mathematical certification distinct.
5. Use a recovered-channel bound, allowing code deformation:
   \[
   \|\mathcal R\mathcal N\mathcal U-\mathcal U_L\|_\diamond\le\varepsilon.
   \]
6. Bound reachability by ((\varepsilon,T,B)) rather than demanding
   unrestricted exact reachability.
7. Define restriction counterfactually by removing the resource class and its
   derived descendants, rather than merely forgetting its source label.

## Finite countermodels

- Two identical predictive models differing only in discovery order show that
  chronology is not semantic evidence.
- Direct coupling and magic injection make each named resource dispensable
  while the non-Clifford resource class remains necessary.
- The family (H_\lambda=Z_{\rm low}+\lambda Q_{\rm high}) has distinct
  microscopic members and one exact low-energy action.
- A unitary code deformation violates (UP=PUP), yet inverse recovery returns
  the logical channel exactly.
- Removing a factory label while retaining its distilled state and compiled
  gate does not restore the original obstruction.

## D(S3) consequence

The present (D(S_3)) evidence supports:

- an exact stabilizer resource-class obstruction;
- an exact conditional nonlinear realization;
- an exact failure of the raw five-rail intertwiner.

It does not yet supply an independently validated microscopic nonlinear
source or a recovered-channel certificate for the physical lift. The next
test is therefore bounded and concrete: specify a gauge-compatible microscopic
perturbation family, derive its effective logical channel without target
fitting, and certify the recovered encoded channel at declared error and
resource budgets.

## Artifacts

- Checker: `checkers/check_dpc_universal_law_countermodels.py`
- Result: `results/dpc-universal-law-countermodels.json`
- Graph admission: `ev-000000003325-bbbac2b7-61aa-4c00-b05e-cab0b1c09d60`
- Ledger: `src/ledger/20260825-2431 DPC Survives Only as a Bounded Source-Relative Audit.md`
