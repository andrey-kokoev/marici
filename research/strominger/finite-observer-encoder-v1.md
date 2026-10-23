# An explicit finite observer-packet encoder

## Result

An actual **candidate encoder L** is now constructed on a five-dimensional family of compact physical observer packets. It is not an unspecified symbol or a set of arbitrary gate-test matrices.

Its two Mellin endpoint observations and three calibrated full-response flux samples determine every packet coefficient. The encoder maps those five observations into the actual native two-direction electron contrast and three-dimensional retained complement.

**17 checks pass**: exact reconstruction in all14 native presentations, transport through all18 interfaces, and endpoint matching at both E exits. This is a declared finite-packet choice, not a uniquely source-forced encoder, a physical preparation result, or an encoding of the entire observer space.

## Compact packet construction

Use the declared logarithmic Mellin convention

    m_h(t) = integral h(u) exp(-i t u) du.

In physical coordinates the half-density is `f(x)=x^(-1/2) h(log x)`. These functions are smooth and compactly supported away from zero; their Mellin transforms are entire. This gives legitimate endpoint evaluations on the compact physical analytic core, not evaluations on an arbitrary independently completed spectral bulk. Application of the source parent charts still requires their common-domain hypotheses.

Choose

    delta = 2 log2, epsilon = delta/4,
    phi(u) = exp(1-1/(1-(u/epsilon)^2)) for |u|<epsilon,
             0 otherwise,
    A = integral phi(u) exp(u/2) du,
    p_j(u) = phi(u-j delta)/A, j=0,...,4.

The bump is even, nonnegative and smooth, with phi(0)=1. Hence A is finite and positive and equals the corresponding integral with exp(-u/2). Translation gives the exact identities

    ell_plus(p_j)=m_pj(i/2)=2^j,
    ell_minus(p_j)=m_pj(-i/2)=2^(-j).

No fitted quadrature values are used. Disjoint supports give

    A p_j(k delta) = delta_kj.

The three regular observations use k=0,1,2. If the source full-response flux is expressed in physical coordinates as B_f(x)=f(x), these observations are `A 2^k B_f(4^k)`. This calibration is part of the candidate, not an unmentioned change of normalization.

## Exact reconstruction

For `h=sum_j a_j p_j`, the five observations are `o=T a`, where

    T = [1  2    4    8    16
         1  1/2  1/4  1/8  1/16
         1  0    0    0    0
         0  1    0    0    0
         0  0    1    0    0].

Its determinant is -3/2, so `a=T^-1 o`. This is an information-reconstruction certificate for the actual packet family.

The choices of five translates, spacing and flux sample sites are explicit design choices. The source supplies the observer class, endpoint functionals and complete-response flux—not a theorem that this packet is uniquely selected.

## Native embedding, not a new native transport law

At the first retained E exit, extract the actual two-row root-coefficient reader

    E = J* (B_exit P_exit)_electron.

Complete its rows to an orthonormal five-frame H by projecting the standard coefficient basis onto its orthogonal complement and applying exact Gram-Schmidt. This retains all three complementary directions; it does not invent new particle operations.

With native root embedding B_root, define

    L = B_root H* T.

For packet presentation a:

    L_a = B_a P_a H* T,
    D_a = T^-1 H P_a^-1 R_a.

Exact arithmetic verifies `D_a L_a = I5` at every packet and verifies all18 native interface transports. At both E exits, the existing contrast reader gives precisely the two endpoint rows of T. The other three coordinates give the declared calibrated flux observations.

The field norm equals `a* T* T a`. This is the chosen observation-pullback norm, **not** an assertion of isometry for the source's natural L2 norm or an ideal passive physical preparation.

## Controls and retained information

The nonzero packet with coefficients `(2,-5,2,0,0)` has both endpoints zero. Its encoded field is nonzero and the flux complement detects it. Thus two endpoints alone do not determine this packet.

Swapping endpoint assignments fails the declared native endpoint match. Dropping the three complementary coordinates destroys reconstruction. The existing order-five native coefficient comparison remains nontrivial even where encoded fields agree; execution histories and packet references are still separately retained.

Any specified linear residual on this fixed packet factors as `F(p_j) D_a`. A sesquilinear residual similarly factors through its packet matrix. This is a reconstruction implication, **not an evaluation of those residual samples or a proof of analytical face/tetrahedral coherence**. Regulator parameters and history-dependent witness data must still be supplied explicitly.

## Remaining gate

Use this declared packet to evaluate the actual intended regulator/face residuals and their witness comparisons, rather than relying only on abstract reconstructibility. Test the common-domain and direction conventions when applying the parent analytical charts. An incompatible residual or witness may reject this candidate.

Full-observer faithfulness, the full esd7 native transport, physical preparation, the114-record producer and evolution remain open.

```sh
python research/strominger/checkers/check_finite_observer_encoder.py
```

- [Frozen candidate profile](contracts/finite-observer-encoder.v1.json).
- [Encoder, decoder matrices and counterexample packet](results/finite-observer-encoder.json).
- [Verification receipt](results/finite-observer-encoder-verification.json).
