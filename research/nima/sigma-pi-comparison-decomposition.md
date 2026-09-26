# Uniform E/Pi comparison decomposition — checked relative theorem

## Question

Can the dependent sum/product constructors supply uniform comparison rules, rather than adding a new law for each observed pair of resolution trees?

Active SCC obligation: route/coherencer compatibility. Stratum: same interpreted Code, arbitrary small types and actual identity witnesses, with source values and the original witness retained in a Certificate. The SCC model/dashboard discovery was read. The Agda target now typechecks; no SCC admission of the global rule-basis claim is asserted.

## Claim boundary

The proposed structural rules are the standard equivalences:

* E: an equality of dependent pairs is an index path p together with an equality of the transported first fibre value and the second fibre value.
* Pi: an equality of dependent sections is a family of pointwise equalities.

For a code Q and values x,y, recursively define Evidence(Q,x,y). At an E node:

Evidence(E(I,F),x,y)
 = Sigma(p:fst(x)=fst(y)).
     Evidence(F(fst(y)), transport(El o F,p,snd(x)), snd(y)).

At a Pi node:

Evidence(Pi(I,F),x,y) = Pi(i:I). Evidence(F(i),x(i),y(i)).

The checked theorem is Evidence(Q,x,y) ~= (x=y), with both inverse laws. It reconstructs each original witness, including its higher identity information. The E step combines the recursive fibre equivalence with dependent-path/transport equivalence and the Sigma path equivalence. The Pi step combines fibrewise equivalences with function extensionality. Induction is on the actual code, not a finite sample bound.

Map nodes use the Pi rule. Retain nodes keep their source provenance in the enclosing Certificate while comparing their interpreted values. A path node transports comparisons through the already constructed equivalence for its lower boundary, using pathLift; repeated path nodes therefore retain higher comparison data.

Atomic identities, index paths and identities of decomposed lower-witness types remain boundary inputs. Equivalence-code nodes now decompose pointwise using propositionality of `isEquiv`; comparison-code nodes decompose through their source projection with contractible fibres. No claim is made that this construction synthesizes those witnesses, decomposes equality of Code itself, or proves completeness of the earlier Generated relation on resolution trees. In particular, interpreting a reified entire package as an atom does not establish its structural comparison completeness.

The full record contains Q, x, y, the original witness, its decomposed evidence and the reconstruction path. Reification packages this record as an admissible next-level input.

### Explanatory issue

The checked result: recursive E/Pi path decomposition accounts uniformly for comparison structure contributed by those constructors, relative to boundary-type identities.

Rivals: only endpoint agreement is recovered; dependent fibre transport is omitted; a whole composite witness is silently imported instead of decomposed. The inverse laws with variable dependent fibres pass typechecking. The subsequent nontrivial index-transport regression passes; see `index-identity-coherence.md`. Residual identity branches are explicitly named above.

## Disposition

`research/nima/agda/SigmaPiComparisonDecomposition.agda` passes `--safe --cubical --guardedness` with no new postulates or holes.

The earlier blocker report was an execution-discovery error: only the direct executable invocation was refused. The existing launcher `C:/Users/andrey/tools/cubical-agda/agda-cubical.ps1` works through the admitted `pwsh -File` route. The operator then explicitly directed shell invocation of that PS1. Both routes succeeded; the final shell check recompiled the changed target and exited 0:

```
pwsh -NoProfile -File C:/Users/andrey/tools/cubical-agda/agda-cubical.ps1 -File research/nima/agda/SigmaPiComparisonDecomposition.agda -Include research/nima/agda
```

The installed launcher selects its bundled `agda-2.8.0/agda.exe` and Cubical 0.9. This is a fresh target check, not an `--ignore-interfaces` rebuild of every dependency. The result record is `research/nima/results/sigma-pi-comparison-decomposition.json`.

The subsequent relative completeness theorem, its exact boundary requirements and fresh verification are recorded in `source-relative-comparison-completeness.md`.
