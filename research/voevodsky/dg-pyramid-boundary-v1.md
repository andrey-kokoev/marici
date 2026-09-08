# Bounded dg pyramid boundary — iteration 1

## Objective slice

Implement a bounded `DGPyramidBoundary` containing object labels, q, e, hM, HC, and their differential equations, with no filler; derive closure of HC-e hM internally from the graded composition law.

## Construction

`agda/DGPyramidBoundary.agda` keeps the three object labels and six relevant Hom-degree types distinct:

- Hom^-1(J,Q), Hom^0(J,Q);
- Hom^2(Q,F), Hom^3(Q,F);
- Hom^1(J,F), Hom^2(J,F).

Only the three composition operations required by the Leibniz calculation are present. The data fields are q, e, hM and HC with

    delta hM = q
    delta e = 0
    delta HC = e q.

The record also requires the degree-two/even composition boundary

    delta(e hM) = (delta e) hM + e (delta hM),

linearity of delta over the required difference, zero composition, and the two additive identities needed to finish the calculation. It deliberately does not request an unrestricted dg category.

`pyramidDiscrepancy` defines

    Delta = HC - e hM.

`pyramidDiscrepancyClosed` proves `delta Delta = 0` by rewriting through the three face equations and `compositionBoundary`. Closure is derived; it is not a user-supplied record field and cannot conceal a sign mismatch.

## Scope

The record gives exact typed obligations for a boundary candidate. Merely constructing a record instance would not establish that the objects or maps are the physical Marici ones; that requires the future adapter and its provenance. There is no filler, framing predicate, support condition, endpoint connector, Q/Rees/Cartier condition, or claim of a current full instance in this iteration.

The use of degree(e)=2 fixes the positive Leibniz sign. A source convention using different shifts will fail to instantiate these types/equations until an explicit reindexing is supplied.

## Verification

Agda 2.8.0.1/Cubical 0.9 accepted the module with `--safe --cubical --guardedness`, exit0 and no warnings. The first run exposed collision of the field name J with Cubical Prelude's interval involution; object fields were renamed SourceObj, GenericObj, SupportedObj and the rerun passed. No holes or postulates.

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/DGPyramidBoundary.agda"
```

Next iteration: define the framed filler as a dependent fibre over this derived closed discrepancy, with support, endpoint, Q, and Rees conditions as separate predicates. No Git operations or analytic-interface changes.
