# The next generated cell is an exchange comparison, not another particle

## Question

Follow the operator's proposed WG-first search: from the retained nested object, identify a comparison boundary and construct its witness with existing rules, rather than selecting another physical interaction or fitting an energy.

Active obligation: source attachment transport and native comparison construction. The starting marked syntax is the previously declared `NestedWitnessTransport.Term`, not a derivation of a physical proton or electron.

## Boundary and supplied inputs

Let t=attach(attach(core,e1),e2). Its global label exchange is sigma(t)=attach(attach(core,e2),e1). The prior formal construction proves sigma is an involution and that these two marked terms are unequal.

There are two different proposed fillings:

1. Treat t and sigma(t) as identical without transport.
2. Compare them under the actual exchange equivalence, retaining their marks.

The first is refuted by `nested-distinct`. The second has the explicit equivalence generated from sigma and its two-sided inverse proof; its value-preservation witness is reflexivity after applying sigma.

`agda/NestedExchangeNextCell.agda` declares exactly two seed premises: the existing source package and the relabeling function package. The already-declared native application extension computes the exchanged target, retaining both inputs. The old native `compare-kind` rule then constructs the exchange comparison from the source and computed target. Neither the target nor its comparison package is seeded.

This distinction matters: the endpoint-generation step uses the separately application-extended runtime, not the frozen twelve-rule closure alone. The exchange function, the marked source syntax and their mathematical proofs are supplied. No physical law or unique extension-selection principle is inferred from their successful admission.

## Return closure

Applying the same function to the retained target produces a second package whose active value is sigma(sigma(t)). The involution proof identifies this active value with t. Another existing comparison rule builds the return comparison under the identity equivalence.

Schematically the active values form

    t --exchange--> sigma(t) --exchange--> t.

But the final package is not reduced to the original package: it retains the intermediate result and function applications as parents. The checker proves the exact retained-expression shape. The return witness certifies agreement of active values without erasing the constructed path.

Thus the chosen next cell is a typed exchange comparison with a checked return closure. It adds neither a third electron nor an independent geometric volume. A full higher coherence between arbitrary histories would require its own boundary and proof; it is not silently supplied by this return check.

## Disposition and verification

The WG-first method produced a concrete next comparison from a stated source and available operation. It discriminated a valid transported comparison from an invalid untransported identification. It does not select a physical amplitude, energy, spatial simplex or universally unique successor. The bounded construction stops at the verified exchange/return obligations rather than inventing a new physical object to fill a picture.

Fresh safe Cubical Agda verification passed:

`pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NestedExchangeNextCell -Fresh`

Execution: `structured_command_execution:e_32876_1791227324437156900_44`; receipt: `results/agda-NestedExchangeNextCell.json`. No commit or publication is claimed.
