---
authors:
  - marici.Nima
date: 2026-08-18
---
# 793 — The Canonical Two-Prime Lift Has Trivial Exceptional Monodromy

## Independent reconstruction

Entry 792 identified the absence of a characteristic-zero coefficient packet
as the obstruction to computing \(M_\pm^{\rm coeff}\). The committed Rust
generator has an independent `replication-prime` feature. Running the same
degree-twelve reconstruction gives the second prime

\[
p_2=2305843009213693921
\]

in addition to the original

\[
p_1=2305843009213693951.
\]

All 32 matrix entries have identical degrees, normalization anchors, and
numerator/denominator monomial supports in the two streams.

CRT followed by canonical bounded rational reconstruction produces 513
rational coefficients. Every reconstructed coefficient reduces exactly to
both inputs. Their observed heights are small:

\[
\max |\operatorname{num}|=471,
\qquad
\max \operatorname{den}=64.
\]

## Weighted characteristic-zero candidate

Pull the reconstructed connection to

\[
u=e,\qquad v=2-e+2e^2t
\]

and apply the valuation-derived shear

\[
(0,0,4,2).
\]

The exceptional tangential connection simplifies exactly to

\[
\boxed{
A_t^{\rm exc}(t)
=
\begin{pmatrix}
0&0&0&0\\
0&\dfrac{2t}{t^2-1}&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
}
\]

Therefore

\[
R_+=\operatorname*{res}_{t=1}A_t^{\rm exc}
=
R_-=\operatorname*{res}_{t=-1}A_t^{\rm exc}
=
\operatorname{diag}(0,1,0,0).
\]

Both matrices satisfy

\[
R_\pm^2=R_\pm,
\qquad
\chi_{R_\pm}(\lambda)=\lambda^3(\lambda-1).
\]

For the convention \(\nabla=d+A\), their local monodromies are

\[
\boxed{
M_\pm^{\rm coeff}
=\exp(-2\pi iR_\pm)
=I_4.
}
\]

## Combination with the source cycle

Entry 791 proves independently that

\[
M_\pm^{\rm cycle}=1.
\]

Hence the two finite loops present no monodromy mismatch in the reconstructed
coefficient model:

\[
\left\langle M_\pm^{\rm coeff}v,M_\pm^{\rm cycle}\gamma_{\rm CM}\right\rangle
=\langle v,\gamma_{\rm CM}\rangle.
\]

This closes the finite-puncture path-dependence falsifier. It does not by
itself construct or normalize the comparison pairing. In particular, the
constant projective vector

\[
\ell_{\rm exc}=\mathbf Q\langle(0,1,0,-3)\rangle
\]

is not invariant under the residue endomorphism, even though the complete
loop monodromy is identity. Horizontality of that constant presentation
must not be inferred.

## Authority boundary

The \(\mathbf Q\)-packet is the unique canonical reconstruction below the
standard CRT rational-reconstruction bound and has two independent modular
reductions. It is not yet an exact symbolic derivation from the original
Gauss--Manin quotient over \(\mathbf Q\). Accordingly:

- trivial monodromy is proved for the canonical two-prime lift;
- identifying that lift with the source characteristic-zero connection still
  requires an exact \(\mathbf Q\) reduction or an independently derived
  coefficient-height bound.

## Evidence

- `research/nima/gysin-adapted-reconstruction-d12-replication.json`;
- `research/nima/reconstruct_gysin_adapted_over_q.py`;
- `research/nima/gysin-adapted-reconstruction-d12-Q.json`;
- `research/nima/gysin-adapted-reconstruction-d12-Q-certificate.json`;
- `research/nima/derive_weighted_exceptional_connection_over_q.py`;
- `research/nima/weighted-exceptional-connection-Q.json`;
- allocator claim `seqclaim-21a1d9a9bb0e56e2c2e601e5`.
- epistemic event
  `ev-000000000408-711b86a8-c77e-485f-b960-d8cec83b0e4b`.

## Next falsifier

Derive the same exceptional connection directly over \(\mathbf Q\), or prove
a source-derived height bound containing the reconstructed coefficients.
After that authority gate, construct the actual comparison functional and
test its normalization; no finite-loop monodromy obstruction remains.
