# Bilateral arithmetic attachment and the explicit conservative port residual

## Results

The reciprocal seam attachment can be constructed on the full line. Its energy balance follows by gluing the positive and negative half-lines. Applying that construction to the recorded Xi history exposes a forcing term that survives seam matching. The adjoint of this forcing gives a concrete candidate conservative return port and an explicit residual equation.

All Hilbert calculations below use Phi in L2(R), generator domain H1(R), and the declared positive inner product. The stable Xi histories must satisfy these membership conditions before the energy identities are applied. For source packets whose membership is only distributional, the translation identities remain distributional and the Hilbert norm arguments require separate justification.

## 1. Reciprocal attachment derived from translation

Set H=L2(R), (U_Lh)(u)=h(u+L), H_plus=L2(0,infinity), H_minus=L2(-infinity,0). Restriction and zero extension identify H with H_minus direct-sum H_plus. Translation is unitary and U_L*=U_-L.

For L>0, define the seam energy sesquilinearly by

Q_L(h,k)=integral_0^L conjugate(h(u)) k(u) du.

Writing G_plus,G_minus for the half-line pairings gives

G_plus(h,k)-G_plus(U_Lh,U_Lk)=Q_L(h,k),

G_minus(U_Lh,U_Lk)-G_minus(h,k)=Q_L(h,k).

Their sum is the full-line conservation law. The same seam form has opposite signs on the two pieces. These formulas supply the reciprocal polarized attachment using restriction and translation.

For j_n(u)=n^(-1/2)Phi(u+log n) on the full line, rational positive labels make A_p=sqrt(p)S_p invertible. The intertwining J A_p=U_(log p)J and full Gram identity G(A_pc,A_pd)=G(c,d) follow directly. The full-line norm exists for the recorded first atom; for any other forcing it follows under the stated L2 premise.

Thus the source has a conservative bilateral realization before spectral specialization. Its source columns are forcing translates, which need not be eigenvectors of translation.

## 2. Actual Xi-history attachment

The prior Rosenbrock packet defines

u_minus(q;z)=integral_(-infinity)^q exp(z(q-r)) Phi(r) dr,

u_plus(q;z)=-integral_q^infinity exp(z(q-r)) Phi(r) dr.

Both solve (partial_q-z)u=Phi. Their seam mismatch is

tau(z)=u_minus(0;z)-u_plus(0;z)=integral_R exp(-zr)Phi(r)dr.

For the completed source, tau is the centered Xi section under the recorded normalization. Glue u_minus on the negative half-line to u_plus on the positive half-line. Its distributional equation is

(partial_q-z)u_z=Phi-tau(z) delta_0.

At a Xi zero, the boundary jump vanishes and the same source forcing Phi remains. Where the glued history belongs to H1, this becomes an ordinary L2 differential equation.

## 3. The exact prime-translation defect

Variation of constants yields, at tau(z)=0,

U_L u_z-exp(zL)u_z
 = integral_0^L exp(z(L-t)) U_t Phi dt.

In general the right side also contains

-tau(z) exp(z(L+q)) 1_(-L,0)(q).

The latter formula holds in distributions and almost everywhere away from the endpoints. The missing homogeneous eigenstate law has an explicit source term. Using the opposite spectral sign replaces z by -z; it preserves this forcing issue.

If the homogeneous law held for every L, differentiation at L=0 would force Phi=0. The same conclusion follows for both L=log 2 and L=log 3 on a strongly continuous full-line representation: the subgroup they generate is dense, so the two laws extend to all L. Thus the nonzero forced Xi history cannot itself be the proposed common prime-translation eigenstate. Any eigenstate realization must include further state components and an operator acting on them.

## 4. Constructing the minimal adjoint return port

Let D=partial_q on H1(R), so D*=-D. Let B:C->H be Bc=c Phi, and B*u=<Phi,u>, with the inner product conjugate-linear in its first slot. The source top equation is

D u-Bc=z u.

Give H direct-sum C the norm ||u||^2+w|c|^2, with w>0. The skew-adjoint completion whose top row is this equation has the form

K_(w,alpha)(u,c)=(D u-Bc, w^(-1)B*u+i alpha c), alpha real.

The off-diagonal row is forced by adjunction once this metric is declared. B is bounded when Phi is in L2; consequently K is a bounded skew-adjoint perturbation of diag(D,i alpha), on H1 direct-sum C. For w=1, alpha=0 this gives a concrete minimal candidate.

The Xi history has c=1. Its remaining eigenstate equation is precisely

r_(w,alpha)(z)=<Phi,u_z>+i alpha w-z w=0.

This is the explicit conservative return-port residual. It is computed from the original forcing and glued history. The Xi seam equation supplies tau(z)=0; equality r(z)=0 is a further statement about this source pair.

The choice of w and alpha requires a derivation from the intended full closure structure. The formulas expose this small freedom instead of choosing it as a function of a desired zero. A source-independent w=1,alpha=0 is a well-defined candidate, with no asserted equality to the independent Green realization.

## 5. What its real part requires

At a matched H1 history, integration by parts gives

0=Re<u_z,D u_z>=Re z ||u_z||^2+Re<u_z,Phi>.

Hence

Re r_(w,alpha)(z)=-Re z (||u_z||^2+w).

For every w>0 the conservative second row can hold only on Re z=0. Its imaginary part is also an equation; confinement alone does not guarantee that a fixed alpha closes it at every Xi zero. The candidate may therefore impose a stronger condition than the desired confinement theorem.

This calculation localizes the metric problem to the mixed forcing/history pairing B*u_z. The positive and negative half-line seam energies have already been glued conservatively. The remaining mixed port is an actual scalar functional of the source, with its formula and domain specified.

## 6. Falsifier for closure-only cancellation

Choose u(q)=exp(-q^2), an off-axis parameter z, and Phi(q)=u'(q)-z u(q). Then both stable histories equal u, because the weighted forcing is the derivative of exp(-zq)u(q). Consequently tau(z)=0. Nevertheless Phi is nonzero and the translation defect in section 3 is nonzero.

This is a synthetic complex forcing, outside the completed-theta arithmetic specification. It shows exactly which argument requires arithmetic information: seam matching and bilateral gluing alone do not remove the forcing or close the adjoint return port.

## Verification

`uv run --with mpmath python research/grothendieck/checkers/check_bilateral_forcing_attachment.py`

Passed at 70 decimal digits: both seam-energy identities, forced translation at p=2,3, the zero-mismatch synthetic hostile, phase-space forcing persistence, and the real part of the conservative residual. These numerical tests supplement the displayed derivations.

Source: `research/voevodsky/the-two-stable-history-sections-form-a-source-derived-rosenbrock-pencil-whose-transmission-determinant-is-exactly-xi.v1.json`, which fixes the stable histories and the sign of the forcing equation. The preceding local attachment is in `arithmetic-theta-attachment-cocone-and-two-prime-polarized-gluing.md`.

## Current construction status

Constructed: reciprocal half-line attachment, complete seam polarization, actual forced Xi-history translation defect, and the minimal adjoint return-port family.

Unproved: a source-generated choice and realization of the conservative return port satisfying r_(w,alpha)(z)=0 on every Xi state. The independent Green target must be compared at this mixed forcing slot and its domain. This is the remaining explicit arithmetic calculation.
