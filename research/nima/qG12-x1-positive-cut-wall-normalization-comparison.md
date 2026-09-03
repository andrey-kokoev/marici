# `q_G12` `X1` positive-cut normalization comparison

## Question

Is the source-normalized `X1` soft strict transform the soft specialization of the sewn `q_G12` wall class with matching measure sign, occurrence sum, conductor grade, and positive-cut phase?

## Exact compatibility

The strict-transform checker starts from the `q_G12`-residue Cayley–Menger kernel itself, not from an independently fitted soft model. In the weighted chart

\[
b=E+X_1\xi,
\]

the pulled kernel has order `X1^2`. Since `db=X1 dxi` at fixed external energies, the Jacobian cancels the square-root factor and the leading measure ratio is one on the chosen positive sheet.

The checker also pulls back all five retained denominators and the unsplit occurrence numerator. After the measure cancellation, the normalized exceptional source factor is

\[
\frac{a+p}{2p(\xi+1)(a-p)^2(a+3p)}.
\]

Thus the `X1` soft object is an exact specialization of the unsplit `q_G12` residue form at rational-form and measure levels. It preserves source sewing and fixes a local positive-sheet sign.

The soft-triangle transport then provides one positive-cut cycle with common orientation and fixed nonzero phase for the four physical endpoint-node germs. The source factor is strictly positive on its open chamber.

## Missing comparison

This does not yet identify the conductor-normalized shared-wall classes `rho_i`:

- the strict transform specializes the full `q_G12` residue surface before taking an individual `q_gi` wall class;
- `q_g1=X1(\xi+1)` becomes an exceptional divisor, while `q_g2-q_g31=X1(\kappa-1)` becomes a collision divisor;
- no map sends the three generic conductor-reduced wall one-forms to the graded soft positive-cut cycle;
- the analytic epsilon normalization and finite conductor remainder are not tracked through the strict transform.

Therefore the positive-cut anchor is compatible with the upper sewn source, but compatibility with `rho_i` and its conductor grade remains unproved.

## Strongest falsification attempt

Equate unit leading measure ratio with equality of normalized wall classes. This fails typing: the former is a bulk strict-transform statement on a chosen sheet; the latter requires sequential wall residue, relative-cohomology reduction, analytic normalization, and cycle pairing.

## First missing arrow

The first missing arrow is a specialization map

\[
\operatorname{sp}_{X_1}:H^1_{\rm rel}(q_{gi})
\longrightarrow \operatorname{Gr}^{\rm soft}H_{\rm node}
\]

that transports each sewn wall class, its conductor grade, and orientation to the positive-cut cycle.

## Acceptance test

1. take each normalized `rho_i` through the weighted chart;
2. compute its strict transform and soft valuation;
3. reduce on the exceptional relative complex;
4. compare with the oriented positive-cut generator;
5. track the epsilon residue and finite remainder;
6. reverse the local square-root sign as a deliberate failure.

## Disposition

The `X1` positive-cut anchor is exactly compatible with the unsplit `q_G12` residue form and its leading measure sign. It is not yet a normalization of the three generic shared-wall cohomology classes.

## Evidence

- `research/benincasa/check_x1_soft_physical_strict_transform.py`
- `research/benincasa/x1-soft-physical-strict-transform.json`
- `research/benincasa/soft-triangle-global-vanishing-transport.json`
- `research/benincasa/soft-triangle-source-port-recovery.json`
