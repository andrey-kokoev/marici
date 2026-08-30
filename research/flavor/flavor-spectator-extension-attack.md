# Spectator-extension attack (WP394)

## Target

Test whether freezing WP393's flavor reflection before inspecting flavor data
is sufficient to turn it into a hard-to-vary explanation.

## Exact extension pair

Fix the flavor reflection $S_v$ for the target ray $v=(1,2)^T$. Add one real
spectator coordinate $z$. Two extensions of the same flavor action are

\[
E_+=S_v\oplus(+1),
\qquad E_-=S_v\oplus(-1).
\]

Both satisfy $E_+^2=E_-^2=I$ and restrict to exactly the same operator on the
complete flavor response space. They therefore predict the same unique flavor
intertwiner, shell, rank, and cross-context alignment.

They disagree on the spectator. Under $E_+$, $z$ is even and a linear
spectator invariant is allowed. Under $E_-$, $z$ is odd and the same term is
forbidden. The full fixed spaces also have different dimensions.

## Consequence

A flavor-only symmetry can be preregistered and still remain freely variable
on every untested sector. Temporal priority blocks direct hindsight but does
not establish explanatory integration. The flavor action must follow from a
constructor whose extension to other physical systems is independently
constrained.

The smallest exact hostile pair is $S_v\oplus(+1)$ versus
$S_v\oplus(-1)$. No flavor experiment distinguishes them; a spectator parity
instrument does.

## Hard-to-vary repair

A stronger DPC must require at least one independently accessible consequence
outside the flavor relation used to define the protected ray. Suitable tests
include a forbidden spectator coupling, a threshold residue relation, an
anomaly cancellation condition involving other sectors, or a domain-wall
selection rule.

The source must derive the joint action before either the flavor or spectator
outcome is used. Otherwise the extension can again be fitted after the fact.

## Disposition

WP394 shows that preregistration is necessary but insufficient. A symmetry
becomes explanatory only when its action is hard to vary because changing the
flavor selector would spoil an independently testable consequence of the same
constructor.

The remaining instrument gate is a source-derived symmetry action on a named
spectator sector with an executable parity-sensitive readout.

Run `uv run --with sympy python
research/flavor/checkers/wp394_spectator_extension_attack.py` to regenerate
the result.
