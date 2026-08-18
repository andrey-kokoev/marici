---
authors:
  - marici.Nima
date: 2026-08-18
---
# 739 — The Certified Corner Packet Does Not Yet Define the Total Bicomplex

## Audit after Entries 736 and 738

Commit `1387762` certifies the local augmented corner maps and materializes
them in

`research/benincasa/marici-gm/gysin-resolved-local-maps.packet`.

The packet fixes:

- the extension-coordinate order \((00,01,10,11)\);
- the augmented source order \((k_1,k_2,p)\);
- two quadratic kernel bases and their Galois involutions;
- the simple-crossing principal columns;
- the weighted principal columns before and after the unnormalized
  \(\mu_2\)-trace;
- the relevant chart transitions.

This is enough to reproduce the horizontal principal-line matrix of Entry
738.  It is not enough to construct the total bicomplex required by Entry
735.

## Missing typed data

The certified packet has no fields specifying:

1. the cochain degree of each homogeneous and principal source generator;
2. the complete internal differential on each vertex complex \(V_i^\bullet\);
3. the complete internal differential on each edge complex
   \(E_{ij}^\bullet\);
4. the target degree and basis label of each exported principal column;
5. the adjacent-degree matrices needed to verify
   \[
   \partial_{ij}r_{i,ij}=r_{i,ij}\partial_i;
   \]
6. the total-degree matrices immediately before and after the degree
   containing the horizontal class \(\lambda\).

In particular, the displayed vector \(C_E\) is a corner-coherence column in
an ambient four-coordinate presentation.  The packet does not state whether
it is an internal cycle, an internal boundary, or the image of the internal
differential of the principal cell.

## Consequence for the candidate line

Entry 738 proves

\[
\operatorname{coker}\delta_{\rm pr}
=\mathbb Q\langle\lambda\rangle,
\qquad
\lambda=x_{12}-x_{13}+x_{23}.
\]

But the two total-cohomology questions

\[
D\lambda=0,
\qquad
\lambda\notin\operatorname{im}D
\]

cannot be evaluated from the certified packet.  Assigning zero internal
differentials would be an additional model choice and would tautologically
make the horizontal line survive.  It is therefore forbidden.

The current conclusion is

\[
\boxed{
\text{canonical horizontal line}
\quad\text{but no defined total-cohomology class yet}.
}
\]

## Minimal completion contract

The next packet version must export each \(V_i^q\) and \(E_{ij}^q\) by
degree, all matrices \(\partial_i^q\) and \(\partial_{ij}^q\), and every
degreewise restriction matrix \(r_{i,ij}^q\).  A checker must then verify

\[
\partial^2=0,
\qquad
\partial r=r\partial,
\qquad
D^2=0,
\]

before reporting the kernel, image, and cohomology dimensions in the total
degree containing \(\lambda\).  The computation should use the certified
exact coefficients; replacing SymPy by Symbolica is implementation-neutral
provided the exported typed matrices agree.

## Evidence

- `gysin-resolved-local-maps.packet` at commit `1387762`;
- Entries 735, 736, and 738;
- allocator claim `seqclaim-78e47d4ea77db479084f6809`;
- epistemic event `ev-000000000353-2f10131e-db36-4d6c-9a32-769ac059a761`.
