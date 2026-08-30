# Typed six-axis optical event compiler

## Why one verdict is invalid

The transferred tests answer different questions.  A dark selected port, a
bright packet, a hidden endpoint class, a nonzero counterterm history, a
disconnected implementation path, and an unauthorized coefficient extension
are not competing explanations on one Boolean axis.

The compiler therefore emits a product of six independent classifications.

## Axes

### Scalar axis

- `bright`
- `dark`
- `flat_normalized`
- `unknown`

### Packet axis

- `zero`
- `bright`
- `unknown`

### Incidence axis

- `matched`
- `aliased`
- `unknown`

### History axis

- `trivial`
- `nontrivial`
- `unknown`

### Path axis

- `admissible`
- `disconnected`
- `unknown`

### Coefficient axis

- `native`
- `requires_extension`
- `unknown`

The value `unknown` is information-preserving.  It prevents a passed local
test from silently authorizing an unmeasured constructor.

## Compiled fixtures

### Rosenbrock-incidence event

`(dark,bright,aliased,unknown,unknown,unknown)`

This is a selected transmission zero with a bright complement and a hidden
fractional-endpoint direction.  No path or coefficient claim is made.

### All-order normalization event

`(flat_normalized,bright,unknown,nontrivial,unknown,unknown)`

The scalar is perfectly flat, but the graded history is nonzero and
reconstructs the raw transition.  No incidence or path claim is made.

### Selective-gate path event

`(unknown,unknown,unknown,unknown,disconnected,requires_extension)`

The endpoint operation is valid, but the standard continuous implementation
leaves the reflection-fixed locus and its mixed dyad requires complexifying
the original real/rational source lattice.  No zero claim is made.

## Derived labels

Derived labels use only the axes they require:

- `selected_transmission_zero` requires scalar dark and packet bright;
- `incidence_alias` requires incidence aliased;
- `normalization_erasure` requires scalar flat and history nontrivial;
- `endpoint_without_symmetric_path` requires path disconnected;
- `coefficient_authority_gap` requires coefficient extension.

No derived label fills an unknown axis.

## Experimental contract

Every acquisition declares which axes it measured.  The compiler rejects a
record that substitutes a default negative for an unmeasured axis.  A complete
theta event would need scalar, packet, incidence, and history axes.  A claim of
source constructibility additionally needs path and coefficient axes.

This structure is the next rung above the individual falsifiers: it composes
their results without collapsing their types.

## Verification

```text
python research/aspect/checkers/compile_typed_six_axis_optical_events.py
```
