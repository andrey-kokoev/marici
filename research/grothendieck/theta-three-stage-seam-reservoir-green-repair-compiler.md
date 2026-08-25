# Theta three-stage seam--reservoir--Green repair compiler

## Typing correction

The requested defect packet names `P` as the arithmetic primitive-prime
current.  Its completed incidence map has not yet been constructed.  The
smallest three-stage subsystem that is presently source-derived replaces it
by

\[
 R_f:f\longmapsto
 J_f(q)=2\int_q^\infty|f(v)|^2\,dv,
 \qquad J_f'=-2|f|^2.
\]

The audited subsystem is therefore

\[
 \boxed{\{S,R_f,D\}},
\]

where `S` retains the seam as an independent state component and `D` is the
full doubled Clark--Green operation.

## Operation signatures

### `S`: seam retention

`S` replaces a lossy tail presentation by

\[
 \mathcal H_{\rm tail}
 \longrightarrow
 \mathcal H_{\rm tail}\oplus\mathcal H_{\rm seam}
\]

with graph norm

\[
 \lVert(g,h)\rVert_S^2=\lVert g\rVert_2^2+\lVert h\rVert_2^2.
\]

- `precedes`: full `D`;
- `commutes_with`: `R_f`;
- `domain_after`: direct-sum tail--seam state space;
- `boundary_delta`: exposes the independent seam trace and mixed incidence;
- `completion_scope`: Hilbert direct sum, with rigged extension still needed
  for arithmetic `k=1`;
- `residual_capability`: can carry seam and mixed-sheet residuals, but cannot
  manufacture arithmetic primitive or square currents.

### `R_f`: continuous forcing reservoir

`R_f` requires `f` in `L2(0,infinity)` and creates the absolutely continuous
boundary current `J_f`, with terminal normalization `J_f(infinity)=0`.

- `precedes`: no strict dependency relative to `S`; may be constructed before
  `D` or used immediately after `D` identifies the typed `-2|f|^2` line;
- `commutes_with`: `S`;
- `domain_after`: source packet augmented by `J_f` in `W1,1` and its endpoint
  charge `J_f(0)=2||f||_2^2`;
- `boundary_delta`: `(J_f(0),J_f(infinity))=(2||f||^2,0)`;
- `completion_scope`: continuous under `L2` convergence of labelled cutoffs;
- `residual_capability`: closes exactly the continuous forcing-norm line and
  no arithmetic `k=1`, `k=2`, or archimedean line.

### `D`: doubled Clark--Green operation

`D` acts on the retained direct/dual graph domains, applies the two Clark
orientations, and forms their Green boundary identity.  Its positive bulk is

\[
 2|G+f|^2+2a^2|\partial_zG|^2.
\]

- `precedes`: later scalar compression or determinant readout;
- `commutes_with`: `R_f` only in the typed sense below;
- `domain_after`: doubled `q`-graph domain with explicit endpoint and seam
  traces;
- `boundary_delta`: produces ordinary Green endpoint flux plus the named
  forcing defect `-2|f|^2`;
- `completion_scope`: closed in each one-sided tail channel by packet 165;
  mixed seam and rigged arithmetic completion remain open;
- `residual_capability`: exposes, but does not itself close, seam,
  archimedean, primitive-prime, and prime-square residuals.

## Dependency graph

The full operation `D` requires `S`:

\[
 \boxed{S\prec D.}
\]

Applying a tail-only Green operation before `S` is a different, lossy
operation `D_tail`.  Adding the seam afterward cannot reconstruct its omitted
mixed boundary form because the seam is not a bounded function of the tail.
Therefore `D S` is not an alternative authorized ordering of the same two
operations.

By contrast, `S` and `R_f` are incomparable and commute.  `S` changes the
state carrier but not `f`; `R_f` changes the declared boundary-current packet
but not the tail--seam carrier:

\[
 \boxed{SR_f=R_fS.}
\]

Their domains and norms agree exactly after either order:

\[
 \left(
 \mathcal H_{\rm tail}\oplus\mathcal H_{\rm seam},
 \lVert g\rVert^2+\lVert h\rVert^2;
 f,J_f
 \right).
\]

## Both authorized three-stage orders

There are exactly two linear extensions:

\[
 S\,R_f\,D,
 \qquad
 R_f,S,D.
\]

In either order, `D` produces the same typed forcing density and `R_f`
supplies

\[
 -2|f|^2=\partial_qJ_f.
\]

The resulting positive bulk, graph domain, seam carrier, forcing endpoint
charge, and unresolved typed residuals coincide.

## Braid residual

Define the braid residual on the common final packet by subtracting the two
compiled Green forms:

\[
 \mathfrak B_{S,R_f;D}
 =D\circ S\circ R_f-D\circ R_f\circ S.
\]

Because `S` and `R_f` act on independent typed factors,

\[
 \boxed{\mathfrak B_{S,R_f;D}=0}
\]

as a domain-, graph-norm-, boundary-, and capability-typed identity.  This is
stronger than scalar endpoint agreement.

## First compiler obstruction

The three-stage subsystem is coherent, but it cannot yet be enlarged by the
arithmetic `P` or `Q` stages.  Their source densities are known from the
three-level Tate filtration, while their incidence maps into the retained
seam/Green boundary object are not.  Substituting `J_f` for those arithmetic
currents would be a type error.

Thus the first real seven-stage compiler obstruction is:

\[
 \boxed{
 \text{construct }P,Q:\mathcal H_{\rm valuation/Fock}
 \longrightarrow\mathcal H_{\rm boundary}
 \text{ before testing their braids with }S,D.}
\]
