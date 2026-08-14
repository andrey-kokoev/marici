# Endpoint-Relative D03 Exit Interval and the Remaining Tor Lift

## Record

Date: 2026-08-14

Status: one proved carrier/associated-grade theorem and one sharp typing
falsifier. The absolute single-\(q_0\) formula proposed in entry 117 is not a
chain-level object. After the canonical endpoint-relative correction, the
hexagon face poset contains a unique marked interval from the \(F_{03}\) road
to the Boolean \(q_0\) endpoint. Its occurrence weights derive the previously
missing road divisibility and Beck--Chevalley sign without fitting. The
reciprocal-standard to original-Borel--Moore \(\operatorname{Tor}_1\) lift is
still unconstructed.

## The typing correction

Over

\[
R=\mathbb Z[x_1,x_5],
\]

entry 117 established the exact Koszul diamond

\[
K:\qquad
R\langle e_3\rangle
\xrightarrow{(-x_1,x_5)^T}
R\langle q_0,q_2\rangle
\xrightarrow{(x_5,x_1)}
R\langle a\rangle.
\]

Consequently,

\[
dq_0=x_5a,
\qquad
d(-x_1q_0)=-x_1x_5a\ne0.
\]

The cancellation in \(d^2e_3=0\) is intrinsically two-ended:

\[
-x_1x_5a+x_5x_1a=0.
\]

Thus a standalone absolute source \(I_{x_1}q_0\) with both a generic
\(e_3\) leg and special boundary \(-x_1q_0\) does not exist. There are two
honest one-endpoint objects:

1. the absolute endpoint packet
   \([Rq_0\xrightarrow{x_5}Ra]\), which has no generic \(e_3\) leg; and
2. the endpoint-relative quotient

   \[
   \boxed{
   K_0
   :=K/[Rq_2\xrightarrow{x_1}Ra]
   \simeq
   [Re_3\xrightarrow{-x_1}Rq_0].
   }
   \]

The second is the smallest legitimate source for a one-endpoint
Beck--Chevalley test. Saying that \(q_0\) is closed always means this explicit
relative quotient; it must not be confused with closure in the absolute
scalar complex.

## The unique marked exit interval

The physical road facet \(F_{03}\cong K_4\times K_4\) has the four
occurrence vertices

\[
v_{00}=\{D03,x_0,x_3\},\quad
v_{10}=\{D03,x_1,x_3\},\quad
v_{01}=\{D03,x_0,x_4\},\quad
v_{11}=\{D03,x_1,x_4\}.
\]

The Boolean endpoint \(q_0=\{x_5\}\) is none of them; indeed \(D03\)
crosses \(x_5\). Nevertheless, exactly one road vertex admits the central
flip \(D03\rightsquigarrow x_5\):

\[
v_{10}=\{D03,x_1,x_3\}
\longleftrightarrow
v_+=\{x_1,x_3,x_5\}.
\]

At \(v_{10}\), the two saturated flags in \(F_{03}\) pass through
\(\{D03,x_1\}\) and \(\{D03,x_3\}\). The established positive \(x_3\)
sink mark of entries 96--97 uniquely selects

\[
Z_3=\{D03,x_3\}.
\]

On the \(q_0\) side, the \(x_1\) mark uniquely selects

\[
e_3=\{x_1,x_5\}.
\]

The resulting marked carrier is the seven-node interval

\[
\boxed{
F_{03}>Z_3>v_{10}<e_c>v_+>e_3>q_0,
\qquad e_c=\{x_1,x_3\}.
}
\]

It is a zigzag through the central flip, not a single comparable flag and
not an identification \(q_0=v_{10}\). Relative to its two endpoints,

\[
H_1(I_0,\partial I_0;\mathbb Z)\cong\mathbb Z
\]

with primitive generator given by the oriented fundamental chain. Only the
\(F_{03}\) endpoint lies outside the short-boundary carrier, so this class
retains a nonzero generic \(Q\)-leg at carrier level.

## Unfitted road coefficient and sign

The selected saturated road flag has occurrence labels

\[
F_{03}\xrightarrow{x_3}Z_3
\xrightarrow{x_1}v_{10}.
\]

Its composite is \(+x_3x_1\). Evaluating the labelled \(x_3\) Thom line
therefore derives, rather than assigns,

\[
\boxed{b_0=+x_1.}
\]

On the Boolean side,

\[
de_3=-x_1q_0+x_5q_2.
\]

In the \(q_0\)-relative quotient, principal-line evaluation of the first
term gives

\[
\boxed{a_0=-1.}
\]

The entry-117 normalized two-path equation now holds exactly:

\[
b_0=-x_1a_0=+x_1.
\]

Equivalently, at carrier/occurrence grade there is a normalized map

\[
\gamma^{\rm car}_0:
[e_3\xrightarrow{-x_1}q_0]
\longrightarrow
[F_{03}\xrightarrow{+x_1}\tau^{\rm car}_0],
\qquad
e_3\mapsto F_{03},
\quad q_0\mapsto-\tau^{\rm car}_0,
\]

where \(\tau^{\rm car}_0\) denotes the marked boundary carrier selected by
the interval. It is not yet the reciprocal/Borel--Moore road
\(\operatorname{Tor}_1\) costalk.

## What remains unproved

The marked interval proves a spatial carrier and its occurrence
generization. It does not by itself construct the six-functor map

\[
\text{reciprocal-standard source}
\longrightarrow
\text{original-twist/Borel--Moore road }\operatorname{Tor}_1.
\]

For an independently constructed ringed correspondence with coefficient
module \(M_0\), the absolute endpoint packet has the two-term mapping
complex

\[
[M_0\xrightarrow{\phi(x_5)}M_0],
\]

so the two adjacent groups are

\[
\operatorname{Ann}_{M_0}(\phi(x_5)),
\qquad
M_0/\phi(x_5)M_0.
\]

At the central fibre \(x_1=x_5=0\), both become copies of \(M_0\); this
does not select the desired endpoint class. The rank-one line appears only
after applying the endpoint-relative functor and retaining the labelled
ideal/conormal lines. Hence central base change remains a test, not a
construction.

The next object is the variance-correct lift of \(\gamma^{\rm car}_0\):

\[
\boxed{
\Gamma^{!,\rm PC}_{0,\rm rel}:
\operatorname{Th}^{\rm mR}_{x_3}\otimes
K_0^{\vee,\rm reg}
\longrightarrow
L_{0,\rm road}^{\rm BM,Tor},
}
\]

subject to

\[
\operatorname{gr}_{\rm car}\Gamma^{!,\rm PC}_{0,\rm rel}
=\gamma^{\rm car}_0,
\qquad
[t_3]\mapsto\eta_{3,\rm mix},
\qquad
[dX_{03}]\mapsto+1.
\]

It must send the endpoint generator with coefficient \(-1\), retain the
second excess \(\operatorname{Tor}_1\) copy under derived base change, and
commute with the two Cartier--PL paths before specializing to the central
fibre.

## Sharp falsifier

The entry-117 formula

\[
\operatorname{Th}_{x_3}^{\rm mR}\otimes I_{x_1}q_0
\longrightarrow[t_3]\tau_{q_0}
\]

is false as an absolute chain-level correspondence. The first obstruction
is already \(d(-x_1q_0)\ne0\); it precedes questions of support, twist, or
Verdier variance. Ordinary face maps, central base change, an external Thom
tensor, the coefficient lcm cap, currying entry 97, and literal cone-roof
restriction do not repair that defect.

This falsifier does not rule out the endpoint-relative lift displayed
above, nor a full two-ended extraordinary correspondence. It fixes their
required domain.

## Evidence

New exact certificate:

- `research/voevodsky/check_d03_q0_endpoint_exit_flags.rs`, SHA-256
  `2be0ca7a8db48656c597e43b7d56d9537fe5659191260a839ce26a5bca228a30`.

The certificate enumerates all fourteen labelled hexagon triangulations,
the four \(F_{03}\) vertices, all eight saturated road flags, the unique
compatible central flip, both marked flag selections, the relative interval
class, the exact occurrence quotients, the road coefficient, the endpoint
sign, and the absolute-closure negative control.

## Outcome contract

```json
{
  "claim": "The absolute single-q0 Gamma is mistyped because dq0=x5*a. After the explicit endpoint-relative correction, the scalar face poset supplies a unique marked interval from F03 to q0; its actual occurrence labels derive b0=+x1 and a0=-1, so the normalized Beck-Chevalley equation holds without fitting. The variance-changing extraordinary Tor1 lift is not yet constructed.",
  "status": "falsified",
  "assumptions": [
    "The x3 sink mark is the established positive F03 face-tube mark.",
    "A single q0 endpoint is interpreted in K0=K/[q2->a], not in the absolute Koszul diamond.",
    "Occurrence, Rees, monodromy, excess, and physical-normal lines remain distinct."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_q0_endpoint_exit_flags.rs",
    "ledger entries 96, 97, 100, 116, and 117"
  ],
  "factorization_test": {
    "absolute_q0_source": "falsified",
    "endpoint_relative_source": "proved",
    "unique_marked_interval": "proved",
    "nonzero_generic_carrier_leg": "proved",
    "road_generization": "b0=+x1, derived",
    "endpoint_value": "a0=-1, derived",
    "carrier_Beck_Chevalley": "proved",
    "extraordinary_Tor1_lift": "unconstructed",
    "full_G03_Cousin": "unconstructed"
  },
  "counterevidence": [
    "Without the x3 mark, v10 has a second saturated road flag.",
    "The interval is a central-flip zigzag, not an ordinary face inclusion.",
    "In the absolute source the q2 arm is required for d-squared to vanish.",
    "The carrier map does not identify the Boolean endpoint with the PC road Tor1 costalk."
  ],
  "next_experiment": "Construct the reciprocal-standard/original-BM lift along the certified relative interval. Require associated grade gamma_0^car, endpoint coefficient -1, [t3] to eta_3,mix, and independent [dX03]=+1."
}
```
