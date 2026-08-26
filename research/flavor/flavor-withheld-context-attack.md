# Withheld-context attack (WP397)

## Bounded question

Can finitely many aligned response contexts establish the DPC claim that every
admissible context factors through one common channel?

## Invisible completion

Let the tested contexts be $c=0,1,2$ and let the observed response direction
be constant,

\[
v(c)=(1,0)^T.
\]

For any nonzero $\epsilon$, define the alternative

\[
w(c)=\left(1,\epsilon c(c-1)(c-2)\right)^T.
\]

The two theories agree exactly at all three tested contexts. Each response is
rank one at every context. At the withheld context $c=3$,

\[
w(3)=(1,6\epsilon)^T,
\]

and the joint Gram determinant with the original direction is

\[
\det(vv^T+w(3)w(3)^T)=36\epsilon^2>0.
\]

Thus no finite collection of aligned contexts proves universal alignment when
arbitrary context dependence remains admissible.

## Bounded-grammar repair

The attack is relative to the functional grammar. If source dynamics
independently restricts the transverse response to a polynomial of degree at
most two, its values at $0,1,2$ determine it exactly. The corresponding
Vandermonde determinant is $2$, and vanishing at all three points forces every
coefficient to vanish.

Therefore finite testing becomes decisive only after the source theory freezes
a complexity bound. Three contexts rule out quadratic rotation but not cubic
rotation. More observations without a source bound merely move the first
unconstrained completion to higher degree.

## Deutschian consequence

A hard-to-vary constructor must specify the admitted context dependence before
the alignment data are inspected. It must then reserve an executable context
whose response is predicted without coefficient refitting. Cross-validation
is not a substitute for source derivation, but it blocks the simplest lookup
completion.

The common-frame transport remains part of the instrument. If contexts are
compared only after a fitted parallelization, the withheld test is again
circular.

## Disposition

WP397 falsifies universal channel coherence inferred from finitely many
contexts without a source grammar. It also gives the exact repair: a
preregistered finite-dimensional response class and enough calibrated
contexts to determine it, followed by a genuinely withheld test.

The smallest falsifier is the cubic completion above. The remaining gate is a
microscopic action that fixes the response class and makes the withheld
context physically executable.

Run `uv run --with sympy python
research/flavor/checkers/wp397_withheld_context_attack.py` to regenerate the
result.
