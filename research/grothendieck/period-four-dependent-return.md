# Period-four dependent return

## Question

Does shifting a witnessed four-period point four times return the full dependent pair without sethood? Operator supplied `C:/Users/andrey/Downloads/marici_period4_witness_handoff.md` and requested execution; shell use was authorized and SCC requirements lifted for this work.

## Claim boundary

`agda/PeriodFourWitness.agda` proves, for arbitrary universe-polymorphic S and F:S→S, that `(F a, cong F p)` equals `(a,p)` in `Σ a, F a ≡ a`. Its explicit square is `compPath→Square refl`: both composite boundary routes are `cong F p ∙ p`. `ΣPathP` uses p as the moving-base path. Specializing to F=G⁴ proves four shifts equal identity pointwise. No sethood, holes, or postulates are used.

The rival strict-root interpretation fails: the reconstructed exact Python controls reproduce changed raw witnesses in 18/19 tested circle windings and 5/10 D5 witnesses, while dependent transport returns each witness. The six-edge endpoint table in `research/nima/agda/ActualSeedEndpointTable.agda` yields six rooted closed four-edge words in cyclic orbits of sizes two and four. Selecting AD,DB,BC,CA is additional data. The product-return counterexample is also checked.

## Disposition

Fresh Agda closure check exited 0:

```sh
agda --ignore-interfaces --transliterate --safe --cubical --guardedness --no-libraries -i research/grothendieck/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/grothendieck/agda/PeriodFourWitness.agda
python research/grothendieck/checkers/check_period_four_witness.py
```

The Python checker passed and wrote `results/period-four-witness.json`. It uses only the standard library and exact integers. An initial Agda invocation without command-line cubical flags failed on library imports; the command above corrects that execution defect.

The handoff's `FourPeriodSeedWitness.agda` and original Python attachment were not found in Downloads or research. Thus no claim is made to have compiled that supplied source-specific module. The reconstructed checker is not its substitute as a formal proof. The source-importing implementation and accumulated-history obstruction are now checked as described below. Higher compatibility of the return homotopy with another shift remains open. A fully coherent C4 action and physical dimensional interpretation are not established. No Nima source was edited.

## Source-bound retained window

`agda/SourcePeriodFourWitness.agda` imports the actual endpoint table and free-path datatype. It explicitly chooses AD,DB,BC,CA, proves the chosen edges have the required endpoints, and specializes the general four-shift theorem. `ReturnWindow` retains its endpoint, an actual directed history, a four-occurrence length proof, and a separate active-vertex equality (identity projection). This is a selected constructor, not a source-derived unique selection or an identification of occurrences with identity paths.

The selected window retains the exact four-edge word. `cycle-not-empty` rejects equality with the empty word. `accumulated-history-does-not-return` proves for every incoming history ending at A that appending the cycle cannot equal that history, by structural recursion on length equality. `alternative-target-distinct` exhibits AB as a source-permitted alternative whose target differs from the selected next A.

Fresh closure compilation of the final module exited 0 using the same flags above, in `/tmp/marici-period4-source.8Ld5W6`, containing copied `.agda` sources from Nima's include directory and both new Grothendieck modules. This isolated generated interface files from Nima's workspace. Imported indexed-pattern warnings remain: Cubical Agda warns that certain imported functions do not compute on transports. They are not holes or postulates; no stronger transport-computation claim is made. The source-bound window is not yet equipped with a coherent cyclic shift action. Higher equivariance is the remaining formal gate.
