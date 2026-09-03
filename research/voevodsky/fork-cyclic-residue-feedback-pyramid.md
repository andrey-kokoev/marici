# Forked model: cyclic residue-feedback coherence pyramid

## Status

Speculative fork. Not evidence, not a conjecture promotion, no effect on
the main RH model, `research/grothendieck/`, or any other locus. The
main model retains the directed chain

\[
A\longrightarrow B\longrightarrow C
\]

with the positivity residual left open. This packet asks whether a
cyclic version is even well-typed, before any theorem attempt.

## Problem

Can the three coherence pyramids be arranged so each vertex is both an
identity generator and a final coherencer, with each vertex's final
residue admitted as a parameter of the counterclockwise neighbor's
identity generator?

## Bold conjecture

There is a well-typed triangle

\[
\begin{array}{ccc}
A & \xrightarrow{\;r_A\;} & B\\
\uparrow r_C & & \downarrow r_B\\
C & \xleftarrow{\;\quad\;} & \cdot
\end{array}
\]

where the maps are residue-to-parameter transports, the composite
around the triangle is coherent, and the loop terminates at a fixed
point carrying no uncohered residual.

## Named rivals

1. **Circularity**: each transport presumes the coherence it feeds,
   so the loop proves nothing.
2. **Type mismatch**: residues live in error monoids, generator inputs
   live in construction spaces, and no natural map exists.
3. **Non-termination**: successive residues do not decrease in any
   admitted order, so the loop never closes.
4. **Vacuity**: the only realizable loop is the identity, recovering
   the existing directed chain in disguise.

## Construction sketch

Label vertices as in `rh-three-pyramid-factorization.md`:

- \(A\): analytic completion, apex \(\rho_{\rm an}\);
- \(B\): arithmetic presentation, apex \(\rho_{\rm ar}\);
- \(C\): positivity probes, cone \(\mathcal S'_{\ge0}\).

Candidate residue types:

\[
R_A = \text{presentation-coherence cell }
(\rho_{\rm an}\simeq\rho_{\rm ar}),
\]

\[
R_B = \text{finite prime-tail interval }
[\Theta_N,\Theta],\qquad N=N(t,\xi),
\]

\[
R_C = \text{Douglas/positivity obstruction class }
[\rho_{\rm ar}]-[\rho^{+}].
\]

Candidate generator parameters:

- \(P_A\): analytic ansatz data (kernel gauge, cutoff schedule);
- \(P_B\): sector source maps and continuation sheets;
- \(P_C\): probe family (test functions, ranks, widths).

The two edges that already exist in substance:

\[
R_A\to P_B \quad(\text{normalization cell feeds arithmetic presentation}),
\]

\[
R_B\to P_C \quad(\text{tail bound feeds probe admissibility}).
\]

The load-bearing new edge is

\[
R_C\to P_A,
\]

required to be a genuine deformation or refinement map: the positivity
obstruction must select new analytic ansatz data without using RH or
positivity as an input.

## Strongest falsification attempt

Attempt to construct \(R_C\to P_A\) on the atomic fixture
\(K(t,z)=e^{-ta^2}\cos(az)\), where positivity holds and the
residue vanishes. A vanishing residue must map to the original ansatz
(not an arbitrary one), or the transport is not natural. If the only
map that works is constant-in-residue, rival 4 holds: the loop is the
identity and the cycle is decoration.

Second test: inject a known negative perturbation of the coded form
(from the scaling scout at margin-collapse windows) and require the
transport to move \(P_A\) strictly, then verify the transported loop's
composite is not the identity while remaining coherent.

## Disposition

Rival 4 is refuted on the enriched type. Version 2 of the checker
(`results/fork_cyclic_residue_feedback.json`, schema
`fork-cyclic-residue-feedback.v2`) enlarges \(P_A\) to the gauge-kernel
family

\[
K_s(t,z)=e^{-(t+s)a^2}\cos(az),\qquad s\in\{0,\tfrac12,1\},
\]

with transport selecting \(s=0\) at zero residue and \(s=\tfrac12\)
otherwise. Naturality at zero holds, the selected widths are distinct,
and the heat-jet coordinate

\[
J_1(s)=a^2e^{-(t+s)a^2}
\]

differs from \(J_1(0)\) by a formally nonzero series in \(a\). The
transport changes an admitted generator datum, so the cycle does not
collapse to the directed chain.

Rivals 1–3 remain open and now carry the load. The rival-3 loop test
(schema v3) iterates the full loop on both fixture regimes. Positive
regime: orbit
\((10^{-6},0,0,0,0)\) terminates at the fixed point in one step. Signed
regime (weights \(1\pm\varepsilon\) at \(\pm a\)): the asymmetry is
preserved exactly under gauging,

\[
\frac{(1+\varepsilon)e^{-sa^2}}{(1-\varepsilon)e^{-sa^2}}
=\frac{1+\varepsilon}{1-\varepsilon},
\]

so the orbit is constant \(10^{-6}\): a period-one cycle, magnitude
nondecreasing. Deliberate-failure control: the constant transport
reproduces both orbits, so the termination-versus-cycle contrast is a
property of the regeneration operator, not of the transport; the
checker records this so the transport's role is not overstated.

Verdict: termination occurs only where the residue is gauge-killable.
In the signed regime—the RH-relevant one, where the obstruction is a
genuine class and not an artifact—no decreasing residual order is
exhibited, and rival 3 remains open. The load-bearing new edge
\(R_C\to P_A\) exists and is non-decorative, but on signed residues it
selects a gauge that leaves the obstruction invariant: the loop
refines the ansatz without refining the defect. Rivals 1 (circularity)
and 2 (type mismatch on \(R_C\)) are untested by this fixture class.

Branch 2 (schema v4) replaces width-schedule transport with support
displacement \(a\mapsto a+\delta\), \(\delta=\tfrac12\), on the signed
fixture, and tests two admitted residual orders:

- class order \(r=|\varepsilon|\): orbit constant, period-one cycle
  confirmed — no transport on this fixture class decreases the class
  order;
- low-frequency mass order \(r=|\varepsilon|e^{-a^2}\): orbit
  \(e^{-1},e^{-9/4},e^{-4},e^{-25/4},e^{-9}\) (times \(10^{-6}\)),
  strictly decreasing with exact contraction factor
  \(e^{a^2-(a+\delta)^2}\).

Honesty control: the contraction under the low-frequency order is
definitional — the obstruction functional was selected to make
displacement contractive. The checker records this as order-selection,
not a transport theorem, so the convergence cannot be cited as loop
convergence without an independent justification of the order
(rival 1). Net fork state: the cyclic edge is well-typed and
non-decorative; convergence exists only relative to a designed order;
on the class order the loop provably cycles on every transport tested
on this fixture class.

Branch 3 (schema v5, rival 2): the natural obstruction functional
\(\|\rho^-\|_{TV}\) (Jordan negative part) is well-typed on \(R_C\).
Under cumulative gauge, its orbit is \(10^{-6}(1,e^{-1/2},e^{-1},
e^{-3/2},e^{-2})\) — strictly decreasing — but the total mass follows
\(2(1,e^{-1/2},e^{-1},e^{-3/2},e^{-2})\) to the zero object. The
mass-normalized functional \(\|\rho^-\|_{TV}/\|\rho\|_{TV}=\varepsilon/2\)
is exactly invariant (orbit constant at \(1/2000000\)) under gauge and
displacement alike. Deliberate-failure control: citing the unnormalized
decrease as convergence is flagged as zero-object collapse and
disqualified. Rival 2 resolves in the negative: a natural obstruction
functional exists, but on this fixture class every transport either
leaves the normalized natural order unchanged or converges only by
annihilating the object.

## Disposition of the fork

Closed on this fixture class, all four rivals addressed: rival 4
refuted (non-decorative edge exists); rival 3 open in the unfavorable
direction (class order provably cycles); rival 2 resolved negatively
(natural functional normalized-invariant, unnormalized-trivial);
rival 1 controlled (all convergence claims pass a collapse check).
The cyclic residue-feedback pyramid, on atomic/signed atomic fixtures,
is a consistent type decoration of the directed chain, not a proof
engine. Escaping this boundary requires a non-atomic fixture with
infinitely supported obstruction — a new programme object, not a
successor leaf of this one; it is not opened here.

## Authority boundary

References `research/grothendieck/` read-only. `marici.Grothendieck`'s
uncommitted source-verification changes are inputs to the main model
only; this fork does not depend on their admission.
