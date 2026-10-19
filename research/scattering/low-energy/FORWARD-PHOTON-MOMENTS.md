# Coherent forward photon cut moments and the IR subtraction boundary

[Contract](contracts/forward-photon-moments.v1.json) · [checker](check_forward_photon_moments.py) · [receipt](results/forward-photon-moments.v1.json)

## 1. The physical forward cut, not off-cut Taylor coefficients

Continue the [windowed representative](WINDOWED-PHOTON-DISPERSION.md), but take moments of the **physical forward photon cut** fixed by unitarity, not Taylor coefficients of that representative's prescribed flow. Work at fixed pure g2^4 order: T=(b/2)*A+b^2*B+..., F(s)=Im B(s,forward). The moment matrices below omit the overall b^2 of the physical absorptive amplitude. They are not physical rates or branching fractions.

Use the incoming two-beam helicity order (++ , -- , +- , -+). This is a polarization fiber in the imported photon framework, not a selected native preparation. Let R(x)=sum_(k>=2) r_k*x^k with real coefficients, either a finite polynomial or in the parent's locally convergent response class. For the conditional spectral comparison r2=c0, r3=c1, r_(n+4)=a_n/pi with a_n=n!*(n+1)!/(2n+3)!; c0,c1 remain free and the spectral extrapolation remains unlicensed.

The complete forward cut has the form

    F=[[D,O,0,0], [O,D,0,0], [0,0,M,0], [0,0,0,M]].

Its eigenvalues are f_minus=D-O, f_plus=D+O and f_mixed=M (twice). These are **forward entries**, not just J=0 partial-wave cuts.

## 2. Gram construction, azimuth averaging and closed bilinear coefficients

Put alpha=(1-cos(theta))/2, t=-s*alpha, u=-s*(1-alpha). In the canonical azimuth-zero frame the equal-helicity Born block is (1/2)*[[R(s),-R(s)-R(t)-R(u)],[-R(s)-R(t)-R(u),R(s)]], while the mixed block has diagonal R(u)/2 and off-diagonal R(t)/2. Set v=(R(t)+R(u))/2. The optical normalization gives

    f_minus=(1/8)*integral_0^1 [R(s)+v]^2 d alpha,
    f_plus =(1/8)*integral_0^1 v^2 d alpha,
    f_mixed=(1/32)*integral_0^1 [R(t)^2+R(u)^2] d alpha.

The full matrix is the normalized angular integral of A^dagger*A/8. One must include the azimuth twirl: incoming helicity differences are (0,0,2,-2), so azimuth averaging retains equal-helicity coherence but kills matrix entries between unequal helicity differences. Merely integrating the azimuth-zero mixed block square leaves a spurious nonzero mixed off-diagonal entry. Twirling is a positive unital average of unitary conjugations; Gram positivity is retained.

For each **ordered** pair k,l, q=k+l and beta_kl=k!*l!/(q+1)!, the forward eigenvalue coefficients are

    f_plus,kl =(-1)^q*[1/(q+1)+beta_kl]/16,
    f_minus,kl=f_plus,kl+[1+(-1)^k/(k+1)+(-1)^l/(l+1)]/8,
    f_mixed,kl=(-1)^q/[16*(q+1)].

Sum r_k*r_l*s^q over ordered pairs; mixed pairs need both orderings and no additional factor of two. These formulas follow by elementary beta integrals and reproduce the parent's full forward Legendre/Jacobi cut. Individual ordered-degree coefficients can be negative; the complete Gram is positive.

For any complex incoming polarization vector z, its unnormalized cut expectation is

    z^dagger*F*z=(f_minus/2)*|z_++-z_--|^2
                +(f_plus/2)*|z_+++z_--|^2
                +f_mixed*(|z_+-|^2+|z_-+|^2).

Dropping the cross term is not a harmless polarization average. For R=c0*s^2, the three eigenvalue coefficients of c0^2*s^4 are (107/480,7/480,1/80). The two coherent equal-helicity Bell combinations give the first two values, whereas their equal incoherent mixture gives D=19/160. A relative phase i also has expectation D, not either Bell eigenvalue.

## 3. Positive moments and their exact IR domain

Define, for nonnegative integer n and 0<tau<1,

    M_n(tau)=integral_0^tau F(s)*s^(-n-1) ds.

Where convergent this is a positive matrix on all coherent incoming polarization vectors. For a response whose first nonzero term is r_(k0)*s^k0, each of the three leading Gram eigenvalues is strictly positive: the nonzero monomial makes each square integral nonzero. Thus the entire matrix moment is finite **iff n<2*k0**. At equality it has a positive-definite logarithmic divergence; above it the divergence is a power. No nonzero fixed polarization vector evades that leading divergence.

For the declared spectral family:

- c0 nonzero: n=0,1,2,3 are finite; n=4 first diverges.
- c0=0,c1 nonzero: finite through n=5; n=6 first diverges.
- c0=c1=0: finite through n=7; n=8 first diverges.

The spectral r4 is nonzero, so the last case is not the zero response. These are IR convergence conditions, not UV subtraction counts for a full dispersion relation.

For a finite response polynomial, retain **all pairs** when squaring it. With its eigenvalue polynomial coefficients f_(i,q),

    eigenvalue_i(M_n)=sum_q f_(i,q)*tau^(q-n)/(q-n),  q>n.

Truncating R first and then forming the full square preserves positivity. Arbitrary homogeneous truncation of F, or subtraction of its leading density, need not do so.

## 4. Certified infinite-family comparison and operator error

For c0=c1=0 strip pi: R_tilde=pi*R has positive coefficients a_n starting at degree four. Truncate it at response degree K>=4 and square the full truncated amplitude. The bounds a_(n+1)<=a_n/4 and a0=1/6 give, uniformly for |x|<=s<=tau<1,

    |R_tilde(x)|<=V(s)=s^4/[6*(1-s/4)],
    |delta R_tilde(x)|<=d_K(s)=a_(K-3)*s^(K+1)/(1-s/4).

The canonical Born blocks have operator norm <=2*V; their truncations obey the same bound, and their difference has norm <=2*d_K. Unitary polarization phases do not alter these bounds. Applying the Gram identity, azimuth twirl and normalized angle integral gives the genuine four-polarization **operator-norm** estimate

    ||F_tilde-F_tilde,K||<=V(s)*d_K(s),  F_tilde=pi^2*F.

Therefore, if n<K+5,

    ||integral_0^tau (F_tilde-F_tilde,K)*s^(-n-1) ds||
       <= a_(K-3)*tau^(K+5-n)/[6*(1-tau/4)^2*(K+5-n)].

For n<8 this is the norm of the difference of the unsubtracted moment matrices. The same error bound applies when the same exactly retained leading density is subtracted from both cuts and the residual moments exist. It does not make the individually divergent unsubtracted n=8 moments finite.

At tau=1/2, K=16 this error is <3*10^(-18) for each of n=2,3. The receipt encloses all three eigenvalues of pi^2*M_2 and pi^2*M_3 in outward-rounded rational boxes with positive lower endpoints. This is a conditional comparison, not a selected window, normalization scale, source spectrum or preparation. General Gram and norm arguments are documented mathematics, not machine-formalized proofs; exact finite controls test their implementation.

## 5. IR subtraction can destroy positivity

To integrate at the first divergent index one can subtract the leading cut density throughout the chosen window. That is an explicit **signed density subtraction**, not another positive optical cut. Squaring the amplitude remainder instead would be positive but omits interference and is a different object.

An exact finite two-monomial control R=s^2+s^3 illustrates the distinction. At tau=1/2, after removing its degree-four density, the n=4 subtracted eigenvalues include

    plus: -79/7680,
    mixed: -25/2688,

while the minus eigenvalue is positive. The unsubtracted lower moments are positive. This polynomial control is labeled separately from the infinite spectral family.

The failure also occurs in that infinite family, with c0=c1=0: define

    N_8=integral_0^tau s^(-9)*[F(s)-r4^2*s^8*C4] ds,

where C4 is the full three-eigenvalue monomial-k=4 forward matrix. Its leading divergence cancels and the integral exists, but both the plus and mixed eigenvalues are **negative** at tau=1/2. The checker certifies this for pi^2*N_8 using K=16 and the operator error above; no floating-point sign test or UV tail estimate is used. This does not violate unitarity: the density difference is not required to be positive. No arbitrary IR finite-part prescription inherits positivity merely by being finite.

## 6. Matching boundary and successor

These moments are calculable positive **right-cut** quadratic forms when unsubtracted and IR finite. They are not the Taylor coefficients of the symmetric off-cut window flow, not complete crossed dispersion sums, and not bounds on finite Wilson coefficients. Such bounds additionally need the correct forward crossing map, treatment of both cuts and poles/IR pieces, and a stated global growth/subtraction law. None of those global physical assumptions is licensed merely by local right-cut positivity. In particular, positivity of this isolated subthreshold order does not imply positivity of each UV perturbative coefficient: interference with lower-order open-channel amplitudes can have either sign. Finite matching, independent dimensionful couplings and physical preparation remain free; C1-C12, exhausted C12 effort, historical owner/hash warnings and the high-energy pause are unchanged.

The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free.

The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected.

**Next:** construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom.

```sh
python -S research/scattering/low-energy/check_forward_photon_moments.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_forward_photon_moments.py
```
