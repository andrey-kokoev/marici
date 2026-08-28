# Contextual Smith traces recover the bounded magnetic grade

## Construction

For each grade (n), define its radius-(r) contextual Smith trace

\[
F_r(n)=\bigl(R(n-r),\ldots,R(n),\ldots,R(n+r)\bigr).
\]

This uses the authorized free-group continuation action. Equality of complete traces,

\[
n\sim m
\quad\Longleftrightarrow\quad
R(n+k)=R(m+k) 	ext{for every }k\in\mathbb Z,
\]

is automatically a constructor congruence: the grade action becomes shift on the trace.

## Bounded result

On the center interval (-20\le n\le20):

- the radius-zero packet has only six classes;
- the class counts increase monotonically as
  [
  6,15,19,23,26,29,32,35,38,40,41;
  ]
- radius ten separates all 41 grades.

The last unresolved pair at radius nine is ((-20,7)), separated by 27. One additional continuation layer distinguishes it.

## Explanation

This supports a different repair from adding a difference port. The source grade already carries the distinction; the unary valuation packet discards it. Authorized contexts recover it.

The canonical candidate explanatory state is therefore the orbit trace

\[
F(n)=\bigl(R(n+k)\bigr)_{k\in\mathbb Z},
\]

with constructor action given by shift. This is a dependent incidence object: it retains which observation belongs to which source continuation. Flattening it to the set of packet values destroys exactly the incidence highlighted by Kitaev's dependent-bundle transfer.

## Claim boundary

The bounded separation does not prove that (F) is injective on all of (mathbb Z). Promotion requires an unbounded source theorem showing that no nonzero translation is a period of the valuation sequence.

If that theorem holds, the minimal future-equivalence quotient is the full grade orbit. If a nonzero period exists, the quotient is the corresponding periodic source factor.

## Next theorem

Prove or falsify

\[
R(n+p)=R(n) 	ext{for every }n
\quad\Longrightarrow\quad
p=0.
\]

This is sharper than searching for additional finite germs. It asks whether the complete contextual observation has any nontrivial translation symmetry.

## Evidence

- Checker: `research/strominger/checkers/future_equivalence_checks.py`
- Result: `research/strominger/results/future_equivalence_checks.json`
- Execution: `structured_command_execution:e_2512_1787935576551053700_27`
