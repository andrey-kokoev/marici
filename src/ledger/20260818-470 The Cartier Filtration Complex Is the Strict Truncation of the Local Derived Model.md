---
id: 470
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Cartier Filtration Complex Is the Strict Truncation of the Local Derived Model

## Record

Status: reconciliation of Entries 467--469.

Entry 467 proves that ambient reduction modulo the doubled carrier does not
descend as an ordinary cokernel map. Entry 468 supplies the odd coherence as
the matrix factorization

\[
(-6z,-z/6)
\]

of \(z^2\). Entry 469 identifies the even class as the tautological relation
cell of the Koszul complex

\[
\mathcal K_{z^2}=[\mathcal O\epsilon\xrightarrow{z^2}\mathcal O].
\]

There is also a strict first-Cartier truncation of this local derived model.
For a normalized exact block

\[
E_A=[S\xrightarrow{zA}R],
\qquad R=\mathbb Q[z]/(z^2),
\]

the bare \(z^2\)-presentation cannot receive a strict chain map with ambient
degree-zero reduction when \(A\bmod z\ne0\). After truncation to first
Cartier order, the receiving complex is

\[
P_{\rm Car}=[R/(z)\xrightarrow{z}R],
\]

with source-degree map \(A\bmod z\). Its chain identity is

\[
z(A\bmod z)=zA\pmod {z^2}.
\]

For the resonant blocks, \(A_+=0\) and \(A_-\) is a unit. Thus this strict
complex receives both first-Cartier maps. It is only a truncation:

- on the odd block it forgets the complementary homotopy \(-z/6\);
- on the even block it forgets the unit second-Cartier symbol of the Koszul
  relation.

The finite dual-number audit verifies exactly these strict first-order chain
identities. It does not establish the complete homotopy fiber.

## Classification

- carrier: unchanged doubled equation \(z^2=0\);
- full local associated model: even Koszul cell plus odd matrix factorization;
- strict first-order shadow: \([R/(z)\xrightarrow z R]\);
- remaining datum: global carrier-reduction morphism through the quartic tail;
- new carrier stratum: none.

## Next falsifier

Transport the complete exact complex and carrier-reduction morphism through the
degreewise weighted Rees splitting. Compute its homotopy fiber and test whether
it is quasi-isomorphic to the local Koszul-plus-factorization model, or whether
a nontrivial extension with the quartic tail survives.

## Evidence

- research/benincasa/marici-gm/src/bin/soft_axis_cartier_chain_map.rs;
- Entries 464 and 467--469.
