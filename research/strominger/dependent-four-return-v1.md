# Dependent four-shift return: checked proof and retained source history

## Question

Can the note's return of a dependent orbit be formalized without identifying a directed execution history with an equality path?

Applicable SCC obligation: route/coherencer compatibility, on the type `Σ a, G⁴(a) ≡ a`. The free directed seed histories remain a separate type. The owner-local SCC manifest validates.

## Claim boundary

`agda/DependentFourReturn.agda` proves the general theorem in safe Cubical Agda, without an `isSet` assumption. Its explicit square has dependent type

```
PathP (λ i → G⁴(p i) ≡ p i) (cong G⁴ p) p
```

Together with base path `p`, this constructs the four-shift return of the entire dependent pair. The formula uses cubical composition rather than assuming equality of raw witnesses.

The first higher equivariance square is also proved for this exact return homotopy:

```
shift-four-equivariant : (x : Per4)
  → cong shift (shift-four x) ≡ shift-four (shift x)
```

The proof constructs preservation of cubical composition by a function **relative to its boundary**, using `hcomp-unique`. Applying it to `G` supplies the required path between the two dependent return squares, with the base component fixed. No replacement return homotopy or proof-irrelevance assumption is introduced.

The source fixture imports the unchanged six-arrow endpoint table and free-path datatype. It selects `AD, DB, BC, CA`, supplies source/target alignment, and retains that exact word beside the terminal vertex equality. A separate non-erasure lemma distinguishes its length-four history from `stop`. Selection of this successor is additional data.

**Fresh kernel verification passed**, including the seed fixture and non-erasure lemma, using Agda 2.8.0-3d04bac and Cubical 0.9 with `--safe --cubical --guardedness --ignore-interfaces`. Included source inventories remained stable during the check. Receipt: `results/dependent-four-return-v1/agda.json`.

The initial direct compiler call was refused by structured-command. The operator subsequently authorized copying and adapting the repository PowerShell wrapper; that admitted invocation succeeded:

```
pwsh -NoProfile -File research/strominger/checkers/check_dependent_four_return_agda.ps1 -Fresh
```

## Disposition

Fresh execution of `checkers/check_dependent_four_return.mjs` passed:

- enumeration directly from the actual source: six rooted four-arrow histories, cyclic orbit sizes two and four;
- the selected cycle and all its rotations;
- retention of an existing prefix while the active endpoint returns and history grows by four;
- 19 circle winding controls, of which 18 change as raw witnesses;
- 10 noncommutative D5 controls, of which five change as raw witnesses;
- rejection of an invalid directed word and the independent-product cyclic-return inference.

Receipt: `results/dependent-four-return-v1/verification.json`. These reproduce finite/model evidence; the separate fresh Agda receipt certifies the general theorem. A coherent C4 action with this canonical generator is now constructed separately in [coherent-four-return-v1.md](coherent-four-return-v1.md). Its specific fourfold-return coherence has not been identified with this module's earlier homotopy. Native edge-five successor/payload return remains unconstructed. Reflection continues to mean reversal/duality, not forward endpoint transport.
