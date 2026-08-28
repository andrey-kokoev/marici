# A degree-four spin-two output forces a 3+2+1 optical instrument

## Global obstruction

The local augmentation ladder cannot be implemented by one globally nonzero scalar phase reference on a degree-four spin-two bundle.

Use north and south charts on the celestial sphere. On their equatorial overlap, the bundle transition has the form

\[
g(\phi)=e^{4i\phi}.
\]

Its winding is

\[
\frac{1}{2\pi i}\int_0^{2\pi}g^{-1}dg=4.
\]

Therefore the bundle is nontrivial. A globally nonvanishing reference section would trivialize it and is impossible. Every global augmentation must use patched local references or carry zeros whose total index is four.

## The minimum generic 3+2+1 architecture

For a transverse section, the smallest zero packet has four simple zeros. Removing them produces a punctured sphere with

\[
\dim H^1(S^2\setminus Z)=4-1=3.
\]

The complete minimum instrument therefore has three layers:

### 3 — defect-period interferometers

Four puncture holonomies obey one total-sum relation, leaving three independent periods. Three loop interferometers measure them. They verify that local phase references patch with the degree-four attachment rather than silently resetting phase across charts.

### 2 — phase quadratures

The residual phase orbit is a circle before a source-derived Real structure is established. One real quadrature has unavoidable collisions. Two real quadratures, or one genuinely complex heterodyne channel retaining both, embed the phase circle.

### 1 — direct source-ray monitor

The calibrated direct feedthrough identifies the driven output ray and reduces the initial \(U(2)\) ambiguity to the orthogonal phase circle.

Thus the minimum generic channel count is

\[
3+2+1=6.
\]

This is the global form of the local output-frame ladder. The one-channel rung fixes incidence, the two-channel rung resolves continuous phase, and the three-channel rung certifies topological attachment.

## Why one homodyne reference fails

A single local oscillator can orient the orthogonal response in one chart. Transporting it around the sphere either accumulates the degree-four transition or forces zeros. Treating it as a global constant erases precisely the defect information that distinguishes a legitimate bundle section from a presentation convention.

The correct apparatus uses chart-local oscillators with recorded transition phases. Around the four-zero packet it measures three independent relative loop phases; the fourth is fixed by the total degree.

## Experimental falsifier

Prepare a generic transverse spin-two response and locate its polarization zeros. Then:

1. measure both quadratures of the orthogonal response in overlapping north and south frames;
2. reconstruct the equatorial transition winding;
3. measure three independent puncture periods;
4. test that the fourth period satisfies the degree-four sum law;
5. verify the direct source-ray calibration independently.

The architecture is rejected if the transition winding is not four, if fewer than four simple zeros appear without compensating multiplicity, if the period sum fails, or if a claimed single global phase reference remains nonzero everywhere.

For degenerate zeros, three separate loop channels may be replaced by jet-sensitive multiplicity channels. The total attachment information remains degree four; it has not disappeared.

## Transfer

Nima's global reference theorem supplies the two-quadrature rung. Strominger's Hodge classification supplies the three defect-period rung. The active theta colligation supplies the direct source ray. Their composition produces a literal 3+2+1 optical instrument rather than a numerical analogy.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_degree_four_321_output_instrument.py
```
