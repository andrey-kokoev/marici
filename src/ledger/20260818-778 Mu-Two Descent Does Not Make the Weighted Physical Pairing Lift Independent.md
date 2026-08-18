---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 778 — Mu-Two Descent Does Not Make the Weighted Physical Pairing Lift Independent

## Hard-to-vary claim

After Entry 774 proves that the cyclic algebraic--elliptic extension is
rationally nonsplit, test the first admissible physical promotion:

\[
\boxed{
\text{weighted nearby specialization}
\longrightarrow
\mu_2\text{-trace}
\longrightarrow
\text{pairing with the nonsplit extension}
}
\]

must be independent of the admissible weighted lift of the Bunch--Davies
relative chain.  Without that independence there is no canonical physical
pairing and hence no supported comparison cone.

## Typed coefficient restriction

At the weighted crossing

\[
D_2\cap D_3:(u,y)=(0,0),
\]

use

\[
U_u:y=u^2t,
\qquad
U_y:u=es,\ y=e^2,
\qquad t=s^{-2}.
\]

After the forced shear \((0,0,4,2)\), the exceptional restriction of the
nonsplit extension block in the common extension-coordinate order is

\[
\boxed{
C_{E,u}^{\rm exc}(t)
=
\frac{1}{2(t^2-1)}
\begin{pmatrix}0\\-1\\0\\3\end{pmatrix}.
}
\]

On the stack chart it is

\[
C_{E,y}^{\rm exc}(s)
=
\frac{1}{2(s^4-1)}
\begin{pmatrix}0\\1\\0\\-3s^2\end{pmatrix}.
\]

The target-row transition inherited from

\[
\operatorname{diag}(1,1,s^{-4},s^{-2})
\]

carries the first expression with \(t=s^{-2}\) exactly to the second.
Therefore the coefficient-side overlap homotopy is zero.  This was checked
by exact rational arithmetic on five overlap points.

Both nonzero components are even under

\[
s\longmapsto-s.
\]

The mandatory unnormalized finite trace therefore doubles the section; it
does not kill it.

## Weighted Bunch--Davies lifts

Entries 749 and 751 derive the admissible family

\[
u=-i\varepsilon,
\qquad
y=-ic\varepsilon^2,
\qquad
t=ic,
\qquad c>0.
\]

Evaluating the traced extension restriction gives

\[
\boxed{
\operatorname{Tr}_{\mu_2}C_{E,u}^{\rm exc}(ic)
=
\frac{1}{1+c^2}
\begin{pmatrix}0\\1\\0\\-3\end{pmatrix}.
}
\]

In particular,

\[
c=1:
\begin{pmatrix}0\\1/2\\0\\-3/2\end{pmatrix},
\qquad
c=2:
\begin{pmatrix}0\\1/5\\0\\-3/5\end{pmatrix}.
\]

Thus the coefficient restriction, chart transition, and \(\mu_2\)-trace are
all explicit, but they retain the unfixed weighted tangent.

## Missing chain datum

A physical scalar would require an exceptional boundary current

\[
\partial_E\widetilde\Gamma_c
\]

whose dependence on \(c\) canonically compensates the displayed factor.
The frozen relative-chain package supplies no such current and no overlap
homotopy for chain lifts.  Entries 746--751 prove that neither the
Bunch--Davies signs, the regulator hierarchy, nor fiber sector decomposition
selects one.

Consequently the requested pairing is not a defined scalar:

\[
\boxed{
\langle
\partial_E\widetilde\Gamma,
C_E^{\rm exc}
\rangle
\text{ is lift-dependent with the available data.}
}
\]

This is neither a vanishing result nor a surviving physical class.  Assigning
either value would choose the absent chain current post hoc.

## Consequences

- the rationally nonsplit extension of Entry 774 is established coefficient
  data;
- its weighted coefficient restriction and \(\mu_2\)-descent are canonical;
- its physical relative-chain pairing is not canonical;
- no supported comparison cone
  \(\operatorname{Cofib}(\Phi_{\rm phys})\) is yet defined;
- therefore a \(\mathcal Q\)-support test on that cone is not authorized.

No new carrier datum is indicated.  The missing input remains a
sector-specific relative-cycle specialization.

## Evidence

- `research/benincasa/check_weighted_extension_chain_pairing_gate.py`;
- `research/benincasa/weighted-extension-chain-pairing-gate.json`;
- Entries 730--732, 736, 746--752, and 774;
- allocator claim `seqclaim-4c7d09f2b8922f4791cc6636`.
- epistemic event
  `ev-000000000393-634c0b30-ca0a-4d32-9c83-02201bf8e985`.

## Next falsifier

Acquire an independently defined weighted relative chain current, for
example from a parameter-space thimble construction.  Before pairing, test
that two admissible presentations induce the same traced exceptional current
under the displayed overlap transition.  Only a lift-independent current
may define \(\Phi_{\rm phys}\), its supported cone, and a subsequent
\(\mathcal Q\)-support calculation.
