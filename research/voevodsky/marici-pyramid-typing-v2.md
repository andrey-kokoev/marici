# Marici conductor–Morse pyramid: normalization obstruction v2

## Iteration-2 question

Can the iteration-1 comparison roof carry the constructed normalized source map

\[
a:J\to T[1]
\]

to the corrected Morse map while preserving the primitive class?

## Fresh-state answer

No, not if the corrected Morse map is used as a nullhomotopic map in the same target.

`research/chatgpt/physical_source_comparison.md` proves that the road-augmentation map sends the physical cycle z to the conductor unit:

\[
d_Jz=0,\qquad a_*[z]=1\ne0\in H_1(T[1]).
\]

Thus a is not nullhomotopic. If a cochain h in Hom(J,T[1]) satisfied

\[
\delta h=a,
\]

then evaluation on the cycle z would make a(z) a target boundary, contradicting the displayed nonzero homology class.

By contrast, `research/chatgpt/physical_delta_result.md` constructs the corrected Morse equation

\[
\delta\widehat h_M=\widehat q_J.
\]

Therefore any comparison identifying a with qhat_J while preserving the normalized homology class is impossible. Equality of their coefficient +1 labels does not repair this: one +1 is a surviving conductor homology class; the other is the coefficient of an exact map in its endpoint-corrected Morse target.

## Consequence for the v1 cell table

The v1 conditional slot

\[
h:J\to T[1],\qquad\delta h=a
\]

is empty for the constructed normalized a. Consequently the conditional formula

\[
\delta(-k_\nu h)=k_\nu a-e_\nu h
\]

is algebraically correct but cannot be instantiated with that a in T[1]. It is not a candidate physical pyramid face until a support-changing comparison changes the target and explains what class is transported.

This also corrects the proposed next move in v1: do NOT seek a quasi-isomorphic square carrying a to an exact qhat_J while preserving homology. The viable alternatives are:

1. map a to a nonexact supported class whose boundary only becomes qhat_J after a relative/support triangle;
2. place qhat_J as a connecting boundary in a larger filtered object, retaining the missing grade;
3. construct an extraordinary support-changing edge for which the target homology comparison is explicitly not the naive one.

Each alternative requires a new object/edge, not another homotopy between the current maps.

## Agda certificate

`research/voevodsky/agda/PyramidNormalizationObstruction.agda` extracts the decisive cycle test. It defines a primitive z with source boundary zero and augmentation one. A nullhomotopy preserving zero must make one equal zero, giving a constructive contradiction. A second record states the transport form: no comparison can both preserve source value one and assign exact target value zero.

Agda 2.8.0.1/Cubical 0.9 accepted the module with `--safe --cubical --guardedness`, exit 0, no warnings, after adding the explicit Empty import required for the contradiction type. No holes or postulates.

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/PyramidNormalizationObstruction.agda"
```

The module is deliberately the extracted normalized-cycle obstruction. It does not formalize the integer matrices, derived roofs, or corrected Morse target, and it does not prove every possible physical Q realization exact.

## Updated next move

Search the mutable research tree for an already constructed relative/support triangle in which the normalized class survives as a connecting or shifted class. Type its three maps against:

- the source roof a;
- the corrected Morse identity including the occurrence-Koszul term;
- both endpoint connector cells.

If no such triangle exists, the missing pyramid edge is now precisely a support-changing extraordinary comparison. The existing endpoint inclusion and native first-jet readout cannot supply it.

## Disposition

Iteration 2 rules out the naive comparison roof proposed in iteration 1 and removes an impossible h-slot from the candidate pyramid. The physical pyramid remains incomplete but its admissible shape is narrower. One new checked Agda module and this packet were created. No Git operations or analytic-interface changes.
