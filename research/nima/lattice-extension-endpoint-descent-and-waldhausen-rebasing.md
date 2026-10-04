# Lattice extension, endpoint descent, and Waldhausen rebasing

## Question and disposition

How do the integral coherence-pyramid transports, the four-state quotient, and the endpoint labels of the proposed Waldhausen witness fit together?

**Established by the explicit identities below:** the lattice extension has a normalized, nontrivial section cocycle. Its pullback to the endpoint pair groupoid is a coboundary. Endpoint transport, displacement representatives, and octahedral midpoints are distinct integral objects with the same finite quotient. The chosen section and cocycle are strictly C3-equivariant.

**Source boundary:** one labelled filtration supplies an endpoint diagram, but its zero-based endpoint assignment is not a simplicial map from the normalized Waldhausen S-construction to the pair-groupoid nerve. The zeroth face rebases the filtration. The additive class map instead lands naturally in BV; retaining endpoints requires the associated origin cover. Compatibility of this cover with the actual Marici witness coefficients and stable morphisms remains unproved.

This is a finite algebraic derivation and a source-interface analysis, not a physical interpretation, an identification with an amplituhedron, or a new proof of the universal source's K0. No new executable checker is claimed in this packet.

Operator provenance: the operator supplied the six-edge descent table and requested documentation. Its arithmetic is derived below; the supplied claim that the lattice construction completes the stable-source comparison is not adopted.

SCC obligation: attachment transport and route compatibility across integral lifts, finite displacement descent, and simplicial rebasing. A successful class-level comparison does not certify a faithful stable realization.

## 1. Existing source material

The following prior packets already supply the lattice and geometric ingredients:

- [Three pairings of four split fibers](../voevodsky/the_two_bits_are_the_three_pairings_of_four_split_fibers.md): the raw parity lattice, Smith invariants (1,2,2), and the three nonzero quotient classes.
- [Oriented half-difference cocycle](../voevodsky/the_pyramid_flow_is_an_oriented_half_difference_cocycle.md): exact endpoint transport and its index-two span in the primitive lattice.
- [Primitive half-sum edges](../voevodsky/the_coherence_pyramid_carries_information_on_primitive_half_sum_edges.md): midpoint carriers and the distinction from individual vertex differences.
- [S3 versus actual seed faces](s3-filtration-seed-face-comparison.md): integral face relations, the splitness counterexample, and the missing stable seed comparison.
- [Augmentation and dephasing fractions](augmentation-fourier-dephasing-fractions.md): the finite character realization and conditional witness prescription.

The present synthesis adds the explicit section cocycle, its endpoint trivialization, and the Waldhausen rebasing condition. The prior lattice intersection form is -2 times the Euclidean coordinate dot product; agreement of displayed coordinates is not an unqualified identification of those metrics.

## 2. Lattice extension and conventions

Let

\[
L_{\rm sat}=\mathbf Z^3,\qquad
L_{\rm raw}=\{(x,y,z):x\equiv y\equiv z\pmod2\},
\]

and fix quotient coordinates

\[
q(x,y,z)=(x-z,y-z)\pmod2.
\]

This yields the exact sequence of abelian groups

\[
0\to L_{\rm raw}\to L_{\rm sat}\xrightarrow q V\to0,
\qquad V=\mathbf F_2^2.
\]

It is a saturation quotient. It is not automatically the full discriminant group of a lattice with its bilinear form. These quotient coordinates differ from the prior checker's coordinates (x-y,x-z) by the stated invertible binary change of basis; they are chosen so the section below satisfies q s = identity.

Write a=(1,0), b=(0,1), and h=a+b. Define

\[
s(0)=0,\quad s(a)=(0,-1,-1),\quad
s(b)=(-1,0,-1),\quad s(h)=(-1,-1,0).
\]

Equivalently, for bits v=(v1,v2),

\[
s(v)=(-v_2,-v_1,-(v_1\mathbin\oplus v_2)).
\]

The bits on the right are regarded as integers after evaluating XOR. This is a set-theoretic section, not an additive map.

## 3. Full extension cocycle

Define

\[
c(x,y)=s(x)+s(y)-s(x+y)\in L_{\rm raw}.
\]

The identity u+v-(u XOR v)=2uv for bits gives

\[
c(x,y)=-2\bigl(x_2y_2,\ x_1y_1,
(x_1\mathbin\oplus x_2)(y_1\mathbin\oplus y_2)\bigr).
\]

The complete nonzero-index table is

| c | a | b | h |
|---|---|---|---|
| a | (0,-2,-2) | (0,0,-2) | (0,-2,0) |
| b | (0,0,-2) | (-2,0,-2) | (-2,0,0) |
| h | (0,-2,0) | (-2,0,0) | (-2,-2,0) |

The row and column indexed by 0 vanish. Cancellation of the section terms proves, for every x,y,z in V,

\[
c(x,y)+c(x+y,z)=c(y,z)+c(x,y+z).
\]

This is group cohomology with trivial V-action on L_raw, since L_sat is abelian. The cocycle is symmetric and normalized. Replacing s by s+lambda, with lambda:V -> L_raw and lambda(0)=0, changes c by the coboundary

\[
\delta\lambda(x,y)=\lambda(x)+\lambda(y)-\lambda(x+y).
\]

Its class is nonzero: if it vanished, a corrected section would be an additive splitting V -> L_sat, impossible because L_sat is torsion-free and V has nonzero elements of order two.

All displayed cocycle values lie in 2Z^3. This does not make the class trivial with coefficients in L_raw: the section itself does not take values in L_raw.

## 4. Endpoint, displacement, and midpoint lifts

Use vertex labels

\[
v_0=0,\quad v_1=a,\quad v_2=b,\quad v_3=h,
\]

and geometric positions

\[
d_1=(1,1,1),\ d_2=(1,-1,-1),\
d_3=(-1,1,-1),\ d_4=(-1,-1,1).
\]

The section satisfies s(v_i)=(d_(i+1)-d_1)/2. For every ordered pair, including reversals and identities, define

\[
t_{ij}=s(v_j)-s(v_i),\qquad
r_{ij}=s(v_j-v_i),\qquad b_{ij}=r_{ij}-t_{ij},
\]

\[
m_{ij}=\frac{d_{i+1}+d_{j+1}}2,\qquad
\lambda_{ij}=d_{i+1}.
\]

Then

\[
t_{ij}=\beta_{i+1,j+1},\quad
r_{ij}=t_{ij}+b_{ij},\quad
m_{ij}=t_{ij}+\lambda_{ij},
\]

and all three have quotient v_j-v_i. Their agreement in the quotient does not identify their integral representatives.

### The six forward edges

| Edge | Displacement | t | r | b |
|---|---|---|---|---|
| 01 | a | (0,-1,-1) | (0,-1,-1) | (0,0,0) |
| 02 | b | (-1,0,-1) | (-1,0,-1) | (0,0,0) |
| 03 | h | (-1,-1,0) | (-1,-1,0) | (0,0,0) |
| 12 | h | (-1,1,0) | (-1,-1,0) | (0,-2,0) |
| 13 | b | (-1,0,1) | (-1,0,-1) | (0,0,-2) |
| 23 | a | (0,-1,1) | (0,-1,-1) | (0,0,-2) |

Thus t retains six forward-edge values while r identifies the opposite pairs 01|23, 02|13, 03|12. The latter is a property of the selected displacement section, not equality of the original stable cofiber objects.

For an edge cochain k use

\[
\delta k(i,j,k)=k_{ij}+k_{jk}-k_{ik}.
\]

Direct cancellation gives

\[
\delta t=0,\qquad
b_{ij}=c(v_i,v_j-v_i),\qquad
\delta b(i,j,k)=c(v_j-v_i,v_k-v_j),
\]

\[
\delta r=\pi^*c,\qquad
\delta m(i,j,k)=d_{j+1}=\delta\lambda(i,j,k).
\]

In particular, the four increasing face defects are

| Face | delta t | delta b = pi* c |
|---|---|---|
| 012 | (0,0,0) | (0,-2,0) |
| 013 | (0,0,0) | (0,0,-2) |
| 023 | (0,0,0) | (0,0,-2) |
| 123 | (0,0,0) | (0,-2,0) |

The general identities prove more than this four-face table. For reversed edges,

\[
t_{ji}=-t_{ij},\qquad r_{ji}=r_{ij},\qquad
b_{ij}+b_{ji}=2s(v_j-v_i)=c(v_j-v_i,v_j-v_i).
\]

For identities, t_ii=r_ii=b_ii=0, whereas m_ii=d_(i+1). Hence the midpoint cochain is not normalized on identity arrows; subtracting lambda turns it into normalized endpoint transport. A test restricted to six forward edges would miss these distinctions.

## 5. Different cohomological bases

Let Pair(V) have all four vertices and one arrow between each ordered pair. The displacement functor

\[
\pi:\operatorname{Pair}(V)\to BV,\qquad (i,j)\mapsto v_j-v_i
\]

sends endpoint composition to addition. The calculations establish

\[
\pi^*c=\delta b.
\]

Thus the nontrivial group-extension class becomes trivial on the endpoint pair groupoid. The midpoint defect is independently the raw-valued coboundary delta lambda there. It is incorrect to infer from this that the midpoint defect and c are two representatives of the same nonzero class on the same base. Both pullback comparisons must retain their source, coefficients, and descent data.

There is also no obstruction to every integral lift from a free K0 group. If K0 is Z^2 and its quotient map sends the two generators to a,b, the homomorphism

\[
F(m,n)=m\,s(a)+n\,s(b)
\]

is an additive integral lift. It differs from the prescribed section at the sum:

\[
s(h)-s(a)-s(b)=(0,0,2)=2\alpha_{14}.
\]

The nonzero class obstructs an additive section defined on V, not an arbitrary lift from Z^2. Preserving the four specified integral representatives is the additional constraint.

## 6. Symmetry

Let

\[
T=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
R(x,y,z)=(z,x,y).
\]

Then qR=Tq and Rs(v)=s(Tv). Consequently

\[
Rc(x,y)=c(Tx,Ty).
\]

This representative is strictly C3-equivariant. More generally, tetrahedral lattice symmetries preserve L_raw and L_sat, so they act on the extension. For a symmetry g with lattice action R_g and induced quotient action g_bar, define

\[
\lambda_g(x)=R_gs(x)-s(\bar g x)\in L_{\rm raw}.
\]

Then

\[
R_gc(x,y)-c(\bar gx,\bar gy)=\delta\lambda_g(x,y).
\]

This establishes invariance of the extension class under the combined coefficient/quotient action; it does not assert strict equivariance of this section under every element of A4. On the quotient of edge classes the action factors through C3. The affine action on four vertex labels is a different action and need not preserve the chosen zero vertex.

## 7. Waldhausen rebasing: the next source condition

For the normalized S-construction, a filtration

\[
0=A_0\to A_1\to\cdots\to A_n
\]

has absolute class labels v_i=[A_i] in V, after a specified additive K0-to-V map. Its zeroth face is the rebased filtration

\[
0\to A_2/A_1\to\cdots\to A_n/A_1.
\]

Its vertex classes are

\[
(0,v_2-v_1,\ldots,v_n-v_1).
\]

By contrast, the zeroth face in the pair-groupoid nerve deletes the first vertex and produces (v_1,...,v_n). For (0,a,b,a+b), these give respectively

\[
(0,a+b,b),\qquad(a,b,a+b).
\]

They are related by translation, not equality. The obstruction is visible already in degree one: both faces of the S1 object 0 -> X are zero objects, but the edge 0 -> a in Pair(V) has distinct endpoints when a is nonzero.

Accordingly, the zero-based endpoint assignment for a single S3 object is not automatically a simplicial map from the full normalized S-construction to N(Pair(V)). Interval indices alone do not remove the issue.

The additive class construction does give

\[
S_\bullet(\mathcal U)^\simeq\longrightarrow N(BV),
\]

where the degree-n value is the list of consecutive quotient classes [A_i/A_(i-1)]. Inner faces add neighboring classes and the outer faces drop the first or last increment. This statement assumes the specified K0-to-V map; it does not compute it for the proposed universal source.

Set

\[
EV=N(\operatorname{Pair}(V)),\qquad EV/V\cong N(BV),
\]

with diagonal translation on endpoint tuples. The endpoint-resolved source is the pullback

\[
\widetilde S_\bullet
=S_\bullet(\mathcal U)^\simeq\times_{N(BV)}EV.
\]

An element includes an origin w. Its endpoints are w+v_i; under d0 the new origin is w+v_1. A zero-origin choice is a degreewise section but is not simplicial. This constructs an origin-retaining extension of the class-level source. It does not assert that the existing Marici realization already retains that datum or transports its coefficients compatibly.

## 8. Relevant indexed PDF source

The requested `pnpm pdf:search` sweep located a directly relevant construction in T. Dyckerhoff and M. Kapranov, *Higher Segal spaces I*, local file `references/1212.3563v1.pdf`:

- **Section 2.6, PDF pages 35–36**, locators `1212-3563v1:p35` and `1212-3563v1:p36`: the Hecke–Waldhausen simplicial groupoid has degree n equal to the action groupoid G // E^(n+1). Example 2.6.2(a), for the regular action E=G, identifies it up to equivalence with the discrete nerve of G. Proposition 2.6.3 states its 1-Segal property.
- **Section 8.3, PDF pages 144–145**, locators `1212-3563v1:p144` and `1212-3563v1:p145`: groupoid cohomology is defined via derived invariants, with transfer maps under the stated finite-fiber hypotheses. These pages use field-valued representations; they are not by themselves a classification of our integral lattice extension.

The relevant extracted pages were read after searching. Use PDF-page locators: the index's inferred printed-page numbers are unreliable for this file. Its text extraction also has encoding artifacts. The reference supports the endpoint-quotient architecture; it does not certify the proposed Marici source comparison or the integral cocycle by attribution.

Reproduce the search with

```text
pnpm pdf:search 'group cohomology' -Book 1212-3563v1 -Limit 8
pnpm pdf:search 'Hecke-Waldhausen' -Book 1212-3563v1 -Limit 8
```

## 9. Next falsifier and retained boundaries

The next source-level test is whether the actual realization retains the origin cover and implements Waldhausen rebasing on the endpoint-dependent witness coefficients. Its comparison must specify:

1. the source K0-to-V map;
2. the retained origin and its d0 transformation;
3. the coefficient transport relating the rebased and original endpoint frames;
4. compatibility with actual cofiber maps and suspension, not only their additive classes.

An executable audit of the finite formulas should cover all 16 ordered endpoint pairs, all 64 composable pairs in Pair(V), and all 64 triples for the group-cocycle identity, including reversals and identities. The displayed algebraic proofs cover these cases; the operator's supplied six-edge table is not reported as an independently executed exhaustive check.

The splitness counterexample in the preceding S3 comparison still applies to claims of faithful identification with the coordinate-support stable model. The finite augmentation/dephasing theorem also remains unchanged. Neither is superseded by constructing the lattice descent datum.

This packet was documented locally. No commit, push, deployment, external linked-paper verification, or new formal-backend check was requested or performed for it.
