# 1747 — Unipotent Reference Holonomy Survives Only in the Matched Character

## Extension-class test

Entry 1746 gives graded reference lines \(L_1,L_2\). Their relative Hom line
has character

\[
\chi=\sigma_1\sigma_2.
\]

A unipotent parabolic loop is represented by a shear cocycle \(a\). Changing
the local lift of the quotient line by \(b\) changes it by

\[
a\longmapsto a+(\chi-1)b.
\]

Hence the intrinsic extension space is

\[
\boxed{
H^1(S^1,\operatorname{Hom}(L_2,L_1))
=\operatorname{coker}(\chi-1).
}
\]

For matched line holonomies, \(\chi=1\), every lift change leaves \(a\)
unchanged and the extension space has rank one. The unipotent shear is then a
genuine filtered-local-system invariant.

For opposite line holonomies, \(\chi=-1\), the map \(\chi-1=-2\) is
invertible over \(\mathbb Q\). The change \(b=a/2\) removes every shear, so
the extension space vanishes rationally.

## Narrow result

\[
\boxed{
\text{A parabolic shear is intrinsic exactly in the trivial relative character.}
}
\]

Thus repeated-weight singular references can carry information beyond their
associated graded, but only as a sector-specific coefficient extension. No
new Cut carrier stratum is required.

The rational qualification matters: with an integral lattice, the opposite
character may leave a \(\mathbb Z/2\) torsion class. That has not been tested.

## Durable artifacts

- `research/benincasa/checkers/unipotent_parabolic_extension.rs`
- `research/benincasa/results/unipotent-parabolic-extension.json`
- `research/benincasa/unipotent-parabolic-extension.md`

## Next falsifier

Restore the integral reference lattice. Determine whether the opposite
relative character carries the predicted \(\mathbb Z/2\) extension and
whether the physical Born/readout pairing detects or annihilates it.
