# Third audit of the RH model against SCC and Interaction Nets

## Scope and evidence boundary

This audit compares Aspect's live SCC contract and generated Interaction Net
with Nima's source mathematics through events 10187--10190. It is a research
audit, not an SCC implementation change and not an RH claim.

Audited SCC artifacts:

- `research/aspect/contracts/theta-rh-interaction-net-state.v1.json`
- `research/aspect/scc/rh_net_state_compiler.py`
- `research/aspect/results/theta_rh_interaction_net_state.json`

The contract predates the operator-Schur, regularized-determinant, and
zero-mechanism results. Its outer dependency spine remains useful, but its
current cell vocabulary cannot express the live proof obligations.

## Overall verdict

The model is structurally conservative but mathematically under-resolved.
It correctly leaves RH open and correctly prevents formal slots from becoming
constructed inhabitants. It does not yet encode:

- the prime-diagonal Schur carrier;
- the Schatten-class split between primitive and higher prime powers;
- the regularized determinant comparison cell;
- legal passive-network wiring;
- the first constructor capable of carrying a zero divisor;
- separation relative to an allowed defect locus;
- the independent relationship between coercivity and spectral
  identification.

The generated Interaction Net therefore certifies the old dependency schema,
not the current mathematical architecture.

## Source-extracted operator packet

For

\[
z=i\left(s-\frac12\right),
\]

the prime-diagonal operator is

\[
S(z)e_p=p^{-1/2}e^{iz\log p}e_p.
\]

In the right open sector it satisfies

\[
\|S(z)\|<1,
\qquad
S(z)\in\mathfrak S_2.
\]

It is trace class only for $\operatorname{Re}s>1$. Hence the coefficient
lenses are realized by an operator-ideal filtration:

```text
ordered lens      prime-diagonal Schur operator S
determinant lens  det_2(I-S), carrying grades k >= 2
additive lens     tr S, the primitive grade k = 1 channel
```

At finite cutoff,

\[
\det(I-S_X)=\det_2(I-S_X)e^{-\operatorname{tr}S_X}.
\]

This comparison formula is a required coherence cell. The SCC contract has no
cells for any of these three typed objects or for their comparison.

## The zero mechanism has moved

Since $\|S(z)\|<1$, both $I-S(z)$ and $\det_2(I-S(z))$ are zero-free in the
right open sector. Multiplication by $e^{-\tau(z)}$ for finite holomorphic
$\tau$ remains zero-free. Therefore the diagonal Euler carrier and any scalar
primitive exponential cannot produce the nontrivial zero divisor.

The first zero-bearing cell must instead be one of:

- determinant-line sewing with noninvertible global section;
- endpoint, reciprocal, or archimedean modification of the operator;
- a boundary pencil $\Theta(z)-M(z)$ whose Lagrangian intersection loses
  transversality.

The current SCC node `relative_determinant_line_coherence` is too late and too
generic to identify this first zero-capable constructor. The contract also
lacks a boundary-pencil or transversality node.

## Corrected dependency topology

The current terminal chain is effectively

```text
relative determinant coherence
  -> five-margin coercivity
  -> spectral identification
  -> critical-line exclusion
  -> RH
```

The live logic is a diamond, not a chain:

```text
zero-free prime Schur carrier
  + primitive wall/history
  + reciprocal and archimedean ports
              |
              v
source-authorized sewing and boundary pencil Theta-M
              |
       +------+------+
       |             |
       v             v
relative off-seam   determinant/spectral
five-margin         identification with xi
coercivity          up to a nonzero factor
       |             |
       +------+------+
              v
off-seam kernel exclusion
              v
RH terminal
```

Coercivity does not construct spectral identification, and spectral
identification does not prove coercivity. They are independent witnesses about
the same completed pencil and must meet at the exclusion cell.

## Relative CCET typing

The SCC margin node presently has no parameter-locus semantics. A global
positive margin would exclude the intended critical-line zeros as well as the
forbidden off-line zeros.

The contract must declare an allowed defect locus $\Sigma$, with $\Sigma$ the
seam in the RH projection, and require

\[
\inf_{s\in K}\operatorname{sep}(\Theta(s)-M(s))>0
\]

for every compact $K$ in the complement of $\Sigma$. Loss of transversality is
permitted on $\Sigma$ and forbidden off it. This is the correct
Constructor-Coherence Exclusion typing.

## Interaction-Net wiring audit

### Legal local wiring

Each prime atom is a passive delay colligation. Prime assembly is legal as a
typed direct sum of channels. Other passive compositions such as cascade or
Redheffer product require their own source-authorized ports and feedback
well-posedness witnesses.

### Illegal scalar wiring

Ordinary scalar addition of local Schur transfers is not closed in the Schur
class. The current Interaction Net does not distinguish scalar sum, direct
sum, cascade, and feedback. Its generic arrows therefore cannot certify
passivity preservation.

### Determinant anomaly

Regularized determinants factorize over direct sums. Under operator products,
$\det_2$ generally carries a trace-class multiplicative anomaly. Any cascade
or feedback cell must expose that anomaly and identify it with an authorized
mixed arithmetic channel. Discarding it is an invalid lens crossing.

### Observer order

The scalar prime-power current must be obtained only after the ordered network
and determinant cells:

```text
passive network
  -> operator Schur transfer
  -> regularized determinant
  -> logarithmic derivative or trace expansion
```

The scalar Euler output is a shadow of the network, not a constructor from
which the passive realization can be reconstructed.

## Required SCC/IN cell refinement

The following cells should be explicit.

### Constructed algebraic cells

1. `prime_diagonal_schur_operator`
2. `hilbert_schmidt_ideal_membership`
3. `det2_higher_prime_power_packet`
4. `finite_det_det2_trace_comparison`
5. `zero_free_diagonal_carrier`

Their source-realization authority remains separately typed where appropriate;
an algebraic formula is not automatically a physical/source constructor.

### Open source cells

1. `valuation_fock_passive_dilation`
2. `primitive_wall_trace_completion`
3. `reciprocal_adjoint_port_orientation`
4. `archimedean_endpoint_operator_lift`
5. `passive_network_assembly`
6. `det2_anomaly_identification`
7. `source_cayley_boundary_relation`
8. `completed_boundary_pencil`

### Independent terminal witnesses

1. `relative_off_seam_five_margin_coercivity`
2. `xi_boundary_pencil_spectral_identification`
3. `off_seam_kernel_exclusion`, depending jointly on the previous two
4. `riemann_hypothesis_terminal`

## First-failure order

The current first unresolved source constructor remains the incidence from the
source-fixed bilateral trace bundle into the causal-history auxiliary block.
Events 10187--10190 add a parallel ordered-lens obligation: realize the
prime-diagonal Schur operator as a passive colligation and prove that the
primitive wall supplies the missing trace component.

These meet at the first zero-capable sewing/pencil cell. Neither branch may be
collapsed into scalar Euler agreement.

## Mandatory hostile fixtures

SCC and the Interaction Net should reject:

1. a scalar sum of individually Schur prime transfers whose norm exceeds one;
2. identification of $\det_2(I-S)$ with the full Euler determinant after
   dropping the primitive trace;
3. an arbitrary holomorphic continuation of the primitive trace chosen to
   import the zeta divisor;
4. a cascade that ignores the $\det_2$ multiplicative anomaly;
5. a reciprocal delay orientation selected for contractivity without a
   source adjoint-port map;
6. a global positive-margin demand that also excludes seam zeros;
7. coercivity promoted to spectral identification;
8. spectral identification promoted to coercivity;
9. a determinant-line cocycle treated as proof of the specific xi divisor;
10. a completed net retaining strict diagonal contraction while claiming that
    its zeros arise from the unchanged diagonal carrier.

## Status classification

- SCC generic coherence machinery: adequate for expressing the refined net.
- Live RH SCC contract: stale and under-typed.
- Generated Interaction Net: internally consistent with the stale contract,
  but not yet a faithful model of the current mathematics.
- Zero-free Euler carrier: established algebraically.
- Primitive trace completion: open.
- First zero-bearing sewing/pencil constructor: not yet identified from source.
- Relative off-seam exclusion theorem: open.
- Spectral identification with the xi divisor: open.
- RH: open.

