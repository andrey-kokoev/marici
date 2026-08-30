# Sheet-commuting dynamics require character-resolved observability

## Question

When the boundary loop preserves the reciprocal sheet involution, can an
aggregate passive observation certify stable invertibility without resolving
the two sheet characters?

## Character decomposition

Let \(R\) be a unitary involution:

\[
R^2=I,\qquad R^*=R.
\]

The boundary state space splits as

\[
\mathcal H=\mathcal H_+\oplus\mathcal H_-,
\qquad
\mathcal H_\pm=\ker(R\mp I).
\]

Suppose the normalized boundary return commutes with the sheet action:

\[
[L,R]=0.
\]

Then \(L=L_+\oplus L_-\). If the passive defect identity

\[
I-L^*L=O^*O
\]

holds, its right side also commutes with \(R\), and every observability
Gramian

\[
W_m=\sum_{k=0}^{m-1}(L^*)^kO^*OL^k
\]

is block diagonal:

\[
W_m=W_{m,+}\oplus W_{m,-}.
\]

Therefore \(W_m\ge\varepsilon I\) holds exactly when

\[
W_{m,+}\ge\varepsilon I_{\mathcal H_+},
\qquad
W_{m,-}\ge\varepsilon I_{\mathcal H_-}.
\]

Aggregate rank or positivity cannot conceal a failed character block.

## Even-row no-go theorem

Let \(E:\mathcal H\to\mathcal Y\) be a sheet-even output:

\[
ER=E.
\]

For every \(x_-\in\mathcal H_-\),

\[
Ex_-=ERx_-=-Ex_-,
\]

so \(Ex_-=0\). Since \(L\) preserves \(\mathcal H_-\),

\[
EL^kx_-=0
\]

for every nonnegative \(k\). Thus no number of repeated even observations can
observe an odd state.

Duplicating an even Clark row, changing its scalar weight, or sampling it at
more return times cannot create odd-sector information. If the dynamics
commutes with the sheet involution, the only repairs are:

1. add an authorized odd-sensitive output;
2. add an output representation containing the odd character; or
3. derive a source interaction that genuinely mixes the character sectors.

The third option changes the constructor and must be source-authorized.

## Minimal passive hostile

Take

\[
R=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad
L=
\begin{pmatrix}
a&0\\
0&1
\end{pmatrix},
\qquad |a|<1,
\]

and

\[
O=
\begin{pmatrix}
\sqrt{1-|a|^2}&0
\end{pmatrix}.
\]

Then

\[
I-L^*L=O^*O.
\]

The even coordinate dissipates and is observed. The odd coordinate is a
lossless unit fixed mode, so \(I-L\) is singular. Arbitrarily accurate or
repeated measurement of the even row leaves this obstruction unchanged.

## Minimal repair

Replace the odd return \(1\) by \(b\), with \(|b|<1\), and add

\[
O_-=
\begin{pmatrix}
0&\sqrt{1-|b|^2}
\end{pmatrix}.
\]

The two typed outputs give

\[
I-L^*L=O_+^*O_++O_-^*O_-.
\]

At horizon one, the observability margin is

\[
\varepsilon=
\min(1-|a|^2,1-|b|^2).
\]

This is the smallest character-complete passive repair. It uses two output
characters, not two duplicate ports.

## Torsor bit versus odd amplitude

A trusted sheet-origin bit labels which summand is called plus. It does not
measure an arbitrary vector in \(\mathcal H_-\). Character framing and
character observability are distinct:

- the origin bit fixes the naming torsor;
- an odd output detects odd amplitude;
- a uniform odd Gramian controls completion.

This is the same distinction previously found between a canonical tensor-unit
frame and executable control of a full noncentral block.

## Implication for the three-by-two sewing architecture

The two sector towers do not become jointly faithful merely by being placed
side by side. Their fifth-level sewing must contain either character-complete
outputs or a source-derived mixing arrow whose iterates move every hidden
character into an observed row.

When sheet dynamics commute, the observability theorem factorizes exactly
into two independent sector certificates. The global bound is their minimum.
Consequently the weakest sector controls the completion margin.

## Finite falsifier

The machine-readable rejection contains:

    {
      "code": "sheet_character_unobservable",
      "character": "odd",
      "commutator_L_R": 0,
      "hidden_state": "v",
      "return_eigenvalue": 1,
      "all_typed_outputs": 0,
      "observation_horizon": "m",
      "character_gramian_minimum": 0
    }

The certificate must name the character and the rows tested. An aggregate
zero without this typing is insufficient.

## Disposition

The abstract boundary theorem now has a sharp representation-theoretic gate:
if the return commutes with the sheet involution, every character must be
uniformly observable in its own block. Repeated even observations never
substitute for one odd-sensitive source row.

For theta/Tate, the immediate source question is whether the seam, primitive,
square, or archimedean channel is genuinely odd under the Clark sheet action.
If none is, the commuting model contains an unavoidable odd observability
kernel unless an independently derived sheet-mixing constructor is present.

## Claim boundary

This packet proves a \(C_2\)-equivariant operator theorem. It does not assert
that the theta boundary loop commutes with its sheet involution, identify an
actual odd source row, or authorize a sheet-mixing interaction.
