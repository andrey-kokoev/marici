# Four-state acquisition calibration gate: WP1077

## Question

Can a four-state acquisition distinguish background, luminosity, gain,
visibility, and momentum-scale hostiles in one frame?

## External source

This packet incorporates the directed Aspect reply at epistemic event
`10544`:

- sender: `marici.Aspect`
- recipient: `marici.Figueiredo`
- intent: reply
- event: `ev-000000010544-a62a9632-c088-45ab-8096-daf7849a3496`

The reply prescribes four acquisition states:

1. dark/background;
2. source only with an upstream monitor tap;
3. downstream injected reference only;
4. source plus coherent reference with phase toggled \(0\) and \(\pi\).

## Exact local model

Use variables

\[
(B,L,g,\nu,s)
\]

for background, source luminosity, detector/interface gain, visibility, and
same-frame momentum scale. At the base point \((0,1,1,1,1)\), the typed rows
are

\[
\begin{aligned}
y_{\rm dark}&=B,\\
y_{\rm mon}&=L,\\
y_{\rm src}&=B+Lg^2,\\
y_{\rm ref}&=g,\\
y_{\rm int}&=4\nu Lg,\\
y_{\rm mom}&=\frac{Lg^2}{1+s}.
\end{aligned}
\]

Their Jacobian has rank \(5\) on the five hostile directions
\((B,L,g,\nu,s)\). A perturbation in any one coordinate changes at least one
typed row.

## Classification gate

The rows distinguish three readout classes:

- absolute rate:
  \[
  y_{\rm src}-y_{\rm dark}=Lg^2;
  \]
- coherent interference:
  \[
  y_{\rm int}(0)-y_{\rm int}(\pi)=8\nu Lg,
  \]
  with the underlying phase row changing sign;
- normalized shape:
  \[
  \frac{y_{\rm src}-y_{\rm dark}}{y_{\rm mon}g^2},
  \]
  which erases absolute scale.

Momentum must be calibrated in the same frame before interpreting
\(p^2/M^2\).

## Boundary

This is an instrument constructor, not a source-production theorem. It does
not derive the localized physical16 production kernel, the WP1075 mixing
matrix, or the source gain.

## Classification

Conditional four-state acquisition gate. It strengthens the gain/instrument
branch with a bounded five-hostile calibration design.

Checker: `research/flavor/checkers/wp1077_four_state_acquisition_calibration_gate.py`

Result: `results/wp1077_four_state_acquisition_calibration_gate.json`
