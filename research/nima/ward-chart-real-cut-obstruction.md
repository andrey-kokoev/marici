# Topic 9, iteration 3: the native Ward chart needs a real-boundary comparison

## Question and frozen conjecture

Can the existing marked-theta Ward chart be read directly as real physical
phase space, with its algebraic polarization closure serving as a positive
state-effect pairing?

**Conjecture:** no. Its generic momentum Gram block has inertia (2,2), whereas
real four-dimensional Lorentzian momentum space has inertia (1,3), up to the
opposite sign convention. The obstruction is to this DIRECT interpretation,
not to reconstructing real amplitudes from complex generalized cuts.

SCC obligation: forward realization / real-slice admission, upstream of any
Born density or detector readout. Contract:
`contracts/ward-chart-real-cut-obstruction.v1.json`.

Rivals are repair by changing a polarization reference or crossing signs;
identifying a rank-two Ward-transverse algebraic closure with a positive
Hermitian sum; substituting a=0 inside the same localized chart; and treating
failure of the real slice as failure of the complex Ward theorem.

## Actual source, not a replacement Gram model

`check_two_open_pair_ward_naturality.rs` retains five cubic vertices, all 243
sector words, twelve spanning-tree carriers, seven base primitives and four
additional transverse test vectors. Its identities are computed in a Gram-free
bilinear polynomial/Laurent chart without choosing spacetime dimension or a
Hermitian positive form. The complete file was inspected; it is not changed.

The new checker reads all 28 entries of the seven-primitive `base_gram` table
and binds the road/reference formulas to the actual Rust definitions. Taking
a principal submatrix is only a necessary test of a realization of the full
source: any such realization must realize this block. No source coordinates
or sector histories are quotiented away to manufacture the obstruction.

In the order p0,p1,k0,k1, that block is

\[
G(a)=\begin{pmatrix}
0&0&0&a\\
0&0&-a&0\\
0&-a&0&0\\
a&0&0&0
\end{pmatrix}.
\]

Here a is a formal source coordinate. A proposed real momentum realization
would have to send it to a real number. Both the original reference choices
and the Laurent divisions use a!=0.

## Exact real-slice obstruction

Use the coefficient vectors for
p0+k1, p1-k0, p0-k1, p1+k0 as columns of B. Direct congruence gives

\[
B^{\mathsf T}G(a)B=
\operatorname{diag}(2a,2a,-2a,-2a),\qquad
\det G(a)=a^4.
\]

For either real sign of nonzero a, the inertia is (2,2). A real realization
G=M^T eta M with eta=diag(1,-1,-1,-1) would require M invertible and would have
the inertia of eta by Sylvester's law. This is impossible. Equivalently, the
block has two positive and two negative directions and cannot embed in a
real Lorentz space with only one direction of either sign.

Incoming/outgoing sign changes and relabelings are real congruences, so they
cannot repair the defect. The checker retains all 384 signed permutations as
implementation controls; the conclusion follows from the displayed congruence,
not from a finite search over momenta. Polarization gauge choices do not change
the momentum block.

Only momenta are required to be real in this test. Ordinary complex helicity
polarizations are not excluded.

## Surviving complex and boundary controls

The source is not algebraically inconsistent. For example, in complexified
Minkowski coordinates take

\[
p_0=(1,0,0,1),\quad p_1=(0,1,i,0),\quad
k_0=(0,a/2,-ia/2,0),\quad k_1=(a/2,0,0,-a/2).
\]

Their BILINEAR Lorentz Gram matrix is G(a). A real split-signature realization
also exists. Both controls extend to the complete seven-primitive base table
at the explicitly tested specialization epsilon_i=p_i. Neither control claims
to realize every independent Gram variable in four dimensions, or to provide
a physical photon preparation. They preserve the legitimate use of complex
leading-singularity data.

At a=0 real collinear momenta can realize the zero momentum block, but every
one of the twelve original edge/reference denominators vanishes. There is no
evaluation of the localized ring at a=0. This does not assert that every
augmented amplitude has a nonremovable pole: cancellations and reconstruction
must be assessed on their own source-defined comparison.

A separately supplied real null reference restores an ordinary physical
polarization sum at that boundary. For n=(1,0,0,1), r=(1,0,0,-1),

\[
-\eta+\frac{nr^{\mathsf T}+rn^{\mathsf T}}{n\cdot r}
=\operatorname{diag}(0,1,1,0)
=\sum_{h=\pm}\epsilon_h\epsilon_h^\dagger,
\quad \epsilon_\pm=(0,1,\pm i,0)/\sqrt2.
\]

This is a positive control on a DIFFERENT reference chart, not a generic
continuation of the native a!=0 point. A separate real noncollinear 2-to-2
massless kinematic control also survives and explicitly has different Gram data.

## Why Ward closure is not yet the positive Cut

At the displayed complex point with a=1, the original slot-2, shift-2 reference
pair is p1,k0. The source closure kernel is

\[
P=-\eta+\frac{p_1k_0^{\mathsf T}+k_0p_1^{\mathsf T}}{p_1\cdot k_0}
=\operatorname{diag}(-1,0,0,1).
\]

It obeys Ward transversality and its mixed-index projection is idempotent of
rank two. Nevertheless J=(1,0,0,0) is Ward-transverse and J^dagger P J=-1;
both native reference choices give the same value. Thus this same-fiber
algebraic kernel cannot be identified with a positive Hermitian Gram sum.

There is no negative physical probability here. The analytic polarization
columns i e0 and e3 reproduce P by a bilinear transpose. Their Hermitian Gram
sum is diag(1,0,0,1), not P. Changing transpose to conjugate transpose changes
the closure operation; a source-defined real-boundary and conjugation
comparison must justify that change. Nor is J asserted to be the full
Yang-Mills current produced by the complete graph: it tests the claimed
positive-kernel interpretation on the admitted transverse input space.

## Claim boundary and disposition

The native source is a marked-theta Yang-Mills leading-singularity calculation,
not already the massive-electron QED amplitude of the external photon packet.
A native marked Laurent coaction, algebraic polarization contraction and
Cutkosky phase-space Gram pairing have distinct domains and pairings. Calling
all of them physical Cut does not identify them. The older scattering Bell
census calls its first gate a factorization CANDIDATE; that structural candidate
must not be promoted into a real phase-space certificate.

The first required comparison is therefore a source-derived reconstruction
from the complex generalized-cut data to a real physical amplitude and its
positive phase-space pairing, including the real structure, physical boundary
and amplitude conjugation. Reference calibration alone cannot supply it.

No obstruction to analytic reconstruction, other graph strata, real QED,
ordinary photon Hilbert spaces or the wider Marici programme follows. No Bell
value, physical apparatus, physical preparation or new probability law is
established here. The full Rust Ward audit is not freshly executed by this
checker; its formal theorem is not withdrawn.

## Verification

The frozen conjecture survives. The reference/sign and automatic-positivity
rivals fail; complex Ward algebra and ordinary real photon controls survive.

- Checker: `checkers/check_ward_chart_real_cut_obstruction.py`.
- Receipt: `results/ward-chart-real-cut-obstruction.json`.
- Owner model: `nima-ward-chart-real-cut-obstruction`.
- Manifest validation: `e_38524_1791417075893082900_135`.
- Freeze: `scc-freezes/nima-ward-chart-real-cut-obstruction.5033c8b01985752f.json`.
- Frozen challenge: `e_38524_1791417083817801700_137`, pass.
- Fresh model check: `e_38524_1791417146327426400_138`, pass.
- Failure/source-dependence controls: `e_38524_1791417327095602000_139`.
  AssertionError and RuntimeError propagate without leaving stale success;
  changing one pairing in a temporary native-source copy is rejected by the
  actual main. Live source, live receipt and recorded source hashes are unchanged.
- Final receipt/source-hash check: `e_38524_1791417736547280700_140`.

Early notice and tested report were admitted as communication proposals
`ep_c1537c78-e089-4d24-a7c9-49657e74f62a` and
`ep_9bfd361c-4e56-480b-b6ea-59dc6fdf96fb`; admission supplies provenance only.

Only owner-local new files and the topic index are changed. The Rust source,
other owners' files and physical apparatus are untouched; no commit or public
ledger publication is made.

## Boundary continuation: now tested separately

Iteration 4 (`ward-real-boundary-null-source.md`) executes the original
unlocalized tree evaluator and proves sectorwise vanishing on the real
collinear physical boundary. That is an additional test, not an inference from
the inertia calculation. Do not repeat the former boundary question or treat
the positive projector as a nonzero preparation. Reconstructed or regulated
amplitudes still require their own source-defined comparison.

Physical testing remains separate: the fresh admitted-surface inventory has no
optical apparatus binding, and the reread Aspect adapter/inventory packets are
simulation/schema material. No independently calibrated physical preparation/
record bundle has been received. Existing amplitude benchmarks explicitly
supply their interaction laws; their scalar/native evaluator comparisons do
not select a physical theory or provide the missing detector implementation.
