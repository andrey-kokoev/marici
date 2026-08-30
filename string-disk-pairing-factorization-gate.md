# String Disk Pairing Factorization Gate

The established all-arity disk readout character is

\[
\chi_n(r)=1,
\qquad
\chi_n(s)=(-1)^n.
\]

To use it as cross-sector evidence for the paired coefficient--Betti
architecture, one would need source-typed characters
\(\chi_{\rm coeff}\) and \(\chi_{\rm Betti}\) with

\[
\chi_n=\chi_{\rm coeff}\chi_{\rm Betti}.
\]

The combined character does not determine those factors.  The rational
rank-one character group of \(D_n\) has order two for odd \(n\) and four
for even \(n\).  For every target character, multiplication admits exactly
that many ordered factorizations.  Hence the disk character has:

\[
2 \text{ factorizations at odd arity},
\qquad
4 \text{ factorizations at even arity}.
\]

The checker exhausts \(3\le n\le16\) and verifies every factorization.

Therefore

\[
\boxed{
\text{the combined scalar disk character is insufficient to establish a
source-typed paired readout.}
}
\]

This does not challenge the all-arity abelian-shadow theorem.  It blocks only
the stronger cross-sector inference.  Admission requires independently
transporting the Parke--Taylor/Koba--Nielsen de Rham class and the ordered
twisted chamber cycle, then verifying their pairing.

Artifacts:

- `research/nima/check_string_disk_pairing_factorization.py`
- `research/nima/results/string-disk-pairing-factorization.json`
