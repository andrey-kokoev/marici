# Annotated coherence and the path-holonomy gate

## Refinement

Joinability of constructor-tree shapes is necessary but insufficient. Every
rewrite edge carries semantic annotations:

\[
\ell(r)=(\Sigma_r,\rho_r,E_r,F_r),
\]

where \(\Sigma_r\) is its support obligation, \(\rho_r\) its resource law,
\(E_r\) its temporal scope, and \(F_r\) its fault domain. A path accumulates
these labels using the typed composition laws:

\[
\Sigma_{pq}=\Sigma_p\cup\Sigma_q,\qquad
\rho_{pq}=\rho_p\circ\rho_q,\qquad
E_{pq}=E_p\cap E_q,
\]

with fault-domain composition defined only when the models admit the
crossing.

Two branches that reach the same constructor normal form are coherent only
when their accumulated annotations agree through a source-authorized
invertible comparison cell. Shape joinability cannot erase an obligation.

## Smallest holonomy falsifier

Consider the filled shape diamond

\[
T\to L\to N,\qquad T\to R\to N.
\]

Let the left path accumulate support \(\{a,c\}\), while the right accumulates
\(\{b,c\}\). Both normalize to \(N\), and both may emit identical bytes, but
their symmetric-difference holonomy is

\[
\Delta_\Sigma=\{a,b\}\ne\varnothing.
\]

The correct result is
\(constructor\_path\_annotation\_mismatch\), not successful coherence. An
admitted comparison cell must explicitly transport \(a\) to \(b\) while
preserving resource, epoch, and fault semantics. A cell that merely declares
the endpoints equal is itself authority laundering.

## Finite test

For every critical diamond:

1. normalize both branches to their constructor-tree normal forms;
2. accumulate support unions, resource transformations, epoch
   intersections, and fault-domain transitions;
3. reject immediately if the tree normal forms differ;
4. if the trees agree, compare accumulated annotations;
5. accept a difference only through a named, source-authorized invertible
   comparison cell whose own support obligations are then accumulated.

The finite falsifier reports the first differing annotation component and
the exact two paths. For support sets it is the symmetric difference. For a
resource law it is a failed equation. For epochs it is a mismatched
intersection. For fault models it is a missing authorized crossing.

## Cross-sector consequences

- **Strominger.** A DPC compiler must compare annotated paths, not only
  constructor normal forms. Otherwise reassociation can silently drop a
  lease, epoch, certificate, or Byzantine-fault obligation.
- **Benincasa.** The integrated Taylor rows violate the three exact source
  relations by stable relative residuals approximately
  \((0.469,0.261,1.0)\). Hence ordinary Taylor monomials and primitive
  insertion classes do not define annotation-preserving paths to a common
  quotient. A source-labelled insertion-to-jet adapter must retain the
  lower-product/coherence terms and descend through the same
  twisted-de-Rham exact complex.
- **Kitaev.** Lexicographic phase-polynomial witness selection supplies a
  deterministic normal representative, verified by repeated hash
  F96F5A8F1DE372D4A0A1898A317C35E96F282B08A4C6965B772B133473FD1304.
  This is required for reproducible falsifiers, but does not prove that
  distinct resource paths have equal annotations.
- **Arithmetic/RH.** The endpoint, gamma, and prime channels can join at the
  same completed scalar kernel while carrying different source annotations.
  The coupled correction \(C_Y\) is the coherence balance. Equality of the
  scalar endpoint does not orient that balance or license deletion of a
  channel obligation.

## Theorem boundary

For a terminating typed rewrite presentation, unique unannotated normal
forms plus vanishing annotation holonomy on every critical diamond yields
path-independent accumulated semantics for the generated rewrites.

This remains presentation-relative. It does not manufacture authority for
the rewrite rules or comparison cells, and higher coherence among cells must
still be checked when those cells are operative.

## Durable statement

> Constructor coherence means equality of typed endpoints together with
> path-independent accumulated support, resource, temporal, and fault
> semantics. A filled shape diamond with nonzero annotation holonomy is an
> authority-laundering defect.

