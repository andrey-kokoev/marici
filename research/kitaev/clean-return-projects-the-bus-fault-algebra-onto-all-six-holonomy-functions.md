# Clean return projects the bus fault algebra onto all six holonomy functions

## Bounded question

What part of the complete six-level ancilla operator algebra is invisible to
the clean-return test of the \(S_3\) holonomy compiler, and how does each part
propagate to the four boundary edges?

The answer is exact. Clean return removes off-diagonal bus transitions from the
accepted branch but preserves every diagonal function of the computed
holonomy. Peter–Weyl decomposition then resolves the six-dimensional accepted
fault space into the trivial, sign, and standard-representation sectors.

## Frozen compute map

Let

\[
U|\mathbf g\rangle|e\rangle
=|\mathbf g\rangle|h(\mathbf g)\rangle,
\]

where

\[
h=g_0g_1g_2^{-1}g_3^{-1}.
\]

Insert an arbitrary ancilla operator \(E\) after compute and before uncompute.
Ignore the intended predicate phase, which commutes with diagonal faults and
can be absorbed into the ideal target for this propagation calculation.

Measure the final ancilla in the group basis. For outcome \(r\), define the
induced data operator

\[
K_r(E)
=\langle r|U^\dagger(I\otimes E)U|e\rangle.
\]

## Exact fault-to-syndrome transform

On a data sector with holonomy \(h\), the error sends the computed bus state
\(|h\rangle\) to

\[
E|h\rangle=\sum_aE_{a,h}|a\rangle.
\]

Uncompute right-multiplies the bus by \(h^{-1}\), so the final outcome is
\(r=ah^{-1}\). Equivalently, \(a=rh\). Therefore

\[
K_r(E)
=\sum_{h\in S_3}E_{rh,h}B^h.
\]

The six final bus outcomes read the six left-shifted diagonals of the
\(6\times6\) error matrix. Across all \(r\), the coefficients

\[
\{E_{rh,h}:r,h\in S_3\}
\]

are exactly all 36 matrix entries of \(E\). The complete syndrome-indexed
family \(\{K_r(E)\}_r\) is therefore an invertible rearrangement of the bus
operator algebra at the level of coefficients.

The final bus label alone does not reconstruct those coefficients, because the
data still carries the holonomy-dependent operator \(K_r(E)\). But the formula
shows exactly where every fault component goes.

## Clean accepted branch

The clean-return outcome is \(r=e\). Its induced operator is

\[
K_e(E)
=\sum_hE_{h,h}B^h.
\]

Thus the accepted branch preserves the full diagonal of \(E\). The clean test
is blind to a six-dimensional linear space of holonomy functions, including a
five-dimensional non-scalar harmful subspace.

For a diagonal unitary

\[
E_f|h\rangle=f(h)|h\rangle,
\qquad
|f(h)|=1,
\]

the bus returns clean with certainty and the data receives

\[
f(h)=\sum_hf(h)B^h.
\]

This characterizes every perfectly hidden unitary phase fault, not only the
sign example.

## Peter-Weyl decomposition for S3

The complex function space on \(S_3\) decomposes as

\[
\mathbb C^{S_3}
\cong
V_{\mathbf 1}\otimes V_{\mathbf 1}^*
\oplus
V_{\mathrm{sgn}}\otimes V_{\mathrm{sgn}}^*
\oplus
V_{\mathrm{std}}\otimes V_{\mathrm{std}}^*.
\]

The dimensions are

\[
1+1+4=6.
\]

Accordingly, the clean accepted fault space contains:

- one trivial scalar direction;
- one sign-character direction;
- four matrix-coefficient directions of the two-dimensional standard
  representation.

Only the trivial scalar direction is automatically neutral. The other five
directions can change coherent endpoint amplitudes while leaving the bus label
clean.

## Gauge-invariant and frame-sensitive parts

Gauge conjugation sends

\[
h\longmapsto xhx^{-1}.
\]

A hidden phase function is gauge invariant precisely when it is constant on
conjugacy classes. The class-function subspace has dimension three, with basis
given by the three irreducible characters:

\[
\chi_{\mathbf1},
\qquad
\chi_{\mathrm{sgn}},
\qquad
\chi_{\mathrm{std}}.
\]

After removing the neutral constant, two independent gauge-invariant harmful
directions remain. They change phases or amplitudes among the identity,
transposition, and three-cycle flux classes without violating gauge
invariance.

The remaining three standard-sector directions are not class functions. They
are frame-sensitive hidden faults. A complete gauge-constraint check may
detect some of them, but clean bus return does not.

Thus ordinary gauge syndrome can at best remove the noncentral portion. It
cannot eliminate the two-dimensional central harmful subspace.

## Ordered propagation of matrix coefficients

Let \(D^\lambda\) be an irreducible representation and take the diagonal bus
operator whose symbol is the matrix coefficient

\[
f_{ij}^\lambda(h)=D^\lambda(h)_{ij}.
\]

On the four-edge holonomy,

\[
D^\lambda(h)
=D^\lambda(g_0)D^\lambda(g_1)
D^\lambda(g_2)^{-1}D^\lambda(g_3)^{-1}.
\]

Therefore

\[
f_{ij}^\lambda(h)
=\sum_{a,b,c}
D^\lambda(g_0)_{ia}
D^\lambda(g_1)_{ab}
D^\lambda(g_2)^{-1}_{bc}
D^\lambda(g_3)^{-1}_{cj}.
\]

This is an ordered matrix-product operator with bond dimension
\(\dim V_\lambda\).

For the sign representation, the bond dimension is one and the result
factorizes into four local sign phases. For the standard representation, the
bond dimension is two. Its hidden fault is an intrinsically ordered correlated
four-edge operator rather than a product of scalar edge phases.

The noncommutative coefficient lens is therefore not optional in the full
fault audit. Scalar character propagation sees the one-dimensional sectors but
misses the ordered standard block.

## Translation-phase operator coordinates

Every bus operator can also be expanded as a sum of a left translation followed
by a diagonal function:

\[
E=\sum_{r\in S_3}L_rD_{f_r}.
\]

In these coordinates,

\[
K_s(E)=D_{f_s}(h)
\]

up to the fixed convention relating matrix entries to left translation. The
final bus label identifies the translation sector, while the data retains its
coefficient function.

This explains the earlier split:

- pure translation faults move the final bus label and are rejected;
- pure diagonal faults remain in the clean sector and kick back to data;
- general faults contain both a visible translation syndrome and a residual
  holonomy-dependent operation.

Rejecting every nonidentity bus outcome does not make the accepted operation
scalar. It only selects the zero-translation sector.

## Dimension hierarchy

The exact dimensions are:

- full bus operator algebra: 36;
- syndrome sectors: six, each carrying six coefficient directions;
- clean accepted coefficient space: six;
- clean gauge-invariant coefficient space: three;
- clean gauge-invariant harmful space modulo scalars: two;
- sign-character witness space: one.

The single sign witness therefore proves failure but does not exhaust it. Even
after imposing gauge invariance, one additional independent central direction
remains.

## Implications for verification

A computational-basis return test observes the translation coordinate of the
bus fault and ignores its diagonal coefficient coordinate. Repeating the same
test cannot close the missing sector.

A complete repair must make every admitted non-scalar diagonal bus operator
either:

- produce a syndrome before output acceptance;
- act as a proved neutral scalar on the logical data;
- or enter a retained recovery port.

Measuring the bus in a Fourier-conjugate basis during computation would reveal
phase information but generally disturb the coherently stored holonomy. The
natural repair is therefore an encoded bus or a coherent verification gadget,
not an untyped additional measurement.

The verification theorem must cover both the one-dimensional character sector
and the four-dimensional standard sector. Protecting only parity leaves the
ordered matrix-coefficient faults unresolved.

## General finite-group theorem

For any finite group \(G\) and a clean product bus, the final outcome \(r\)
after an inserted bus error \(E\) induces

\[
K_r(E)=\sum_{h\in G}E_{rh,h}B^h.
\]

The clean branch is the diagonal symbol map

\[
E\longmapsto\sum_hE_{h,h}B^h.
\]

Its image has dimension \(|G|\) and decomposes under Peter–Weyl as

\[
\bigoplus_{\lambda\in\widehat G}
V_\lambda\otimes V_\lambda^*.
\]

The class-function portion has dimension equal to the number of conjugacy
classes. Unless the admitted logical data collapses every nonconstant class
function to a scalar, clean return alone leaves central undetected faults.

## Exact falsifiers

- Clean return claimed to retain only scalar ancilla faults.
- The accepted fault-space dimension for the six-level bus claimed smaller
  than six without an additional check.
- The sign direction claimed to exhaust gauge-invariant hidden faults.
- A standard-representation matrix coefficient claimed to factor into four
  scalar edge functions.
- Final bus outcome claimed to reconstruct the full error without access to
  the data residual.
- Rejection of all nonidentity bus labels claimed to remove diagonal phase
  faults.
- A parity-only repair claimed to protect the full ancilla operator algebra.
- Fourier measurement during compute claimed nondemolition without a coherent
  encoding or recovery proof.

## Machine-readable decomposition

```json
{
  "code": "holonomy_bus_clean_return_peter_weyl_decomposition",
  "group": "S3",
  "bus_operator_dimension": 36,
  "final_bus_outcomes": 6,
  "coefficient_directions_per_outcome": 6,
  "clean_accepted_dimension": 6,
  "clean_harmful_mod_scalars_dimension": 5,
  "peter_weyl_block_dimensions": [1, 1, 4],
  "class_function_dimension": 3,
  "gauge_invariant_harmful_mod_scalars_dimension": 2,
  "standard_sector_dimension": 4,
  "standard_sector_edge_bond_dimension": 2,
  "clean_return_complete_for_full_fault_algebra": false,
  "encoded_phase_sensitive_verification_required": true
}
```

## Deutschian explanation

The bus has two conjugate kinds of error information. Translation errors change
which label returns and are visible to the label check. Phase errors change the
meaning of the coherent path while leaving the returned label untouched.

Uncompute sorts these two kinds rather than destroying them. Translation is
left in the bus syndrome; phase is deposited as a function of the holonomy on
the data. Peter–Weyl theory lists every possible function and reveals the
ordered two-dimensional sector that a scalar parity audit cannot see.

## Shared Carrier geometry and quantum coefficient lens

The Carrier geometry is the exact syndrome-indexed diagonal transform

\[
E_{a,h}\longmapsto E_{rh,h},
\qquad
r=ah^{-1}.
\]

It applies to any finite product bus. The quantum coefficient lens supplies the
Fourier duality between translations and phases and the noncommutative matrix
coefficients whose propagation remembers edge order.

## Claim boundary

This packet derives the complete linear propagation transform for an arbitrary
single bus operator inserted after compute and before uncompute. It classifies
the clean accepted space by Peter–Weyl and gauge conjugation. It does not yet
propagate faults inserted inside individual multiplication gates, construct an
encoded bus, or prove a minimum physical overhead for phase-sensitive
verification.

## Process calibration

Excitement is 10/10 and confidence in the finite decomposition is 10/10. The
fault gap is now fully typed at the central bus location: five non-scalar clean
directions, including two gauge-invariant directions and an ordered
four-dimensional standard block. The next constructive target is the smallest
coherent bus encoding whose accepted single-rail diagonal faults are scalar.
