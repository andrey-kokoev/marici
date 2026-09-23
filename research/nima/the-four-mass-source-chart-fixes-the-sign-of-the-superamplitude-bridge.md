# The four-mass source chart fixes the sign of the superamplitude bridge

## Question

Is there a primary-source map from the oriented four-pair cell form to the COMPLETE starred ψ on-shell superfunction, avoiding a forbidden pointwise comparison of positive-real and nilpotent external data?

## Source-backed result

Yes, at the RELABELLED eight-column cell level, with an EXPLICIT orientation sign. In arXiv:1212.5605, Table `g2n_yangian_invariants`, the starred four-mass cell's published positive chart has ordered coordinates `α1,...,α8` and row matrix

    (1, α1, α2+α3, (α2+α3)α4, α3α5, α3α6, 0, 0)
    (0,  0,       1,             α4,    α5,    α6, α7, α8).

Gauge columns 1 and 3 to the identity. It agrees EXACTLY with the previously checked four-pair chart via

    (w2,w4,w5,w6,w7,w8,t,u)
      =(α1,α4,α2α5,α2α6,(α2+α3)α7,(α2+α3)α8,
        1/α2,1/(α2+α3)).

All `αi>0` imply `t>u>0`. Pulling back our declared fourfold intrinsic cyclic residue `-d^8(w,t,u)/[w2 w4 w5 w6 w7 w8 u(t-u)]` gives **minus** the ordered authored source form `dlogα1∧...∧dlogα8`. The checker derives this sign from the full eight-by-eight chart Jacobian. The earlier zero-column residue ratio from nine to retained eight columns is one; it does not erase this relative sign. Any identification with the source's PLUS ψ must therefore reverse our declared source orientation once, or show that the source has chosen the opposite wedge ordering. A silent sign change is not admissible.

A second PRIMARY SOURCE supplies the missing global operation, not a pointwise scalar substitution: arXiv:1312.2007, section `The Superamplitude`, states that for a `4k`-dimensional positive cell the complete form under `Y=Y0`, formal `Z=(z,φ·η)` and Berezin extraction equals its `∫(∧dlogα) δ^{4k|4k}(C(α)·𝒵)` on-shell diagram. Together with arXiv:1212.5605's starred row identifying this on-shell invariant as its TWO-SOLUTION `ψ[A,1,2,3,4][B,5,6,7,8]`, the chain identifies the complete extracted superfunction of our eight-column cell as that sourced object **up to the computed orientation ratio -1**. The source's two-solution sum, not the positive real sheet alone, is required.

## Claim boundary and disposition

This is a SOURCE-TYPED, orientation-qualified comparison of the retained-eight cell. It is NOT an expanded rational formula for the global bosonic traced eight-form at arbitrary positive six-dimensional `Z`, and it does not prove that the zero-column EMBEDDING occurs among the authored nine-point generalized-R tree-history terms. The earlier numerical fixed-target component and bosonic density still must not be equated: they lie on different source inputs. The next executable comparison is to derive the ordinary target rational trace, verify its orientation against this dlog chart, and separately inspect the nine-point history list for a compatible sourced coefficient.

Checker: `research/nima/checkers/check_four_mass_source_chart_and_bosonization_bridge.py`; result: `research/nima/results/four-mass-source-chart-bosonization-bridge.json`.
