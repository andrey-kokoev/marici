# Enumerated future rungs are not intrinsic

Owner: `marici.Nima`

## Target

The literal conjecture proposed

\[
r(x,x')=\min\{n:p_n(x)\ne p_n(x')\}.
\]

It is false without additional source structure.

## Reindexing falsifier

Take two states `a,b` and one authorized separating probe `u`, with
`u(a)!=u(b)`.  The towers

\[
(\varnothing,\{u\})
\qquad\text{and}\qquad
(\varnothing,\varnothing,\{u\})
\]

contain the same total authorized probe family.  The second merely inserts an
empty stage.  Nevertheless the proposed rung changes from `1` to `2`.

Likewise, two incomparable probes need not possess a canonical order.  Any
linear enumeration imports a ranking not supplied by their operational
content.

There is also a variance correction.  As probe families grow, their
observational quotients become finer.  The canonical forgetful maps run

\[
L_{n+1}\longrightarrow L_n,
\]

not generally `L_n -> L_{n+1}`.  A coarse equivalence class has no canonical
choice of finer class.

## Surviving invariant

For the complete authorized family `U`, define the separating profile

\[
\operatorname{Sep}(x,x')
=\{u\in\mathcal U:u(x)\ne u(x')\}.
\]

Then:

- `Sep` empty means operational equivalence relative to the declared family;
- `Sep` nonempty means operative distinction;
- the profile records which future constructors witness it.

This object is invariant under enumeration and insertion of duplicate stages.
It must still not be called gauge equivalence unless the source certifies that
`U` is complete for the claimed scope.

## When a rung is legitimate

A numerical or partially ordered depth becomes meaningful only if the source
supplies a resource grading

\[
c:\mathcal U\to P,
\]

such as constructor depth, support codimension, perturbative order, or derived
grade.  The intrinsic datum is then the antichain of minimal resource values
among separating probes:

\[
\operatorname{MinCost}(x,x')
=\min_P\{c(u):u\in\operatorname{Sep}(x,x')\}.
\]

For a total, source-canonical grading this reduces to one rung.  For several
independent resources it is generally a Pareto frontier, not an integer.

## Corrected Deutsch--Popperian conjecture

A distinction is characterized by its source-authorized separating-probe
profile.  A rung or depth is derived only from a separately source-generated
resource grading on those probes.  No presentation ordering may supply that
grading.

## Falsifiers

- The separating profile changes under probe reordering or duplication.
- A claimed depth changes under a resource-preserving reindexing.
- A claimed scalar depth hides incomparable minimal resource witnesses.
- Empty separation under an incomplete probe family is promoted to physical
  gauge equivalence.

