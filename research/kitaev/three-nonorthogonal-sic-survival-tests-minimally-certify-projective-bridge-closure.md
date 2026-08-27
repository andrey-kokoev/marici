# Three nonorthogonal SIC survival tests minimally certify projective bridge closure

Owner: `marici.Kitaev`

## Bounded question

What is the smallest existing qutrit tester that can certify that two charged
sector-transfer routes have trivial relative logical holonomy?

Three prepared SIC lines suffice, and fewer than three cannot suffice in
dimension three. Choose three linearly independent, pairwise nonorthogonal
states from the pinned nine-line SIC orbit. If the closed route comparison
returns each state to its own line with probability one, then the complete
qutrit channel is the identity. For a unitary loop, the gate is a scalar phase.

The proof needs neither full state tomography nor nine-by-nine process
tomography. Nonorthogonality aligns the otherwise invisible phase on each
probe line, while linear independence spans the qutrit.

## Claim boundary

The exact theorem assumes a trace-preserving qutrit channel and exact survival
probability one for three independently prepared probe states. The approximate
operator-norm bound below is stated for a unitary loop. Extending it optimally
to arbitrary noisy channels requires a separate robust Stinespring estimate.

Physical use remains conditional on independently compiled state preparation,
route execution, return measurement, and setting labels. A common conjugation
of the loop and all probes can preserve every internal test while changing the
external semantic frame.

## Minimal SIC triple

Use the monomial qutrit basis

\[
|q_0\rangle,
\qquad
|q_1\rangle,
\qquad
|q_2\rangle.
\]

Select the three zero-phase edge states

\[
|u_{01}\rangle
=
\frac{|q_0\rangle+|q_1\rangle}{\sqrt2},
\]

\[
|u_{02}\rangle
=
\frac{|q_0\rangle+|q_2\rangle}{\sqrt2},
\]

and

\[
|u_{12}\rangle
=
\frac{|q_1\rangle+|q_2\rangle}{\sqrt2}.
\]

They are three members of the vacuum-projector SIC orbit. Every distinct pair
has overlap

\[
\langle u_i|u_j\rangle=\frac12.
\]

Their Gram matrix is

\[
G
=
\begin{pmatrix}
1&1/2&1/2\\
1/2&1&1/2\\
1/2&1/2&1
\end{pmatrix}
=
\frac12I_3+\frac12J_3.
\]

Its eigenvalues are

\[
2,
\qquad
\frac12,
\qquad
\frac12.
\]

Hence the three states are linearly independent and span the qutrit. If
`Psi` is the matrix with these vectors as columns, then

\[
\|\Psi^{-1}\|=\sqrt2.
\]

## Exact unitary proof

Let `U` be the relative bridge holonomy. Test the survival probabilities

\[
p_i
=
|\langle u_i|U|u_i\rangle|^2.
\]

If `p_i=1`, then

\[
U|u_i\rangle=e^{i\phi_i}|u_i\rangle.
\]

Unitarity preserves pairwise inner products, so

\[
\langle u_i|u_j\rangle
=
e^{i(\phi_j-\phi_i)}
\langle u_i|u_j\rangle.
\]

Every pairwise overlap is nonzero. Therefore all three phases agree. Since the
three states span the qutrit,

\[
U=e^{i\phi}I_3.
\]

Thus the relative holonomy is projectively trivial.

## Stronger channel theorem

The exact result does not require the loop to be assumed unitary. Let `Phi` be
a trace-preserving channel and suppose

\[
\Phi(|u_i\rangle\langle u_i|)
=
|u_i\rangle\langle u_i|
\]

for all three probes.

Choose a Stinespring isometry `V`. Purity of each fixed output implies

\[
V|u_i\rangle
=
|u_i\rangle\otimes|e_i\rangle
\]

after absorbing a branch phase into the environment vector. Isometry of `V`
gives

\[
\langle u_i|u_j\rangle
=
\langle u_i|u_j\rangle
\langle e_i|e_j\rangle.
\]

Since every probe overlap is nonzero,

\[
\langle e_i|e_j\rangle=1.
\]

All three environment vectors are equal. By linear independence,

\[
V\psi=\psi\otimes e
\]

for every qutrit state `psi`. Therefore

\[
\Phi=\operatorname{id}.
\]

The three tests exclude both hidden unitary holonomy and route-induced
dephasing, provided the effective returned process is a trace-preserving
qutrit channel.

## Why fewer than three probes fail

Any set of fewer than three qutrit vectors spans a proper subspace. Choose a
unitary that is identity on that span and applies a nontrivial phase on an
orthogonal complement. Every tested line survives with probability one while
the unitary is not scalar.

Therefore at least three pure-state probes are necessary for a universal
identity test against arbitrary qutrit unitaries. The chosen SIC triple attains
the lower bound.

Nonorthogonality is also necessary for this three-probe construction. Three
orthogonal basis states would detect population movement but remain blind to
independent diagonal phases.

## Approximate unitary stability

Assume

\[
p_i\geq1-\epsilon
\]

for all three probes, with `epsilon` between zero and one, and assume that the
returned loop is unitary. Define

\[
\delta
=
\sqrt{2\left(1-\sqrt{1-\epsilon}\right)}.
\]

For each probe, choose a phase `a_i` such that

\[
\|Uu_i-a_iu_i\|\leq\delta.
\]

Inner-product preservation and the overlap magnitude `1/2` give

\[
|1-a_i^*a_j|
\leq
4\delta+2\delta^2.
\]

Choose `a=a_1`. Then every column obeys

\[
\|(U-aI)u_i\|
\leq
5\delta+2\delta^2.
\]

Using the frame inverse norm gives the explicit bound

\[
\inf_{|a|=1}\|U-aI\|
\leq
\sqrt6
\left(
5\delta+2\delta^2
\right).
\]

The constant is deliberately elementary rather than optimal. Its purpose is
to show that the exact three-line certificate has a finite local stability
margin fixed by the smallest Gram eigenvalue `1/2`.

## Route-comparison protocol

Let `R` and `S` be two independently compiled charged bridges. Their relative
loop on the initial qutrit sector is

\[
U=S^*R.
\]

For each of the three SIC lines:

1. prepare `u_i` in the initial sector;
2. traverse route `R`;
3. return through the inverse of route `S`;
4. test the projector onto `u_i`;
5. retain the route, probe, return-charge, and binary survival labels.

Exact survival in all three settings proves projective route equivalence. A
failed setting supplies a witness state on which the two constructors differ.

This is a three-setting sacrificial test. It is not one simultaneous
measurement on one unknown qutrit.

## What the test certifies

Under its assumptions, the test certifies:

- equality of the two logical bridge routes up to global phase;
- absence of qutrit dephasing in the closed returned channel;
- projective identity of the relative multiplicity holonomy.

It does not by itself certify:

- transient leakage during either route;
- reference or environment return outside the effective qutrit channel;
- locality, gap preservation, duration, or fault spread;
- correctness of the external names assigned to the SIC lines;
- independence of preparation and measurement calibration.

Those data remain in the physical constructor packet.

## Common-frame hostile model

Let one unknown unitary `W` conjugate:

- both charged routes;
- all three prepared probes;
- all three return effects.

Every survival probability is unchanged. The internal test still correctly
reports whether the two routes agree in that transported frame, but it cannot
identify the frame relative to an external logical convention.

Likewise, a shared implementation fault in route `R` and route `S` cancels in
`S*R`. Relative testing cannot certify either route absolutely. At least one
route or probe frame must have independent authority.

## Record and disturbance boundary

Each trial consumes a prepared qutrit copy. The final binary effect records
survival or failure and generally disturbs that copy. The theorem is about
ensemble certification of a repeatable constructor, not nondestructive
inspection of a data qutrit during computation.

The classical record can be copied and compared across trials. The unknown
input amplitudes cannot. This is the objective-record boundary in the
charged-route setting.

## Exact falsifiers

- Three selected SIC states are linearly dependent.
- Any selected pair has zero overlap while phase alignment is still claimed.
- The displayed Gram eigenvalues differ from `2,1/2,1/2`.
- Two or fewer pure probes are claimed sufficient against arbitrary qutrit
  unitaries.
- Three orthogonal basis-state survival tests are claimed sensitive to all
  diagonal phases.
- Unit survival on the three lines holds while a non-scalar unitary is
  retained.
- The channel theorem is applied to a trace-decreasing accepted branch without
  typing its success probability.
- The approximate unitary bound is promoted to arbitrary noisy channels.
- The same physical copy is used for all three incompatible survival tests.
- Internal route equivalence is promoted to absolute external frame
  calibration.
- Charge and reference return are inferred solely from logical survival.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies minimal separating probes, frame
conditioning, repeated sacrificial trials, route comparison, setting labels,
and relative versus absolute certification.

The quantum coefficient lens supplies SIC lines, unitary phase alignment,
Stinespring dilation, pure-output rigidity, channel identity, projective gate
distance, and measurement disturbance.

## Disposition

The existing SIC frame contains a minimal closure tester for charged bridge
routes. Three zero-phase edge lines are linearly independent and pairwise
nonorthogonal. Exact survival of all three proves that the complete returned
qutrit channel is identity; for a unitary loop it proves scalar holonomy.

This reduces route-equivalence certification from full process tomography to
three binary settings and supplies an explicit approximate unitary bound. It
still requires independently compiled preparations and effects, sacrificial
copies, and separate audits of leakage, reference return, locality, and
common-frame faults.

No build, checker, or Git operation was run for this research-only packet.
