# Universal-R proof of target-state-independent D(S3) monodromy readout

Owner: marici.Kitaev

## Bounded question

Does the normalized-monodromy classifier require maximally mixing the unknown
target sector, or is mixing only the prepared reference sufficient?

Mixing only the reference is sufficient for every ordered pair of simple
D(S3) sectors.

## Exact construction

The checker constructs all eight induced irreducible representations from a
conjugacy class, a frozen transporter from its representative to every flux
label, and an irreducible centralizer representation. Their dimensions are

    (1,1,2,3,3,2,2,2).

For representations a and b, it evaluates the universal quantum-double
operator

    R = sum_g (P_g tensor 1) tensor (1 tensor g)

and full monodromy M_ab = R_21 R on V_a tensor V_b. All 64 ordered
monodromy matrices are exactly unitary.

## Partial-trace theorem

For every simple pair,

    Tr_b(M_ab)/d_b = mu_ab I_a,
    mu_ab = 6 S_ab/(d_a d_b).

Therefore, for every target density matrix rho_a, not merely the maximally
mixed one,

    Tr[(rho_a tensor I_b/d_b) M_ab] = mu_ab.

Target internal-state preparation is not a hidden classifier input. The
scalarity is the microscopic induced-representation realization of a closed
reference loop acting centrally on a simple target sector.

For references D and F, the normalized signatures are:

| target | mu_D | mu_F |
|---|---:|---:|
| A | 1 | 1 |
| B | -1 | 1 |
| C | 0 | -1/2 |
| D | 1/3 | 0 |
| E | -1/3 | 0 |
| F | 0 | 1 |
| G | 0 | -1/2 |
| H | 0 | -1/2 |

The imaginary twist quadrature supplies the remaining C/G/H separation, as
in the three-setting packet.

## Apparatus consequence

The abstract controlled-trace instrument needs a maximally mixed prepared
reference, not a maximally mixed unknown target. For the selected
trivial-centralizer-charge references D and F, uniform random group
conjugation uniformizes the flux basis. A full lattice preparation/fusion
audit and local fault-tolerant controlled-R synthesis remain open.

Carrier geometry supplies the linked target/reference ribbons and ordering.
The coefficient lens supplies induced representations, the universal R,
partial trace, reference mixture, and central scalar action.

## Verification

Command:

    uv run --with sympy python -u research/kitaev/checkers/check_s3_universal_R_partial_trace.py

Seven aggregate gates pass. The checker verifies the S3 group law in every
induced representation, constructs and tests all 64 monodromies, and compares
all 64 partial-trace scalars with the independently frozen modular matrix.
Fresh stdout matches the saved JSON.

## Boundary and falsifiers

The theorem assumes the target lies in one simple superselection sector. A
coherent direct sum of sectors, leakage, or unresolved multi-anyon fusion
space requires a larger instrument analysis. Reference maximization,
controlled monodromy, and ancilla readout remain capabilities.

Any failed group law, nonunitary monodromy, nonscalar reference partial trace,
or eigenvalue different from 6 S_ab/(d_a d_b) falsifies the packet.

Primary boundaries: Kitaev quant-ph/9707021 and Cowtan--Majid 2107.04411.
