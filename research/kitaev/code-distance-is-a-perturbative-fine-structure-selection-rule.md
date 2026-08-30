# Code Distance Is a Perturbative Fine-Structure Selection Rule

Let (H_0) be a commuting Pauli stabilizer Hamiltonian with ground-space
projector (P) and code distance (d). By definition, every Pauli operator of
weight below (d) either is detectable by the stabilizer syndrome or acts as
a stabilizer scalar on the code space.

Perturb by

\[
V=\lambda\sum_jV_j,
\]

where each (V_j) is a Pauli term of weight at most (w). A (k)-th order
virtual process contains an ordered product of (k) perturbation terms. Its
total support has weight at most (kw).

If

\[
kw<d,
\]

then the product cannot be a nontrivial logical Pauli. If it leaves a residual
syndrome, projection back to the ground space kills it. If it returns to the
ground space, it acts there as a stabilizer scalar. Therefore every effective
term below order

\[
k_*=\left\lceil\frac d w\right\rceil
\]

is proportional to (P) and cannot split the logical degeneracy.

At order (k_*\), logical splitting becomes allowed, not guaranteed. Path
selection rules, destructive interference, coefficient symmetry, or absent
authorized perturbation terms can still make the coefficient vanish.

## Resolvent form

For a gapped commuting stabilizer Hamiltonian, degenerate perturbation theory
contains terms schematically of the form

\[
PV_{j_k}R_0V_{j_{k-1}}R_0\cdots R_0V_{j_1}P,
\]

where (R_0\) is the reduced resolvent on excited syndrome sectors. The
resolvents change denominators and path weights but not the Pauli support
condition for returning to the code space. The first traceless logical term
still requires a product representing a nontrivial normalizer class.

If the excitation gap is \(\Delta\), a length-(k\) path has the nominal scale

\[
\lambda^k\Delta^{1-k}
\]

times its ordered-path coefficient. A genuine fine-structure estimate must
also control the number of paths and cancellations; distance alone supplies
the forbidden lower orders, not the prefactor.

## Toric code on an (L\times L) square torus

For the standard qubit toric code with one qubit per edge, the shortest
noncontractible primal or dual loop has weight

\[
d=L.
\]

Under single-edge Pauli perturbations, (w=1), so no logical splitting is
possible before order (L). At order (L), a product winding once around the
torus can produce a logical loop.

The leading permitted scale is therefore of the form

\[
t_\gamma
=
O\!\left(\lambda^L\Delta^{1-L}\right)
\]

before path multiplicities are evaluated. This is the algebraic origin of
exponentially small finite-size splitting when \(|\lambda|<\Delta\) and path
growth is controlled.

## Exact finite homology audit

For periodic square lattices of sizes (L=2,3,4), exact enumeration verifies:

- every cycle of weight below (L) is homologically trivial;
- a horizontal row loop of weight (L) has nonzero horizontal winding;
- a vertical column loop of weight (L) has nonzero vertical winding.

Thus the first allowed single-edge virtual process has precisely the geometric
length predicted by code distance.

## Readout is not splitting

A logical Wilson probe can distinguish ground sectors while the unperturbed
Hamiltonian remains exactly degenerate:

\[
R|_{P\mathcal H}\text{ non-scalar}
\quad\not\Rightarrow\quad
PHP\text{ non-scalar}.
\]

Conversely, physically coupling a probe can add a perturbation that splits or
dephases sectors. The readout row and the Hamiltonian perturbation must be
typed separately.

This is Sommerfeld's fine-structure demand in finite form: calculate which
process first lifts the multiplet, rather than inferring splitting from the
existence of a sector label.

## Completion boundary

Increasing distance suppresses each fixed local process, but a uniform
thermodynamic conclusion also requires:

- a gap \(\Delta\) bounded away from zero;
- controlled growth in the number of winding paths;
- bounded local perturbation strength;
- no source-authorized nonlocal term of weight comparable to (d).

Without those hypotheses, the first allowed order may grow while its total
coefficient fails to vanish.

## Cross-sector lesson

Grothendieck's flat jet connection transports zero multiplicity but does not
constrain zero location. Analogously, logical probes and syndrome transport
identify sectors without generating a splitting law. In both cases the
comparison must be derived on the uncompressed state space before scalar
readout. The analogy supplies no theta perturbation formula.

## Falsifiers

- Inferring energy splitting from a faithful logical readout.
- Claiming a nonzero (k_*\)-th order coefficient from distance alone.
- Applying the selection rule to unrestricted nonlocal perturbations.
- Ignoring a closing excitation gap or proliferating path count.
- Treating a finite-size exponential estimate as a uniform completion theorem
  without constants.
- Importing the toric perturbative scale into the theta/Fock sector.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to convert Sommerfeld's fine-structure question into an
exact selection rule.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Code distance forbids logical splitting below a computable perturbative
order; the coefficient and completion stability remain separate calculations.
