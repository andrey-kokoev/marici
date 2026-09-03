# A presented index category makes residual holonomy enumerable

## Question

How can the global residual-period condition be checked without quantifying independently over every path?

## Generators

On the rational observer skeleton, present the index category using these typed generators:

1. packet inclusion, permutation, and repetition;
2. rational translation;
3. rational heat-semigroup step;
4. derivative-order increment;
5. arithmetic cutoff enlargement;
6. prime-derived to completed comparison;
7. Mellin, Fourier, and theta comparison arrows where already source-defined.

The list is countable. Each generator carries its edge residual and transport map.

## Relations

Declare only source-proved relations, including:

- associativity and identity for packet maps;
- translation group composition;
- heat-semigroup composition;
- commutation of heat and translation;
- heat-generator versus second-translation-derivative identity;
- naturality of packet restriction;
- cutoff composition and cutoff/observer interchange;
- equality of the admitted completion routes.

Each relation gives a finite parallel-path curvature test.

## Tree potentials and fundamental periods

Choose a root presentation and a spanning family of preferred paths. Transporting residuals along a preferred path defines a candidate potential `s_i` at every reachable object.

For each generating arrow not used by the preferred family, compare:

1. the preferred path to its source followed by that arrow;
2. the preferred path to its target.

The difference is a fundamental period. If all such periods vanish and all declared relation cells commute, the candidate potentials trivialize the residual cocycle on the generated category.

For invertible parameter symmetries this is the usual spanning-tree basis of loops. For noninvertible cutoff and restriction arrows, the test is formulated as a pair of parallel directed paths rather than by inserting a formal inverse.

## Residual ledger

A meta-observer record for one generator or relation should contain:

\[
(\text{source},\text{target},\text{path words},
\Omega,\kappa,\text{tail bound},
\text{completion trivializer},\text{status}).
\]

Path words make composition reproducible. The completion trivializer must be the same endpoint--gamma zero-cochain throughout; a different correction per loop is not descent.

## Completeness boundary

This reduction is valid only after proving that the declared generators and relations present the intended observer category. Omitted Mellin branches, noncanonical quotient maps, or continuity completions can carry undetected periods. The presentation theorem is therefore part of the meta-observer contract, not administrative syntax.

## Disposition

Global holonomy is countably checkable once the rational observer category is given by a proved presentation. Local cell tests plus fundamental non-tree periods replace arbitrary path enumeration. The next source-specific task is to list the actual prime, heat, Fourier, Mellin, theta, and completion generators with their typed domains and residual formulas.
