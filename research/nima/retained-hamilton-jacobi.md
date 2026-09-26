# Endpoint variation with retained comparison phases

Active SCC obligations: attachment transport and readout descent. This is a
conditional calculation on the phase-lift model already written in chat. It
must not replace the missing source-to-Hamiltonian or source-to-clock map.

## Frozen inputs and types

The analytic inputs are a smooth classical Hamiltonian H(q,p,t), a reference
parameter t, and a positive phase scale hbar. Work on a local smooth family of
classical trajectories with nonsingular endpoint projection, before a caustic.
The initial configuration and initial time are fixed. A regular Legendre map
permits the corresponding Lagrangian description.

The independent retained input is the declared Clifford word model from
`checkers/check_clifford_retained_order.py`. Keep the full word, its signed lift,
and its action grade. It is not permissible to identify them. This finite model
does not supply classical coordinates, the Hamiltonian, or elapsed time.

A source comparison is not automatically a transition between HJ branches.
The action-phase realization below is a condition on such a proposed bridge,
not evidence that the bridge already exists. No completed infinite path sum,
physical amplitude, or continuum completion of native histories is used.

## Endpoint calculation

For a classical trajectory gamma, its action is

\[
S[\gamma]=\int(p\dot q-H)\,dt.
\]

At fixed time endpoints, integration by parts gives

\[
\delta S=[p\,\delta q]_i^f+
\int\bigl[(\dot q-H_p)\delta p-(\dot p+H_q)\delta q\bigr]dt.
\]

On a Hamiltonian trajectory the bulk term vanishes. Allowing the final time to
vary and interpreting delta q as the total endpoint displacement gives

\[
dS=p\,dq-H\,dt.
\]

Consequently every smooth local principal-action branch satisfies

\[
S_t+H(q,S_q,t)=0.
\]

The phase lift records dphi=dS/hbar along this action branch. Along a Hamiltonian
characteristic its rate is (p H_p-H)/hbar=L/hbar. These facts alone are standard
Hamiltonian/Hamilton-Jacobi theory; no new term has appeared.

## Carry the comparisons, not just the action

Suppose two local action branches have an admitted comparison phase chi_ab on
an overlap, with a locally chosen real logarithm:

\[
S_a=S_b+\hbar\chi_{ab}\pmod{2\pi\hbar}.
\]

Integer logarithm choices are constant on a connected smooth overlap. Direct
substitution transports the HJ equation to

\[
\partial_t S_a-\hbar\partial_t\chi_{ab}
+H_b(q,\partial_q S_a-\hbar\partial_q\chi_{ab},t)=0.
\]

Equivalently the Hamiltonian in that momentum/energy frame is

\[
H_a(q,p,t)=H_b(q,p-\hbar\partial_q\chi_{ab},t)
-\hbar\partial_t\chi_{ab}.
\]

An endpoint-dependent phase therefore requires transporting momentum and energy.
It cannot simply be appended while claiming an unchanged H in unchanged
coordinates. These gradient terms are frame transport; they are not, by
themselves, new forces or a quantum potential.

For the existing discrete Clifford comparisons between lifts of the same action,
the relative lift is +1 or -1. On a smooth connected overlap a realization of
these fixed signs is locally constant. Its derivatives vanish. Thus the local
HJ equation remains unchanged, while the proposed realization must satisfy

\[
\exp\bigl(i(S_a-S_b)/\hbar\bigr)=\epsilon_{ab},
\qquad \epsilon_{ab}\in\{1,-1\}.
\]

In particular a negative comparison requires an odd multiple of pi*hbar as the
action-branch offset, modulo 2*pi*hbar. This is a test for an action-phase
realization. It is not a derivation that native histories already have such
classical actions, nor a quantization condition on physical orbits.

The distinction matters even for ordinary free-particle HJ: both
S=m(q-q0)^2/(2t) and S+pi*hbar solve the same equation for t>0, while their phases
are opposite. This example supplies a local consistency check, not a new source
Hamiltonian or a selection of its initial phase.

## Real logarithms require additional retained data

The exact source prototype has the sign cocycle

\[
\sigma((a,b),(c,d))=(-1)^{bc}.
\]

Its phase-valued associativity is exact. Its chosen principal-angle cochain
ell(g,h)=pi*b*c, however, has an integer carry:

\[
\ell(g,h)+\ell(g+h,k)-\ell(h,k)-\ell(g,h+k)
=2\pi n(g,h,k).
\]

Here grade addition is bitwise XOR. All 64 triples give n in {-1,0,1}.
For the word RLL, grouping (RL)L gives pi+pi while grouping R(LL) gives zero in
these coarse-grade angle representatives. Both represent the same phase and
signed lift, but their real logarithms differ by 2*pi. The integer carries
satisfy the next cocycle identity on all 256 four-tuples. This is a checked
higher comparison of chosen logarithms, not a new dynamical source term.

The history cannot be replaced by one action-grade label with a multiplicative
lift selector: all 16 sign selectors fail. This independently reproduces the
finite obstruction described in Voevodsky's
`retained-history-lift-action-and-the-missing-section.md`; that packet's Agda
root was not independently rerun here.

For a fixed positive-word presentation, inversion count gives one real angle
unwrap: pi times the number of R-before-L pairs. Its concatenation law uses the
FULL letter counts, not just parity. This restores the lost 2*pi in the RLL
example independently of grouping. It is presentation-dependent, still loses
history, and is not a physical action or clock. Matrix/grade data must remain
present, especially under reversal; scalar principal angles alone are not a
representation of the signed Clifford group.

## Bounded outcome

The current candidate HJ enrichment is a packet of local action branches, full
histories, signed lifts, comparison phases and their logarithm-branch witnesses.
Its existing constant sign comparisons constrain proposed gluing but add no
local HJ correction. Their correspondence to actual action branches remains a
source-realization obligation. A new local dynamical equation would require an
additional source-derived coupling or variational condition absent from the
H-plus/L-plus expressions used in this calculation.

Verification:

```text
uv run --with sympy python research/nima/checkers/check_retained_hamilton_jacobi.py
uv run --with sympy python research/aspect/scc/scc.py check nima-retained-hamilton-jacobi
```

The checker covers symbolic phase-frame covariance, a fixed-H rephasing hostile,
a transported-H control, free-particle action branches, exact log carries,
absence of a multiplicative selector, and retained word controls. The endpoint
variation is an analytic derivation under the smoothness assumptions above,
not an Agda formalization. Receipt: `results/retained-hamilton-jacobi.json`.
