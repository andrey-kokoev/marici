# The Typed Plus Total Complex Still Has Quadratic Homology

Entries 514--515 construct a finite free
`R=Q[u]/(u^2)`-linear plus subcomplex.  Its middle homology can therefore be
computed without the typing defect of Entry 513.

The scalar component makes `D_0` surjective onto the finite plus quotient
`(B/(K))^+`.  Hence the middle rank is obtained from the target dimension,
the quotient dimension, and the exact matrix rank of `D_{-1}`.  Repeating
the calculation after tensoring the entire complex with `R/(u)` gives the
homology of the actual frozen base change.

\[
\begin{array}{c|r|r}
D&\dim H^0(C_D^+)&\dim H^0(C_D^+\otimes_R R/(u))\\\hline
12&110&69\\
16&196&125\\
20&306&197\\
24&440&285
\end{array}
\]

Writing `n=D/2`, the tested stable laws are

\[
\dim H^0(C_D^+)=3n^2+n-4,
\qquad
\dim H^0(C_D^+\otimes_R R/(u))=2n^2-3.
\]

Their dual-number rank combination is

\[
2\dim H^0(C_D^+\otimes_R R/(u))-\dim H^0(C_D^+)
=n^2-n-2,
\]

which is `28,54,88,130`, not one.

Thus retaining the principal cell, its coherence differential, the full
`u`-action, and the deck-paired plus source repairs the categorical typing
but does not isolate the proposed physical defect.  The labelled
principal-gradient total complex is still too large.  Any further removal
must be derived from additional relative-support geometry; it cannot be
justified as a repair of dual-number descent.

## Evidence

- `research/benincasa/labelled_total_plus_homology.py`
- Entries 513--515.
