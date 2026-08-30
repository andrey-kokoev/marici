# 1731 — A Labelled Interference Reference Recovers Relative Flat Holonomy

## Relative-readout test

Let \(L\) be a signal amplitude line and \(R\) a labelled reference amplitude
line.  Their density objects are insensitive to central phase because

\[
L\otimes\bar L
\]

has trivial central character.  The interference coefficient instead belongs
to

\[
\operatorname{Hom}(R,L)=L\otimes R^*.
\]

## Holonomy

The comparison line has

\[
\boxed{
\operatorname{Hol}_{\rm int}
=\operatorname{Hol}_L\operatorname{Hol}_R^{-1}.
}
\]

An exact Čech audit over the subgroup \(\mathbb Z_4\subset U(1)\) verifies
that this relative holonomy is unchanged by independent local gauges of the
signal and reference lines.  Density holonomy remains trivial.

If signal and reference carry the same flat twist, interference is also
trivial.  Therefore no absolute central phase is recovered; only relational
phase topology is observable.

## Physical-selection condition

The comparison becomes a physical readout only when the source supplies:

1. a labelled reference line;
2. a nonzero overlap/interference pairing;
3. a relative cycle or measurement that evaluates that pairing.

Without these data, the flat twist remains an internal coefficient class.  It
must not be declared observable from algebra alone.

## Narrow result

A supported interference comparison can recover the flat phase information
forgotten by density, but only relatively and only after source-defined
activation.  This uses the existing labelled pair incidence and coefficient
duality; no new Cut carrier stratum is required.

## Durable artifacts

- `research/benincasa/checkers/interference_relative_flat_holonomy.rs`
- `research/benincasa/results/interference-relative-flat-holonomy.json`
- `research/benincasa/interference-relative-flat-holonomy.md`

## Next falsifier

At a zero of the interference overlap, compute the supported costalk of the
comparison line.  Test whether relative holonomy survives in a nearby-cycle
grade or becomes physically unselected, paralleling the weighted cosmological
chain obstruction.
