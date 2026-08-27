# The alternating Green polarization is relational before source correlation

## Question

Does antisymmetrizing the four mixed Green products make the physical
cross-sheet polarization descend through four scalar endpoint traces?

## Four-port carrier

Let each port carry the half-line graph domain

\[
\mathcal D=H^1(\mathbb R_+)
\]

with endpoint trace

\[
\tau(G)=G(0).
\]

Before imposing a common theta-source incidence, write a plus-side state as

\[
x=(P_z,Q_{-z},Q_z,P_{-z})
\]

and the reciprocal state as

\[
y=(Q_{-w},P_w,P_{-w},Q_w).
\]

The carrier-level alternating Green form corresponding to the four terms of
the physical polarization is

\[
\Omega(x,y)=
\langle P_z,Q_{-w}\rangle
+\langle Q_{-z},P_w\rangle
-\langle Q_z,P_{-w}\rangle
-\langle P_{-z},Q_w\rangle,
\]

where every bracket is the half-line mixed Green pairing.

## Exact kernel contraction

Choose nonzero

\[
h\in C_c^\infty(0,\infty).
\]

Activate only

\[
P_z=h,
\qquad
Q_{-w}=h,
\]

and set the other six ports to zero. Every endpoint trace vanishes, while

\[
\Omega(x,y)=\lVert h\rVert_2^2>0.
\]

Each active tail is source-admissible for its local first-order flow by
choosing its forcing to be the negative graph differential of (h).

Therefore the full alternating form fails the slotwise kernel-annihilation
criterion on the independent four-port graph carrier. Antisymmetrization
does not make it a function of endpoint scalars.

## What reflection cancellation proves

The scalar theta polarization satisfies

\[
\mathcal X_a(z,-\overline z)=0.
\]

This is cancellation after two further restrictions:

1. all four ports are placed in the correlated image of one theta source;
2. the spectral parameters are placed on the reflection-fixed relation.

It does not imply that the carrier form descends through independent endpoint
quotients. Vanishing on a distinguished subspace is weaker than annihilating
every local quotient kernel in every slot.

## Exact remaining theorem

Let

\[
J_{z,w}:\mathcal S_{z,w}\longrightarrow\mathcal D^8
\]

be the actual common-source incidence producing all four plus ports and all
four reciprocal ports. The physical question is now the pullback test

\[
J_{z,w}^*\Omega.
\]

There are two possible outcomes.

- If the pullback still contracts nontrivially with the kernel of the
  source-derived endpoint observation, relational-first sewing remains
  mandatory even on physical states.
- If the pullback annihilates that kernel identically, the cancellation is a
  theorem of common-source incidence, not a consequence of
  antisymmetrization alone.

Thus the missing constructor is precisely the correlated incidence map
(J_{z,w}). No endpoint-only argument can replace it.

## Architectural consequence

The order of operations is now separated cleanly:

1. local graph carriers authorize the four Green pairings;
2. alternating signs specify the symplectic combination;
3. common-source incidence correlates the eight ports;
4. reflection incidence may make the correlated pullback a coboundary;
5. scalar endpoint compression is admitted only after a kernel test of that
   pullback.

The third and fourth operations are constructors. They cannot be inferred
from the final scalar cancellation.

## Falsifier certificate

    {
      "code": "alternating_green_form_not_four_endpoint_descending",
      "active_plus_port": "P_z",
      "active_reciprocal_port": "Q_minus_w",
      "all_endpoint_traces": 0,
      "alternating_pairing": "||h||_2^2 > 0",
      "carrier_level": true,
      "common_source_pullback_tested": false
    }

## Disposition

The complete alternating Green polarization does not descend through scalar
endpoint traces on the independent four-port graph carrier. The possible
rescue has been localized to the actual common theta-source incidence and
its reflection relation.

## Claim boundary

This packet proves a carrier-level non-descent theorem. It does not claim
that the correlated physical theta-source image contains the one-pair
witness. The next calculation must derive and test that image rather than
manufacture independent physical ports.
