# 931 — Integer Exponent Shifts Force a Rank-Eight Symbol Closure

## Admissible transport

Entry 930 excludes a rational differential connection in Koba--Nielsen
exponent space. Integer exponent shifts remain source-derived and rational.
For

\[
A_c=e^{i\pi s_c},
\]

the unit shift \(s_c\mapsto s_c+1\) acts by

\[
A_c\mapsto-A_c.
\]

Apply these sign changes directly to Entry 927's exact six-component source
row \(r\).

## Exact projective test

For the two pivot monodromies,

\[
A_2\mapsto-A_2,
\qquad
A_3\mapsto-A_3,
\]

all five projective minors vanish. In fact each shift acts on the source line
with character \(-1\):

\[
r\longmapsto-r.
\]

The pair-coordinate shifts behave differently:

\[
\begin{array}{c|c}
\text{shift}&\text{nonzero projective minors}\
\hline
B_{24}\mapsto-B_{24}&3\\
B_{34}\mapsto-B_{34}&3.
\end{array}
\]

Thus neither preserves \(\langle r\rangle\).

## Character decomposition

Under the pair-shift deck group

\[
\Gamma_B=(\mathbf Z/2)^2,
\]

the six word coordinates split into four nonzero character supports:

\[
\begin{array}{c|c}
(-,-)&\{0,2\}\\
(-,+)&\{1\}\\
(+,-)&\{3\}\\
(+,+)&\{4,5\}.
\end{array}
\]

Because these supports are disjoint, the orbit span has exact source rank

\[
\boxed{
\operatorname{rank}\langle\Gamma_B r\rangle=4.
}
\]

Tensoring with the established rank-two target gives

\[
\boxed{
\operatorname{rank}\mathcal N_{\rm shift}=2\cdot4=8.
}
\]

## Interpretation

Discrete exponent transport exists, but it does not rescue the proposed
rank-two local system. It canonically enlarges it to an eight-dimensional
shift module. This is stronger than Entry 928's rank-four first-derivative
closure: differential and difference transport expose different finite
associated structures.

No new carrier cell is implicated. The enlargement is entirely in the
Koba--Nielsen coefficient object and is forced by the labelled pair-coordinate
characters.

## Narrow surviving claim

\[
\boxed{
\text{rank-two normal symbol}
\xrightarrow{\text{integer exponent shifts}}
\text{rank-eight coefficient module}.
}
\]

The constant syzygy \(M_x+M_y-M_z=0\) persists on every orbit component
because the same source shift acts on all three branches.

## Next falsifier

Construct the four character-projected rows explicitly and test the
finite-difference cocycle on commuting shifts:

\[
T_{24}T_{34}=T_{34}T_{24}.
\]

Then compare occurrence reflection with the character exchange
\(B_{24}\leftrightarrow B_{34}\). A failure would be a genuine coefficient
coherence obstruction; success would produce the first source-derived
horizontal replacement for the rejected rank-two connection.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_shift_transport.rs;
- packet:
  research/benincasa/string-six-point-shift-transport.json;
- allocator claim:
  seqclaim-6652a87e46c2622f629d2861.
- epistemic event:
  ev-000000000548-f599fcf5-0974-4852-916c-28b58db4c805.
