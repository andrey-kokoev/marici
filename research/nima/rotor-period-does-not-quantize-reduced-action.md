# Rotor return does not quantize the reduced action

## Frozen question — iteration 4

The overview `conceptual-steps-table.md` and diagram `progression-mermaid.md`
claim that a retained spinor period forces action quantization and identify
the connection integral with the lifted clock. Test those arrows, not whether
another Hamiltonian or phase lift can be constructed.

Reuse the COMPLETED `retained-rotor-phase-transport.md` realization, including
its defining module, connection, selected constant C=kappa, both parity laws
and sewn HJ charts. The earlier zero-offset phase mismatch was already repaired
conditionally; it is not evidence against this stronger implementation.

Keep the existing full algebra state (s,q,p,z), with no new source operation,
metric or phase rule. Its rotor parameter theta is an angle, not physical time.
The phase phi is modulo 2*pi; the corresponding planar adjoint rotation has
angle 2*theta. A 4*pi adjoint-angle return is theta=2*pi, not a new phase period.

**Conjecture to test:** closure of that existing lifted rotor forces the reduced
action I=integral(beta), beta=p*dq+s*dz, onto a fixed 4*pi*kappa lattice (or even
the usual circle-period 2*pi*kappa lattice), and integral(alpha) equals
Delta(phi)-Delta(F)/kappa, with F=(qp+sz)/2.

**Closure:** either derive those consequences for the existing allowed states,
or exhibit a closed lifted rotor with off-lattice I and the exact missing
connection term. Distinguish reduced action I from complete trajectory action
S=integral(beta-H*dtheta), and dynamical rotor transport from alpha=0 horizontal
transport. A condition on a different protocol cannot rescue the conjecture.

**Rivals:** failure was only the discarded C=0 model; full phase closure removes
all amplitude freedom; integrality follows only after additionally imposing
horizontal lifted closure; the clock and connection differ by a retained term.

SCC obligations: attachment transport and readout comparison on the declared
real Clifford phase realization. This is not a native quantization no-go theorem
or a rejection of the conditional phase/HJ construction.

## Exact comparison on the completed lift

Let r^2=q0^2+p0^2. The existing equations give

\[
q=q_0\cos(2\theta)+p_0\sin(2\theta),\qquad
p=p_0\cos(2\theta)-q_0\sin(2\theta),\qquad
H^+=r^2+\kappa.
\]

The s,z components remain present and stationary. Along this trajectory,

\[
\beta(\dot Q)=2p^2,\qquad
\frac{dF}{d\theta}=p^2-q^2,\qquad
\alpha(\dot{\widetilde Q})=-1-\frac{r^2}{\kappa},\qquad
\frac{dT}{d\theta}=1.
\]

Thus beta-dF is not zero along the trajectory. At theta=2*pi the base and
module-phase endpoints return, while the retained angular lift advances by
2*pi. Histories and winding have not been erased. Exact integration gives

\[
I=\oint\beta=2\pi r^2,\qquad
S=\int_0^{2\pi}(\beta(\dot Q)-H^+)\,d\theta=-2\pi\kappa,
\]

\[
\Delta\varphi=-2\pi,\quad \Delta F=0,\quad
\int\alpha=-2\pi\left(1+\frac{r^2}{\kappa}\right).
\]

The complete action correctly gives exp(i*S/kappa)=1. No action/phase mismatch
has been resurrected: this is the already successful C=kappa model.

Choose r^2=kappa/2, an allowed nonzero initial state of the declared realization.
Then I=pi*kappa, outside both proposed 2*pi*kappa and 4*pi*kappa lattices,
despite exact lifted endpoint closure. More generally r^2=kappa*sigma is allowed
for every positive sigma, and I/(2*pi*kappa)=sigma. The permitted reduced
action and H^+ therefore vary continuously; this is not a finite-sample inference.

The claimed connection identity has the exact residual

\[
\int\alpha-\left(\Delta\varphi-\frac{\Delta F}{\kappa}\right)
=-\frac{I}{\kappa}.
\]

In the displayed counterexample the actual connection integral is -3*pi,
whereas the claimed expression is -2*pi. The corrected relation is
alpha=-dT-(beta-dF)/kappa, not alpha=-dT.

## What a horizontal-loop condition would change

For alpha=0 along a specified base loop, Delta(phi)=I/kappa. ADDITIONALLY
requiring its phase-circle lift to close imposes I in 2*pi*kappa*Z. That is a
condition on selected horizontal loops, not a consequence of the phase circle
existing and not a spectral quantization theorem.

The actual rotor path is not horizontal: at r^2=kappa/2 its alpha evaluation
is -3/2. Horizontal transport over the same base loop ends with phase -1,
whereas the dynamical rotor lift ends with phase +1. Replacing one by the other
changes the protocol. The previous calibration analysis already distinguished
these protocols; this comparison uses that stronger result rather than its
zero-offset predecessor.

## Disposition and repaired overview

**Closed negatively:** lifted periodicity alone does not quantize reduced
action or energy in this declared model. It also does not identify the
connection integral with the angular clock. Closure of the COMPLETE action
phase still holds, and the completed phase/HJ construction remains valid.

The old overview's claim that the construction includes quantum mechanics,
with only the Born rule missing, is withdrawn. A supplied phase module and
connection do not derive all quantum structure. The old Pauli/Bohr-Sommerfeld
and cocycle/Jacobi slogans were not theorem inputs and are not used as bridges.

`conceptual-steps-table.md` now separates established conditional results from
their independent physical interfaces. `progression-mermaid.md` displays those
separate dependencies rather than an unproved Newton-to-QM-to-Marici derivation.
The two originals are hash-preserved in
`quarantine/20261007-conceptual-summary/manifest.json`. The old rotor generator
packet and two SCC manifests no longer advertise already completed phase or
history-clock constructions as missing.

No additional oscillator, quantization postulate or normalization was inserted.
A source-selected state restriction or an admitted horizontal-loop protocol
would be a different question; this negative closure is not reopened by asking
for a physical quantization theorem.

## Verification and execution correction

`checkers/check_rotor_period_action_boundary.py` executes the existing completed
phase lift and calibration checkers, then derives the orbit integrals and the
explicit off-lattice witness. Its receipt is
`results/rotor-period-action-boundary.json`. The only predecessor-code change
exports its already checked objects for reuse.

The initial checker compared two equivalent SymPy expressions structurally
and failed: 2*pi*(-p0^2-q0^2)/kappa versus -2*pi*(p0^2+q0^2)/kappa.
Diagnostic `e_38524_1791393248951408100_34` gives exact difference zero.
The corrected gate tests that zero residual; no mathematical condition changed.
The original and corrected SCC freezes are retained. The first challenge's
`survives` label described a checker failure, not scientific survival of the
conjecture. Corrected challenge `e_38524_1791393318183860700_36` passes with
exit zero meaning that the claimed implication is falsified. Final scoped
check `e_38524_1791393650446364800_37` passes all 25 added controls with the
completed predecessors rerun. Integrity check
`e_38524_1791393819201385800_38` confirms the four current implementation hashes
and both archived overview copies.

Graph result and overview criticism:
`ev-000000015819-38787cee-d094-4974-97ae-1002f72fc223`, proposal
`ep_b677a887-882e-40d3-a493-4e28598b1f52`. This turn's [15819,15819] and the
preceding audit/correction interval [15815,15818] remain uncommitted. No commit,
push or publication occurred; admission is provenance, not verification.

These are exact symbolic checks on the declared analytical realization, not
a new native Agda theorem, physical clock calibration, Planck constant, detector
model or universal obstruction to quantization.
