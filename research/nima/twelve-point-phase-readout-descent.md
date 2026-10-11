# The retained twelve-point phase law and its mixing readout

## Frozen question and closure condition

Does the ACTUAL full twelve-by-twelve phase implementation define its advertised
CKM readout on the declared matter spaces, independently of choices of bases in
degenerate eigenspaces? Can its phase law split the repeated singular values?

SCC obligation: attachment typing followed by readout descent on a fixed finite
matrix source. Retain every entry of the archived full implementation, its old
3456/1152/576 base matrix, all twelve phase slots, and its actual row/column
selections. The corrected subgroup counts from iteration 7 are NOT substituted.
That iteration's block/action classification and physical-selection boundary
remain closed (`twelve-arrow-blocks-and-generation-selection.md`).

Reuse the stronger flavor convention in
`../flavor/flavor-nine-link-conventions.md`: the shared doublet space carries
both left Grams; independent singlet basis changes are not CKM mixing. The
existing `../flavor/checkers/nine_link_exact_checks.py` supplies the independent
noncommuting positive control. Its already closed chart/basis distinction is not
being reopened. No flavor fitting or cross-owner mutation is authorized here.

**Conjecture:** the full implementation uses a diagonal unitary conjugation of
its supplied Gram. Its selected mass matrices have common doublet columns and
independently rephased singlet rows, hence identical doublet-side squared maps.
Their spectra cannot split under that phase law. The printed mixing instead
compares row-side singlet eigenframes and does not descend through degenerate
basis freedom.

**Rivals:** the full twelve-point attachment generates nontrivial common-doublet
misalignment missed by a reduced model; the apparent defect is merely a transpose
convention; the existing phase solver removes the repeated singular values;
all phase-sensitive flavor models fail for this reason.

**Risky consequences:** replay the complete preserved numerical producer and
its original phase values, bind it to the exact twelve-slot law, construct the
explicit adjoint adapter to the existing doublet-row convention, and change
only a degenerate eigenframe at unchanged source data. Recover the stronger
nine-link nonzero commutator as a control against a programme-wide inference.
The large old phase scan is not a valid substitute for a uniform identity.

**Equivalences:** retain the labelled full Gram as the source. On the conditional
Yukawa interpretation, quotient simultaneous doublet and independent singlet
unitary changes. At a repeated singular value, eigenframes have U(2) freedom;
individual entries of a chosen CKM matrix need not descend. Phases may still
matter to a separately specified coherent probe held fixed; no universal claim
that carrier phases are meaningless is intended.

**Closure:** either exhibit invariant, nonzero common-doublet misalignment from
the SAME full source, or establish its exact alignment and a fixed-source
counterexample to the printed readout. Separately settle whether the solver's
phase law can change singular values. Further physical selection requires new
data or a different law, not a finer search within this one.

## Exact comparison on the full source

The original phase loop, replayed symbolically rather than replaced by a
three-by-three ansatz, gives

\[
G(\theta)=D^\dagger G_0D,\qquad D_{ii}=e^{i\theta_i}.
\]

This preserves the complete twelve-dimensional spectrum, determinant and
positivity for EVERY phase vector. The compendium's purported phase-dependent
inflationary determinant therefore does not follow from this law either;
that direct consequence is visibly superseded without claiming to test a
separate cosmological potential. In particular, positivity of all sectors cannot force
nonzero phases: the zero-phase point satisfies it, and every other phase point
is unitarily similar. The phase factors also telescope around every cycle.
No implemented higher-order constraint in this model selects a different orbit.
The supplied base remains positive; its erroneous group-count interpretation
was already separated from numerical validity in iteration 7.

Let A=576(I3+J3), and restrict D to the original up-singlet rows, down-singlet
rows and common doublet columns, obtaining Ru, Rd and L. The actual submatrices
are

\[
M_u=R_u^\dagger A L,\qquad M_d=R_d^\dagger A L.
\]

Their singular values are 576,576,2304, for all twelve phases. This remains
true even when either displayed M is non-Hermitian.

The existing flavor implementation puts doublets in ROWS. The typed adapter
is Y=M-dagger, not reuse of the same numerical array with changed labels. Hence

\[
H_u=Y_uY_u^\dagger=M_u^\dagger M_u
    =L^\dagger A^2L=M_d^\dagger M_d=H_d.
\]

The heavy line and the light two-plane coincide. Independent singlet frame
changes and one COMMON doublet frame transform the pair to (A,A). There is an
identity CKM representative, but not a uniquely labelled light-eigenvector
basis. Calling arbitrary entries within that degenerate plane distinct physical
predictions would repeat the presentation/physics error.

The old script instead computes M_u M_u-dagger and M_d M_d-dagger. These live
on two different singlet spaces; their displayed coordinate identification is
not the charged-current comparison on the shared doublet space. Transposition
is not a harmless explanation of this difference: carrying the attachment
through the explicit adjoint adapter yields the equality above.

## Fixed-source eigenframe counterexample

The exact spectral frame for A consists of (1,-1,0)/sqrt(2),
(1,1,-2)/sqrt(6), and (1,1,1)/sqrt(3). Every U(2) change of the first two
columns preserves the diagonalized matrix. For ANY unitary displayed comparison
C, at least one column has a nonzero vector v in its first two rows. Write
r=norm(v)>0. A U(2) frame change sends v to (r,0); composing a 45-degree
rotation sends it to (r/sqrt(2),r/sqrt(2)). A displayed squared modulus therefore
changes from r-squared to r-squared/2 without changing either source operator.
This is not a change of phase parameters or a different physical model.

At the original script's unchanged numerical input phase vector, a full replay
produces displayed angles 66.00,54.06,50.7984 degrees, not its advertised observed
values. Changing only the up singlet's degenerate eigenframe changes the squared
(0,2) modulus from approximately 0.86236718 to 0.43118359. Reconstruction errors
are below 5e-9 on the original squared matrices. Those floating-point figures
are diagnostics; the uniform U(2) argument, not a tolerance or a particular
LAPACK eigenbasis, establishes non-descent. The generic nondegenerate CKM chart
cannot be used as a faithful coordinate on this degenerate stratum.

## The phase solver is a different attachment, but cannot split masses

The existing `check_flavor_solver.py` was inspected before replacement. Its
matrix-building function is lifted directly to exact arithmetic:

\[
Y(\phi)=P^\dagger A P,\qquad P_{ii}=e^{i\phi_i}.
\]

Contrary to its comment, this Y IS Hermitian. Its normalized singular values
are identically (1,1/4,1/4). Against its supplied target
(1,0.0685,0.00013), the squared mass residual is always
953772669/10000000000. A finer version of its 37-to-the-fourth phase scan cannot
split the repeated masses. The actual setup/functions were replayed; the scan
was deliberately not run, and no replacement fit was supplied.

This solver gives the two sectors independently phased doublet attachments;
it is NOT the common-column attachment of the full twelve-point model. It can
change a surviving invariant: its original constructor at phases (0,pi,0) and
(0,0,0) gives heavy-projector overlap Tr(Pu Pd)=1/9 and noncommuting squared
matrices. That conditional fact is retained. It does not remove spectral
degeneracy or define unique three-angle CKM coordinates.

## Stronger predecessor and scope control

The imported `nine_link_exact_checks.py` Example I and its existing rational
weak-basis comparison still transport the declared invariants. Its original
rational witness has full-rank Yukawas, simple squared spectra and NONZERO
commutator determinant. Thus the same correctly typed comparison detects
misalignment in the stronger existing flavor source. Nothing here refutes that
construction, its fitted observables, or all phase-sensitive flavor models.

Nor does conjugation invariance of a spectrum imply that a fixed coherent
probe cannot detect phases. The completed comparison in
`retained-relative-phase-readout.md` retains endpoint calibrations precisely
because a reference-sensitive reading is not a spectrum. Its scope is unchanged.

## Disposition and evidence repair

**Closed:** the full model's shared-doublet operators align; its printed
singlet-eigenframe CKM does not descend. Its phase-only solver cannot reach its
own nondegenerate mass target. The surviving positive data are the full positive
Gram, its exact attachment maps, and the separate solver's relative heavy-line
invariant—not measured SM masses or mixing.

The first missing data for a different physical result are a source-derived
change of the mass/attachment law and a correctly typed shared-doublet readout.
Another compatible rephasing, a finer scan or a claim that an unspecified
higher-order closure will select the answer does not reopen this branch.

`check_ckm_variational.py` also has a reproduced quote SyntaxError at line 191.
Its printed assertion that simultaneous consistency forces nonzero CKM is not
an implemented constraint. Fixing that quote alone would not supply one. This
execution defect is separate from the uniform algebraic obstruction above.

That script and `check_flavor_solver.py` now refuse verification with exit 2.
Their complete originals and three pre-correction index/compendium/session pages
are preserved under `quarantine/20261007-phase-readout-evidence/SHA256SUMS`.
The original full phase producer remains in the earlier generation quarantine;
none of its entries or phases were rewritten. All three historical receipt
paths remain untouched. The current claim entry points visibly link here.

## Verification and failed-test accounting

Producer: `checkers/collect_phase_readout_diagnostics.py`, admitted SciPy profile;
exact consumer: `checkers/check_twelve_point_phase_readout.py`, SymPy profile.
The consumer replays the original phase-loop AST and the original solver's
matrix-building function. Euler's identity supplies exact phase arithmetic;
no new matrix entries or phase parameters are fitted. Original numerical output
is diagnostic transport, not exact proof. Deliberately asserting a zero mass
residual is rejected by the failure gate.

Initial freeze `640629db46353261` and challenge
`e_38524_1791400499584145800_66` failed at the two-vector lemma. Diagnostic
`e_38524_1791400537933979300_67` localized the residual to SymPy's
conjugate(1/sqrt(a-squared+b-squared)): the stated nonzero domain had not been
encoded in its assumptions. The repair uses an explicitly positive radius and
polar components; it still covers a zero in either component. Neither the
source law nor the closure predicate was weakened. The failed freeze remains
available; it is not reported as a passing run.

Corrected freeze:
`scc-freezes/nima-twelve-point-phase-readout.8ca22fe2968a18bf.json`.
Challenge `e_38524_1791400615828905900_69` passes. Results:
`results/phase-readout-transport.json` and `results/twelve-point-phase-readout.json`.
The frozen conjecture survives on the declared source; that is not a physical
selection or a general flavor no-go.

Final producer replay `e_38524_1791401072007340000_70` and fresh headless closure
`e_38524_1791401088192478500_71` pass. The earlier generation comparison also
passes unchanged (`e_38524_1791401089385867400_72`). Integrity check
`e_38524_1791401220009342900_73` finds no drift in the 14 consumed inputs and
confirms the three old receipts remain absent. Graph event:
`ev-000000015823-9dd4189b-845f-4b29-9c84-4733eeb05cea`, proposal
`ep_cce07a10-f8a0-49e1-9495-c1bf0cbafe47`. The admitted audit/correction interval
[15815,15823] remains uncommitted; no push or publication was performed.
