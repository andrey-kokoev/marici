# The physical half twist leaves one noncyclic operational direction

> **Typing correction.** The differential interpretation below is
> superseded by `cosmology-frozen-krylov-annihilator-typing-correction.md`.
> The ranks and dual vector remain valid finite linear-algebra data, but the
> repeated frozen-point operator closure is not a Gauss--Manin orbit: after
> the first derivative it omits derivatives of the reduced coefficients and
> of the connection.  Consequently the displayed line is not presently a
> physical, horizontal, or source-inaccessible quotient line.

The five-mark quotient remains rank 26 at \(\gamma=-1/2\) through common
\(K\)-pole depths two and three. However, after complete pivot elimination,
the literal unsplit physical numerator and its two implemented horizontal
operators generate rank 25, not 26. At generic \(\gamma=5\), the identical
construction generates rank 26.

This pattern replicates over \(\mathbf F_{32003}\) and
\(\mathbf F_{32009}\):

\[
(\dim H,\dim\operatorname{Orb}(s))=
\begin{cases}(26,26),&\gamma=5,\\(26,25),&\gamma=-1/2.\end{cases}
\]

The result separates two notions that had been conflated:

- the physical module is a regular base change of the generic module family;
- the literal source is not a cyclic generator after physical specialization.

Therefore one quotient line is present algebraically but inaccessible to the
implemented source-operation orbit. It may be readout-only, supported,
extension data, or an artifact of retaining only two kinematic operators. No
interpretation is authorized until its intrinsic annihilator and the missing
third-direction audit are computed.

## Full-direction and dual-line result

Adding the third external kinematic derivative leaves the orbit rank equal to
25 at both primes and both \(K\)-pole depths. The residual is therefore not an
omitted-axis artifact.

The intrinsic annihilator is one-dimensional. In the common physical
Plücker chart it has the replicated representative

\[
\boxed{
\ell_{\rm phys}
=
[a^5]^\vee-[a^4b]^\vee.
}
\]

It is supported entirely in numerator degree five and is identical at
\(K\)-pole depths two and three. This is lower than the degree-six/seven
replacement-relation packet, so the noncyclic line is not simply one of the
five changed relations re-labelled.

The displayed two-coordinate formula is a representative in the certified
Plücker chart; the invariant object is the annihilator line of the full
three-direction source orbit. No primal complement has been selected.

Next, transport this dual line through the cyclic residue-chart relabelings
and compare it with the canonical Leray period covector. Agreement would
identify the source-inaccessible direction as physical readout data;
disagreement would keep it as an algebraic operational residual.

Evidence:

- `research/nima/checkers/check_rank26_half_twist_kpole_stabilization.py`
- prime-indexed result packets of the same name.
- `research/nima/checkers/check_rank26_physical_orbit_annihilator.py`
- its two prime-indexed result packets.
