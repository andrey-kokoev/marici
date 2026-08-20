---
title: "The Seven Marked Nodes Generate the Entire Reduced Vanishing Lattice"
date: 2026-08-20
entry: 1179
status: active
sector: cosmology
---

# 1179 — The Seven Marked Nodes Generate the Entire Reduced Vanishing Lattice

Sequence claim: `seqclaim-40e797be2e573550dd694779`.

## Reduced localization map

Let

\[
E=\mathbf Q\langle e_\epsilon:\epsilon\in C_2^3\rangle
\]

be the eight local node occurrences, with the total-parity relation

\[
r=\sum_\epsilon
\epsilon_2\epsilon_3\epsilon_4e_\epsilon.
\]

Entry 1172 gives

\[
V_{\rm van}=E/\langle r\rangle,
\qquad \dim V_{\rm van}=7.
\]

Entry 1178 places precisely the seven nonpositive occurrences on the source
marked divisor. Let

\[
E_D=\langle e_\epsilon:\epsilon\ne(+,+,+)\rangle.
\]

Because the coefficient of \(e_+\) in \(r\) is one,

\[
E_D\cap\langle r\rangle=0.
\]

Therefore the localization map at the reduced node grade is an isomorphism:

\[
\boxed{E_D\xrightarrow{\sim}V_{\rm van}.}
\]

## Positive class

The same relation gives the exact identity

\[
\boxed{
e_+
=-
\sum_{\epsilon\ne(+,+,+)}
\epsilon_2\epsilon_3\epsilon_4e_\epsilon
\quad\text{in }V_{\rm van}.
}
\]

Thus the positive class is nonzero, but it already belongs to the image of
the seven supported classes.

Consequently the ordinary open quotient vanishes:

\[
\boxed{
V_U=V_{\rm van}/\operatorname{im}(E_D)=0.
}
\]

The reduced mapping cone is also acyclic.

## Interpretation

Set-theoretic separation in Entry 1178 does not produce an isolated positive
vanishing cycle in the marked complement. Global topology identifies that
class with a signed combination on marked support.

This explains Entry 1173's failure of the positive coordinate functional to
descend: the positive occurrence cannot be read independently after imposing
the global relation.

Any surviving marked-relative cosmological object must therefore occur in
higher support-sensitive structure:

\[
\boxed{
\text{incidence-depth Čech/Kato extension}
\quad\text{or}\quad
\text{physical relative-chain pairing},
}
\]

not in the reduced node quotient.

## Next falsifier

Use Entry 1178's four incidence-depth profiles to build the labelled local
Čech complex of the seven marked nodes for one representative term of each
profile. Include residue orientations and repeated occurrence labels. Test
whether its map to the total-parity relation has nonzero higher cone
cohomology. A surviving class would be coefficient complexity over the
existing marked carrier; zero cohomology would close the node branch.

## Evidence

- `research/benincasa/checkers/four_site_qg_node_localization.py`
- `research/benincasa/results/four-site-qg-node-localization.json`
- Entries 1172--1173 and 1178.
