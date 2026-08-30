# 2906 — Carrier Cut Sewing Does Not Yet Type the Pointed Kummer Torsor Map

## Global sewing question

Entry 2905 produces a pointed Kummer torsor for one frozen source graph.  To
sew two such objects across a Cut requires a map

\[
S_{\rm Cut}:
\mathcal T_L\boxtimes\mathcal T_R
\longrightarrow
\mathcal T_G.
\]

The map must be derived from the composite source integrand and intertwine the
three affine monodromy representations.

## What the Carrier supplies

The occurrence-resolved Cut carrier supplies the physical diagonal
identification of the two interface occurrences.  Each local source chain also
supplies its own affine origin:

\[
F_L(2)=0,
\qquad
F_R(2)=0.
\]

These data type the base variables and point the two input torsors separately.
They do not define a map into a composite coefficient torsor.

## Finite underdetermination test

Even after imposing additivity, left-right symmetry, and preservation of the
pointed origin, the family

\[
S_c(P_L,P_R)=c(P_L+P_R)
\]

survives for arbitrary nonzero rational \(c\).  Distinct values of \(c\) give
distinct outputs while respecting every presently frozen condition.

Selecting \(c=1\), or adjoining a contact correction, would therefore be a
choice of coefficient adapter rather than a consequence of Carrier Cut
sewing.

## Result

The global test is currently untyped:

- shared Carrier Cut sewing exists;
- each local Kummer torsor is canonically pointed;
- the composite coefficient-torsor sewing map is absent.

Consequently there is not yet a canonical sewing theorem, but neither is there
a defined mismatch obstruction.  A mismatch class can be formed only after
the source-derived map \(S_{\rm Cut}\) exists.

This is evidence for the refined H2 architecture: shared carrier and calculus
do not automatically identify sector-specific coefficient adapters.

## Next admissible move

Freeze the smallest composite cosmological source integral containing two
such marked soft subgraphs.  Derive its Cut factorization before reducing
either side to finite parts, then read off the induced map on the two pointed
Kummer torsors.  Reject any map selected solely by symmetry, normalization, or
the desire to eliminate a mismatch.

## Durable artifacts

- `research/benincasa/check_pointed_kummer_cut_sewing_typing.py`
- `research/benincasa/pointed-kummer-cut-sewing-typing.json`
