# Iteration 4: recover all four analytic ports from existing endpoint data

## Question

Are the two ports outside the prior active reader absent from the source?
No new data are needed: the existing endpoint reader O_n has rank four. Its
active projection P_n has rank two. The omitted endpoint sector is present
inside the previously retained hidden data.

SCC obligation: attachment transport and continuous-generator compatibility,
with an explicit audit of the distinct discrete operations. Reuse the original
six labelled packets, history extension, active section and generator.

## Source-derived endpoint splitting

From the actual packet incidence, in endpoint order A,B,C,D,

  M=[[0,1,1,0],[1,0,0,1],[0,1,0,0],[1,0,0,0]].

Its characteristic polynomial is

  (x^2+x+1)(x^2-x-1).

The first factor is the existing order-three active tick. The other two modes
have eigenvalues (1+sqrt5)/2 and (1-sqrt5)/2, not +1 and -1. Thus the source
already contains the two missing dimensions, but their native update law is
different from the Fourier stationary characters.

Let R be the previously used four-by-two active endpoint basis (the prior RB)
and p=(R^T R)^(-1)R^T. Its identity pM=Cp is checked afresh. Consequently ker p
is M-invariant. Choose a rational basis V for ker p and set Q=[R,V]. Then

  Q^(-1) M Q=diag(C,K), K^2-K-I=0.

The checker derives V and K, rather than prescribing desired eigenvectors.
The choice of basis within the retained complement is explicit chart freedom.

## Full analytic attachment

Keep iteration 2's metric-correct active map B into cyclic Fourier coordinates.
Complete it with t_+=(1,1,1,1) and t_-=(1,-1,1,-1), giving

  T=[B,t_+,t_-], J=T Q^(-1).

This declared chart identifies both actual complementary endpoint coordinates
with the two remaining analytic coefficient ports. It neither claims that
native incidence selects that pairing nor changes their native dynamics.
Composing J with iteration 1's comb basis B_a gives an explicit injective map
from the complete endpoint space to the analytic four-port span.

Let A be the existing active angular generator, and define

  A_endpoint=Q diag(A,0,0) Q^(-1).

Then, with D=F-F^(-1) in cyclic Fourier coordinates,

  DJ=J A_endpoint.

This extends the continuous-generator bridge without altering its action on
the original active plane. The full analytic Gram pulled back by J is a
chosen endpoint metric; it is not proved equal to the original history metric.

## Reuse the coherent section law on actual histories

Write Pfull_n=Q^(-1)O_n. Keep the old initial active section Ea. Choose an initial
complementary section using the same inherited metric G_n:

  Ec=G_n^(-1) O_n^T (O_n G_n^(-1) O_n^T)^(-1) V.

It has O_n Ec=V and p O_n Ec=0. Thus Efull=[Ea,Ec] is a section of Pfull_n,
without modifying the existing active section. Transport it using the same
previously proved policy, now with the actual full endpoint tick:

  Efull_(n+1)=step_n Efull_n diag(C,K)^(-1).

The active columns obey exactly the prior rule Ea_next=step Ea C^(-1).
The previous generator L_n=Ea A P_n is unchanged. Its full endpoint identity is

  O_n L_n=A_endpoint O_n.

Hence (B_a J O_n)L_n=(F-F^(-1))(B_a J O_n) at the distribution level. Composing
with the earlier oriented radial/Mellin maps connects all four constructions
on this continuous-generator representation, not just on its active two-plane.

Let Nfull_n=I-Efull_n Pfull_n. Exact reconstruction and coherent transport give

  I=Efull_n Pfull_n+Nfull_n,
  Nfull_(n+1)step_n=step_n Nfull_n.

The original hidden projector splits as Ec Pcomp+Nfull. Two of its coordinates
were visible to the full endpoint reader all along; the remaining n-4 are
endpoint-invisible. They are retained, not set to zero.

## The discrete distinction remains exact

The native endpoint evolution is M, whose spectrum is disjoint from the four
Fourier roots 1,-1,i,-i. Solving FX=XM gives only X=0, even without requiring
injectivity. Therefore no fixed nonzero endpoint attachment can identify the
native discrete tick with the Fourier tick.

One can define an additional operation F_endpoint=J^(-1)FJ. It has order four
and gives the Fourier action in these endpoint coordinates. But it is not M,
and for this declared complementary basis it does not commute with M. It is
an added mathematical operation, not a discovered native successor. A
stage-dependent change of frame could manufacture a commuting tick square;
that would change the comparison convention, not prove equality of operations.

The coherent continuous bridge does not need that substitution: A_endpoint
commutes with M, so the existing native-extension/generator square remains
valid on the complete endpoint space. The gamma-matrix and Hurwitz statements
remain the imported analytic Fourier representation; Fourier is a separate
operation from native word extension.

## Verification and continuation

Run `uv run research/voevodsky/checkers/check_full_endpoint_fourier_bridge.py`.
The exact tests construct four actual retained stages, check rank-four endpoint
readers, the unchanged active generator, full section/hidden transport, the
source polynomial, the analytic adapter, and the absence of any same-tick
intertwiner. Result: `results/full-endpoint-fourier-bridge-v1.json`.

The next analytic gate is the Riemann specialization: the generic shifted-comb
orbit is four-dimensional, but the unshifted self-dual comb relevant to ordinary
zeta may lose independent ports. That specialization must retain the endpoint
correction and cannot be inferred by substituting a=0 into a generic basis.
No RH proof or native arithmetic execution is claimed.
