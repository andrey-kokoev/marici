---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2140 — The Minimal Kummer Twist Produces a Nonsplit Extension, Not an Identification

> **Scope correction from Entry 2143.** The abstract one-wall twist statement
> remains valid. It does not classify the tensor-product mixed variation of
> the actual all-deleted contact term.

## Hard-to-vary claim

There is a unique rank-one monodromy character that can align the deletion
contact with the lower Kummer line, but applying it does not identify their
coefficient objects.

## Minimal character

Entry 2139 gives

\[
T_{\log}=
\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
T_{\rm Kum}=-1.
\]

For a rank-one character \(\chi\), matching the semisimple eigenvalue requires

\[
\chi=-1.
\]

The twisted contact monodromy is therefore forced to be

\[
T_{\log}\otimes\chi
=
\begin{pmatrix}-1&-1\\0&-1\end{pmatrix}.
\]

Its nilpotent part remains nonzero and has rank one. Hence the twisted contact
object is a nonsplit self-extension

\[
0\longrightarrow\mathcal K_-
\longrightarrow\mathcal L_{\log}\otimes\mathcal K_-
\longrightarrow\mathcal K_-
\longrightarrow0,
\]

not a rank-one Kummer system.

## What the twist permits

The equation for a horizontal map from \(\mathcal K_-\) into the twisted
logarithmic block has a one-dimensional solution: the invariant line. Thus
the twist permits a unique projective Kummer subline and a Kummer quotient.
It does not choose between them, split the extension, or provide a
source-normalized comparison map.

## Consequence

\[
\boxed{
\text{matching monodromy characters is necessary but insufficient for a
cross-sector identification.}
}
\]

Even the strongest minimal repair still requires two independently derived
data:

1. the occurrence/Kummer twist itself;
2. a typed injection, quotient, or splitting selected by the source.

Neither is supplied by the additive deletion adapter. Introducing both only
to reproduce the lower line would be a prohibited post-hoc repair.

## Classification

- carrier wall: unchanged \(\nu_i=0\);
- admissible abstract twist: uniquely \(\mathcal K_-\);
- resulting coefficient: nonsplit rank-two Kummer self-extension;
- identification with the lower line: absent;
- new carrier datum: none.

## Evidence

- Entries 2138--2139;
- `research/benincasa/checkers/twisted_contact_extension.rs`;
- allocator claim `seqclaim-b752ff987168c64fe0d948fd`.

## Next falsifier

Audit the frozen occurrence and residue orientations for a pre-existing sign
local system on the deletion contact. If none is present, close the twist
route. If one is present, derive its map into the twisted logarithmic block
before choosing the invariant line or quotient.
