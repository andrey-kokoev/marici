# Finite-time source-normalization closure

## Question

Does Collins--Holman--Vardanyan, arXiv:1408.4801, instantiate the three jointly
faithful normalization records required by Ledger 3045?

## Complete source census

The primary TeX source contains:

- six explicit occurrences of `infinite part` in the worked renormalization
  formulas;
- the three symbols \(I_0^f,I_2^f,I_4^f\), described only as finite parts;
- no subtraction scale;
- no normalization point;
- no on-shell condition;
- no measured input.

The introduction mentions unit propagator residue as a general example of a
condition one may wish to preserve. The worked toy model does not compute its
pole residue, turn that example into an equation, or combine it with two other
independent conditions.

The actual finite-time condition cancels initial-time-dependent terms so that
the result matches the chosen renormalized infinite-past correlator. This fixes
the boundary action relative to the finite bulk scheme; it does not fix that
scheme.

## Result

The frozen primary source contains no rank-three physical normalization map.
It therefore does not select a point in Ledger 3037's finite-scheme orbit or
instantiate Ledger 3045's minimal three-port interface.

The finite constants in this toy branch are external renormalized inputs. They
are not predictions of the Carrier, the loop coefficient object, Ward
coherence, Hadamard admissibility, or the source's finite-time matching rule.

This closes the branch under the current source. Reopening requires a new
primary source or an explicitly declared physical preparation supplying three
jointly faithful normalization conditions.

## Scope

The result does not claim that inflationary observables can never fix the
parameters. It says only that this paper's worked toy construction does not do
so. The paper's general discussion of possible renormalization conditions is
not an instantiated readout map.

## Verification

- `research/benincasa/results/finite-time-source-normalization-census.json`
- arXiv:1408.4801 `paper.tex` lines 24, 54, 289, 345--355, and 427--428
- Ledgers 3037, 3040, 3043, and 3045
