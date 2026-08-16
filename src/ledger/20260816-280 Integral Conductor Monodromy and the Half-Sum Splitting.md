---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Integral Conductor Monodromy and the Half-Sum Splitting

## Result

Entry 279 constructs the canonical marked residue extension

\[
0\to H^2(S_E)\to H^2(S_E\setminus W)
\to H^1(W)(-1)\to0,
\qquad W=W_1\cup W_2.
\]

This entry determines the local-system structure internal to the
rank-three conductor quotient. It is not a direct sum over \(\mathbb Z\).
The two conductor-root swaps act by

\[
\boxed{
\begin{aligned}
\sigma_1(g_{101})&=-g_{101},&
\sigma_1(g_{110})&=g_{110},&
\sigma_1(\widetilde g_{111})
&=\widetilde g_{111}-g_{101},\\
\sigma_2(g_{101})&=g_{101},&
\sigma_2(g_{110})&=-g_{110},&
\sigma_2(\widetilde g_{111})
&=\widetilde g_{111}-g_{110}.
\end{aligned}
}
\]

Therefore

\[
0\to\mathcal K_{\Delta_{W_1}}\oplus
\mathcal K_{\Delta_{W_2}}
\to H^1(W)
\to\mathbb Z_{\rm top}\to0
\]

has integral extension class

\[
\boxed{(1,1)\in(\mathbb Z/2)^2.}
\]

It splits after inverting \(2\), with invariant top lift

\[
\boxed{
g_{111}^{\rm inv}
=\widetilde g_{111}
-\frac12(g_{101}+g_{110}).
}
\]

Thus the first explicitly computed non-elliptic extension is an
occurrence-identification \(2\)-torsion class. It requires no new carrier
stratum.

## Frozen graph

Use entry 267's edge order

\[
(n_{1a},n_{1b},n_{2a},n_{2b},P_+,P_-)
\]

and primitive cycles

\[
g_{101}=(1,-1,0,0,0,0),
\]

\[
g_{110}=(0,0,1,-1,0,0),
\]

\[
\widetilde g_{111}=(1,0,0,-1,-1,1).
\]

The root discriminants derived in entry 265 are

\[
\Delta_{W_1}=-4xD_1,
\qquad
\Delta_{W_2}=-4yD_2.
\]

A loop around \(\Delta_{W_1}=0\) exchanges
\(n_{1a}\leftrightarrow n_{1b}\); a loop around
\(\Delta_{W_2}=0\) exchanges
\(n_{2a}\leftrightarrow n_{2b}\). The rational same-sheet sections
\(P_\pm\) remain labelled on this generic locus.

No monodromy matrix is fitted from the desired support. Both matrices are
the literal edge permutations on the frozen normalization graph.

## Exact monodromy matrices

In the ordered column basis

\[
(g_{101},g_{110},\widetilde g_{111}),
\]

the matrices are

\[
\boxed{
M_1=
\begin{pmatrix}
-1&0&-1\\
0&1&0\\
0&0&1
\end{pmatrix},
\qquad
M_2=
\begin{pmatrix}
1&0&0\\
0&-1&-1\\
0&0&1
\end{pmatrix}.
}
\]

Direct integer arithmetic gives

\[
M_1^2=M_2^2=I,
\qquad
M_1M_2=M_2M_1.
\]

The mixed sublattice is the direct sum of the two sign characters. The top
quotient is trivial because both matrices act as the identity modulo that
sublattice.

## Integral nonsplitting

Any lift of the top quotient has the form

\[
v=\widetilde g_{111}+a g_{101}+b g_{110}.
\]

The equations \(M_1v=v\) and \(M_2v=v\) are

\[
-1-a=a,
\qquad
-1-b=b.
\]

Hence

\[
a=b=-\frac12.
\]

There is no integral solution. There is a unique rational invariant lift:

\[
g_{111}^{\rm inv}
=\widetilde g_{111}
-\frac12(g_{101}+g_{110}).
\]

Equivalently,

\[
2g_{111}^{\rm inv}
=(1,1,-1,-1,-2,2)
\]

in edge coordinates. The invariant line is index two relative to a
primitive lift of the top quotient.

For one sign character,

\[
H^1(C_2;\mathbb Z_{\rm sign})\simeq\mathbb Z/2.
\]

The two independent swaps give a pair of such classes, and the displayed
cocycle represents \((1,1)\in(\mathbb Z/2)^2\). Both components are
nonzero because neither invariance equation has an integral solution.

## Coefficient support and connection

Over a characteristic-zero de Rham field, finite-group representations are
semisimple and the invariant half-sum supplies the symmetry-averaged
decomposition

\[
H^1(W)_{\mathbb Q}
\simeq
\mathcal K_{\Delta_{W_1}}
\oplus
\mathcal K_{\Delta_{W_2}}
\oplus
\mathbb Q_{\rm top}.
\]

The two mixed lines have Kummer monodromy \(-1\) around their
source-derived conductor discriminants. Locally their logarithmic
connections may be represented as

\[
\frac12d\log\Delta_{W_1},
\qquad
\frac12d\log\Delta_{W_2},
\]

up to integral-residue gauge. The top quotient has trivial finite
root-swap character.

This rational decomposition does not split the larger sequence

\[
0\to H^2(S_E)\to H^2(S_E\setminus W)
\to H^1(W)(-1)\to0.
\]

It only fixes the quotient connection and removes its internal ambiguity
before the ambient off-diagonal block is computed.

## Deutsch--Popperian verdict

The hard-to-vary conjecture was

\[
\boxed{
\text{the mixed and top grades are three independent integral
Tate/Kummer summands.}
\]

It is falsified. They form a nontrivial integral extension detected by the
two root permutations.

The surviving narrower statement is

\[
\boxed{
\text{the conductor quotient is rationally Tate/Kummer split but
integrally glued by }(1,1)\in(\mathbb Z/2)^2.
}
\]

This is precisely the recurring Marici pattern

\[
\text{resolved occurrence normal}
\longrightarrow
\text{factor two under coarse identification}.
\]

## Classification

\[
\boxed{
\begin{array}{c|c}
\text{structure}&\text{home}\\
\hline
\Delta_{W_1},\Delta_{W_2}
&\text{frozen wall/branch resultants}\\
g_{101},g_{110}
&\text{Kummer conductor coefficient lines}\\
\mathbb Z_{\rm top}
&\text{same-sheet intersection quotient}\\
(1,1)\in(\mathbb Z/2)^2
&\text{integral normalization/conductor extension}\\
\tfrac12(g_{101}+g_{110})
&\text{rational symmetry-averaged correction}\\
\text{new carrier datum}&\text{none}
\end{array}
}
\]

## Limits

This entry does not compute:

- the off-diagonal Gauss--Manin block coupling the conductor quotient to
  \(H^2(S_E)\);
- monodromy when conductor and elliptic discriminants collide;
- extension through soft or signed-energy support;
- the physical relative integration chain;
- the role of \(\mathcal Q\) in the ambient rank-twelve extension.

The rational half-sum is forced by the frozen symmetry, but it must not be
mistaken for an integral or global splitting of the full coefficient
system.

## Exact evidence

- entry 265 for the two node discriminants;
- entry 267 for the primitive cycle basis and saturated filtration;
- entry 279 for the rank-twelve localization extension;
- research/benincasa/two-wall-conductor-monodromy.json.

## Next hostile falsifier

Use the fixed rational quotient frame

\[
(g_{101},g_{110},g_{111}^{\rm inv})
\]

to derive the off-diagonal connection

\[
\Theta\in
\Omega^1\otimes
\operatorname{Hom}
(H^1(W)(-1),H^2(S_E)).
\]

Compute its gauge class using only source residue representatives and the
physical Leray germ. The finite falsifier is a pole of \([\Theta]\)
outside the frozen elliptic, energy, conductor, soft, and
\(\mathcal Q\) supports. Only such a pole can require a new carrier datum.

## Outcome contract

~~~json
{
  "claim": "The mixed and top proper grades are three independent integral Tate/Kummer summands.",
  "status": "falsified",
  "root_swap_group": "C2 x C2",
  "mixed_characters": ["Kummer(Delta_W1)", "Kummer(Delta_W2)"],
  "top_quotient_character": "trivial",
  "integral_extension_group": "(Z/2)^2",
  "integral_extension_class": [1, 1],
  "integral_split": false,
  "rational_split": true,
  "rational_invariant_top_lift": "top_lift-(g101+g110)/2",
  "new_carrier_datum": false,
  "remaining_problem": "ambient rank-twelve Gauss-Manin extension class and physical-chain realization"
}
~~~
