# Iteration 5: specialize to Riemann zeta without pretending four ports survive

## Prior constructions reused

The source comparison now uses three existing Grothendieck packets:
`fourier-self-sewing-uniquely-selects-the-unit-unshifted-affine-lattice.md`,
`archimedean-theta-completion-gate.md`, and
`theta-endpoint-dilation-complex-derives-both-the-pole-packet-and-completion-polynomial.md`.
They provide affine-lattice self-sewing, the Gaussian theta/Mellin calculation,
and the boundary dilation operator. We do not reconstruct their result from
five desired scalar factors.

SCC obligation: specialization and readout descent, preserving the endpoint
terms and recording loss of rank. Exact checks cover finite maps and boundary
algebra; Poisson summation and Mellin continuation remain imported analysis.

## The unshifted orbit has only one independent distribution

For Delta=sum_(n in Z) delta_n in the self-dual Fourier convention,
F Delta=Delta. As a approaches zero, all four generic ports
P_a,C_-a,P_(1-a),C_a converge distributionally to Delta. On orbit coefficients
c=(c0,c1,c2,c3), the specialized map is

  c -> (c0+c1+c2+c3) Delta.

It has rank one and kernel dimension three. The twelve-coordinate map obtained
by composing with iteration 1's J P therefore has rank one and kernel dimension
eleven. The direct and six-step carrier descent still commute with Fourier,
but the specialized analytic image is not faithful on four visible coordinates.
Those lost distinctions remain in the labelled coefficient/history records;
they cannot be recovered from this single distribution.

The common character survives; the alternating and both odd characters vanish.
In particular, the active history rotor maps to zero in this specialization.
Its successful generic Hurwitz bridge is not a nontrivial Riemann-zeta rotor.
The full endpoint reader of iteration 4 does have a nonzero Riemann readout,
but that row is not invariant under its native incidence update. Native word
extension still does not become Fourier self-sewing.

## Removing zero does not commute with Fourier

The integer comb includes its zero atom. In the same normalization,

  F delta_0=1, F 1=delta_0,
  F(Delta-delta_0)=Delta-1.

Thus the zero-removed comb is NOT self-Fourier. A Fourier-stable distributional
boundary extension is span{Delta,delta_0,1}, of dimension three, with the last
two basis vectors exchanged. These are independent tempered distributions,
not three new native coefficient controls.

The singular Hurwitz term must also be removed explicitly. For Re(s)>1,

  zeta(s,a)=a^(-s)+zeta(s,1+a).

As a decreases to zero, the second term tends to zeta(s); the first is singular.
The opposite oriented component zeta(s,1-a) tends to zeta(s). Consequently the
nonzero unshifted oriented pair is (zeta(s),zeta(s)), not four independent
functions and not the naive value of zeta(s,a) at a=0. The character series
also tend to zeta(s) in this convergence region. Continuation follows through
the completed analytic formula, not by assuming uniform convergence at poles.

## The existing theta construction supplies the five factors

Choose the previously declared Gaussian and self-dual measure:

  theta(t)=<Delta,exp(-pi t x^2)>, t>0.

Fourier self-sewing gives theta(t)=t^(-1/2)theta(1/t). For Re(s)>1,

  Lambda(s)=1/2 integral_0^infinity (theta(t)-1)t^(s/2) dt/t
           =pi^(-s/2)Gamma(s/2)zeta(s).

The gamma and pi factors come from the Mellin integral of each Gaussian term,
with substitution u=pi n^2 t. The 1/2 removes the double counting of positive
and negative integers. These factors are derived from this analytic source;
the finite twelve-arrow carrier by itself does not specify that source or
its Gaussian/Haar normalization.

Splitting at t=1 and using reciprocity gives

  Lambda(s)=1/[s(s-1)]
     +1/2 integral_1^infinity (theta(t)-1)
                         [t^(s/2)+t^((1-s)/2)] dt/t.

The integral is entire in s, by Gaussian decay uniformly on compact s sets.
The source endpoint monomials 1 and t^(-1/2) carry the previously derived
operator D_s=2t d/dt+s with matrix diag(s,s-1). Its determinant is s(s-1),
and its oriented inverse trace is -1/s+1/(s-1)=1/[s(s-1)]. Hence

  xi(s)=s(s-1)Lambda(s)/2
       =1/2+s(s-1)/4 integral_1^infinity (theta(t)-1)
                              [t^(s/2)+t^((1-s)/2)] dt/t.

The boundary contributes the constant 1/2. Pole cancellation and reflection
xi(s)=xi(1-s) now have the existing source explanation. On endpoint coordinates,
reflection swaps the two modes and reverses both the dilation matrix and the
incidence grading; these two signs are checked rather than suppressed.

This supplies analytic provenance for the five multiplication arrows:
AB=Gamma(s/2), BC=pi^(-s/2), AC=their product, CD=s(s-1)/2, AD=the full product.
They are factorized descriptions of Gaussian Mellin completion and boundary
cancellation. They are not five independent native edge-local actuators.

## What is connected, and what is not

The chain is now explicit:

  twelve-arrow source -> four cyclic coefficients -> Fourier-comb orbit
  -> unshifted self-dual comb with retained boundary -> theta/Mellin completion
  -> Lambda and xi.

The first reduction can be direct or the parity-resolved six-step route.
The retained-history construction maps to the same generic analytic orbit
through iteration 4's full endpoint map; its continuous generator matches,
while its discrete incidence operation is different. The Riemann specialization
then collapses the analytic orbit to its common character.

We have connected the existing constructions under their declared choices;
we have not shown that the finite source forces the analytic choices, that
four distinct Riemann ports remain, or that xi has only critical-line zeros.
The analytic parameter, Gaussian family and all-test function space have not
been compressed into four numerical coefficients.

## Verification

`uv run research/voevodsky/checkers/check_riemann_comb_specialization.py`
checks the upstream source hashes, specialization ranks and kernels, native
readout noninvariance, the zero-atom Fourier exchange, endpoint determinant,
polar residues and reflected signs, and the half-theta s=2 normalization.
It does not numerically certify an infinite theta integral or prove RH.
Results: `results/riemann-comb-specialization-v1.json`.
