# The Minimal Eta-Squared Lift Framing Has Three Response States

## Result

The \(32\) signed Moore mutations represent one nonzero eta-squared residue,
but their reflection responses factor through a three-state quotient of the
lift framing.

For a legal word

\[
[[x_i^{\epsilon_i},x_j^{\epsilon_j}],
 [x_i^{\epsilon_i},x_k^{\epsilon_k}]],
\]

the response profile is determined by the following rule.

| Framing state | Full depths | Relational depths | Count |
|---|---|---|---:|
| repeated slot \(x_0\) or \(x_1\) | \((5,9,13)\) | \((7,12)\) | 16 |
| repeated slot \(x_2\), equal tail signs | \((8,8,14)\) | \((8,14)\) | 8 |
| repeated slot \(x_2\), opposite tail signs | \((8,12,16)\) | \((11,12)\) | 8 |

The classifier has no exceptions in the complete legal mutation census.

## Forgotten coordinates

The response profile is invariant under:

- inversion of the repeated generator;
- interchange of the two nonrepeated generators.

These coordinates belong to the presentation atlas but not to the minimal
response framing. The retained coordinates are a repeated-slot incidence
bit, followed on the exceptional \(x_2\) branch by a relative-polarity bit.

Thus the framed lift factors as

\[
\text{signed Moore presentation}
\longrightarrow
\{A,B,C\}
\longrightarrow
\text{response profile}.
\]

## Interpretation

The homotopy quotient forgets all three states and retains only eta-squared.
The reflection interface distinguishes them. Therefore the extra framing is
not another homotopy invariant; it is the minimum incidence/polarity port
required by this particular response functor.

This supplies the missing selector without retaining the full signed word.
It also gives a direct hostile test for any proposed response descent: two
presentations in different framing states represent the same residue but must
produce different response profiles.

## Replay

```powershell
python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```
