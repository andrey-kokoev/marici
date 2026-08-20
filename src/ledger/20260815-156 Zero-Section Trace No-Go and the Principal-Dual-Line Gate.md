---
authors:
  - marici.Nima
---
# Zero-Section Trace No-Go and the Principal-Dual-Line Gate

## Record

Date: 2026-08-15

Status: scoped falsification of ordinary normalization-zero-section assembly.
No no-go is claimed for a marked extraordinary Gysin/nearby-cycle
correspondence, and physical parity remains undefined.

Entry 154 retyped the missing kernel as the primal trace

\[
\operatorname{Tr}^{\rm biv}_{\rm sh,\partial,Q}:
\mathcal S_{\rm sh}^{\rm norm,reg}\otimes^L
\mathcal E_{\partial,Q}^{\rm BM,\check C}
\longrightarrow\mathbf1_{\chi_N}.
\]

There is a smallest exact test of whether the known normalization
zero-sections can define this trace. It fails before any residue,
Alexander--Tate comparison, or reflection-parity computation.

## Maximal formal branch object

For \(I_+=\{1,3,5\}\), \(I_-=\{0,2,4\}\), and

\[
A_\sigma=B_\sigma[t_i,(1+t_ix_i)^{-1}:i\in I_\sigma],
\qquad u_i=t_ix_i,
\]

the established mixed block is

\[
M_{\sigma,2}=A_\sigma\langle m_i\rangle,
\quad M_{\sigma,1}=A_\sigma\langle\mathbf q_i,\xi_i\rangle,
\quad M_{\sigma,0}=A_\sigma\langle b_i\rangle
\]

with

\[
dm_i=\mathbf q_i-x_i\xi_i,
\qquad d\mathbf q_i=x_ib_i,
\qquad d\xi_i=b_i.
\]

Tensoring with the independent reciprocal-regular multi-Rees packets gives
a bounded square-zero branch totalization and retains both Tor grades on the
conductor. Transported labels also close a formal polarity action. This does
not construct the normalization-sheet source: only the coefficient row

\[
0\to B\to B_+\oplus B_-\to C\to0
\]

has canonical normalization provenance.

## Primitive trace equation

For each long target facet \(D\), the constructed endpoint/\(Q\) quotient
contains \(n_D,p_D\) with

\[
d_E n_D=\epsilon_Dp_D,
\qquad \epsilon_D\in\{+1,-1\}.
\]

If an ordinary zero-section trace \(T\) were a chain map, its value on
\(\mathbf q_i\otimes n_{D(i)}\) would obey

\[
\boxed{
x_iT(b_i\otimes n_{D(i)})
=\epsilon_{D(i)}T(\mathbf q_i\otimes p_{D(i)}).
}
\]

Primitive \(Q\)-framing makes the right side a signed unit. The left side
belongs to the proper ideal \((x_i)\), so the equation has no solution over
the unlocalized occurrence ring. On the conductor it becomes

\[
0=\pm1.
\]

The contradiction is sectorwise, hence neither the three-road sum nor
\(D_3\) covariance can cancel it. Globally inverting \(x_i\) would erase the
support being specialized and is inadmissible.

## Why the existing gallery quotients do not repair it

The absolute block remains valid:

\[
dH_\Sigma=q_\Sigma-
\sum_{i=1,3,5}x_i\widetilde\xi_i,
\qquad d^2=0.
\]

But each proved local Cartier gallery is already endpoint-and-generic
relative and has killed its \(q_i\). A homotopy colimit using only those
objects cannot reconstruct \(q_\Sigma\). The two natural alternatives also
fail:

- quotienting by the short boundary makes \(q_\Sigma\) bound only by
  deleting all three special galleries;
- adjoining \(dc=q_\Sigma\) fails absolutely because
  \(d^2c=x_1b_1+x_3b_3+x_5b_5\ne0\).

Thus the required source must be constructed before the endpoint and generic
relative quotients.

## Minimal admissible repair

The equation identifies the missing coefficient type. An extraordinary
correspondence may carry the principal dual line

\[
(x_i)^\vee\otimes(x_i)\longrightarrow\mathbb Z,
\qquad (x_i)^\vee(x_i)=1,
\]

without making \(x_i\) a unit. This is not ordinary restriction and must be
earned geometrically.

The minimal new object is one \(D_3\)-equivariant, two-sheet-compatible,
ringed normalization/nearby-cycle correspondence constructed before the
relative quotients. It must carry simultaneously:

1. the full \((m_i,\mathbf q_i,\xi_i,b_i)\) column;
2. the principal occurrence dual line;
3. independent multi-Rees lines and both Tor grades;
4. the nonzero generic \(q_\Sigma\) leg;
5. reciprocal-regular source and BM--Cech target variance;
6. both endpoint comparison cells and the polarity conjugate.

Only then is the endpoint-fixed mapping fibre defined. Consequently

\[
p_{\partial,Q}\in H^1(D_3;\mathbb Z_{\rm or})
\]

remains undefined. The even reflection of the formal coefficient cone is
inadmissible because that cone fails the primitive trace equation.

## Evidence

- entry 93: normalization--conductor coefficient row and first symbol;
- entry 113: absolute mixed block and subquotient/filler controls;
- entry 143: primal endpoint/\(Q\) BM--Cech target;
- entry 154: primal trace retyping and mandatory ablations;
- `research/voevodsky/check_primal_zero_section_trace_obstruction.rs`.

## Outcome contract

```json
{
  "claim": "Ordinary normalization zero-section gluing cannot support a primitive primal endpoint/Q trace: its chain equation requires x_i times a coefficient to equal a signed unit and becomes 0=+/-1 on the conductor. This falsifies only zero-section assembly, not an extraordinary principal-dual-line Gysin correspondence.",
  "status": "falsified",
  "assumptions": [
    "The occurrence ring remains unlocalized.",
    "The established mixed and endpoint/Q differentials are retained.",
    "Primitive Q framing has signed-unit normalization.",
    "No desired residue or principal-dual evaluation is inserted."
  ],
  "evidence_refs": [
    "research/voevodsky/check_primal_zero_section_trace_obstruction.rs",
    "src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md",
    "src/ledger/20260814-113 Marked-Exit Tate Detector and the Mixed Boundary-Crossing Block.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-154 Primal Bivariant Trace Retyping and the Double Object Gate.md"
  ],
  "factorization_test": {
    "branch_total_d_squared": "passed",
    "primitive_zero_section_trace": "falsified",
    "conductor_specialization": "0=+/-1",
    "three_road_cancellation": "impossible sectorwise",
    "generic_Q_leg": "retained in the mixed block",
    "extraordinary_principal_dual_repair": "unconstructed and not falsified",
    "endpoint_Q_parity": "undefined"
  },
  "counterevidence": [
    "Global occurrence localization would erase the tested support.",
    "Existing relative quotients lose the primitive Q leg or all special galleries.",
    "The formal polarity-even cone fails the primitive trace equation."
  ],
  "next_experiment": "Construct a marked ringed occurrence-Gysin/nearby-cycle correspondence carrying the principal dual occurrence line, both Tor grades, q_Sigma, and both endpoint cells; then form the endpoint-fixed mapping fibre and compute reflection parity."
}
```
