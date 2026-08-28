# The Eta-Squared Residue Has an Explicit Artin Block Word

## Result

The presentation compiler left open in the preceding packet closes in the
standard pure-braid generators. Bardakov and Wu define the simplicial injection

\[
\Theta:F[S^1]\longrightarrow AP_*,\qquad AP_n=P_{n+1},
\]

from the seed

\[
c_{11}=\sigma_1^{-2}=A_{12}^{-1}
\]

by strand doubling. Its degree-three generators are

\[
c_{31}=s_1s_0c_{11},\qquad
c_{22}=s_2s_0c_{11},\qquad
c_{13}=s_2s_1c_{11}.
\]

Comparison of their deletion tables with Mikhailov's degree-three basis gives

\[
x_0=c_{31},\qquad x_1=c_{13},\qquad x_2=c_{22}.
\]

Hence the exact pure four-braid representing the five-point residue is

\[
W_{\eta^2}=[[c_{31},c_{13}],[c_{31},c_{22}]].
\]

The fifth marked point is the fixed point at infinity. Thus a pure four-braid
in the disk is a five-marked-point spherical configuration.

## Artin expansion

With products written in stacking order, block cabling gives

\[
\begin{aligned}
c_{31}&=A_{34}^{-1}A_{24}^{-1}A_{14}^{-1},\\
c_{13}&=A_{14}^{-1}A_{13}^{-1}A_{12}^{-1},\\
c_{22}&=A_{24}^{-1}A_{14}^{-1}A_{23}^{-1}A_{13}^{-1}.
\end{aligned}
\]

Substitution into \(W_{\eta^2}\) produces a freely reduced word of length 52
in the standard \(A_{ij}^{\pm1}\) alphabet. The machine-readable result records
the complete expanded list rather than printing an error-prone display.

## Literal deletion audit

Deleting a strand sends every \(A_{ij}\) incident to it to the identity and
reindexes the remaining letters. The cabling words obey

\[
\begin{array}{c|ccc}
 &c_{31}&c_{13}&c_{22}\\
\hline
d_1&c_{21}&1&c_{12}\\
d_2&c_{21}&c_{12}&c_{12}\\
d_3&c_{21}&c_{12}&c_{21}\\
d_4&1&c_{12}&c_{21}.
\end{array}
\]

Each deletion therefore kills one inner commutator or identifies the two inner
commutators. All four expanded deletion words freely reduce to the identity.
No braid relation is required for this audit.

## Claim boundary

The exact finite-strand representative is now compiled. Its nontriviality in
the filling quotient is not inferred from the nonempty Artin word or from its
four deletion identities. It remains certified by the independent
identification

\[
[W_{\eta^2}]=\eta\circ\Sigma\eta\ne0
\quad\text{in}\quad
\pi_4(S^2)\cong\mathbb Z/2.
\]

This is precisely the two-gate architecture required by Aspect's frozen law:
presentation checks establish a strict Brunnian braid, and the invariant
filling quotient establishes the residue.

## Replay

```powershell
uv run python research/strominger/checkers/eta_squared_artin_braid_expansion_checks.py
```
