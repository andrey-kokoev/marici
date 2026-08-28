# Two-response closure of the mediator physical quotient

Work package: WP990  
Owner: marici.Figueiredo

## Question

Does the WP977 source already generate the one complementary invariant required
by WP989?

## Source-derived response pair

Leading elimination gives

\[
q=\frac{\mu^2}{2m_A^2},\qquad
\frac{k}{q}=\frac{\gamma^2\mu^4}{m_s^2(m_A^2)^5}.
\]

In WP989's logarithmic coordinates, the corresponding response rows are

\[
r_q=(0,2,0,-1),\qquad
r_\rho=(2,4,-1,-5).
\]

Both arise from the same declared source elimination. Neither is imported from
a texture chart, fitted scalar coincidence, or reference port.

## Exact contextual partition

The two rows annihilate the scalar and adjoint kinetic-normalization
generators

\[
n_s=(-1/2,0,-1,0),\qquad
n_A=(-3/2,-1/2,0,-1).
\]

Their joint rank is two. Their kernel also has dimension two and contains the
two independent normalization generators, so it equals the normalization
orbit exactly.

Therefore two labelled source packets have equal \((q,k/q)\) responses if
and only if they represent the same point of the local faithful quotient.
The pair is jointly faithful on that quotient. This is the corrected
contextual equivalence partition.

## Separation versus selection

The response pair separates physical quotient points but does not select any.
Positive source coefficients allow \(q\) and \(k/q\) to vary. For any
positive target pair \((q_*,\rho_*)\), choose
\(m_A^2=m_s^2=1\),
\(\mu=\sqrt{2q_*}\), and
\(\gamma=\sqrt{\rho_*}/(2q_*)\). The auxiliary quartic coefficient can
then be chosen above \(|\gamma|/16\) to retain coercivity.

Hence the response image is the full positive quadrant on the declared local
grammar. No proper admissible subfamily or distinguished point is selected.
The operation is a separator only.

## Descent and instrument

Both coefficients multiply full weak-basis invariants, so the response pair
descends under the full weak-basis groupoid and under kinetic field
normalization. It requires no reference port.

No calibrated physical instrument is admitted for either coefficient. The
pair is a source-derived theoretical response family, not an experimentally
typed probe family. The first nonfaithful arrow in an attempted experiment is
the absent source-to-record interface, not the quotient response algebra.

## Smallest falsifier

The smallest algebraic falsifier is a non-normalization tangent vector
annihilated by both rows. The exact checker proves none exists. The smallest
physical falsifier is a completed source-to-detector map whose response to the
two quotient directions has rank below two.

## Reproduction

Run:

    python research/flavor/checkers/wp990_two_response_physical_quotient_closure.py

The generated result is
research/flavor/results/wp990_two_response_physical_quotient_closure.json.
