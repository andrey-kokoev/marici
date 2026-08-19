# 980 — The Exceptional Cochain Has the Existing Four-Character Shift Closure

## Correct transport category

Entry 979 proposed differential horizontality as its next test. Entries
929–930 already exclude that test in the frozen rational word frame: exponent
differentiation produces digamma/logarithmic insertions. The smallest
source-derived transport is instead the integer exponent shift

\[
s_c\mapsto s_c+1,
qquad
A_c\mapsto-A_c.
\]

Apply these shifts to Entry 977's exact six-component cochain \(\lambda\).

## Pivot characters

Exact reduction gives

\[
T_{A_2}\lambda=-\lambda,
qquad
T_{A_3}\lambda=-\lambda.
\]

Thus the two pivot shifts preserve the line with the same character already
found for the source row in Entry 931.

## Pair-shift closure

Let (T_{24}) and (T_{34}) negate (B_{24}) and (B_{34}),
respectively. Form the four character projectors

\[
\lambda_{\epsilon\eta}
=
\sum_{a,b\in\{0,1\}}
\epsilon^a\eta^bT_{24}^aT_{34}^b\lambda.
\]

All four are nonzero and obey their defining characters exactly. Therefore

\[
\boxed{
\operatorname{rank}
\langle T_{24},T_{34}\rangle\lambda=4,
}
\]

with one copy of each character

\[
(++),quad(-+),quad(+-),quad(--).
\]

This is the regular representation of ((\mathbb Z/2)^2), exactly the
character set of Entry 931's source shift closure.

## Narrow conclusion

\[
\boxed{
\text{The exceptional cochain introduces no new integer-shift character.}
}
\]

Its admissible finite-difference closure is the same rank-four deck
representation already required by the six-word source row. Thus the global
cochain comparison is compatible with the established discrete coefficient
architecture; no additional carrier or coefficient sector is forced here.

This does not identify the two rank-four modules canonically, and it does not
restore a rational differential connection.

## Next falsifier

Construct the characterwise comparison between the source-row shift module
and the exceptional-cochain shift module. Since every character has
multiplicity one, each block is a scalar. Derive those four scalars from the
loaded evaluation map and test whether they are regular units on their
generic character supports. A vanishing or pole not already declared would
be a genuine discrete-comparison defect.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_exceptional_cochain_shift.rs;
- packet:
  research/benincasa/string-six-point-exceptional-cochain-shift.json;
- verified command:
  cargo run --quiet --bin string_six_point_exceptional_cochain_shift;
- allocator claim:
  seqclaim-3546fe970cf67a709995b213.
- epistemic event:
  ev-000000000597-cdc4c347-cdd3-4226-a17f-297bf7d377f1.
