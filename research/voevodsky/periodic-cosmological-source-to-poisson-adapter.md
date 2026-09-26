# A periodic cosmological source-to-Poisson adapter

## Outcome

A concrete periodic source-to-field adapter now works exactly, but requires a
background split. Positive total mass cannot source a periodic Poisson potential
directly: the source must have zero mean. With the density contrast as source,
Fourier inversion determines the potential up to its constant mode. Fixing
that mode gives a unique finite-grid solution and its tidal readout.

This is a NEW declared Newtonian perturbation model, motivated by the recovered
FRW spatial metric. It is not claimed to have been present in the primary
cosmology source, to derive that model's scalar amplitudes into masses, or to
prove a general-relativistic Newtonian limit. Its periodic boundaries differ
from Nima's original isolated-space two-source fixture.

## Inputs and source relation

The preceding audit recovered the primary source's supplied spatially flat
FRW metric a(eta)^2 delta_ij. At one chosen epoch take a>0 as fixed and supply

    Delta_com Phi = 4*pi*G*a^2 (rho_phys-rho_background).

This is the usual form of a peculiar-potential Poisson model, admitted HERE
as physics. It has not been derived from the source's scalar action. A
cosmological perturbation derivation would additionally specify stress-energy,
gauge, background Einstein equations and approximation regime.

For an explicit finite test use a periodic 4 by 4 by 4 cubic grid, comoving
spacing 1, masses 2 at (1,0,0) and 1 at (0,1,0), and 4*pi*G=1. These are cell
mass weights. They are NOT the point-source radii 3 and 4 of the isolated-space
fixture, nor does this coupling convention equal that fixture's G=1.
No original source file or convention was silently changed.

At a=1, total mass is 3 and mean density is 3/64. The contrast at each cell is
its mass minus 3/64. At a general fixed epoch, physical cell volume is a^3,
so rho_phys=m_cell/a^3 and the mean background is 3/(64 a^3).

## Why the background is required

Define the discrete Laplacian by

    (Delta f)(x)=sum_j [f(x+e_j)+f(x-e_j)-2 f(x)],

with periodic indices. Summing over all cells cancels every term, so

    sum_x Delta f(x)=0.

Thus Delta Phi=rho has no solution for the positive mass source of total 3.
Subtracting the mean makes the compatibility condition hold. This subtraction
is a physical background/perturbation split, not a gauge transformation that
leaves the source unchanged. Total physical mass remains in the retained
background plus contrast package. Contrast values may be negative without
negative underlying particle masses.

The nonzero Fourier modes have positive -Delta eigenvalues

    lambda(k)=sum_j [2-2 cos(2*pi*k_j/4)].

Each summand is 0,2,4,2. Only k=0 has lambda=0. Hence

    Phi_hat(k)=-contrast_hat(k)/lambda(k),  k!=0,
    Phi_hat(0)=0

is the unique zero-mean solution. The zero-source homogeneous kernel consists
only of constants on this connected periodic grid. The inverse is a section
after the zero-mean convention is specified; it does not derive the source.

## Fibration interpretation

The finite linear map Delta:potential fields -> source fields has

- empty fibers over nonzero-mean sources;
- affine constant-mode fibers over zero-mean sources;
- a unique representative in each nonempty fiber after imposing mean Phi=0.

This concretely separates admission (solvability), residual presentation
freedom (constants), and selection of a representative (zero-mean section).
A table-fibration recovery theorem does not make an empty solution fiber
inhabited. Retaining the background resolves the obstruction by changing the
source problem explicitly, rather than pretending that invertibility alone
generated a solution.

On a torus, nonconstant affine functions are not globally periodic. Thus the
original local affine-jet quotient must not be mistaken for a global periodic
gauge freedom: only constants lie in this periodic Laplacian kernel.

## Exact results

The Fourier calculation uses integer fourth roots of unity and rational real
and imaginary parts, with no floating-point FFT. All 64 Poisson equations and
the Fourier roundtrip are checked exactly. At the origin,

    Phi(0)=-257/2560,
    E_xx(0)=Phi(-e_x)-2 Phi(0)+Phi(e_x)=-67/320.

Moving the same two mass weights to the y and z axes preserves mean density
but changes this readout to 57/320. Background data do not determine the local
source perturbation or its tides.

At fixed comoving mass weights, physical dilation by a gives

    Phi_a=Phi_1/a,
    E_proper,a=E_com,1/a^3.

The checker verifies this at a=2, including physical mass conservation and
Delta_com Phi_a/a^2=rho_phys-rho_background. These compare differently scaled
physical configurations at frozen epochs; they do not evolve particles or
solve for the scale factor.

A cell with no positive mass still has negative density CONTRAST. Consequently
the trace of the peculiar tidal second-difference tensor there need not vanish.
That differs from the original isolated vacuum fixture. The homogeneous
background contribution to full cosmological relative acceleration is not
computed here, so this is only the peculiar-field readout.

## Verification and scope

Run:

    python research/voevodsky/check_periodic_cosmological_poisson_adapter.py

All 15 exact tests passed. They include wrong-sign rejection, refusal of an
unsubtracted positive-total source, constant-shift invariance, exact residuals,
scale laws and distinct tides with identical mean background.
Receipt: `research/voevodsky/periodic-cosmological-poisson-adapter.json`.

The universal discrete solvability argument is written linear algebra. The
checker covers the stated finite fixtures; it is not a continuum limit, a
proof-assistant formalization, an independent derivation of gravity or a test
against observational cosmology.

## What this settles and what remains

We now have an executable candidate map from a DECLARED cosmological-style
mass/background packet to a local peculiar tidal readout. The minimum packet
includes source distribution, spatial scale, boundary conditions and the
physical Poisson law. Source distribution is not recoverable from a total
momentum defect alone.

A genuine connection to the primary scalar cosmology requires its actual
state-to-stress-energy map and a controlled perturbative Einstein/Poisson
reduction. The earlier research already warns that matter alone is insufficient
for general relativistic curvature: homogeneous gravitational boundary data
must also be retained. The periodic elliptic toy removes most of that freedom
by explicit modeling choices; it does not solve the general source-state gate.

References:
- `research/voevodsky/spatial-momentum-to-position-source-audit.md`
- `research/voevodsky/particle-source-to-newtonian-spatial-adapter.md`
- `research/nima/marici-machian-gravity-direction.md`, especially 'Linearized
  source--boundary decomposition'
- `research/nima/graph-action-selection-audit.md`, which already detects the
  analogous nonzero-total-load obstruction on an unpinned closed graph.
