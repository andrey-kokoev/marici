# RH modular-filling invariance audit

## Question

Do graded theta sewing and the fixed-cycle Mellin theorem define a source-authorized modular filling \(M\) with boundary \(C_f\), invariantly and without choosing an antiderivative or using zero data?

## Claim boundary

The audit distinguishes a relative homology class from a chain-level filler and from a completed continuous filler family. It does not alter the Grothendieck source packets.

## What is constructed

On the ordinary test-function domain, the Mellin orbit

\[
t\longmapsto A(tw),\qquad -1\leq t\leq1,
\]

is source-derived from the generator \(Qf(q)=qf(q)\). Its endpoint boundary is

\[
A(-w)-A(w)=C_f.
\]

This uses neither a fitted antiderivative nor zero data. Graded theta sewing cancels internal seam boundaries, while the fixed-cycle theorem identifies completed relative classes by their admitted endpoint incidence. These results determine an invariant relative class \([M]\) whenever the orbit lies in the admitted relative chain complex.

## What is not constructed

They do not define a unique chain representative \(M\). Let \([x,y]\) denote a labelled oriented edge with boundary \([y]-[x]\). For distinct labels \(w,a,-w\), compare

\[
M_0=[w,-w]
\]

and

\[
M_1=[w,a]+[a,-w].
\]

Both have boundary \([-w]-[w]\), but they are distinct elements of the free labelled chain group. Their difference is the boundary of the labelled 2-simplex \([w,a,-w]\) when that simplex is admitted. Thus endpoint incidence determines the relative class, not a strict representative.

This finite fixture falsifies any claim that the fixed-cycle theorem alone selects a unique \(M\).

## First missing higher-categorical datum

A strict invariant filling requires a natural chain-level section or contraction

\[
s:\operatorname{im}(\partial)\longrightarrow C_1,
\qquad
\partial s=\operatorname{id},
\]

together with coherent 2-cells comparing \(s\) under modular sewing, basis mutation, and Euler-cutoff refinement. The 2-cells must satisfy the next tetrahedral compatibility. Neither graded seam cancellation nor endpoint-class uniqueness supplies this section.

At completion, the requirement is stronger: the chosen family \(M_X\) must preserve boundary-null sequences uniformly in the declared graph topology. This is exactly the descent/closability gate already isolated in the Mellin-orbit packet.

## Answer

- **Algebraic ordinary domain:** a canonical straight Mellin-orbit representative is available because the spectral parameter has declared affine structure.
- **Invariant relative object:** the class \([M]\) is determined by endpoint incidence.
- **Strict modular chain-level object:** not invariantly determined by the cited theorems.
- **Completed boundary object:** unverified until natural chain contraction and uniform cutoff descent are established.

## Disposition

The route-mismatch cocycle is algebraically exact, but the requested invariant completed modular filler is not constructed. The first missing datum is a coherent natural chain-level contraction; its first finite falsifier is the pair \(M_0,M_1\) above.

## Verification

- `research/voevodsky/checkers/check_rh_modular_filling_invariance.py`
- `research/voevodsky/results/rh_modular_filling_invariance.json`
