# Fourier graph conormal correspondence

## Correct completed seam

Let `E` be the arithmetic test space and `E'` its continuous dual. For a
continuous Fourier--Tate map `F:E->E`, the reciprocal bulk graph is

`Gamma_F = {(x,Fx)}`.

Its canonical seam object is the conormal in the dual:

`N*Gamma_F = {(-F'lambda,lambda)}`.

The pairing vanishes identically:

`<-F'lambda,x> + <lambda,Fx> = 0`.

This construction needs continuity and the transpose map. It does not require
a Hilbert metric, unitarity, or a Riesz identification.

## Relation to the finite anti-graph

At a finite unitary cutoff, a Riesz map identifies covectors with vectors.
Under that temporary identification, the conormal becomes the anti-graph
normal used in the finite checker.

The flat-comb hostile proves that this Riesz picture does not survive cutoff
growth. The infinite augmentation object is a covector, so the conormal is the
durable construction and the state anti-graph is only its finite shadow.

## Effect on the 3+4+3 tower

The four mixed controls remain canonical: they are the four evaluations
between two bulk state coordinates and two conormal covector coordinates.

The final three pure-seam quadratic controls are no longer automatic. A
quadratic form on two covectors requires a source-derived dual--dual pairing,
kernel, or nuclear identification. Evaluation alone pairs a covector with a
state, not two covectors with each other.

Thus the completed tower is currently:

- three bulk quadratic controls;
- four canonical state--dual comparisons;
- three conditional dual quadratic controls.

The full terminal `sp4` interpretation survives only if Grothendieck derives
the missing continuous dual--dual seam pairing.

## Apparatus retyping

The finite sixteen-power tomograph remains a valid cutoff diagnostic. It is
not the completed instrument.

For the rigged apparatus:

1. prepare two bulk state probes;
2. implement two seam covectors as calibrated coherent functionals;
3. measure the four state--dual response coefficients;
4. do not coherently add a covector to a state field;
5. activate pure-seam quadratic tomography only after a physical realization
   of the source-derived dual--dual pairing is supplied.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_fourier_graph_conormal_correspondence.py
```
