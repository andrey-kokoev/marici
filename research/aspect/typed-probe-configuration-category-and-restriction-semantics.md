# Typed probe-configuration category and restriction semantics

## Question

What is the minimal categorical structure needed to make unary, joint, and higher probe constraints well typed without conflating pullback defects with additive cross-effects?

## Claim boundary

This packet defines a finite categorical interface and checks one finite instance. It does not assert that every SCC net carries the interface, that the assignment reconstructs its source pyramid, or that a probe placement is a physical measurement.

## Typed placements

Let \(L\) be a finite set of locations with interface types \(\tau_L(\ell)\). Let \(I\) be a finite set of instruments with placement types \(\tau_I(i)\). A placement \(i@\ell\) is individually typed when

\[
\tau_I(i)=\tau_L(\ell).
\]

A configuration is a finite partial assignment of instruments to locations satisfying individual typing and an explicit joint-admissibility predicate. Joint admissibility is not inferred from pairwise type equality. Require downward closure: every subconfiguration of an admissible configuration is admissible.

Define \(\mathsf{Conf}(L,I)\) as the face poset of admissible configurations. There is one morphism \(c\to d\) exactly when \(c\subseteq d\). Composition is inclusion. The empty configuration is initial. An incompatible joint placement is absent from the category; its interaction defect is undefined rather than zero.

## Restriction semantics

Let \(\mathcal C\) be a category with the finite limits used below. A constraint semantics is a presheaf

\[
\mathcal K:\mathsf{Conf}(L,I)^{\mathrm{op}}\longrightarrow\mathcal C.
\]

For \(c\subseteq d\), the map \(\rho_{d,c}:\mathcal K(d)\to\mathcal K(c)\) forgets placements while retaining the constraints visible on \(c\). It must satisfy

\[
\rho_{c,c}=1,
\qquad
\rho_{e,c}=\rho_{d,c}\rho_{e,d}
\quad(c\subseteq d\subseteq e).
\]

For an admissible pair \(p,q\), the unary restriction maps induce

\[
\chi_{p,q}:\mathcal K(\{p,q\})
\longrightarrow
\mathcal K(\{p\})\times_{\mathcal K(\varnothing)}\mathcal K(\{q\}).
\]

The semantics is binary Segal at \(p,q\) when \(\chi_{p,q}\) is an isomorphism. Otherwise the map itself and its classified failure are the binary interaction datum. In a generic finitely complete category there is no canonical numerical defect.

## Additive specialization

Subtraction requires separate structure. If a response valuation

\[
F:\operatorname{Ob}(\mathsf{Conf})\to A
\]

lands in an abelian group or the Grothendieck group of an additive category, define

\[
\operatorname{cr}_{p,q}F
=F(\{p,q\})-F(\{p\})-F(\{q\})+F(\varnothing).
\]

This cross-effect is not the generic pullback comparison. It is an additive invariant derived from a chosen valuation. The Schur residue \(-CA^{-1}B\) is an instance of this specialization.

## Higher configurations

For an admissible finite configuration \(c\), form the matching object from all proper faces when the corresponding limit exists:

\[
M_c\mathcal K=
\lim_{d\subsetneq c}\mathcal K(d).
\]

The canonical map \(\mathcal K(c)\to M_c\mathcal K\) tests whether proper-face constraints determine the full configuration. Failure at cardinality three can remain invisible to every binary comparison. No matching map exists when \(c\) itself is inadmissible.

## Finite witness

The diagnostic uses three binary probes in separate compatible charts. An admissibility chart excludes a declared incompatible pair and every configuration containing it. A binary chart carries the non-Segal equality relation. A fully admissible ternary chart carries the even-parity relation with full pairwise faces. Keeping the binary and ternary witnesses in separate presheaves is necessary: the full pairwise projection of the parity relation cannot restrict into an equality-only pair object. The diagnostic verifies downward closure, identity and composition of restrictions, the non-Segal equality pair, the undefined incompatible pair, and the higher parity obstruction.

## Falsifiers

1. A configuration family that is not downward closed does not define the stated face category.
2. Restriction maps that fail identity or composition do not define a presheaf.
3. An inadmissible pair cannot be repaired by assigning it an empty constraint object; absence and emptiness are distinct.
4. A numerical cross-effect without additive target structure is untyped.
5. Full pairwise projections do not establish a higher matching isomorphism.

## Disposition

The minimal interface is a downward-closed typed configuration category plus a constraint presheaf. Generic interactions are failures of matching maps. Additive cross-effects are optional derived invariants and require declared additive structure. This separation repairs the ambiguity between the finite-set Segal example and the Schur additive example.
