# C1 audit: the physical cusp readout is currently conditional

C1 asserts that the source-derived Bunch--Davies residue current specializes with multiplicity one to the primitive conductor half-boundary

\[
(1,-1,1,-1).
\]

The audit separates two stages.

## Stage supplied by the source

The published negative-imaginary boundary value and the transverse coordinate

\[
q_{\mathcal G_{12}}=E+y_{12},
\qquad dq=dy_{12},
\]

fix a unique local Leray residue germ with multiplicity one:

\[
\operatorname{Disc}\frac1{q-i0}=2\pi i\,\delta(q).
\]

Thus the physical positive current has a canonically oriented residue continuation on every generic transverse patch.

## Stage awaiting construction

C1 also requires the external-total-energy specialization

\[
\operatorname{Sp}_E(\Gamma^{\rm res}_{\rm BD})
\longrightarrow
C_1(\widetilde S_0,\mathcal C;\mathbb Z).
\]

The available source packets leave this map unmaterialized. In particular:

- the literal positive chain has zero incidence with the marked cut union before analytic continuation;
- the residue germ belongs to the analytically continued nearby-cycle problem;
- the source supplies fiberwise Gauss--Manin transport rather than a parameter-space current;
- the conductor cospan audit still requests two labelled degree-one chains and their relative Stokes pairing.

The geometric calculations determine the candidate image and its orientation:

\[
(1,-1,1,-1),
\]

while the integer intersection coefficient of the transported source current with that candidate remains to be computed.

## Disposition

C1 remains open. The current evidence supports neither confirmation nor rejection.

The previously assembled physical formulas are conditional predictions:

\[
\operatorname{Disc}\Pi_{111}^{\rm reg}
=\pm2\pi i\,\Pi_{\varepsilon_6},
\qquad
(a,b)=(1,0),
\]

conditional on the multiplicity-one comparison. Their algebraic extension, cellular incidence, Picard calculation, and logarithmic consequences remain valid within that hypothesis.

The decisive next computation is explicit: write the transported residue current using the Cayley--Menger and signed-minor inequalities near \(E=0\), lift it through the simultaneous resolution of the four \(XY=Es^2\) points, and intersect it with the two oriented node bridges.

Certificate:

- `research/voevodsky/checkers/audit_C1_physical_current_specialization.py`;
- `research/voevodsky/results/C1_physical_current_specialization_audit.json`.
