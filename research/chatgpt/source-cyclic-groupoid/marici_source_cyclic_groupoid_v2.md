# A source-based cyclic transport infinity-groupoid

Date: 2026-09-06

## Result and scope

The four-term integral complex serialized in Marici's physical derived-pullback checker admits a normalized marking that is not strictly invariant under rotation of its three road coordinates. It nevertheless admits explicit coherent cyclic transport. The normalized marking space is contractible, and its homotopy quotient by the specified cyclic action is equivalent to the classifying space of the cyclic group of order three.

This is a local instance of the proposed whole-packet construction. The input matrices are taken from the repository, not from the earlier derived-coinvariant example. The cyclic action and coherent marking are specified and checked below. This audit does not independently revalidate the geometric construction of the input complex, its complete upstream dependencies, or compatibility with every other Marici transport.

The accompanying standard-library Python checker performs 88 exact checks, including all nine group composition comparisons and all 27 tetrahedral coherence identities. The proofs below establish the statements beyond finite checking.

## 1. Fixed source packet and admitted transports

Let

\[
G=C_3=\langle\tau\mid\tau^3=1\rangle,
\qquad P=\mathbb Z^3,
\qquad \tau(p_0,p_1,p_2)=(p_2,p_0,p_1).
\]

In words: transport cyclically permutes the three integral road coordinates. Integers and this source symmetry are inputs; this construction does not derive the integers from a coefficient-neutral carrier.

Put

\[
\epsilon(p)=p_0+p_1+p_2,
\qquad \nu=(1,1,1),
\qquad A=\ker\epsilon.
\]

In words: augmentation sums the coordinates; the norm vector has every coordinate equal to one; the contact module consists of zero-sum vectors.

Retain the entire equivariant source extension

\[
E:\quad 0\longrightarrow A\longrightarrow P
\xrightarrow{\epsilon}\mathbb Z\longrightarrow0.
\]

In words: the contact module, road module, primitive quotient, and their maps remain part of the fixed packet. Marici identifies this extension as the generator of its order-three equivariant extension group [S3]. It is not replaced by an isolated residue quotient.

The other fixed part is the full physical chain complex from [S1–S2]:

\[
C_3=\mathbb Z,\qquad
C_2=\mathbb Z\oplus P,\qquad
C_1=\mathbb Z^2\oplus P,\qquad
C_0=\mathbb Z.
\]

In words: the chain groups have ranks one, four, five, and one, in descending degrees.

The differentials are

\[
\begin{aligned}
d_3(k)&=(0,k\nu),\\
d_2(t,q)&=(t,t,(I-\tau)q),\\
d_1(a,b,p)&=a-b-\epsilon(p).
\end{aligned}
\]

In words: the top differential inserts the cyclic norm; the next inserts a conductor difference and road transport differences; the last tests their augmentation compatibility.

These formulas reproduce the repository matrices exactly:

\[
d_3=\begin{pmatrix}0\\1\\1\\1\end{pmatrix},\quad
d_2=\begin{pmatrix}
1&0&0&0\\
1&0&0&0\\
0&1&0&-1\\
0&-1&1&0\\
0&0&-1&1
\end{pmatrix},\quad
d_1=\begin{pmatrix}1&-1&-1&-1&-1\end{pmatrix}.
\]

In words: these are the three boundary matrices in the original ordered integral bases.

Extend cyclic transport by rotating each displayed copy of P and fixing the other summands. The matrices commute with this action, consecutive differentials compose to zero, and the readout below is invariant. This is a specified chain-level lift of the source road rotation. Only this cyclic subpacket is assembled here; no arbitrary automorphism of a final complex is admitted.

Source is fixed up to these specified relabellings. Fixing every source label pointwise would remove these transports. Thus the local base of transported packets is BG, not a rigidly framed point. The full extension E and complex C remain attached to its single packet throughout.

## 2. Integral homology and normalized readout

For a degree-one chain set

\[
r(a,b,p)=\epsilon(p).
\]

In words: the readout is its road augmentation. It vanishes on degree-two boundaries.

A normalized primitive cycle is

\[
z=(1,0,1,0,0),\qquad d_1z=0,\qquad r(z)=1.
\]

In words: this is the repository's primitive degree-one representative, with road augmentation one.

Every degree-one cycle v has a completely integral reduction. Writing

\[
v=(a,b,p_0,p_1,p_2),\qquad a-b=p_0+p_1+p_2,
\]

in words, the cycle condition equates the conductor difference to the road sum, define

\[
s(v)=(b,-p_1-p_2,-p_2,0).
\]

In words: this degree-two chain removes all of v except its multiple of the primitive cycle. Direct multiplication gives

\[
d_2s(v)=v-r(v)z.
\]

In words: every cycle is homologous to its road augmentation times z, with no denominators.

Moreover, the kernel of d2 consists exactly of the vectors of the form (0,k,k,k), which are the image of d3. The map d3 is injective, and d1 is surjective. Therefore

\[
H_1(C)\cong\mathbb Z,\qquad H_i(C)=0\quad(i\ne1).
\]

In words: the full complex has one primitive integral homology class and no integral torsion. This independently verifies the matrix-level homology claim of [S2]. It does not rely on testing ranks over finitely many finite fields.

## 3. The precise marking space and infinity-groupoid

Define a nonnegative chain complex K by

\[
K_0=\ker d_1,\qquad K_1=C_2,\qquad K_2=C_3,\qquad K_n=0\ (n>2),
\]

with boundaries given by d2 and d3.

In words: vertices are actual degree-one cycles of the full complex, edges are their degree-two homotopies, and two-dimensional comparisons come from degree three. The degree-zero term C0 has not been discarded: it defines the cycle constraint in K0.

The readout is a chain map from K to Z concentrated in degree zero. Apply Dold–Kan and take the fibre over the source-normalized value one:

\[
X=\operatorname{hofib}_{1}\bigl(\operatorname{DK}(K)
\xrightarrow{\operatorname{DK}(r)}\mathbb Z\bigr).
\]

In words: X retains every normalized marking, its homotopies, and the higher comparisons between those homotopies. Dold–Kan makes this an explicit Kan-complex model [S5].

Equivalently, an n-simplex is a chain map

\[
F:N_*(\Delta^n;\mathbb Z)\longrightarrow K,
\qquad rF=\epsilon_{\Delta^n}.
\]

In words: each vertex is assigned a normalized cycle, edges and faces are assigned chains satisfying their boundary equations, and the simplex augmentation sends each vertex to one. Faces and degeneracies act by restriction and repetition. This defines all dimensions, not just those checked numerically.

The proposed local transport infinity-groupoid is

\[
\mathfrak G_{\rm cyc}=X//G
=\operatorname*{colim}_{BG}X.
\]

In words: take normalized markings modulo their specified cyclic transports, retaining all homotopies. The extension E, complex C, and readout r are frozen parts of every object.

In the bar model, the simplicial-space level n is X times G to the nth power. Equivalently, a bisimplicial model has

\[
\mathcal B_{p,q}=G^p\times X_q.
\]

In words: one index counts source transports and the other counts homotopies of markings. Taking the diagonal or an equivalent realization gives the homotopy quotient. A whole infinity-groupoid is not being identified with a face of a tetrahedron.

This instantiates the prior construction with local packet base BG, coefficient functor sending its object to K and its generating loop to the specified rotation, and a natural readout to the constant integral unit. The underlying arithmetic source extension is retained separately from this readout functor.

## 4. Strict transport fails at the unit

A strictly invariant cycle must have road coordinates (m,m,m). Its readout is therefore 3m. Consequently,

\[
X^G=\varnothing.
\]

In words: there is no strictly rotation-invariant integral normalized marking.

This is the same divisibility obstruction seen in the source extension:

\[
\epsilon(P^G)=3\mathbb Z,\qquad H^1(G,A)\cong\mathbb Z/3.
\]

In words: invariant road vectors only lift multiples of three; the unit has a nonzero extension obstruction. The extension E remains nonsplit as an equivariant sequence of modules [S3].

## 5. Explicit homotopy-coherent transport

Set

\[
h=(0,-1,0,0)\in C_2,\qquad k=-1\in C_3.
\]

In words: h is the one-rotation comparison chain, and k is the next comparison.

They satisfy

\[
\begin{aligned}
d_2h&=(\tau-1)z,\\
d_3k&=(1+\tau+\tau^2)h,\\
(\tau-1)k&=0.
\end{aligned}
\]

In words: the first chain joins the normalized marking to its rotation; the second fills the accumulated comparison around three rotations; the next compatibility is exact. These equations follow the generator-difference and cyclic-norm structure of the standard cyclic resolution [S6].

The full bar-coherence data can be written without relying only on the group presentation. Represent group elements by g,h,l in {0,1,2}, and define

\[
H_g=\sum_{i=0}^{g-1}\tau^i h,
\qquad
\kappa_{g,h}=-\left\lfloor\frac{g+h}{3}\right\rfloor.
\]

In words: compare a marking with its g-fold rotation by adding the intervening comparison chains. A composition that crosses a complete cycle contributes the integer minus one in the next degree.

For every pair,

\[
d_3\kappa_{g,h}
=H_g+\tau^gH_h-H_{(g+h)\bmod3}.
\]

In words: this fills the triangle comparing composed transport with the chosen comparison for the resulting group element.

For every triple,

\[
\kappa_{h,l}-\kappa_{(g+h)\bmod3,l}
+\kappa_{g,(h+l)\bmod3}-\kappa_{g,h}=0.
\]

In words: the four triangular comparisons satisfy the tetrahedral boundary equation. Cyclic transport acts trivially on C3, so no action term is omitted in this formula.

The identity follows because both ways of adding g,h,l count the same carries modulo three. The checker tests all nine pairs and all 27 triples. All higher bar components can be zero: the target complex has no groups above K2, and the only remaining nonautomatic chain-map condition is exactly the displayed tetrahedral identity. Thus these formulas define a coherent fixed point, not merely a partial list of compatible arrows.

## 6. Homotopy type

The normalized marking space X is contractible. An explicit proof uses L=ker(r:K -> Z). Translation by z identifies X, as a nonequivariant simplicial space, with DK(L).

The formula s above contracts L0. For q=(t,q0,q1,q2) in L1=C2,

\[
q-s(d_2q)=d_3(q_2).
\]

In words: the remaining degree-one discrepancy is removed by the final road-relation coordinate. On L2, that same coordinate map is a left inverse to d3. These identities give an integral contraction of L in every degree.

Hence

\[
X\simeq *,\qquad X^{hG}\simeq *,\qquad
\mathfrak G_{\rm cyc}\simeq BG.
\]

In words: normalized markings form a contractible space; coherent normalized descent also forms a contractible space; the transport quotient retains the cyclic transport group. Here group actions are ordinary homotopy-coherent actions on spaces, not genuine equivariant homotopy types whose equivalences are tested on every strict fixed-point space.

The map X to a point is equivariant and an underlying equivalence. Its homotopy limit gives the second equivalence, and its homotopy colimit gives the third.

Therefore

\[
\pi_0(\mathfrak G_{\rm cyc})=*,\qquad
\pi_1(\mathfrak G_{\rm cyc})\cong C_3,\qquad
\pi_n(\mathfrak G_{\rm cyc})=0\quad(n\ge2).
\]

In words: the local quotient is connected, has an order-three fundamental group, and has no higher homotopy groups. It is an infinity-groupoid equivalent to a one-groupoid, rather than an example with nontrivial homotopy in arbitrarily high dimensions.

The nonsplit extension E has not been split or declared zero. Its strict lifting obstruction does not prevent a coherent marking of the larger complex C. Those are different lifting problems with different targets.

## 7. Source-exact negative control

Marici's cosmological three-Cut example is a distinct coefficient packet. Its first-residue vector satisfies

\[
c_1=(1,1,1,1,1,1),\qquad
 d_0\Omega_{\rm src}=c_1,\qquad d_1c_1=0.
\]

In words: the vector is closed but already has a specified primitive in the full source complex [S4]. Therefore it cannot be counted as a surviving absolute cohomology class in this construction. The physical-chain test in [S4] does not rescue that named class as a relative class.

The accompanying code checks the supplied boundary relation on its one-dimensional source subcomplex. It does not claim to reconstruct the full Cousin complex or its physical chain pairing from that small check.

## 8. Correction to the earlier cyclic example

The earlier example used derived coinvariants of the augmentation ideal and obtained order-three homotopy groups in all positive even dimensions. That is a mathematically different functor applied to a different coefficient object. It was not a computation of the complete physical complex C in this note.

The source-based calculation here gives BG. It supplies an explicit non-strict coherence using source degrees already present, without adjoining generators to force a filler. It does not establish a global source assembly, a derivative operation on primes, or a relation between these local coherence equations and RH.

To enlarge this local example, a new sector or higher-point packet must supply its actual coefficient diagram and comparison maps, with the source readout and all relative degrees retained. Merely replacing G with a larger abstract cyclic group does not supply a new physical arithmetic realization.

## Sources and provenance

[S1] Repository input, fetched through the GitHub connector on 2026-09-06:
`https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/check_physical_derived_pullback_after_transform.py`
Git blob: `7993b2b1bbdba03d05c3f443a45717d7b8efeec5`.
The matrices and normalized representative were extracted. The imported upstream audit pipeline was not executed.

[S2] Marici, entry 436, “The Physical Derived Pullback Is One Primitive Integral Line,” 2026-08-17:
`https://marici.narada.systems/ledger/20260817-436-the-physical-derived-pullback-is-one-primitive-integral-line/`

[S3] Marici, entry 410, “The Filtered Road Recollement Has a Primitive Order-Three Extension,” 2026-08-17:
`https://marici.narada.systems/ledger/20260817-410-the-filtered-road-recollement-has-a-primitive-order-three-extension/`

[S4] Marici, entry 1555, “Physical Prime Descent Requires Survival in the Relative Totalization,” 2026-08-21:
`https://marici.narada.systems/ledger/20260821-1555-physical-prime-descent-requires-survival-in-the-relative-totalization/`

[S5] The Stacks Project, Section 14.24, “Dold–Kan,” especially Theorem 14.24.3:
`https://stacks.math.columbia.edu/tag/019D`

[S6] Kiran S. Kedlaya, Class Field Theory, Section 3.4, “Cohomology of cyclic groups”:
`https://kskedlaya.org/cft/sec_cohom-cyclic.html`
