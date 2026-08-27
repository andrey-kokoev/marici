# Three deeper layers of the relational calculus

## Question

What breaks if the current kernel-descent compiler is treated as the complete
calculus rather than its linear first layer?

## Layer one: kernels are only the linear shadow of fibers

Take the nonlinear completion and target

\[
q(x)=x^2,
\qquad
r(x)=x^3.
\]

At every nonzero point, the differential of `q` has trivial kernel. At zero,
both differentials vanish on the tangent direction. Thus the local
differential-kernel test finds no obstruction.

Globally,

\[
q(-1)=q(1)=1,
\qquad
r(-1)=-1\ne1=r(1).
\]

Therefore `r` does not descend through `q`. The true general criterion is
constancy on complete fibers:

\[
q(x)=q(y)\Longrightarrow r(x)=r(y).
\]

Kernel annihilation is exact for linear quotients and multilinear relations.
Outside that setting it is an infinitesimal diagnostic, not the theorem.

## Layer two: binary mates can miss native ternary relations

Consider uniform distributions on the even- and odd-parity triples. Every
one-body and two-body marginal is identical between them. Their triple parity
expectations are `+1` and `-1`.

Consequently, completing all three pairwise relations before asking the
three-way question destroys the target even though every binary audit passes.

The general architecture is therefore a relational hypergraph or operadic
tree, not necessarily a binary tree. A target of native arity three requires:

- a direct ternary mate; or
- binary intermediate mates that retain the complete three-instance carrier
  and its associator data until final sewing.

The formula `n(2+1)+(n-1)` is only safe when binary factorization has been
proved coherent for the declared target.

## Layer three: descent is not selection

Let the source fiber contain two points `a,b`, both completed to one point
`star`. A constant relation descends perfectly through this quotient. There
are nevertheless two sections selecting a source representative:

```text
star -> a
star -> b
```

If the source admits the symmetry swapping `a` and `b`, neither section is
invariant. Descent authorizes a quotient observable. It does not choose a
realization.

This is the abstract core of the flavor obstruction: even a correct
carrier-level completion and descended detector law do not supply the missing
source selector.

## Revised compiler

The deeper calculus has three separate gates.

### Fiber gate

Test whether the target is constant on the full equivalence relation generated
by the proposed completion. Use kernel contractions only when linearity makes
them equivalent to the fiber test.

### Arity gate

Test the target at its native arity. Do not infer an `n`-way relation from all
lower-order marginals unless a factorization or reconstruction theorem is
already available.

### Authority gate

After descent, ask separately whether the quotient is faithful enough for
reconstruction and whether a source law supplies a canonical realization
section. Neither follows from descent.

## Deeper unit statement

The marked carrier germ is not an absolute atom. It is an interface object
relative to a declared target family. Type, identity, provenance, and open
ports are retained only to the extent required to keep that family defined.
Changing the target family can refine or coarsen the admissible unit.

The genuinely primitive datum is therefore not a thing but a distinction that
must remain available for a declared transformation.

## Disposition

The kernel compiler survives as the exact linear layer. The full calculus is
fiberwise, higher-arity, and authority-sensitive. This strengthens rather than
discards the previous hostile proofs, all of which were linear and therefore
inside the exact kernel regime.

## Verification

Run:

```text
python research/aspect/checkers/check_deeper_relational_calculus_layers.py
```
