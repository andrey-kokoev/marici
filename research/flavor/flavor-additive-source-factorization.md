# Additive-source factorization (WP343)

## Source theorem

Assume six binary domains have a strictly additive identical one-site source
action, with positive local weights (w_0,w_1), no global constraint, and no
shared latent field. The partition function is

\[
Z=(w_0+w_1)^6,
\]

and the normalized law factorizes with

\[
p=\frac{w_1}{w_0+w_1}.
\]

Every subset coincidence is then forced to be

\[
u_j=p^j.
\]

This exact source theorem excludes the WP342 parity law from the admitted
family and authorizes WP340's first-order sufficiency conditionally on the
grammar.

## What the theorem does not do

The weight ratio remains a free source datum, so factorization does not select
a numerical value of (p). Further, an action that looks additive after
conditioning on a shared mediator need not remain product after that mediator
is marginalized. Global conservation laws can likewise reintroduce dependence.

The no-latent and no-constraint clauses are therefore physical assumptions,
not algebraic conveniences.

## Falsifier and instrument

Any calibrated connected coincidence

\[
u_j-p^j\neq0
\]

falsifies the strict product grammar. At least one higher-order control remains
valuable even when first order is the sufficient identification probe.

Run `uv run --with sympy python
research/flavor/checkers/wp343_additive_source_factorization.py` to regenerate
the exact factorization audit.
