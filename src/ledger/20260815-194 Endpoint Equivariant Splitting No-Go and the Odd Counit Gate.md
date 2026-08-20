# Endpoint Equivariant Splitting No-Go and the Odd Counit Gate

Date: 2026-08-15  
Status: scoped integral endpoint-splitting obstruction proved. The minimal
endpoint-supported odd-counit enlargement is characterized algebraically but
not geometrically constructed. No global extraordinary-kernel no-go and no
graph admission are claimed.

## Finite endpoint complex

Work only in the explicitly labelled integral endpoint coefficient model.
The homogeneous polarity-equivariance differential on the defect line is

\[
d_{\mathrm{eq}}=[2]:\mathbb Z\longrightarrow\mathbb Z.
\]

Its Smith normal form is \([2]\). Consequently

\[
H^0=0,
\qquad
H^1\cong\mathbb Z/2.
\]

A normalized endpoint splitting has the form

\[
s_n(1)=(n+1,n).
\]

Polarity exchanges the two endpoint entries, so equivariance would require

\[
n=-n-1,
\qquad\text{equivalently}\qquad
2n+1=0.
\]

This equation has no integral solution. Its obstruction is the nonzero class

\[
[1]\in\operatorname{coker}[2]\cong\mathbb Z/2.
\]

This is an intrinsic no-go for an integral polarity-equivariant normalized
splitting inside the stated finite endpoint complex.

## Why the existing special Tor class does not repair it

Adjoin a special \(\operatorname{Tor}_1\) variable in degree \(-1\) with
zero differential. The resulting local complex has the form

\[
\mathbb Z[-1]\xrightarrow{0}\mathbb Z\xrightarrow{2}\mathbb Z.
\]

It adds

\[
H^{-1}\cong\mathbb Z
\]

but leaves

\[
H^1\cong\mathbb Z/2.
\]

Thus a closed odd class whose endpoint boundary is zero cannot absorb the
splitting obstruction. In particular, this finite calculation does not turn
the entry-176 central exceptional Tor class or the entry-192 DNC
\(\operatorname{Tor}_1\) symbol into an endpoint correction. Their required
support comparisons are absent, and a zero endpoint restriction would leave
the same cokernel.

The checker takes the literal central-support restriction in this finite
packet to be zero as a declared scoped input. It does not derive that
restriction from a six-functor, purity, deformation-to-the-normal-cone, or
ringed-support theorem.

## Minimal endpoint-supported odd counit

Let a new framed variable \(\epsilon_{v_+}\) have boundary

\[
d\epsilon_{v_+}=m\,e_{\mathrm{def}},
\]

where \(e_{\mathrm{def}}\) generates the endpoint equivariance defect line.
The presentation becomes

\[
\left[2\;m\right]:\mathbb Z^2\longrightarrow\mathbb Z,
\]

with

\[
\operatorname{coker}\left[2\;m\right]
\cong
\mathbb Z/\gcd(2,m).
\]

Therefore the obstruction dies exactly when \(m\) is odd. The smallest
normalized choice is

\[
m=\pm1.
\]

Accordingly the minimal algebraic repair is one odd, endpoint-supported
counit whose boundary evaluates primitively on the defect line. Merely adding
a closed odd generator, a degree-zero polarity line, or an even endpoint
evaluation does not suffice.

This statement characterizes the required enlargement; it does not construct
\(\epsilon_{v_+}\) as a geometric class. A geometric realization must type it
on the selected endpoint support and prove that its boundary is odd after
the literal endpoint restriction.

## Scope boundary and dependencies

The theorem depends only on the finite integral endpoint matrix, normalized
splittings, polarity exchange, and the declared zero central-support
restriction. It is compatible with, but does not instantiate, the following
repository data:

- entry 138 supplies the loaded polarity character, not an endpoint-supported
  odd boundary;
- entry 158 fixes the local Cartier/coorientation degree budget and leaves the
  global primal trace and endpoint comparison unconstructed;
- entry 176 constructs a degree-zero relative cap after cancellation of its
  exceptional \([1]\) and extraordinary \([-1]\) shifts;
- entry 190 isolates the missing branch-selected logarithmic
  Beck--Chevalley comparison;
- entry 192 constructs a line-valued DNC Bockstein but not its restriction to
  the literal endpoint packet.

The minimal missing geometric arrow is consequently an endpoint-supported
extraordinary or logarithmic counit

\[
\gamma_{v_+}^{\mathrm{odd}}:
\mathcal W_{v_+}
\longrightarrow
E_{v_+}^{\mathrm{BM},\check C}
\]

together with a proved boundary equation

\[
d\gamma_{v_+}^{\mathrm{odd}}
=\pm e_{\mathrm{def}}
\pmod{2}.
\]

Its source support \(\mathcal W_{v_+}\), branch/conormal framing, literal
entry-131 purity comparison, and entry-143 Boolean/costalk realization remain
unconstructed. No assertion here rules out an extraordinary, proper,
DNC, nearby-cycle, or logarithmic Gysin kernel that supplies such a map.

Until that map, its reflected endpoint mate, the generic \(Q\) leg, and the
global endpoint connector coherences are constructed, the physical
endpoint/\(Q\) mapping fiber is uninstantiated. Hence
\(p_{\partial,Q}\), its parity, and its Bockstein remain undefined.

## Falsifiers

The scoped no-go is falsified if the endpoint equivariance matrix is not
\([2]\), if its Smith diagonal is not \([2]\), if an integer solves
\(2n+1=0\), or if adjoining a zero-boundary degree-\(-1\) generator changes
the cokernel of \([2]\).

The minimal-repair criterion is falsified if
\(\operatorname{coker}\left[2\;m\right]\) is not
\(\mathbb Z/\gcd(2,m)\), or if the obstruction vanishes for even \(m\) or
survives for odd \(m\).

A future geometrically typed odd counit does not falsify the theorem: it
realizes precisely the enlargement absent from the scoped endpoint complex.

## Provenance and validation

Exact certificate:

- `research/voevodsky/check_d03_endpoint_equivariant_splitting_obstruction.rs`,
  SHA-256
  `cc84e4baa08e47e69d559d8dbdbeb18d4d426c0b81b2fba759e0d3f7ac4b99f5`.

The checker certifies the matrix, Smith form, affine parity obstruction,
zero-boundary Tor negative control, and odd-boundary repair criterion. Its
central-support vanishing is explicitly a declared input. It does not certify
a spatial comparison or a global nonexistence theorem.

Relevant ledger inputs are entries 131, 138, 143, 158, 176, 190, and 192.

## Next experiment

Construct a branch-selected endpoint support object \(\mathcal W_{v_+}\)
from the logarithmic DNC/conductor geometry and a support-typed counit
\(\gamma_{v_+}^{\mathrm{odd}}\). Verify, without inverting a branch or normal
parameter, that its literal entry-143 endpoint boundary is primitive and odd.
Then construct the reflected endpoint counit and connector square before
attaching the generic \(Q\) leg or evaluating any physical parity.

## Outcome contract

~~~json
{
  "claim": "In the finite integral endpoint equivariant splitting complex the homogeneous differential is [2], so H0=0, H1=Z/2 and the normalized affine equation 2n+1=0 has no integral solution. A zero-boundary Tor1 variable adds Hminus1=Z but leaves the obstruction. Enlarging the presentation to [2 m] kills the obstruction exactly when m is odd.",
  "status": "proved_scoped_integral_obstruction",
  "scope": "finite integral endpoint equivariant splitting complex and algebraic odd-boundary repair criterion only; central-support restriction is a declared input; no global extraordinary-kernel no-go, spatial comparison, physical mapping fiber, or graph admission",
  "factorization": {
    "equivariance_matrix": [[2]],
    "smith_diagonal": [2],
    "H0": "0",
    "H1": "Z/2",
    "normalized_splitting": "s_n(1)=(n+1,n)",
    "affine_obstruction": "2n+1=0 has no integral solution",
    "zero_boundary_Tor": "adds Hminus1=Z and leaves H1=Z/2",
    "enlarged_presentation": "[2 m]",
    "enlarged_cokernel": "Z/gcd(2,m)",
    "repair_condition": "m odd",
    "minimal_normalized_evaluation": "m=+/-1",
    "central_support_restriction": "zero is a scoped declared input",
    "endpoint_supported_odd_counit": "algebraically characterized, geometrically unconstructed",
    "physical_mapping_fiber": "unconstructed",
    "physical_p_partial_Q": "undefined"
  },
  "checker_sha256": "cc84e4baa08e47e69d559d8dbdbeb18d4d426c0b81b2fba759e0d3f7ac4b99f5",
  "evidence_refs": [
    "research/voevodsky/check_d03_endpoint_equivariant_splitting_obstruction.rs",
    "src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md",
    "src/ledger/20260815-138 Physical Polarity Loading and the Shifted Butterfly Obstruction.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-158 Local Gysin Sufficiency No-Go and the Global Mapping-Fiber Definition Gate.md",
    "src/ledger/20260815-176 Central Exceptional Relative Cap and the Conditional Parity Test.md",
    "src/ledger/20260815-190 Rees-Line Cancellation and the Log Branch-Selected Beck-Chevalley Gate.md",
    "src/ledger/20260815-192 Flat DNC Log-Node Bockstein and the Toric Framing Gate.md"
  ],
  "unconstructed": [
    "geometric endpoint-supported odd counit with primitive odd boundary",
    "branch/conormal support and logarithmic or extraordinary comparison",
    "literal entry131 purity and entry143 endpoint realization",
    "reflected endpoint mate and endpoint connector coherences",
    "generic Q leg and physical endpoint mapping fiber",
    "physical p, parity, and Bockstein"
  ],
  "counterevidence": [
    "A closed Tor1 variable has zero boundary and leaves the Z/2 obstruction.",
    "The entry176 exceptional shift is canceled by its extraordinary Cartier shift and is not a spare odd endpoint class.",
    "The declared central-support restriction is not derived from spatial geometry.",
    "No present arrow identifies the DNC or exceptional support with the literal endpoint defect line."
  ],
  "minimal_repair": "Construct one endpoint-supported odd counit whose boundary evaluates by an odd integer, minimally +/-1, on the endpoint equivariance defect line.",
  "next_experiment": "Build the branch-selected endpoint support object and odd counit, prove its literal endpoint boundary is primitive without inversion, and attach its reflected mate and connector square before the generic Q leg."
}
~~~
