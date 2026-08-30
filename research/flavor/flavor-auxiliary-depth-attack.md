# Auxiliary-depth attack on context bounds (WP398)

## Bounded question

Does restricting every local source interaction to polynomial degree at most
four make WP397's finite-context alignment test decisive?

## Quartic compilation of the cubic loophole

Introduce two auxiliary gate variables and positive weights:

\[
V=a\bigl(z-c(c-1)\bigr)^2
+b\bigl(w-z(c-2)\bigr)^2.
\]

Every term has total polynomial degree at most four. The exact zero-energy gate
solution is

\[
z=c(c-1),
\qquad w=c(c-1)(c-2).
\]

The auxiliary Hessian is positive definite, with

\[
\det H_{\mathrm{aux}}=4ab>0.
\]

Coupling the transverse response to $\epsilon w$ reproduces WP397 exactly: it
vanishes at contexts $0,1,2$ and equals $6\epsilon$ at context $3$. The
withheld joint determinant remains $36\epsilon^2$.

## General obstruction

Sequential multiplication gates can compile products with arbitrarily many
zeros while keeping each gate penalty quartic. Increasing auxiliary count and
circuit depth raises effective context degree without raising local vertex
degree.

Therefore locality or a degree-four scalar presentation alone does not bound
the response class tested in WP397. Calling the gates renormalizable would
add further assumptions about spacetime dimension, kinetic terms, field
dimensions, and gauge representations; none is supplied by the abstract
circuit.

## Required source bound

A decisive finite-context test needs a source-authorized bound on the complete
constructor grammar, including:

- number and representations of auxiliary fields;
- circuit depth and topology;
- allowed threshold states;
- derivative order and nonlocal kernels;
- RG closure of the bounded class.

These data must be frozen before choosing the tested contexts. Otherwise every
new observation can be absorbed by another stable gate.

## Disposition

WP398 refutes local polynomial degree as a sufficient hard-to-vary criterion.
It does not refute WP397's bounded-class repair; it identifies the stronger
class datum that must be bounded. The smallest exact falsifier is the two-gate
quartic compilation of the cubic withheld completion.

The next gate is a physically derived finite mediator grammar whose complete
effective response dimension can be calculated before the withheld test.

Run `uv run --with sympy python
research/flavor/checkers/wp398_auxiliary_depth_attack.py` to regenerate the
result.
