# 2672 — The Exact Presentation Has No Strict Base Connection

## Proposed object

The previous frontier asked for a connection on the two-term exact presentation

\[
P^4\xrightarrow{g}P,
\qquad
g=(5K_a,5K_b,5K_c,zK-1),
\]

followed by its Atiyah commutator.

## Typing condition

A strict connection in base direction \(\mu\) would require a matrix \(B_\mu\) on the generator module such that differentiation commutes with the presentation map:

\[
\partial_\mu g+gB_\mu=0.
\]

Reducing modulo \(I\), this requires

\[
[\partial_\mu g]=0\quad\text{in }I/I^2.
\]

The class on the left is precisely the labelled Kodaira–Spencer section \(\kappa_\mu\).

## Falsifier

Entry 2656 established

\[
\operatorname{rank}\langle\kappa_1,\kappa_2,\kappa_3\rangle=3.
\]

Therefore no labelled base direction admits the required strict presentation connection. The proposed two-term Atiyah commutator is not merely uncomputed; it is undefined on that object.

## Narrow result

The canonical replacement is the cotangent-transitivity or Kodaira–Spencer cone retaining both the base tangent module and \(I/I^2\):

\[
T_B\xrightarrow{\kappa} I/I^2.
\]

The curvature obstruction must be tested in this relative cone. It cannot be assigned to a strict connection on \(P^4\to P\), and failure of that nonexistent connection must not be repaired by selecting a generator splitting.

## Existing evidence

- `research/benincasa/checkers/check_cm_conormal_kodaira_spencer.py`
- `research/benincasa/results/cm-conormal-kodaira-spencer.json`
- Entry 2656

## Next falsifier

Construct the finite cotangent-transitivity complex from the already exported three labelled sections. Compute its degree-zero and degree-one cohomology, retain the unique pair-wedge relation as a syzygy cell, and test whether Entry 2662's obstruction defines a typed secondary operation on that cone.
