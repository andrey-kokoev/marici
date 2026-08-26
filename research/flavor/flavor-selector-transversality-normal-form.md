# Selector transversality normal form

## Question

What exact local condition must the completed source dynamics satisfy to remove
the sole coefficient ambiguity that still changes \(g_Ff/v\)?

## Existing quotient

Use the WP543 log-coordinate order

\[
x=(\log a,\log w,\log g_F^2,\log g_P^2).
\]

The strongest admitted source-equality Jacobian has rank three and kernel

\[
k=(2,-1,0,0)^T.
\]

Its first row is the fixed-electroweak relation

\[
d\log a+2d\log w=0.
\]

The vector \(k\) is therefore the clock-preserving coefficient direction
exhibited by WP537, not a weak-basis presentation tangent.

## Exact acceptance condition

Let one proposed source-derived equality have gradient

\[
\ell=(\ell_a,\ell_w,\ell_g,\ell_p).
\]

Appending it to the WP543 Jacobian gives

\[
\det J_{\mathrm{aug}}=2\ell_a-\ell_w=\ell k.
\]

Consequently the augmented source system has rank four exactly when

\[
2\ell_a-\ell_w\ne0.
\]

This is necessary and sufficient for local removal of the \(t\)-fiber. A row
with \(\ell_w=2\ell_a\) merely repeats a clock-preserving constraint.

## Hostile typing gate

The measured clock-ratio gradient contracts with \(k\) to \(-1\). It is
algebraically distinguishing but is not a source equation. Promoting it to the
source Jacobian would infer selection from readout and violate the declared
quotient typing.

Likewise, WP544's 29 scale, twist, renormalization, and threshold controls are
external instrument coordinates. Their rank may establish measurement
faithfulness but cannot provide \(\ell\).

A qualifying row must instead be derived from the WP545-complete action as a
scheme-declared beta zero, stable invariant-manifold equation, or finite
threshold relation whose normalization is frozen independently of the desired
clock ratio.

## Post-selection spectral gate

The WP537 hostile pair changes every vector mass squared by an exact factor of
four. Therefore a future selected value of \(t\) cannot inherit the present
benchmark spectrum.

After selection, the programme must recompute in order:

1. the coupled vacuum and physical Hessian;
2. the complex pole positions;
3. pole residues in the declared current channels;
4. every kinematically open partial width and each total width;
5. the WP535/WP544 calibrated response on the recomputed packet.

Widths and residues are independently frozen only after this complete channel
and calibration calculation. They are not source equations and may not be
used to choose the selected solution.

## Disposition

WP546 supplies the exact orientation test for the missing selector equation.
It does not produce that equation or a numerical value. The smallest exact
falsifier is a proposed row with \(\ell_w=2\ell_a\), for which the augmented
rank remains three.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp546_selector_transversality_normal_form.py

The generated result is
research/flavor/results/wp546_selector_transversality_normal_form.json.

The reviewed graph admission is
ev-000000004904-ea1557d8-567b-4b42-ac50-2d83c38d69e6.
