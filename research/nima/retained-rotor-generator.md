# A continuous Clifford sector and its action-phase mismatch

Active obligations: forward realization and attachment transport. This is the
first bounded leaf of the retained-development-to-generator programme. The
input is the existing declared real Cl(2,0) realization, not a newly chosen
Hamiltonian. Full word histories remain separate from every matrix reading.

## Continuous family: existence and the enlargement boundary

The eight signed source lifts form a finite discrete matrix group. Any continuous
map from the connected real line into that group is constant. A one-parameter
group starting at identity is therefore trivial if required to stay in it.
Its topological closure is still finite. Word retention alone supplies no
continuous topology or interpolation rule.

The already declared real Clifford algebra has a larger even unit group. With
J=e1*e2, J squared=-1 and reversion(J)=-J, it admits

\[
U(\theta)=\exp(\theta J)=\cos\theta+J\sin\theta,
\qquad U(\theta+\eta)=U(\theta)U(\eta).
\]

This is an exponential ENLARGEMENT inside the ambient algebra, not the closure of
the finite subgroup. The real algebra, its reversion metric and analytic
exponentiation are explicit assumptions. Their selection by the full native
retained source is not proved by this construction.

The family retains the old lifts: U(pi/2)=J, U(-pi/2)=-J. At angle pi its adjoint
action returns to identity while U(pi)=-1. Only at 2*pi does the lift return to 1.
Even then a complete path/history record must not be replaced by its endpoint.

Neither elementary lift e1 nor e2 can be joined to 1 through real invertible
2-by-2 matrices: each has determinant -1, while identity has determinant +1.
Both conjugate U(theta) to U(-theta). They are reversers of the continuous
family, not individual positive-time members of it.

## Derive a generator on the existing observable carrier

Keep the same four-dimensional real algebra carrier as before, writing

\[
Q=s\,1+q\,e_1+p\,e_2+z\,J.
\]

Here q,p are algebra coefficients. They acquire a canonical-coordinate role in
this model below; they have not been identified with physical position and
momentum. The active source-sector identification remains a linear intertwiner,
not an assertion that the native source supplied this metric or an isometry.

Differentiate the adjoint family rather than inserting a Hamiltonian:

\[
D(Q)=\left.\frac{d}{d\theta}\right|_0 U(\theta)QU(-\theta)
=[J,Q]=2p\,e_1-2q\,e_2.
\]

The declared positive reversion metric is g(A,B)=Tr(A^T B)/2. Construct the
constant symplectic form from this metric and the ordered generator J:

\[
\Omega(A,B)=g(A,JB),
\qquad \Omega=dq\wedge dp-ds\wedge dz.
\]

It is skew and nondegenerate. The adjoint flow preserves it, and

\[
\iota_D\Omega=d(q^2+p^2).
\]

Thus its Hamiltonian generator, relative to the angular parameter, is

\[
H_\theta=q^2+p^2+C.
\]

The differential determines it only up to a constant C. The scalar and bivector
coordinates are stationary. Both elementary adjoint involutions pull Omega back
to -Omega, so they are anti-symplectic reversers, not Hamiltonian evolutions for
this form. The construction provides a candidate angular generator, not a
physical energy scale or clock.

## Derive action and local HJ, then test the retained lift

On the active plane the equations are q'=2p, p'=-2q. For C=0 a principal action
with initial coordinate q0 and angular interval theta is

\[
S(q,\theta;q_0)=
\frac{(q^2+q_0^2)\cos(2\theta)-2qq_0}{2\sin(2\theta)}.
\]

This is local, requiring sin(2*theta) nonzero. Exact differentiation gives

\[
S_\theta+(S_q)^2+q^2=0.
\]

Its singular endpoint charts are caustics; no smooth global principal-action
branch across them is asserted. Use the actual trajectory to compute the full
closed-orbit action rather than substitute through a singular chart.

The adjoint orbit completes one period at theta=pi. On that orbit, for C=0,

\[
\oint(p\,dq-H_\theta\,d\theta)=0.
\]

The reduced action integral of p*dq alone is not this full action. Indeed the
Lagrangian on this oscillator trajectory is the derivative of q*p/2, so the
full action vanishes on the closed trajectory. But the retained Clifford lift
has returned as -1. Therefore the previously written phase-only prescription
exp(i*S/kappa), for any positive action scale kappa, gives +1 and fails this
retained-sign comparison.

The candidate generator has thus been constructed, and its simplest action-phase
realization has failed a concrete witness test. Discarding the sign would falsely
report compatibility.

Changing the undetermined constant changes this test without changing the orbit:

\[
S_{\rm cycle}=-\pi C,
\qquad \exp(-i\pi C/\kappa)=-1
\quad\Longleftrightarrow\quad C/\kappa\in 2\mathbb Z+1.
\]

This is only the one-cycle matching condition. It does not select a unique
constant, establish all intermediate comparison maps, or derive a zero-point
energy. A separately constructed geometric/caustic phase could instead carry
the sign. Neither mechanism may be silently inserted as source-derived.

## Nonredundant successors

1. Construct the lift-compatible action/caustic comparison for this continuous
   sector. Distinguish a Hamiltonian constant from geometric transition data;
   retain full histories and test composition, reversal and full-cycle signs.
2. Audit which native source structure authorizes the real analytic enlargement,
   metric and angular parameter, rather than treating the finite subgroup as
   if its topological closure were already continuous.

The first is the selected continuation. The second remains a separate upstream
realization branch. A physical clock and phase/energy calibration remain open.

Verification:

```text
uv run --with sympy python research/aspect/scc/scc.py check nima-retained-rotor-generator
```

`checkers/check_retained_rotor_generator.py` checks the group law, derivative,
source-lift samples, symplectic and anti-symplectic identities, Hamiltonian
primitive, local HJ equation and closed action integral symbolically.
`results/retained-rotor-generator.json` records the assumptions and hashes.
The finite-group connectedness obstruction is an elementary topological argument,
not an Agda formalization. No physical quantization, full native continuous
realization, or successful full phase-witness sewing is claimed.
