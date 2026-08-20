# The source disk readout has an all-arity dihedral abelian shadow

For the source-normalized open-string disk period, transport the ordered
chamber, Parke--Taylor cocycle, Koba--Nielsen loading, and kinematic labels
simultaneously.  Cyclic rotation preserves the cyclic denominator.  Reversal
reverses its \(n\) oriented factors.  The physical readout therefore has

\[
\chi_n(r)=1,
\qquad
\chi_n(s)=(-1)^n.
\]

These assignments respect

\[
D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle
\]

and define a one-dimensional character.  Consequently every commutator is
killed.  More explicitly,

\[
[D_n,D_n]=
\begin{cases}
\langle r\rangle,&n\text{ odd},\\
\langle r^2\rangle,&n\text{ even},
\end{cases}
\]

and

\[
D_n^{\rm ab}\simeq
\begin{cases}
C_2,&n\text{ odd},\\
C_2\times C_2,&n\text{ even}.
\end{cases}
\]

Thus the physical disk-period readout factors through dihedral
abelianization at every arity.  Odd arity retains the reflection sign; even
arity is trivial on the displayed source readout character.

The exact checker enumerates every element and product for
\(3\le n\le16\), derives each commutator subgroup rather than supplying it,
and verifies that the character kills it.

This theorem concerns simultaneous source transport.  It does not say that
Koba--Nielsen coefficient modules, exceptional Rees grades, or fixed labelled
charts are commutator-blind.  Nor does it construct the missing global pairing
for the six-point exceptional shift module.

Evidence: Ledger Entries 891 and 894--896; checker
`research/nima/check_string_disk_readout_dihedral_all_arity.py`.
