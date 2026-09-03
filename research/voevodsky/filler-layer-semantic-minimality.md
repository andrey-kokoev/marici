# Filler-layer semantic minimality

## Question

Are the boundary, filler, relative-class, selected-representative, and completed-filler stages genuinely independent?

## Claim boundary

The result proves necessity relative to exhibited countermodels. It does not claim that the chosen signature is the unique smallest presentation.

## Finite two-filler model

Take one boundary datum \(c\), two fillers \(M_0,M_1\), and one relative class \([M]\). Both fillers map to \(c\) and to \([M]\), but remain distinct chains. This separately falsifies:

- boundary determines filler;
- relative-class equality implies chain equality.

## Symmetry obstruction to canonical selection

Let a \(\mathbb Z/2\) action swap \(M_0\) and \(M_1\) while fixing \(c\) and \([M]\). The filler fiber has no fixed point. Hence no equivariant selection from the fixed class can exist without additional symmetry-breaking or a higher comparison datum.

This is a finite categorical no-go: canonical class does not entail canonical representative.

## Completion independence

The ordinary Mellin orbit supplies an algebraic selection, while completed boundary-null descent remains unverified. Therefore selected representative and completed filler cannot be collapsed into one stage.

## Disposition

Four consecutive distinctions are independently necessary for current examples:

1. boundary datum versus filler;
2. filler versus relative class;
3. relative class versus selected representative;
4. selected representative versus completed filler.

The filler layer is not only conservative; each of its semantic stages prevents a demonstrated false implication.

## Verification

- `research/voevodsky/filler-layer-minimality-contract-v1.json`
- `research/voevodsky/checkers/check_filler_layer_minimality.py`
- `research/voevodsky/results/filler_layer_minimality.json`
