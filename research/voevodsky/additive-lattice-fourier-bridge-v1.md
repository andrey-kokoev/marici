# An additive atom lift connects lattice Fourier to physical Fourier

## Change from the failed comparison

The earlier Tate/radial comparison used delta_n -> delta_(exp(n)). That
embedding converts additive labels into multiplicative positions, so physical
Fourier yields an exponential-of-exponential phase. Its no-go remains valid.

Use instead the additive lift j_h delta_n=delta_(hn), h>0, into tempered
distributions on the real line. This is a different, explicitly declared
realization of the already constructed channel lattice. It preserves source
addition. The finite carrier does not thereby identify its logarithmic prime
grades with physical additive positions.

SCC obligation: source-operation transport and route compatibility. The tested
source is the canonical channel-lattice construction, not an asserted new
identification of that channel set with the twelve directed carrier arrows.

## Exact lattice/torus/real Fourier square

For a finite coefficient packet c, write

  j_h c=sum_n c_n delta_(hn),
  Fc(theta)=sum_n c_n exp(-2pi i n theta).

If L_h lifts a torus function periodically by (L_h f)(y)=f(hy), then

  F_R j_h c=L_h Fc.

Both sides are the same finite trigonometric sum. By the distributional
Fourier theorem, F_R L_h Fc=j_h(reflect c). Consequently all four charts of
the lattice Fourier orbit have a concrete realization in real tempered
distributions, with reflection on the second step. This is not an equality
between a lattice point mass and an L2 function on the real line.

For c in l2(Z), j_h c is tempered by Cauchy--Schwarz against Schwartz samples;
Fc lies in L2 of the normalized torus, and its periodic lift is a locally L2
tempered distribution. The square extends by continuity in these types. It
is not a unitary embedding from l2(Z) into L2(R); neither comb atoms nor
nonzero periodic lifts belong to that real-line Hilbert space.

The formulas extend coordinatewise to the canonical multichannel lattice
Z^D and real space R^D, preserving channel permutations. Reducing that
multichannel object to the one-dimensional zeta lattice is a separate map,
not silently accomplished by writing the one-coordinate formulas.

## Native lattice operations retain their meaning

Let T_b push atoms x to x+b, and let M_alpha multiply by exp(2pi i alpha x).
For b=hk, the source shift n->n+k becomes T_b, while its character multiplier
becomes M_alpha. Exactly,

  T_b M_alpha=exp(-2pi i alpha b) M_alpha T_b,
  F_R T_b=M_(-b) F_R,
  F_R M_alpha=T_alpha F_R.

Convolution of finite atom packets goes to multiplication of their Fourier
characters. The phase is determined by the lattice evaluation pairing, not
by assigning arbitrary eigenvalues to a four-cycle.

For nested meshes h_r=2^(-r), the bonding n->2n preserves atom positions:
j_(h/2)(i c)=j_h c. Their character sums also agree after periodic lifting.
Thus the square respects this explicitly chosen refinement. Other cofinal
rational meshes can be used; selecting dyadic meshes is a computational
choice, not a law inferred from the twelve-arrow source.

## Compose with the existing radial operator, not the failed exponential lift

Only AFTER forming the physical additive distribution do we apply the existing
oriented logarithmic half-density chart U. The operators then satisfy

  W_or U j_h=U F_R j_h=U L_h F,
  W_or=U F_R U^(-1).

This uses the actual oscillatory Hankel kernel already derived in the prior
packet, not a new abstract fourth root of reflection. For a nonzero atom
x0=hn, the half-density image is

  U delta_(x0)=|x0|^(-1/2) delta_(log|x0|)

in its signed channel. Applying the kernel cancels that factor and gives
exp(v/2)exp(-2pi i epsilon' x0 exp(v)), precisely U applied to the Fourier
character of delta_(x0). The atom at zero is kept in its separate endpoint
port; its Fourier image is the constant function, whose radial image is
exp(v/2) in both channels. This requires the induced test/dual domain, not
arbitrary distributions paired against arbitrary growing tests in log radius.

The crucial difference is log|hn|, not hn, in radial coordinates. We have not
made the old two kernels equal in the old chart. We have constructed different
embeddings on the lattice and torus sides for which the square commutes.

Composing next with the existing Mellin calculation yields its same gamma
matrix and spectral reflection. Gamma now follows the actual analytic
operation reached from the lattice pairing, rather than being installed as
an edge label.

## Quadratic source and Gaussian limit

The prior source-derivation packet characterizes the local reciprocal
quadratic regulator on the channel lattice up to heat-time scale. In one
coordinate, its heat coefficients are exp(-pi t h^2 n^2), after declaring the
physical mesh and time convention. Thus the sampled Gaussian measures

  mu_(h,t)=h sum_n exp(-pi t h^2 n^2) delta_(hn)

converge in tempered distributions, for fixed t>0, to exp(-pi t x^2)dx.
Indeed pairing with any Schwartz function is its ordinary convergent Riemann
sum; Schwartz decay controls the tails. Continuity of real Fourier gives
the corresponding Fourier limit. This is an analytic argument, not an
extrapolation from finite checks.

At h=1 the unweighted lattice comb paired with the same Gaussian is theta(t).
Poisson summation and the already constructed endpoint dilation complex then
supply the previous Lambda and xi completion. The new contribution is the
operation-preserving lattice-to-real Fourier interface; the Gaussian/theta
and boundary calculations are reused.

## What remains to identify

This constructs the missing comparison for the canonical channel-lattice
realization using additive positions. It does not preserve the earlier
log-prime/exponentiation assignment as the same physical coordinate. It also
does not establish that the channel-lattice source and the twelve-arrow
carrier share a particular constructor, or select a one-dimensional channel
without a source rule.

Those are now concrete source-map questions. Repeating the old phase mismatch
or constructing another four-cycle would not answer them. The positivity of
a channel coefficient norm is likewise not an identity with the signed Weil
form; that needs an explicit form pullback on the resulting test space.

## Verification

`python research/voevodsky/checkers/check_additive_lattice_fourier_bridge.py`
checks finite rational atom/character squares, four dyadic meshes, bonding,
convolution, shifts, modulations and the Weyl phase before evaluating the
formal rational phases as complex exponentials. It also retains the elementary
failure of exponential positions to preserve additive composition. The
infinite distributional and Gaussian-limit arguments are stated above.

Receipt: `results/additive-lattice-fourier-bridge-v1.json`.
