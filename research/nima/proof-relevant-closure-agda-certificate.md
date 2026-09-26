# Checked witness-preserving record equivalence

`research/nima/agda/ProofRelevantCoherenceClosure.agda` passes a fresh Agda check with `--safe --cubical --guardedness`, Agda 2.8.0.1 and Cubical 0.9. No new postulates or holes are introduced.

## Proved interface

For arbitrary types A,B and an equivalence e:A~=B:

* pathLift: (x=y) ~= (e(x)=e(y)); its forward function computes to cong e.
* higherLift: (p=q) ~= (cong e p = cong e q).

For an arbitrary source type Q, a dependent Trace:Q->Type, two endpoints left/right depending on both q and its trace t, and e:Y~=Z:

SourceRecord = Sigma q. Sigma t:Trace(q). (left(q,t)=right(q,t)),
TargetRecord = Sigma q. Sigma t:Trace(q). (e(left(q,t))=e(right(q,t))).

recordLift proves these types equivalent. Separate checked declarations establish source retention, trace retention, witness transport and both round-trip paths. recordPathLift and recordHigherLift then apply the same construction to equalities of the complete records and equalities between those paths.

Trace is a parameter: complete intermediate Sigma/Pi chains and their maps can be stored there without being discarded by recordLift. The theorem proves preservation of supplied traces; constructing the concrete dependent-normalizer traces and their equivalences in Agda remains the next integration step. The Python normalizer has not been verified by this module.

The implementation reuses Cubical's checked congIso (via half-adjoint equivalence) and Sigma congruence. The record assembly and retention/iteration interface are the local formalization. This is a general type-level statement, beyond the finite groupoid tests. Universe levels remain explicit.

## Fresh verification

```
agda --ignore-interfaces --transliterate -i research/nima/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/nima/agda/ProofRelevantCoherenceClosure.agda
```

Exit 0. The first run identified the library's required guardedness flag; adding it and rerunning the fresh check succeeded. A final fresh check including both record round-trip theorems also succeeded.
