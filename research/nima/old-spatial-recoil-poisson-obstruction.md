# Can the retained spatial and recoil readings be one canonical pair?

## Frozen question and closure condition — iteration 2

Keep the existing `shared-recoil-cotangent-binding.md` implementation, its
six labelled pulses, metric, preparation, records, and full nonzero-anchor
chart. Here “old spatial reader” means specifically the canonical-chart
endpoint-vector reader x=Aq, not an intensity reader or an independently
measured position. A is the existing 3-by-6 target-vertex matrix.

Can three C1 functions of the retained real-amplitude recoil readings serve
as canonical momenta conjugate to this SAME x on an open state domain? Allow
arbitrary nonlinear postprocessing and even the retained reference pair as
additional arguments: f=f(P0,pi,Q,phi), where

    P0=b*R-D*q,  pi=b*R+q,
    R=sqrt((Q-E(q,p))/mu),  E=q^T*K*q+p^T*K^-1*p/4,
    Omega=sum dq_i wedge dp_i+dQ wedge dphi.

The angle phi is only a local reference-phase coordinate, not a clock. The
source domain is Q>E (equivalently R>0); all six q,p pairs remain present.
Use the inherited bracket convention {q_i,p_j}=delta_ij and {phi,Q}=-1.
The SCC obligation is readout compatibility/descent on this already checked
source realization, not a new forward realization or route-coherence claim.

**Conjecture to test:** such momenta exist. Closure requires either a literal
canonical map with {x_a,f_b}=delta_ab and commuting momenta, or a rank bound
that excludes even the necessary mixed-bracket identity throughout this
reader class. A stronger physical-selection question cannot reopen this one.

**Rivals:** reference coupling rescues the mixed bracket; all brackets vanish
because the anchor was silently fixed; the obstruction holds only for linear
maps or selected endpoints; canonical momenta do exist but use information
outside the recoil reading.

**Risky test:** derive the full Poisson tensor from the current implementation,
not from an independently supplied oscillator. Test the mixed reader Jacobian
symbolically. Retain reference coupling, all internal directions, and check
both a nonzero-bracket state and an actual retained endpoint. Compare with
the already constructed positive pair (Aq,Wp), W=(AA^T)^-1 A. A chain-rule
argument must cover nonlinear readers; a sample rank calculation alone does
not close the question.

## Full-source comparison

The existing implementation supplies the change matrix from canonical
coordinates (phi,-Q,q,p) to (R,phi,q,p). Transporting its Poisson tensor gives
exactly minus the inverse of its full inherited Omega. Thus the reference
coupling is included rather than inferred from a fixed-anchor slice.

At fixed Q, differentiation of the existing radius formula gives

\[
\{q,R\}=-\frac{K^{-1}p}{4\mu R},\qquad
\{Aq,Q\}=\{Aq,\phi\}=0.
\]

Let y=(P0,pi,Q,phi) denote all fourteen reported components. Their mixed
bracket with x is the outer product

\[
\{x,y\}=v w^T,\qquad
v=-\frac{AK^{-1}p}{4\mu R},\qquad
w^T=(b^T,b^T,0,0).
\]

The current source has b nonzero and rank(A)=3. The mixed matrix therefore
has rank one where AK^-1*p is nonzero, and rank zero on its vanishing locus.
This is an identity on the whole R>0 chart, not a conclusion from sampled
endpoint ranks.

For any admitted C1 triple f(y), the chain rule gives

\[
\{x,f\}=v w^T(Df)^T,\qquad
\operatorname{rank}\{x,f\}\leq1<3.
\]

It cannot equal the required identity matrix. Nonlinear postprocessing,
reference-pair access, invertible component changes or mass rescalings of
these readings cannot repair the rank. Allowing new p-directional information
would change the reader class, not evade this theorem.

## Strongest falsification and surviving alternative

A source-domain state with R=1, q=0 and p=4*mu*K*W^T*e1 gives v=-e1, hence
rank exactly one. Its radius, budget and shared-recoil inverse are checked
by the existing constructors. Silently fixing the anchor instead makes the
real-recoil mixed bracket zero and fails the full symplectic inverse test.
The rival claim that the bracket vanishes identically is therefore rejected.

The actual retained endpoint AB,BA,AB,BA,AB,BA,AB,BA has p=0 and mixed bracket
zero; its original family/slot/sample record is retained. The stronger
all-state rank bound does not rely on extrapolating from this endpoint.

The already constructed pair (Aq,Wp) still has mixed bracket I3 and commuting
momenta. It is not a counterexample: states (q,p) and (q,-p) in the preceding
source-domain witness have identical P0,pi,Q,phi but opposite nonzero Wp.
They are not asserted to be two native forward words. The full chart and
shared recoil configurations distinguish them; only the chosen momentum/
reference reader forgets that information.

## Disposition and decision

**Closed negatively:** the fixed reader x=Aq cannot have three independent
canonical conjugates formed solely from the admitted recoil/reference data.
This removes the joint canonical interpretation, including nonlinear versions,
without eliminating either existing canonical presentation separately.

Keep the complete shared recoil/cotangent embedding and the old (Aq,Wp) chart.
Do not fit further masses or reader postprocessing to make this same pair
canonical. Neither construction identifies laboratory positions or momenta;
selection between their physical interpretations remains underdetermined by
this comparison. A noncanonical constrained physical reading is not excluded.
No further compatible example can settle that selection without an independent
source/readout criterion. This is a stopping boundary for that branch, not an
open request to construct more polarizations.

## Verification and evidence boundary

`checkers/check_old_spatial_recoil_poisson_obstruction.py` freshly runs the
existing shared-recoil implementation, including its 1,152 controls and its
22/882/455-control predecessor chain. Its 23 additional controls verify the
full Poisson inverse, symbolic factorization, positive comparison and the
specified hostile states. The chain-rule proof above supplies the nonlinear
quantifier; the checker does not claim to enumerate all C1 functions.

Receipt: `results/old-spatial-recoil-poisson-obstruction.json`, including
transitive source hashes and exact rational witnesses. Frozen SCC comparison:
`scc-freezes/nima-old-spatial-recoil-poisson-obstruction.226e4b04deb15b42.json`.
Execution `e_38524_1791390220819502100_19` exits zero; its declared convention
is that zero **falsifies the joint-reading conjecture**, not that the candidate
survives. SCC's challenge wrapper uses an exit-code-only adapter; the symbolic
evidence is in the checked source and receipt, not that adapter. Final scoped
SCC check `e_38524_1791390532121538000_20` passes after the predecessor's closure
notice was added; `e_38524_1791390618976973000_21` confirms all twelve transitive
implementation hashes remain current.

The prior-search packet `canonical-polarization-and-recoil-prior-clues.md`,
the shared-recoil packet and iteration-1 continuation now visibly point to the
completed comparisons rather than inviting their repetition.

Graph report: `ev-000000015817-a6a1d6fe-4410-463c-a602-0b92c650a860`, proposal
`ep_bdf75811-0934-4e6e-a75c-35cf93576b53`. This turn's interval [15817,15817]
and the preceding audit/repair intervals [15815,15816] remain uncommitted.
Admission records provenance, not truth. No commit, push or publication occurred.

This is an exact comparison theorem within the existing analytical realization,
not a new native Agda theorem, NumPy/137-port source comparison, experiment,
or physical position/particle/charge/time identification. No existing source
operation, metric, preparation or script was replaced.
