---
id: 392
date: 2026-08-17
title: Physical Realization Is a Recollement Morphism
---

# Physical Realization Is a Recollement Morphism

Entry 391 identified logarithmic simple-pole residue as the integral closed
coefficient operation. It cannot, and should not, retain the generic
\(q_{03}^{Q}\) state: residue is supported on \(Z=V(x_3)\), so its restriction
to the open set \(U=D(x_3)\) is zero.

Therefore physical realization is not one functor applied uniformly to the
raw packet. It is a morphism of localization triangles.

## The two forced boundary components

On \(U\), the first-Rees bridge of Entries 383--387 supplies the generic
component. Its coefficient is
\[
 k=x_3,
\]
which is a unit on \(U\), and its image retains the nonzero
\(q_{03}^{Q}\) leg.

On \(Z\), the finite Cartier packet and the logarithmic lattice of Entries
377 and 391 supply the closed component:
\[
 \operatorname{res}_{x_3}(d\log x_3)=+1.
\]
The \(x_4\) support line has already been projected away. Fine grading and
positive Cartier normalization leave no scalar freedom in either component.

They must be assembled in
\[
\begin{array}{ccccccc}
i_*i^!\mathcal S&\to&\mathcal S&\to&j_*j^*\mathcal S
 &\xrightarrow{\delta_{\mathcal S}}&i_*i^!\mathcal S[1]\\
\downarrow\alpha_Z&&\downarrow\alpha&&\downarrow\alpha_U&&
\downarrow\alpha_Z[1]\\
i_*i^!\mathcal E&\to&\mathcal E&\to&j_*j^*\mathcal E
 &\xrightarrow{\delta_{\mathcal E}}&i_*i^!\mathcal E[1].
\end{array}
\]

## The sole remaining cell

For the source relation
\[
 dH_{03}=q_J-x_3\widetilde\xi_{03},
\]
the gluing condition is exactly the Entry-160 Beck--Chevalley homotopy
\[
 \delta_{\mathcal E}\alpha_U(q_J)
 \simeq
 \alpha_Z[1](-[\widetilde\xi_{03}]).
\]

Both sides of this homotopy are now independently fixed: the left by the
generic first-Rees bridge and the right by the positive logarithmic Cartier
residue. Thus no coefficient remains to search.

Entries 387--388 show that the endpoint-relative deformation group vanishes.
Consequently, if this Beck--Chevalley cell exists, it is unique up to
admissible homotopy and automatically has the required reflection parity.
They do not prove its existence.

## Updated frontier

The realization problem has reduced to one geometric question:

> Does the marked middle-corner log blowup induce the displayed
> Beck--Chevalley homotopy between its independently fixed open and closed
> boundary maps?

The next calculation should evaluate the two boundary composites on the
primitive weighted broken-path carrier
\[
 X_1E_{13}+X_{D_{03}}E_{D3}
\]
inside the expanded pentagon. Equality gives the cell and hence the
one-road realization; inequality is a concrete obstruction.

The executable audit is
research/voevodsky/check_d03_recollement_realization_gate.py.
