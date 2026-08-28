# Moore-Face Legality Does Not Force Gauge-First Response

## Structural mutation census

Start from the Moore representative

\[
[[x_0,x_1],[x_0,x_2]]
\]

and form every signed permutation

\[
[[x_i^{\epsilon_i},x_j^{\epsilon_j}],
 [x_i^{\epsilon_i},x_k^{\epsilon_k}]],
\qquad
\epsilon_i,\epsilon_j,\epsilon_k\in\{1,-1\}.
\]

There are \(48\) formal mutations. Exact free reduction against all four
Moore face maps leaves \(32\) legal mutations.

After substituting

\[
x_0\mapsto c_{31},
\qquad
x_1\mapsto c_{13},
\qquad
x_2\mapsto c_{22},
\]

their response Smith depths split into three classes:

| Full depths | Relational depths | Count |
|---|---|---:|
| \((5,9,13)\) | \((7,12)\) | 16 |
| \((8,8,14)\) | \((8,14)\) | 8 |
| \((8,12,16)\) | \((11,12)\) | 8 |

Thus the common Moore deletion packet does not determine one response
filtration.

## Minimal hostile mutation

The legal word

\[
[[x_2,x_0],[x_2,x_1]]
\]

has all four trivial Moore faces. Its full and relational depths are

\[
(8,8,14)
\qquad\text{and}\qquad
(8,14).
\]

At the first surviving grade,

\[
\frac{R-I}{256}equiv
\begin{pmatrix}
0&0&1&1\\
0&0&1&1\\
1&1&0&0\\
1&1&0&0
\end{pmatrix}
\pmod2.
\]

This matrix has rank two and already survives in the relational quotient.
Hence gauge-first response is not forced by Brunnian face vanishing.

## Corrected explanatory boundary

The census supports a weaker statement: within this complete signed-
permutation family, Moore legality prevents a depth-four response. But it
does not force either the depth-five origin or a gauge-valued first survivor.

The original word's nested-commutator explanation remains valid for that
source ordering. It cannot be promoted to a theorem about the Moore deletion
type alone. An additional orientation or generator-incidence constructor is
required to select its response profile.

## Replay

```powershell
python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```
