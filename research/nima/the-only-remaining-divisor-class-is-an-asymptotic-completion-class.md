# The Only Remaining Divisor Class Is an Asymptotic Completion Class

## Finite flatness

At every finite prime cutoff, the currently constructed coefficient systems
are exact:

- moving-window comparisons factor through a common chamber refinement;
- the full Euler multiplier is strictly multiplicative;
- every prime seam Gram is a Stein coboundary of one source Gram.

Therefore no finite divisor loop carries the required residual.

## Completion comparison cell

Let $\mathsf C$ denote the constructor-generated completion functor and let

\[
\Delta_p(H)=H-A_p^*HA_p
\]

be the finite prime difference. The missing comparison is a natural cell

\[
\kappa_p:
\mathsf C(\Delta_pG)
\longrightarrow
\Delta_p(\mathsf C G).
\]

If both sides exist and $\kappa_p$ is an isomorphism for every prime, the
finite Stein exactness survives completion. If the map is undefined,
noninvertible, or fails higher coherence, its defect is the only remaining
place for a new class.

For two primes, the cells must satisfy the square comparing
$\kappa_p\kappa_q$ with $\kappa_q\kappa_p$. For three primes, those squares
must close around the proper-divisor hexagon. Thus the higher divisor topology
tests coherence of completion, not coherence of the already-flat finite
system.

## Asymptotic quotient

Let $(K_X,d_X)$ be finite Hilbert complexes representing a proposed common
refinement at increasing cutoffs. Assume the differentials are uniformly
bounded. Form the bounded-sequence quotient

\[
\mathcal Q(K)
=
\frac{\prod_X K_X}
{\{(v_X):\|v_X\|\to0\}}.
\]

A sequence of normalized states satisfying

\[
\|d_Xv_X\|\to0,
\qquad
\|d_X^*v_X\|\to0
\]

defines a nonzero harmonic class in $\mathcal Q(K)$. This is emergent
cohomology at infinity: every finite packet can be exact while the asymptotic
system acquires an unpaired state.

Equivalently, with Hodge Laplacian

\[
\Lambda_X=d_X^*d_X+d_Xd_X^*,
\]

the obstruction is

\[
\inf_X
\inf_{\|v\|=1}
\langle v,\Lambda_Xv\rangle
=0.
\]

A uniform positive lower bound excludes asymptotic cohomology and supplies a
uniformly bounded contraction. Loss of the bound is precisely the
completion-at-infinity mechanism.

## Categorical meaning

The finite divisor spheres identify possible coherence degrees, but their
known coefficient systems are coboundaries. The completion functor can
nevertheless fail to preserve the contraction that proves those coboundaries
exact.

Thus the candidate higher class is not a new finite cell. It is the derived
defect of completion:

\[
\mathsf C\circ\Delta
\quad\Longrightarrow\quad
\Delta\circ\mathsf C.
\]

This is the precise categorical version of a partner escaping to infinite
norm.

## Relation to the RH lane

No RH claim follows until one source-derived common complex has been
constructed whose distinguished scalar section is the completed theta
section. Conditional on that bridge, an off-seam zero would be relevant only
if it produced a nonzero class in the asymptotic quotient.

The required theorem would then be source-specific: prove that the completed
theta complex has no asymptotic cohomology for nonzero horizontal spectral
displacement. Universal Hilbert, Fourier-window, and tail complexes already
admit hostile approximate states and cannot prove this.

## Finite falsifier

For a proposed common refinement, compute the smallest positive eigenvalue of
its finite Hodge Laplacian after removing declared exact gauge directions.
A sequence

\[
\lambda_{\min}^+(\Lambda_X)\longrightarrow0
\]

together with normalized approximate harmonic vectors is the decisive
falsifier for completion-stable exactness.

Agreement of all finite determinants, pathwise first jets, and divisor-loop
cells does not override this failure.

## The bare divisor-chamber tower fails the gap test

Let the divisor interval have $N=\tau(n)-1$ chambers and use its unweighted
cellular incidence differential. After removing the constant vertex mode,
the smallest Hodge eigenvalue of the path complex is

\[
\lambda_1(N)
=
2-2\cos\left(\frac{\pi}{N+1}\right).
\]

Hence

\[
\lambda_1(N)
\sim
\frac{\pi^2}{(N+1)^2}.
\]

For a squarefree packet with $r$ distinct primes, $N=2^r-1$, so the gap
collapses on the order of $4^{-r}$.

Thus the exponentially refined chamber topology automatically develops
slow approximate modes. It does not provide uniform exactness merely because
every finite interval complex is contractible.

Using physical interval lengths rather than unit cellular weights does not
give a universal repair. The total interval has length $\log n$, and the
first nonconstant interval-Laplacian scale is proportional to
$(\log n)^{-2}$, which also tends to zero.

Therefore any completion-stable theorem must use additional source dynamics
or weights that control these modes. The raw divisor complex, its reciprocal
pairing, and its exponential relationship count are insufficient.

This is a decisive correction to the tower intuition: adding all missing
relationships restores finite faithfulness but simultaneously creates new
long-wavelength completion modes. Higher relational complexity does not
automatically reduce total incoherence.

## Horizontal mass controls the bulk but misses the source port

The source-derived tail differential contains the required form of dynamical
control. Write

\[
z=a+it,
\qquad
D_z=\partial_q+z.
\]

Conjugation by the unitary phase $e^{itq}$ removes $t$ from the bulk singular
values. Up to the declared boundary terms, the Hodge energy contains

\[
\|D_zg\|^2
\supseteq
a^2\|g\|^2.
\]

Thus nonzero horizontal displacement supplies a mass term capable of
controlling the long-wavelength modes of increasingly refined seam
partitions. The unitary seam $a=0$ is exactly where this bulk control may
disappear.

The actual source system is augmented:

\[
\mathcal D_z=
\begin{pmatrix}
\partial_q+z&f\\
0&\partial_q
\end{pmatrix}.
\]

Its spectral parameter acts through a singular weight. The constant source
channel lies in the kernel of that weight, so the horizontal mass controls
the transported tail but not the complete augmented state.

This is why the bulk differential alone does not exclude off-seam zero
states. The remaining approximate class can use the unpaired source channel
and its forcing incidence.

Making that channel dynamical by inserting the Hilbert adjoint of $f$ changes
the native affine source equation. The source-faithful repair must instead
retain separate input and response ports and derive their comparison through
the completed boundary object.

The next gate is therefore narrower than generic coercivity: determine
whether the source-derived response port transfers the horizontal bulk mass
to the completion class while preserving the fixed input constructor. If it
does not, the augmented complex retains an off-seam escape direction despite
the massive tail block.

## The horizontal mass closes every homogeneous bulk escape

The previous statement can be made exact once the boundary ports are removed.
Let \(h\) be a tail state with the declared homogeneous endpoint condition and
put

\[
D_z h=h'+zh,
\qquad z=a+it.
\]

After the unitary gauge \(h(q)=e^{-itq}g(q)\), integration by parts gives

\[
\|D_zh\|^2
=
\|g'\|^2+a^2\|g\|^2
\]

when the endpoint trace vanishes. Consequently

\[
\|D_zh\|^2\ge a^2\|h\|^2.
\]

The same calculation on every finite divisor-chamber refinement says that
the massive Hodge operator is

\[
\Lambda_{X,a}=\Lambda_X+a^2I,
\]

so

\[
\lambda_{\min}(\Lambda_{X,a})\ge a^2
\]

uniformly in the cutoff whenever \(a\ne0\). The gap collapse of the bare
divisor complex is therefore completely repaired in the homogeneous bulk.
There can be no off-seam cohomology at infinity supported entirely in that
bulk.

This removes one ambiguity from the frontier. A surviving off-seam class
must enter through a boundary trace, a fixed source input, or its adjoint
response. It cannot be blamed on ever finer divisor chambers alone.

## The minimal response realization is conservative but indefinite

The fixed input can be retained by adjoining a distinct accumulated response.
For real source profile \(f\), consider

\[
u'=-zu-fc,
\qquad
c'=0,
\qquad
r'=fu.
\]

On the ordered state \(x=(u,c,r)^T\), this has generator

\[
M_z=
\begin{pmatrix}
-z&-f&0\\
0&0&0\\
f&0&0
\end{pmatrix}.
\]

Introduce the Hermitian port metric

\[
J=
\begin{pmatrix}
1&0&0\\
0&0&1\\
0&1&0
\end{pmatrix}.
\]

Direct multiplication yields

\[
M_z^*J+JM_z
=
-2a
\begin{pmatrix}
1&0&0\\
0&0&0\\
0&0&0
\end{pmatrix}.
\]

Thus the system is exactly \(J\)-skew on the seam and obeys the off-seam
balance

\[
\frac{d}{dq}
\left(
|u|^2+2\operatorname{Re}(c\overline r)
\right)
=-2a|u|^2.
\]

This constructs the local source-faithful response dynamics, but it also
exhibits the obstruction sharply. The metric \(J\) is indefinite. The input
and response form a hyperbolic pair, so the positive horizontal mass on \(u\)
does not become a positive mass on the complete port state.

For a two-ended tail state, integration gives

\[
2a\int |u|^2\,dq
=
-2\operatorname{Re}
\left(c\,\overline{r(\infty)-r(0)}\right).
\]

Therefore an off-seam state is excluded precisely when the completed sewing
law closes the relative response pairing on the distinguished zero domain.
The local colligation, its seam conservativity, and the homogeneous mass gap
do not imply that closure.

## Revised finite falsifier

At a labelled cutoff, first verify the exact port identity

\[
M_{z,X}^*J_X+J_XM_{z,X}
=-2aP_{u,X}.
\]

Then evaluate the completed response increment on every declared scalar-zero
state. A nonzero value of

\[
\operatorname{Re}
\left(c_X\,\overline{r_X(\infty)-r_X(0)}\right)
\]

is not a small analytic error. It is the exact typed witness that the proposed
completion fails to terminate the open relative port. Conversely, imposing
its vanishing without a source-derived sewing constructor merely restates the
zero-confinement requirement.

## Categorical form of the remaining boundary law

The input and response coordinates have canonical types

\[
c\in U,
\qquad
r\in U^*.
\]

Their contribution to the port energy is the hyperbolic evaluation pairing on

\[
U\oplus U^*.
\]

Thus the global sewing problem is not the construction of another positive
bulk observer. It is the construction of a boundary relation

\[
L_{\mathrm{src}}
\subset
(U\oplus U^*)_{q=0}
\oplus
(U\oplus U^*)_{q=\infty}
\]

that is neutral for the endpoint difference of this pairing. Maximal
neutrality is the port version of a self-adjoint boundary condition. It makes
the local \(J\)-skew colligation into a closed global realization without
identifying the input with its response.

This supplies the missing coherencer type:

1. fixed source input;
2. massive transported tail;
3. dual response;
4. source-derived maximal neutral boundary relation.

The last arrow is dynamical in the relevant sense: it is a relation among
admissible boundary states, not a scalar equality appended after evaluation.
It must be derived before taking the completed scalar readout.

The strongest admissible theorem is now conditional and exact. If the
labelled theta/Tate constructors generate a completion-stable maximal neutral
relation containing every distinguished scalar-zero boundary state, then the
integrated port balance excludes \(a\ne0\) for every nonzero transported
state. If the relation is merely chosen to contain those states, the argument
is circular.

This formulation also separates two independent failure modes:

1. failure of neutrality leaves a measurable response-flux residual;
2. failure of maximality leaves an unpaired boundary direction even when all
   admitted states have zero flux.

The second failure cannot be detected by checking the scalar endpoint current
alone. A finite audit must therefore test both the Gram matrix of the boundary
pairing restricted to the proposed relation and the dimension or annihilator
condition that establishes maximality.

## Neutral relations do not canonically become unitary phases

Suppose first that the proposed boundary relation is the graph of an operator

\[
T:U\longrightarrow U^*,
\qquad
\Delta r=Tc.
\]

Neutrality for the hyperbolic evaluation pairing is exactly

\[
T+T^*=0.
\]

Thus a graph-type termination is generated by a skew-adjoint response law.
This is already a useful finite test: the Hermitian part of the response
matrix is the boundary-flux residual.

There is, however, no canonical Cayley phase at this level of typing. To add
or subtract an input \(c\in U\) and a response \(\Delta r\in U^*\), one must
first choose a positive pivot or impedance

\[
Z:U\longrightarrow U^*.
\]

Only after that choice can one define normalized incoming and outgoing
coordinates such as

\[
w_\pm
=
\frac{1}{\sqrt2}
\left(
Z^{1/2}c
\pm
Z^{-1/2}\Delta r
\right).
\]

In these coordinates, maximal neutral relations have the familiar scattering
form

\[
w_+=Vw_-,
\qquad
V^*V=I.
\]

Therefore passing from a maximal neutral relation to a unitary boundary phase
is not type-free. It requires the additional source datum \(Z\). Changing
\(Z\) changes the unitary presentation even when the intrinsic neutral
relation is held fixed.

This identifies the response-port form of the existing Cayley-phase
obstruction. The adelic Weyl algebra may determine a maximal commuting
boundary algebra, yet it does not by itself determine either:

1. the impedance that compares source input with dual response; or
2. the unitary phase selecting one maximal neutral graph.

The completed theta source must supply both, or supply the intrinsic relation
directly without passing through a chosen unitary chart.

## Spectral independence gate

A self-adjoint realization has one fixed domain. Its boundary relation and
impedance must therefore be constructed independently of the spectral
parameter \(z\). The eigenvalue equation may depend on \(z\); the rule
selecting admissible boundary states may not be fitted separately at each
candidate zero.

This gives a particularly cheap hostile test. Given any nonzero boundary
state at a chosen \(z_0\), one can manufacture a skew-adjoint graph containing
that state whenever its flux is neutral. Such a \(z_0\)-dependent graph passes
the pointwise energy identity but proves nothing. A candidate constructor is
admissible only if the same \(L_{\mathrm{src}}\) and the same pivot \(Z\):

1. act at every cutoff;
2. commute with the declared reciprocal and arithmetic transports;
3. survive completion; and
4. are fixed before the scalar determinant or zero condition is evaluated.

The RH-bearing selection problem is consequently smaller and harder than
generic self-adjointness. It is the source derivation of one spectrally fixed
maximal neutral relation on the fully typed input-response boundary object.

## The prime-square current is not the missing impedance

The three-level Schatten filtration suggests a tempting assignment:
primitive degree as input displacement, square degree as boundary metric, and
higher degrees as determinant readout. That assignment is not type-correct.

On the seam, the connected prime-square contribution to the local Tate phase
is

\[
i\,p^{-1}\sin(2t\log p).
\]

It is anti-Hermitian phase data and changes sign with \(t\). A positive
impedance \(Z\), by contrast, is Hermitian and satisfies

\[
\langle c,Zc\rangle>0
\]

for every nonzero admitted input. No scalar normalization can turn the
sign-changing imaginary prime-square phase into such a positive form while
preserving its source coefficient.

The positive local comparison instead comes from self-dual Haar and
Plancherel structure. Those data make Fourier exchange unitary and place the
evaluation and integral observers in one normalized local duality. The
prime-square current has a different job: it records the second connected
phase removed from the order-three regularized determinant.

This yields a general typing rule. Cumulant degree does not determine
operator modality:

- first and second connected currents may live in a determinant-line
  connection;
- a positive pivot lives in a Hermitian metric channel;
- equality of polynomial degree does not authorize transport between them.

Any proposal identifying the \(k=2\) countercurrent with the port impedance
must exhibit an explicit source-derived modality-changing constructor. Its
finite falsifier is immediate: evaluate the proposed metric at two spectral
heights where \(\sin(2t\log p)\) has opposite signs. If the resulting
quadratic form changes sign, it is a phase current rather than an impedance.

## Sharpened frontier

The local architecture now has three independently typed pieces:

1. self-dual Haar/Plancherel data supply the positive input-response pivot;
2. the labelled Fourier--Tate source must select a fixed maximal neutral
   boundary relation;
3. the primitive, square, and connected-tail currents trivialize the
   determinant-line anomaly and construct the scalar readout.

The first piece is locally canonical. The third has the exact Schatten-three
filtration. The missing theorem is the second piece together with its
restricted-product compatibility. Neither local Fourier unitarity nor the
regularized determinant counterterms currently select it.

## Valuation covariance leaves two Fourier-character branches

The finite-place boundary observer plane already carries the exact source
operators

\[
A_p(a)=
\begin{pmatrix}
|a|_p^{1/2}&0\\
0&|a|_p^{-1/2}
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]

with

\[
BA_p(a)B=A_p(a)^{-1}.
\]

After the self-dual Haar pivot identifies the local input and response
coordinates, let \(T\) be a skew-adjoint unitary satisfying

\[
TA_p(a)=A_p(a)^{-1}T
\]

for every valuation dilation. Then

\[
T=
\begin{pmatrix}
0&e^{i\theta}\\
-e^{-i\theta}&0
\end{pmatrix}
\]

for some phase \(\theta\). If \(T\) must also commute with the Fourier exchange
\(B\), this continuous ambiguity collapses to

\[
T\in\{+iB,-iB\}.
\]

That is the Fourier-even branch. It was the provisional choice in the first
version of this calculation, but it is not the character carried by the
unresolved theta response.

The relative response changes sign when the reciprocal sectors are exchanged.
Its source typing therefore requires

\[
BTB=-T.
\]

Write

\[
Q=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

On the Fourier-odd branch, the same local uniqueness calculation gives

\[
T\in\{+QB,-QB\}.
\]

Both choices satisfy

\[
T^*=-T,
\qquad
T^2=-I,
\qquad
TA_p(a)=A_p(a)^{-1}T.
\]

Their graphs are maximal neutral for the hyperbolic port pairing. The
quarter-turn is now constructed from two independently typed source
operations: valuation coorientation \(Q\) and reciprocal exchange \(B\).
The order matters because

\[
QB=-BQ.
\]

Thus the earlier \(iB\) candidate was mathematically valid but typed to the
common response. The RH-bearing forcing defect lives in the relative response
and selects the \(QB\) branch instead.

Local valuation covariance, skew-adjointness, unitarity, and a declared
Fourier character reduce the continuous Cayley ambiguity to one orientation
bit. This is substantially more rigid than the unrestricted phase family,
but the response character must be fixed before the reduction is applied.

## What this does and does not solve

The relative local neutral graph is now source-shaped rather than fitted to a
zero.
What remains is global:

1. determine whether source ordering selects one orientation at every place;
2. prove compatibility of that selection with the archimedean port;
3. construct the restricted-product maximal neutral relation while
   retaining the primitive and square anomaly currents;
4. prove that the resulting fixed relation has the completed theta
   determinant as its source readout.

The next calculation resolves the finite-place part of the first item. It
does not yet establish the archimedean comparison or continuity through the
global arithmetic completion.

## Ordered observer types fix the local sign

At a finite place the two boundary observers are not an unordered basis. They
have different source meanings:

\[
\epsilon_p(f)=f(0),
\qquad
\mu_p(f)=\int_{\mathbb Q_p}f(x)\,dx.
\]

The first is the puncture germ and the second is its global Fourier mate.
Their declared order defines the alternating boundary form

\[
\omega_p
=
\epsilon_p\wedge\mu_p.
\]

In the ordered basis \((\epsilon_p,\mu_p)\), its matrix is

\[
\Omega_p
=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
=QB.
\]

The opposite candidate \(-QB\) is not another phase on the same ordered
packet. It is the form obtained by reversing the declared observer order.
Such a reversal requires an explicit coorientation-changing constructor.

The source covariance is exact:

\[
A_p(a)^*\Omega_pA_p(a)=\Omega_p
\]

and

\[
B^*\Omega_pB=-\Omega_p.
\]

Thus valuation transport is symplectic, whereas reciprocal Fourier exchange
reverses the boundary coorientation. This is precisely the Fourier-odd
character required by the relative response.

Self-dual Haar normalization fixes the relative scaling of \(\epsilon_p\) and
\(\mu_p\). Their source labels fix the order. Together they select
\(\Omega_p=QB\) without inspecting \(z\), the completed determinant, or its
zeros.

The local orientation problem is therefore closed at the algebraic
two-observer level. The remaining global question is not a product of
arbitrary sign choices. It is whether the direct sum of the canonically
oriented local forms extends to a continuous nondegenerate boundary form on
the constructor-generated arithmetic completion.

This distinction is essential. On the algebraic finite-support one-particle
prime module,

\[
\Omega_{\mathrm{fin}}
=
\bigoplus_p\Omega_p
\]

is automatically well defined and nondegenerate. Maximal neutrality of its
graph is finite-cutoff exact. Extending this form through the positive-Fock
constructor is an additional typed operation; it must not be replaced by a
free direct sum on composite labels. Nothing yet proves that the resulting
form remains nondegenerate or maximal in the pro-Gram topology.
Adjacent-label collapse can erase precisely the arithmetic directions on
which the local forms act.

The next finite-to-completion compiler must therefore test one fixed
constructor family \(F\) for uniform domination of the oriented boundary
form:

\[
\left|
\Omega_X(v,w)
\right|
\le
C
\|v\|_{Q_{F,X}}
\|w\|_{Q_{F,X}}
\]

with a cutoff-independent \(C\), followed by a nondegeneracy test on the
completed quotient. Failure of domination means the form does not descend.
Successful descent with a nontrivial annihilator means it descends but loses
maximality. These are the exact two global failure modes.

## Fock parity makes the primitive current the orientation carrier

Let the local positive-Fock constructor lift \(\Omega_p\) to symmetric degree
\(k\):

\[
\Gamma_k(\Omega_p)
=
\left.\Omega_p^{\otimes k}\right|_{\operatorname{Sym}^k}.
\]

Because

\[
\Omega_p^2=-I,
\]

the lifted operator satisfies

\[
\Gamma_k(\Omega_p)^2=(-1)^kI.
\]

Reversing the local coorientation has the degreewise effect

\[
\Gamma_k(-\Omega_p)
=
(-1)^k\Gamma_k(\Omega_p).
\]

Consequently every even symmetric grade is blind to the orientation sign.
In particular, the even Veronese endpoint tower cannot distinguish
\(\Omega_p\) from \(-\Omega_p\). The first primitive grade can.

This gives the non-Hilbert primitive current a precise structural role. It is
the lowest Fock channel that carries the source coorientation erased by every
even scalar endpoint shadow. Removing it before global sewing does more than
regularize a divergence: it forgets which maximal neutral relation is being
assembled.

The prime-square grade has the complementary behavior. It survives at the
Hilbert level but is orientation-even. It can contribute determinant-line
phase and quadratic transport data, but it cannot recover a lost primitive
orientation. This independently confirms that the \(k=2\) current is not the
missing impedance or coorientation selector.

The three Schatten grades now have a rigorously separated minimum typing:

1. \(k=1\) retains odd coorientation and must remain as a distributional
   boundary channel;
2. \(k=2\) is orientation-even, Hilbert, and determinant-line sensitive;
3. \(k\ge3\) supplies the absolutely summable connected tail after the first
   two cumulants are retained externally.

This does not yet prove that the Fock lift is continuous in the global
constructor topology. It identifies exactly what continuity must preserve.
Any completion map that kills the odd primitive character while retaining
only even endpoint grades cannot construct the required global neutral
boundary relation.

The smallest finite falsifier is the second Veronese map

\[
\nu_2(x)=x\odot x.
\]

It obeys

\[
\nu_2(-x)=\nu_2(x)
\]

while the primitive orientation character changes sign. Hence no function of
the even endpoint carrier can reconstruct that character. A proposed global
sewing that derives its coorientation only after even Veronese projection
fails before any analytic or determinant calculation.

## Hilbert maximality excludes the primitive orientation carrier

The arithmetic test rigging already constructed for the prime boundary is

\[
\mathcal S_P
\subset
\mathcal H_0
\subset
\mathcal S_P',
\qquad
\mathcal H_0=\ell^2(P).
\]

The primitive current has coefficient sequence

\[
b_p=\frac{\log p}{\sqrt p}.
\]

It belongs continuously to \(\mathcal S_P'\), but

\[
\sum_p|b_p|^2
=
\sum_p\frac{(\log p)^2}{p}
=\infty.
\]

Hence \(b\notin\mathcal H_0\). This gives an immediate no-go theorem: no
bounded unitary

\[
V:\mathcal H_0\longrightarrow\mathcal H_0
\]

can have the primitive response \(b\) as an output on an admitted Hilbert
input. A maximal neutral graph constructed only in
\(\mathcal H_0\oplus\mathcal H_0\) necessarily omits the odd channel that
carries the source coorientation.

Fourier saturation does not repair this mismatch. It transports the
primitive current continuously inside the dual rigging, but it does not turn
that current into a Riesz vector in \(\mathcal H_0\).

The correct global target must therefore be a rigged boundary relation

\[
L_{\mathrm{rig}}
\subset
\mathcal S_P'\oplus\mathcal S_P'
\]

with a declared graph domain \(D\) satisfying

\[
\mathcal S_P\subset D\subset\mathcal S_P'.
\]

Its Green pairing is defined by test--distribution duality, not by an illicit
Hilbert identification. Maximality must be stated relative to this dual pair
and the chosen graph domain.

This changes the completion compiler. Uniform boundedness of a Hilbert
scattering matrix is too strong and excludes the physical primitive current.
Mere weak continuity in \(\mathcal S_P'\) is too weak and does not close the
Green identity. In the two-sector refinement below, these conditions apply to
the appropriate direct and reciprocal domains and their common boundary
object:

1. the oriented primitive and square currents define continuous
   vector-valued boundary maps on their source domains;
2. the doubled differential maps each domain into its declared dual grade;
3. the sewn Green pairing closes on the common boundary object;
4. the resulting neutral relation equals its annihilator in the rigged
   pairing; and
5. cutoff states converge in the graph topology of all four structures.

The finite falsifier is membership. If a proposed completed neutral graph is
contained in the middle Hilbert space, evaluate whether it contains \(b\).
It cannot. If it is enlarged to the full dual without a graph domain, test
whether the Green pairing is defined on every claimed pair. A single
undefined dual--dual contraction rejects that enlargement.

## Every positive Hilbert grade works, but none is canonical

For \(\delta\in\mathbb R\), define the weighted prime Hilbert scale

\[
\mathcal H_\delta
=
\left\{
c:
\sum_p p^{2\delta}|c_p|^2<\infty
\right\}.
\]

The test and distribution spaces are the projective and inductive ends of
this scale. The primitive coefficient satisfies

\[
b\in\mathcal H_{-\delta}
\]

for every \(\delta>0\), because

\[
\sum_p
p^{-2\delta}|b_p|^2
=
\sum_p
\frac{(\log p)^2}{p^{1+2\delta}}
<\infty.
\]

At each fixed positive grade there is a weighted Riesz pivot

\[
Z_\delta:
\mathcal H_\delta
\longrightarrow
\mathcal H_{-\delta},
\qquad
(Z_\delta c)_p=p^{2\delta}c_p.
\]

It is an isometric isomorphism. Combining it with the oriented local form
produces a grade-dependent skew response map

\[
T_\delta=Z_\delta\Omega_{\mathrm{fin}}.
\]

Thus every \(\delta>0\) admits an ordinary Hilbert-scale realization in which
the primitive response is legal and the neutral graph can be maximal.

The family has no endpoint member. At \(\delta=0\), the primitive current is
not in \(\mathcal H_0\). There is also no least positive \(\delta\) selected by
the rapid-decay rigging. Worse, the pivots do not restrict to one common map:

\[
Z_{\delta_1}c
\ne
Z_{\delta_2}c
\]

for a generic nonzero packet whenever \(\delta_1\ne\delta_2\).

Therefore choosing one weighted Hilbert grade constructs a boundary phase by
choosing a regularity scale. Fourier and Mellin covariance preserve every
grade and do not select among them. Such a choice is presentation data unless
an additional source operation fixes \(\delta\).

The unweighted oriented inclusion remains canonical across the projective
system, but it is not a maximal Riesz graph on any boundary space containing
the primitive distribution. Conversely, the gradewise maximal graphs are not
natural across the projective system.

The next object to test is consequently a scale-natural rigged relation,
not a single Cayley operator. It requires comparison cells

\[
\kappa_{\delta_2,\delta_1}
:
T_{\delta_2}
\Longrightarrow
T_{\delta_1}
\]

for \(\delta_2>\delta_1>0\), compatible on triple overlaps, and a controlled
boundary value as \(\delta\downarrow0\). The next calculation separates these
two requirements.

## The positive-grade tower is flat; the primitive section escapes

Define unitary grade trivializations

\[
U_\delta:
\mathcal H_\delta\longrightarrow\mathcal H_0,
\qquad
(U_\delta c)_p=p^\delta c_p
\]

and

\[
U_{-\delta}:
\mathcal H_{-\delta}\longrightarrow\mathcal H_0,
\qquad
(U_{-\delta}r)_p=p^{-\delta}r_p.
\]

Since the prime weights commute with the sheet operator
\(\Omega_{\mathrm{fin}}\), direct substitution gives

\[
U_{-\delta}T_\delta U_\delta^{-1}
=
\Omega_{\mathrm{fin}}.
\]

Thus all positive-grade neutral graphs are unitarily the same. The induced
comparison cells between grades compose exactly, and every triple-overlap
holonomy is the identity. There is no scale-coherence anomaly on
\(\delta>0\).

The distinguished primitive section behaves differently. Its norm is

\[
\|b\|_{\mathcal H_{-\delta}}^2
=
\sum_p
\frac{(\log p)^2}{p^{1+2\delta}}.
\]

This is finite for every \(\delta>0\) and diverges as
\(\delta\downarrow0\). Hence the relation tower is flat while the physical
odd section has no finite middle-Hilbert boundary value.

This is a cleaner form of the primitive anomaly:

- the constructor comparisons do not accumulate incoherence;
- the maximal neutral graphs do not change up to canonical unitary
  equivalence;
- the source section carrying coorientation escapes every bounded set at the
  endpoint grade.

The Hilbert completion problem is therefore an escape problem for a
distinguished distributional section, not a search for another coherence
cell among the positive grades. But the arithmetic test rigging already gives
the correct non-Hilbert compactification: \(b\) is a fixed continuous element
of \(\mathcal S_P'\).

Indeed, if one instead normalizes

\[
\widehat b_\delta
=
\frac{b}{\|b\|_{\mathcal H_{-\delta}}}.
\]

then every fixed test \(c\in\mathcal S_P\) satisfies

\[
\left\langle
\widehat b_\delta,c
\right\rangle
=
\frac{\langle b,c\rangle}
{\|b\|_{\mathcal H_{-\delta}}}
\longrightarrow0.
\]

Thus the normalized Hilbert ray loses the primitive current in the weak test
pairing. The source-faithful endpoint object is the unnormalized covector
\(b\in\mathcal S_P'\), not a unit Hilbert limit.

The live obstruction is consequently domain compatibility. The completed
zero-state must be admitted by sewn graph domains on which the primitive
current, square current, seam response, and doubled differential form one
defined boundary packet. The primitive current itself no longer needs to be
constructed or compactified; its joint action in that packet does.

## A single common scalar domain is still too strong

The last sentence needs a sector qualification. Test the primitive covector
against the raw centered Mellin packet

\[
c_p(z)=p^{-z}.
\]

Its formal scalar pairing is

\[
\langle b,c(z)\rangle
=
\sum_p
\frac{\log p}{p^{1/2+z}}.
\]

Absolute convergence requires

\[
\operatorname{Re}z>\frac12.
\]

The reciprocal packet \(c_p(-z)\) gives the opposite convergence cone

\[
\operatorname{Re}z<-\frac12.
\]

Thus the two primitive scalar pairings are born on disjoint source domains.
Neither is individually defined by its Euler series near the critical seam.
Analytic completion is precisely the operation that transports their coupled
boundary data across the intervening strip.

Consequently the correct global domain cannot require every typed current to
produce an independent scalar on one common state space. That would either
exclude the completed seam states or silently import analytic continuation
into each channel separately.

The minimum source-faithful object has two rigged graph domains,

\[
D_+,
\qquad
D_-,
\]

their vector-valued primitive, square, seam, and archimedean boundary maps,
and a sewing relation between their boundary objects. The scalar completed
readout is permitted only after that relation has combined the channels.

Categorically, the domain is a recollement or gluing diagram rather than an
intersection:

1. \(D_+\) carries the direct Euler-cone current;
2. \(D_-\) carries the reciprocal Euler-cone current;
3. a boundary object retains their oriented distributional limits;
4. the maximal neutral relation lives on that boundary object;
5. scalar completion is a final readout of the sewn packet.

This repairs the overly strong single-domain formulation. What must be
jointly continuous is the vector-valued sewing constructor, not every
channel's premature scalarization.

The hostile test is now exact. If a proposed domain evaluates the primitive
Euler sum as an ordinary convergent scalar for

\[
|\operatorname{Re}z|\le\frac12,
\]

it has smuggled in a continuation or regularization. The proposal must instead
name the coupled boundary object and show how the direct and reciprocal
distributional currents enter it before any scalar cancellation occurs.

## The source cover has three charts, not two half-planes

The convergence thresholds expose a categorical error in the informal
two-half-plane picture. In the centered coordinate \(z=s-\tfrac12\), the
direct primitive Euler current is born on

\[
E_+
=
\left\{
z:
\operatorname{Re}z>\frac12
\right\},
\]

while its reciprocal source current is born on

\[
E_-
=
\left\{
z:
\operatorname{Re}z<-\frac12
\right\}.
\]

These open sets are disjoint. Their intersection is empty, and the critical
seam is contained in neither source convergence domain. Therefore no ordinary
transition map on \(E_+\cap E_-\) can produce analytic continuation or the
boundary relation.

The completed theta/Mellin construction supplies a third chart \(M\) spanning
the intervening strip and overlapping the two Euler charts in separate
regions after the appropriate endpoint subtractions. The source descent
diagram runs from the direct Euler chart through the theta/Mellin bridge and
then to the reciprocal Euler chart.

There is no primitive direct arrow between the outer charts. Their apparent
comparison is the composite through \(M\).

This changes the interpretation of the critical seam. It is not literally
the overlap of the two original Euler sectors. It is an internal
coorientation locus of the bridge chart, where the two completed
presentations acquire equal modular weight.

Consequently the often-used two-half-plane Ubersector is a derived,
post-continuation object. Treating it as the source object silently grants the
very analytic continuation whose operator-valued lift remains under
construction.

The minimum categorical carrier is instead:

1. the direct Euler rigging on \(E_+\);
2. the reciprocal Euler rigging on \(E_-\);
3. the theta/Mellin bridge rigging on \(M\);
4. a transition correspondence on \(E_+\cap M\);
5. a transition correspondence on \(M\cap E_-\);
6. the oriented neutral boundary object internal to \(M\).

The two transition correspondences must transport the primitive
coorientation into the same bridge-boundary form. Their composite is the
completed reciprocal sewing. This is the exact location where the
operator-valued continuation can fail even though the scalar functional
equation succeeds.

## Revised descent falsifier

Construct the two transition correspondences independently from the direct
and reciprocal theta/Tate integrals. When a finite-cutoff correspondence is
the graph of a map

\[
T_{\pm,X}:
\mathcal B_{\pm,X}
\longrightarrow
\mathcal B_{M,X},
\]

the correctly typed naturality residuals are

\[
R_{\pm,X}
=
T_{\pm,X}^*
\Omega_{M,X}
T_{\pm,X}
-
\Omega_{\pm,X}.
\]

Both must vanish before the two legs may be composed. Agreement only after
applying the completed scalar readout is insufficient, because that readout
can annihilate an orientation residual.

If a transition is a genuine relation rather than the graph of a map, no
pushforward form should be invented. Its graph must instead be maximal
isotropic in the product boundary object carrying the difference form

\[
-\Omega_{\pm,X}\oplus\Omega_{M,X}.
\]

Only then is relational composition through \(\mathcal B_{M,X}\) admitted.
The composite must also be checked for clean intersection; otherwise excess
middle states create a new kernel even when both legs are individually
isotropic.

Nonzero \(R_{\pm,X}\), failure of graph maximality, or a nonclean middle
intersection is an operator-valued continuation defect. If all finite tests
pass, the remaining gates are stability of maximality and clean composition
through the restricted-product completion.

## The meeting of the two legs generates an excess observer

Let

\[
L_{+,X}
\subset
\overline{\mathcal B_{+,X}}
\oplus
\mathcal B_{M,X}
\]

and

\[
L_{-,X}
\subset
\overline{\mathcal B_{M,X}}
\oplus
\mathcal B_{-,X}
\]

be the two finite transition relations. Their composition eliminates the
middle boundary coordinate. The states lost by that elimination form the
excess space

\[
\mathcal E_X
=
\left\{
m\in\mathcal B_{M,X}:
(0,m)\in L_{+,X},
\ (m,0)\in L_{-,X}
\right\}.
\]

Every element of \(\mathcal E_X\) is invisible at both outer Euler ports. It
is nevertheless a genuine bridge state admitted by both transition laws.
Therefore it cannot be detected by either one-sided observer or by the final
outer relation after middle elimination.

This is the categorical form of an emergent coherencer residue. It is not an
extra probe appended by hand. It is generated by the fiber product of the two
source-derived transition relations.

Three cases are now exact:

1. \(\mathcal E_X=0\): composition is transverse at the cutoff, and no hidden
   bridge observer is required;
2. \(\mathcal E_X\ne0\) with constant dimension: composition is clean but
   carries an excess determinant or orientation line that must remain typed;
3. varying or unbounded \(\dim\mathcal E_X\): the proposed finite
   coherencer does not survive completion without an additional bridge
   sector.

The scalar functional equation can hold in all three cases because scalar
outer readout kills \(\mathcal E_X\) by definition. Thus scalar agreement
cannot distinguish transverse sewing from sewing with hidden excess.

The first decisive calculation for the actual theta bridge is now finite:
construct \(L_{+,X}\) and \(L_{-,X}\) from the two source integrals and compute
\(\mathcal E_X\) before taking a determinant. A nonzero vector in
\(\mathcal E_X\) is the smallest possible finite witness that the apparent
two-sector operator is missing a third, bridge-internal observer.

There is an important restraint. If \(L_{+,X}\) and \(L_{-,X}\) are graphs of
ordinary maps, then

\[
(0,m)\in L_{+,X}
\]

already forces \(m=0\), and therefore \(\mathcal E_X=0\). Excess cannot be
manufactured by rhetoric or by replacing a map with a relation after the
fact.

A nontrivial bridge observer can arise only when the source transition is
genuinely relational. Relevant mechanisms include:

- a distributional trace with a multivalued closure;
- a quotient whose eliminated kernel survives in the middle carrier;
- a nonclosed-range completion;
- or a clean canonical relation with positive excess.

This places the earlier additive-to-idelic trace obstruction in the correct
position. Since restriction from additive \(L^2(\mathbb A)\) to the
additive-Haar-null idelic locus is not a Hilbert map, the required theta/Tate
bridge is a legitimate candidate for relational excess. It is not evidence
that the excess is nonzero. That must still be computed from the rigged trace
correspondence.

When \(\mathcal E_X\) is finite dimensional, its determinant line

\[
\det\mathcal E_X
\]

is the natural carrier of the clean-composition anomaly. This supplies a
precise possible relationship among the bridge observer, the determinant
line, and the earlier coherence residue. The identification is conditional:
the primitive and square anomaly lines may map into
\(\det\mathcal E_X\), but equality cannot be asserted until the actual
transition relations and their excess are constructed.

## Aspect's completed sewing map has zero algebraic excess

The available source bridge is more rigid than the general relational model.
Let

\[
\tau:
\mathcal S(\mathbb A)
\longrightarrow
\operatorname{Ran}\tau
\]

be the idelic trace on Schwartz--Bruhat sources. On its injective source
range, Aspect's forward and reverse maps are

\[
J_0(\tau\phi)=\tau(\mathcal F\phi)
\]

and

\[
J_0^{-1}(\tau\phi)=\tau(\mathcal F^{-1}\phi).
\]

Injectivity of \(\tau\) makes both formulas representative-independent.
Fourier inversion makes them mutually inverse. Therefore their transition
relations are graphs of honest maps, and the algebraic excess space is

\[
\mathcal E_{\mathrm{alg}}=0.
\]

The general excess construction remains valid, but it does not produce a new
finite observer for the currently defined sewing bridge.

Completion could create a multivalued closure only if there were a sequence
\(\phi_n\) for which

\[
\tau\phi_n\longrightarrow0
\]

while

\[
\tau(\mathcal F\phi_n)\longrightarrow y\ne0.
\]

That is exactly failure of closability in the chosen trace topology. The
Fourier-saturated pro-Gram topology rules out this mechanism: by construction
the sewing action is isometric in every saturated seminorm. Hence zero input
limit forces zero Fourier-output limit, and the completed graph remains
single valued.

This closes the most immediate third-observer hypothesis:

- the middle theta/Mellin chart is necessary because the two Euler charts do
  not overlap;
- its admitted forward and reverse transports have no algebraic excess;
- Fourier-saturated completion does not generate multivalued excess;
- therefore the missing RH observer is not the kernel of composing these
  sewing maps.

The unresolved arrow occurs after completed sewing:

\[
\operatorname{Ran}\tau
\longrightarrow
\mathcal B_{\mathrm{Green/response}}.
\]

It must send the trace presentation into the rigged boundary object carrying
the primitive coorientation, relative response, Green form, and maximal
neutral relation. Aspect's bridge supplies source-derived continuation, but
not this operator-valued boundary incidence.

The next falsifier should therefore stop testing the already invertible
sewing square. At the algebraic Schwartz--Bruhat level, injectivity already
makes the boundary packet representative-independent whenever its source map
exists. The live test is continuity: construct a sequence with

\[
\tau\phi_n\longrightarrow0
\]

in the completed trace topology and ask whether the proposed Green/response
packet also tends to zero in its graph topology. A nonzero limiting packet is
the exact witness that boundary incidence fails to descend through completed
trace sewing, even though scalar and algebraic sewing remain exact.

## The local idelic trace splits off exactly two boundary observers

The missing trace-to-boundary incidence is already visible at one finite
place. Normalize multiplicative Haar measure by

\[
\mu^\times(\mathbb Z_p^\times)=1.
\]

Every valuation shell

\[
p^k\mathbb Z_p^\times
\]

then has multiplicative measure one.

Let \(f\in\mathcal S(\mathbb Q_p)\). If \(f(0)=c\ne0\), local constancy gives
an integer \(N\) such that

\[
f(x)=c
\]

for every \(v_p(x)\ge N\). Therefore

\[
\int_{\mathbb Q_p^\times}|f(x)|^2\,d^\times x
\ge
\sum_{k\ge N}|c|^2
=\infty.
\]

Conversely, if \(f(0)=0\), local constancy makes \(f\) vanish on all
sufficiently deep shells. Compact support removes all sufficiently negative
shells. Its multiplicative trace then has finite shell support and belongs to
\(L^2(\mathbb Q_p^\times,d^\times x)\).

Hence the exact criterion is

\[
f|_{\mathbb Q_p^\times}\in L^2(d^\times x)
\quad\Longleftrightarrow\quad
\epsilon_p(f)=f(0)=0.
\]

Applying the same criterion after Fourier transform and using self-dual Haar
normalization gives

\[
(\mathcal F_pf)|_{\mathbb Q_p^\times}\in L^2(d^\times x)
\quad\Longleftrightarrow\quad
\mu_p(f)=\int_{\mathbb Q_p}f(x)\,dx=0.
\]

Therefore the largest Fourier-stable Schwartz--Bruhat subspace whose direct
and Fourier traces are both multiplicatively square integrable is

\[
\mathcal S_p^\circ
=
\ker\epsilon_p
\cap
\ker\mu_p.
\]

It has codimension two, and the quotient map is

\[
\mathcal S(\mathbb Q_p)/\mathcal S_p^\circ
\cong
\mathbb C^2,
\qquad
[f]\longmapsto
(\epsilon_p(f),\mu_p(f)).
\]

Its dual observer plane is

\[
\operatorname{span}\{\epsilon_p,\mu_p\}.
\]

This is a source-derived short exact boundary decomposition. The two endpoint
observers are not optional rows appended to an idelic Hilbert trace. Their
dual carrier directions are precisely the quotient directions excluded from
that trace by multiplicative square integrability.

## Consequence for the completed sewing matrix

Aspect's algebraic sewing formulas remain correct on the injective trace
range. But a finite matrix equipped only with an idelic \(L^2\) Gram metric
can represent at most the common core \(\mathcal S_p^\circ\). It necessarily
misses both endpoint quotient directions.

The minimum local completed carrier is therefore an extension

\[
0
\longrightarrow
\mathcal S_p^\circ
\longrightarrow
\mathcal S(\mathbb Q_p)
\xrightarrow{(\epsilon_p,\mu_p)}
\mathbb C^2
\longrightarrow
0,
\]

with Fourier acting on the quotient by

\[
B=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

Globally, the unramified vacuum has nonzero endpoint germ at almost every
prime. The corresponding construction must therefore be relative to that
vacuum or use a restricted product of these extensions; it cannot form an
ordinary Hilbert sum of all endpoint coordinates.

This identifies the exact additional data required by Aspect's finite matrix:

1. an interior trace basis drawn from \(\mathcal S_p^\circ\);
2. the two separately typed quotient coordinates
   \((\epsilon_p,\mu_p)\);
3. the extension or graph projection joining the core to the quotient; and
4. a relative-vacuum law for restricted-product assembly.

A convenient finite Fourier matrix on the interior trace core cannot test the
boundary extension. It can be perfectly unitary while omitting the two
directions on which primitive coorientation and endpoint completion live.

## Fourier-equivariant boundary splittings are nonunique

The short exact sequence has continuous linear splittings, and averaging over
the finite Fourier orbit produces Fourier-equivariant splittings. This
existence does not make the graph projection canonical.

Assume the standard self-dual finite-place normalization

\[
\mathcal F_p1_{p^n\mathbb Z_p}
=
p^{-n}1_{p^{-n}\mathbb Z_p}.
\]

For \(n\ge1\), define

\[
h_n^+
=
1_{p^n\mathbb Z_p}
+
p^{-n}1_{p^{-n}\mathbb Z_p}
-
(1+p^{-n})1_{\mathbb Z_p}.
\]

Then

\[
\mathcal F_ph_n^+=h_n^+,
\qquad
\epsilon_p(h_n^+)=0,
\qquad
\mu_p(h_n^+)=0.
\]

Thus \(h_n^+\) is a nonzero Fourier-even vector in the interior trace core.

For the odd character, put

\[
g_n
=
1_{p^n\mathbb Z_p}
-
p^{-n}1_{p^{-n}\mathbb Z_p}.
\]

It satisfies

\[
\mathcal F_pg_n=-g_n,
\]

and

\[
\epsilon_p(g_n)=1-p^{-n},
\qquad
\mu_p(g_n)=-(1-p^{-n}).
\]

For distinct positive integers \(m,n\), the combination

\[
h_{n,m}^-
=
\frac{g_n}{1-p^{-n}}
-
\frac{g_m}{1-p^{-m}}
\]

is nonzero, Fourier-odd, and belongs to
\(\mathcal S_p^\circ\).

Consequently both Fourier characters occur nontrivially inside the kernel of
the boundary quotient. A Fourier-equivariant lift of either quotient
character may be shifted by the corresponding \(h^+\) or \(h^-\) without
changing:

- its endpoint coordinates;
- its Fourier character;
- or the quotient exchange matrix \(B\).

The equivariant graph projections therefore form an affine space over

\[
\operatorname{Hom}_{C_4}
\left(
\mathbb C^2,
\mathcal S_p^\circ
\right),
\]

which is already nontrivial at one prime.

This is the exact remaining local selector problem. The quotient carrier and
its Fourier action are canonical; its embedding back into the source is not.
A proposed Green/response boundary map that depends on a chosen splitting
must either:

1. prove invariance under all core shifts \(h_n^+\) and \(h_{n,m}^-\); or
2. derive one splitting from an additional source law such as support,
   valuation filtration, or a declared minimal graph condition.

The cheapest finite falsifier is to evaluate the proposed boundary packet on
two equivariant lifts differing by one explicit core vector above. If the
packets differ while all quotient data agree, the construction depends on an
unauthorized graph projection.

## Minimum conductor selects the unramified local splitting

The local Tate source carries more structure than Fourier equivariance alone.
At an unramified finite place it specifies:

- invariance under multiplication by \(\mathbb Z_p^\times\);
- the self-dual lattice \(\mathbb Z_p\);
- and its conductor filtration by the balls \(p^n\mathbb Z_p\).

In the Fourier-even quotient character, the unique unit-invariant source with
both support and Fourier support contained in \(\mathbb Z_p\) is

\[
e_p^+=1_{\mathbb Z_p}.
\]

It satisfies

\[
\mathcal F_pe_p^+=e_p^+,
\qquad
(\epsilon_p(e_p^+),\mu_p(e_p^+))=(1,1).
\]

No Fourier-odd source exists at this conductor. At the first enlarged radial
conductor, define

\[
e_p^-
=
\frac{
1_{p\mathbb Z_p}
-
p^{-1}1_{p^{-1}\mathbb Z_p}
}{
1-p^{-1}
}.
\]

Then

\[
\mathcal F_pe_p^-=-e_p^-,
\qquad
(\epsilon_p(e_p^-),\mu_p(e_p^-))=(1,-1).
\]

Inside the unit-invariant radial space generated by

\[
1_{p\mathbb Z_p},
\qquad
1_{\mathbb Z_p},
\qquad
1_{p^{-1}\mathbb Z_p},
\]

the Fourier-odd eigenspace is one dimensional. Hence \(e_p^-\) is the unique
normalized odd lift at minimum conductor.

The resulting splitting is explicit:

\[
\sigma_p(a,b)
=
\frac{a+b}{2}e_p^+
+
\frac{a-b}{2}e_p^-.
\]

It obeys

\[
(\epsilon_p,\mu_p)\sigma_p=I_{\mathbb C^2}
\]

and intertwines the quotient exchange \(B\) with additive Fourier transform:

\[
\mathcal F_p\sigma_p
=
\sigma_pB.
\]

This removes the infinite-dimensional splitting ambiguity after imposing
three independently source-defined conditions: unit invariance, Fourier
character, and minimum conductor. The previously constructed core shifts are
excluded because they require a larger conductor than the selected lift.

The splitting is also restricted-product compatible. The even vector
\(e_p^+\) is the standard unramified vacuum at almost every prime. The odd
vector \(e_p^-\) is a typed local excitation. Finite odd excitations therefore
belong to the algebraic restricted product without changing its vacuum.

This is a genuine advance, but it does not yet complete the RH boundary
operator. The primitive Fock current is an infinite distributional
superposition of these odd local excitations. The remaining theorem is that
the minimum-conductor splittings assemble continuously in the arithmetic
test rigging and that the resulting odd distribution has the required
Green/response incidence.

The immediate finite gate is now concrete: use \(e_p^+\) and \(e_p^-\), not
an arbitrary discrete Fourier basis, as the first two local columns of the
completed sewing matrix. Any source-derived additional columns must lie in
\(\mathcal S_p^\circ\) and preserve the conductor filtration. The matrix
must reproduce the quotient exchange exactly before uncertainty or optical
calibration is considered.

## The minimum-conductor odd lift gives the local response symbol

Use the local multiplicative zeta integral

\[
\mathcal Z_p(f,s)
=
\int_{\mathbb Q_p^\times}
f(x)|x|_p^s\,d^\times x.
\]

With unit-shell normalization, the even vacuum gives

\[
\mathcal Z_p(e_p^+,s)
=
\sum_{k\ge0}p^{-ks}
=
\frac{1}{1-p^{-s}}.
\]

For \(e_p^-\), direct shell summation gives

\[
\mathcal Z_p(e_p^-,s)
=
\frac{
p^{-s}-p^{s-1}
}{
(1-p^{-1})(1-p^{-s})
}.
\]

Therefore the odd-to-even readout ratio is

\[
\rho_p(s)
=
\frac{\mathcal Z_p(e_p^-,s)}
{\mathcal Z_p(e_p^+,s)}
=
\frac{p^{-s}-p^{s-1}}{1-p^{-1}}.
\]

It has the exact reciprocal character

\[
\rho_p(1-s)=-\rho_p(s).
\]

In the centered coordinate \(s=\tfrac12+z\),

\[
\rho_p\left(\frac12+z\right)
=
-\frac{
2p^{-1/2}\sinh(z\log p)
}{
1-p^{-1}
}.
\]

Thus the minimum-conductor odd boundary lift produces the native
Fourier-odd response multiplier before any scalar completion is fitted. Its
normal derivative at the seam is

\[
\rho_p'\left(\frac12\right)
=
-\frac{
2(\log p)p^{-1/2}
}{
1-p^{-1}
}.
\]

The leading term is the primitive orientation coefficient
\((\log p)p^{-1/2}\). The factor

\[
\frac{1}{1-p^{-1}}
\]

is the exact minimum-conductor normalization required to give the odd lift
boundary coordinates \((1,-1)\). It must not be dropped when comparing the
response derivative with the primitive asymptotic coefficient.

This closes the local algebraic incidence that was previously missing:

1. the even lift supplies the local Euler port;
2. the odd lift supplies its reciprocal relative-response port;
3. ordered endpoint observers fix their coorientation;
4. the Mellin ratio produces the exact odd response symbol.

The construction uses only the self-dual lattice, unit invariance, minimum
conductor, Fourier character, and multiplicative Mellin readout. It does not
inspect global zeros.

## New global gate

The local response symbols are distributional at prime infinity. Their seam
derivatives have size

\[
\frac{(\log p)p^{-1/2}}{1-p^{-1}},
\]

so they do not form a Hilbert vector across primes. This is exactly the
primitive dual grade already identified.

The next theorem is no longer the discovery of a local response row. It is
the construction of the global vector-valued sum of the \(\rho_p\) inside the
Fourier-saturated arithmetic rigging, together with:

1. the prime-square determinant-line channel;
2. the archimedean odd response;
3. the seam graph current;
4. and the completed Green boundary pairing.

The finite falsifier is explicit. At each prime, derive the two local columns
from \(e_p^+\) and \(e_p^-\), compute their shellwise Mellin integrals, and
compare the relative column with \(\rho_p(s)\). Any residual means that the
proposed trace-to-response map is not the minimum-conductor Tate incidence.

## The global odd response is not tempered

On the seam, put \(z=it\). The local response becomes

\[
\rho_p\left(\frac12+it\right)
=
-\frac{
2i\,p^{-1/2}\sin(t\log p)
}{
1-p^{-1}
}.
\]

Its Fourier-side carrier is therefore proportional to the signed discrete
measure

\[
\nu
=
\sum_p
\frac{p^{-1/2}}{1-p^{-1}}
\left(
\delta_{\log p}
-
\delta_{-\log p}
\right).
\]

On the positive-frequency interval \([0,U]\), its total variation has the
same order as

\[
\sum_{p\le e^U}p^{-1/2},
\]

and the prime number theorem with partial summation gives

\[
\sum_{p\le e^U}p^{-1/2}
\sim
\frac{2e^{U/2}}{U}.
\]

Thus it grows exponentially in \(U\), up to the prime-density factor. A
positive-frequency test can isolate these coefficients, so cancellation with
the negative-frequency part does not make \(\nu\) tempered.

The seam derivative is still more singular: it multiplies each coefficient
by \(\log p\). Thus neither the response nor its primitive normal derivative
belongs to the ordinary Schwartz dual in the spectral variable.

They do act on test functions whose Fourier transforms have sufficient
two-sided exponential decay. For example, a bound stronger than

\[
|\widehat\varphi(u)|
\le
C e^{-(1/2+\varepsilon)|u|}
\]

for some \(\varepsilon>0\) makes the prime pairing absolutely convergent.
This recovers the previously identified exponential primitive rigging from
the explicit minimum-conductor response symbol.

## The seam carrier is naturally hyperfunctional

Let \(\Sigma\) denote the critical seam inside a complex neighborhood \(M\).
An analytic functional of the growth above is naturally represented as a
hyperfunction boundary value. In one complex dimension, its carrier has the
local-cohomology form

\[
\mathcal B_\Sigma
\simeq
H^1_\Sigma(M,\mathcal O).
\]

Equivalently, it is represented by holomorphic data on the two sides of the
seam, modulo addition of a common holomorphic continuation. This is the exact
mathematical form of the two-sector relationship:

1. the direct representative approaches \(\Sigma\) from one side;
2. the reciprocal representative approaches from the other;
3. their difference modulo common continuation is the seam class.

The bridge chart \(M\) is essential in this description. It supplies the
ambient holomorphic object relative to which the two boundary values are
compared. The seam coherencer is not an extra scalar port; it is the
local-cohomology class of the two-sided response.

This also explains how a class can appear only at completion. At finite prime
cutoff,

\[
R_X(z)
=
\sum_{p\le X}
\rho_p\left(\frac12+z\right)
\]

is an entire odd function. Its seam hyperfunction class is therefore
cohomologically trivial when the direct and reciprocal representatives are
aligned as restrictions of this same entire function. The infinite family
does not converge normally in any neighborhood of the seam. A nontrivial
boundary class can arise from this failure of normal convergence even though
every finite cutoff extends holomorphically.

That is precisely emergent cohomology at infinity in analytic form. It is not
finite path holonomy and not relational excess of Aspect's invertible sewing
map.

## Hyperfunction completion gate

The next source theorem must construct the completed pair of holomorphic
representatives and prove that their boundary-value class:

1. contains the minimum-conductor local symbols \(\rho_p\);
2. retains the primitive and square grades separately;
3. is compatible with the archimedean response;
4. is continuous in the exponential test rigging;
5. carries the ordered coorientation fixed by
   \((\epsilon_p,\mu_p)\); and
6. enters the Green boundary relation before scalar readout.

The cheapest falsifier is a test function with admissible exponential decay
for which the direct and reciprocal cutoff pairings fail to converge to the
declared boundary values. A second falsifier is a common holomorphic shift
that changes the proposed physical response: a true hyperfunction
construction must be invariant under changing representatives by such a
shift.

Even successful construction of this seam class would not prove RH. It would
finally place the primitive relative response in its correct completed
category and make the maximal-neutral boundary question well typed.

## The local response is a normalized sewing defect

The local Tate transition is

\[
\gamma_p(s)
=
\frac{1-p^{-s}}{1-p^{s-1}}.
\]

The minimum-conductor response satisfies the exact identity

\[
\rho_p(s)
=
\frac{1-p^{s-1}}{1-p^{-1}}
\left(
1-\gamma_p(s)
\right).
\]

Thus \(\rho_p\) is not an unrelated odd observable. It is a
conductor-normalized defect of the local sewing map from the identity.

This corrects the first global formulation. Sewing factors compose
multiplicatively, so their defects do not compose by ordinary addition. Put

\[
d_p=1-\gamma_p.
\]

For two primes,

\[
1-\gamma_p\gamma_q
=
d_p+\gamma_p d_q
=
d_q+\gamma_q d_p.
\]

The two ordered expressions agree because they are factorizations of the same
product defect. Their equality is the finite coherence square. The transport
factor \(\gamma_p\) or \(\gamma_q\) is essential.

By contrast, the naïve additive response gives

\[
d_p+d_q.
\]

Its difference from the correctly transported defect is

\[
d_pd_q.
\]

This is the smallest mixed \(pq\) relationship. It is composite rather than
primitive, exactly as required by the positive-Fock grammar. Deleting it
breaks multiplicative sewing; promoting it to a new primitive erases Euler
typing.

For a finite prime packet \(X\), the correct global defect is

\[
d_X
=
1-\prod_{p\in X}\gamma_p.
\]

Adding a prime obeys

\[
d_{X\cup\{p\}}
=
d_X
+
\left(
\prod_{q\in X}\gamma_q
\right)d_p.
\]

This is a multiplicative cocycle or transported Writer effect. The additive
primitive current is its tangent or connected logarithmic shadow, not the
full response law.

## Revised hyperfunction target

The non-tempered sum of the local \(\rho_p\) remains the correct carrier for
the linearized primitive response. It must not be identified with the full
completed scattering defect.

The global boundary object needs two coupled levels:

1. a cocycle-valued hyperfunction retaining the finite product transport;
2. its connected or infinitesimal hyperfunction carrying the primitive,
   square, and higher cumulant grades.

The order-three determinant belongs to the second level. The maximal neutral
boundary relation must be compatible with the first. Passing directly to the
connected logarithm can forget zeros or branch data of the multiplicative
transport, while staying only at the product level hides the typed primitive
and square currents.

The two-prime falsifier is now exact and minimal. For independently derived
local responses, compare the proposed packet increment with

\[
d_p+\gamma_p d_q.
\]

If it returns \(d_p+d_q\), the missing residual \(d_pd_q\) proves that the
compiler treated a transported cocycle as an additive ledger. If it inserts
an independent \(pq\) primitive to repair the residual, it violates the
source Fock grammar.

## The cocycle has an exact affine transport lift

Package the local sewing factor and its response defect as

\[
\mathcal A_p(s)
=
\begin{pmatrix}
\gamma_p(s)&1-\gamma_p(s)\\
0&1
\end{pmatrix}.
\]

Matrix multiplication gives

\[
\mathcal A_p\mathcal A_q
=
\begin{pmatrix}
\gamma_p\gamma_q&
d_p+\gamma_p d_q\\
0&1
\end{pmatrix}.
\]

Thus the complete transported-response law is ordinary composition in the
affine group. The vector

\[
\begin{pmatrix}1\\1\end{pmatrix}
\]

is fixed because \(\gamma_p+d_p=1\). The source value remains fixed while the
relative coordinate is transported; no dynamical equation for the source
amplitude has been invented.

Reciprocal sewing is also exact. Since

\[
\gamma_p(1-s)=\gamma_p(s)^{-1},
\]

we have

\[
\mathcal A_p(1-s)
=
\mathcal A_p(s)^{-1}.
\]

This is the finite-dimensional route-effect form of the local Tate
comparison.

There is also a decisive no-go. Let

\[
P=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]

Then

\[
P^{-1}\mathcal A_pP
=
\begin{pmatrix}
\gamma_p&0\\
0&1
\end{pmatrix}.
\]

Therefore the finite affine response cocycle is a coboundary. It restores the
ordered input--response typing but carries no finite spectral information
beyond \(\gamma_p\).

Any RH-strength gain must consequently arise from a global obstruction to
performing this trivialization compatibly with:

- restricted-product completion;
- the primitive and square dual currents;
- the archimedean response;
- and the determinant-line normalization.

If the same constant \(P\) acts continuously on the fully completed boundary
object and preserves every typed channel, the affine lift adds no information
beyond the scalar Tate sewing. If \(P\) fails to extend, the failure must be
recorded as a typed completion anomaly rather than interpreted as automatic
positivity.

## The affine coboundary fails the linear arithmetic grade filtration

The diagonalizing matrix \(P\) adds the fixed source coordinate to the
relative response coordinate. At one prime this is harmless because both
coordinates lie in a finite two-dimensional space. Across all primes they
have different regularity.

The global augmentation coefficient is

\[
a_p=1.
\]

In the weighted dual grade \(\mathcal H_{-\delta}\), it satisfies

\[
\|a\|_{\mathcal H_{-\delta}}^2
=
\sum_p p^{-2\delta}.
\]

This is finite only when

\[
\delta>\frac12.
\]

The primitive response coefficient

\[
b_p=\frac{\log p}{\sqrt p}
\]

belongs to \(\mathcal H_{-\delta}\) for every \(\delta>0\).

Therefore, throughout the interval

\[
0<\delta\le\frac12,
\]

the primitive response is an admitted dual coordinate while the augmentation
translation used by \(P\) is not. The local coboundary does not define a
grade-preserving automorphism of the full arithmetic Hilbert scale.

Both coordinates belong to the coarse strong dual
\(\mathcal S_P'\), so \(P\) can be written after forgetting the filtration.
That does not authorize it in the distinction-preserving completion. It
identifies channels whose threshold grades are different.

In the category of linearly filtered vector spaces, the affine response
cocycle is:

- algebraically trivial;
- trivial after coarse dual completion;
- but not trivialized by the same map in the filtered rigged category.

The provisional surviving object is a filtered extension class. Its finite
matrices split, yet the linear splitting crosses the half-order augmentation
boundary and cannot be transported through every vector grade. The affine
audit below shows why this is not the final category.

This supplies an exact interpretation of the primitive anomaly without
claiming positivity. The primitive current records the obstruction to
diagonalizing source and response while preserving the arithmetic regularity
filtration.

The minimal compiler test is deletion of the filtration. If a proposed
trivialization works only after embedding augmentation and primitive response
into the undifferentiated strong dual, it has erased the source distinction.
A valid trivialization must act continuously at every admitted positive
grade and commute with the grade embeddings. The constant matrix \(P\) fails
that test for \(0<\delta\le\tfrac12\).

## The obstruction has a half-order persistence interval

For a coefficient packet \(c\), define its dual-grade birth threshold by

\[
\beta(c)
=
\inf
\left\{
\delta>0:
c\in\mathcal H_{-\delta}
\right\}.
\]

The primitive and augmentation channels satisfy

\[
\beta(b)=0,
\qquad
\beta(a)=\frac12,
\]

with neither endpoint attained. The primitive response is therefore present
throughout the positive-grade tower, while the augmentation translation
appears only after the half-order threshold.

The attempted affine trivialization has the persistence pattern:

- for \(\delta>\tfrac12\), both channels exist and the finite coboundary
  matrix \(P\) is defined;
- for \(0<\delta\le\tfrac12\), the primitive response exists but its proposed
  augmentation mate does not.

Thus the filtered obstruction is supported on the interval

\[
\left(0,\frac12\right].
\]

This gives the half-unit a source-summability meaning independent of the
zero set. It is the exact distance between the birth of the primitive odd
response and the birth of the constant augmentation needed to trivialize it.

The result does not orient the completed scalar section. Signed hostile prime
weights can preserve the same birth thresholds. At this stage it supplies a
canonical location and duration for the obstruction to a linear
trivialization.

## The restricted-product vacuum trivializes the affine cocycle

The augmentation sequence is not an ordinary tangent excitation. It is the
source-selected unramified vacuum at almost every prime. The arithmetic state
space is therefore naturally a pointed affine restricted product rather than
a vector space containing the vacuum as a square-summable element.

Let \(x_0\) denote the global vacuum section and write an admitted state as

\[
x=x_0+y,
\]

where \(y\) belongs to the declared finite-excitation or completed tangent
rigging. The affine Tate action has the form

\[
x
\longmapsto
\gamma x+(1-\gamma)x_0.
\]

Subtracting the fixed source point gives

\[
y
\longmapsto
\gamma y.
\]

This centering is globally meaningful even when \(x_0\) is not an element of
the tangent Hilbert space. A basepoint need not satisfy the summability law
imposed on differences from that basepoint.

Thus the matrix \(P\) should not be interpreted as a grade-preserving linear
automorphism that adds an augmentation vector to a primitive vector. It is
the coordinate change from a pointed affine restricted product to its tangent
space. In that category the cocycle is canonically trivialized by the
unramified vacuum.

The half-order persistence interval remains a correct diagnosis of why the
vacuum cannot be promoted to an ordinary tangent vector. It is not an
obstruction to affine centering, and therefore not an RH-bearing extension
class.

This closes another tempting route:

- the local response defect is source-derived;
- its transported cocycle law is exact;
- the unramified vacuum supplies a canonical affine origin;
- centering reduces the response transport to the original multiplicative
  Tate factor.

Any hostile source preserving the same pointed affine architecture inherits
the same reduction. RH-strength information must again enter through the
operator-valued boundary incidence, completion domain, or determinant
readout—not through the affine defect cocycle itself.

## The minimum-conductor Gram derives the Schatten-three threshold

Although the affine cocycle adds no new spectral law, the selected local lifts
carry a nontrivial source metric. Use additive self-dual Haar measure with

\[
\operatorname{vol}(\mathbb Z_p)=1.
\]

The even vacuum has

\[
\|e_p^+\|_2^2=1.
\]

Since

\[
p\mathbb Z_p
\subset
\mathbb Z_p
\subset
p^{-1}\mathbb Z_p,
\]

the even--odd inner product is

\[
\langle e_p^+,e_p^-\rangle
=
\frac{
\operatorname{vol}(p\mathbb Z_p)
-
p^{-1}\operatorname{vol}(\mathbb Z_p)
}{
1-p^{-1}
}
=0.
\]

The odd norm is

\[
\|e_p^-\|_2^2
=
\frac{
\operatorname{vol}(p\mathbb Z_p)
-
2p^{-1}\operatorname{vol}(p\mathbb Z_p)
+
p^{-2}\operatorname{vol}(p^{-1}\mathbb Z_p)
}{
(1-p^{-1})^2
}
=
\frac{2}{p-1}.
\]

Thus the source Gram matrix in the ordered minimum-conductor basis is

\[
G_p
=
\begin{pmatrix}
1&0\\
0&\dfrac{2}{p-1}
\end{pmatrix}.
\]

The odd singular scale is therefore

\[
\sigma_p
=
\sqrt{\frac{2}{p-1}}
\asymp
p^{-1/2}.
\]

Its connected Fock degrees have asymptotic scales

\[
\sigma_p^k
\asymp
p^{-k/2}.
\]

Consequently:

- degree one is not square summable across primes but belongs to every
  \(\ell^q\) with \(q>2\);
- degree two is square summable but not absolutely summable;
- every degree \(k\ge3\) is absolutely summable.

This recovers the primitive, square, and connected-tail Schatten filtration
directly from the additive Gram norm of the canonical odd boundary lift. The
threshold is no longer inferred only from the scalar gamma expansion.

The cycle factor \(1/k\) remains a separate Fock symmetry normalization. It
changes coefficients within a fixed degree but not these summability
thresholds.

This gives the minimum-conductor splitting a durable role even though its
affine defect cocycle is trivial: it constructs the local metric origin of the
global order-three regularization.

## The oriented form and the metric define the true local quarter-turn

The earlier matrix

\[
\Omega_p=QB
\]

should be typed as the canonical alternating form on the ordered quotient
ports. It is not by itself the metric-normalized complex structure.

In the Fourier-character basis \((e_p^+,e_p^-)\), put

\[
g_p=\frac{2}{p-1}.
\]

The source Gram metric is

\[
G_p=
\begin{pmatrix}
1&0\\
0&g_p
\end{pmatrix},
\]

and the normalized alternating form may be written

\[
\Omega_0=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

The unique orientation-compatible complex structure obtained from this pair
is

\[
\mathcal J_p
=
\sqrt{g_p}\,G_p^{-1}\Omega_0
=
\begin{pmatrix}
0&-\sqrt{g_p}\\
1/\sqrt{g_p}&0
\end{pmatrix}.
\]

It satisfies

\[
\mathcal J_p^2=-I,
\]

\[
\mathcal J_p^*G_p\mathcal J_p=G_p,
\]

and

\[
\mathcal J_p^*G_p+G_p\mathcal J_p=0.
\]

Thus \(\mathcal J_p\) is the actual source-metric quarter-turn. Its two
off-diagonal scales are reciprocal:

\[
\sqrt{g_p}
\asymp
p^{-1/2},
\qquad
\frac{1}{\sqrt{g_p}}
\asymp
p^{1/2}.
\]

The contracting and expanding valuation sectors are therefore paired inside
one metric-compatible local complex structure. Neither scale can be removed
without destroying \(\mathcal J_p^2=-I\).

Fourier acts diagonally in this basis:

\[
F_p=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

It reverses the quarter-turn:

\[
F_p\mathcal J_pF_p=-\mathcal J_p.
\]

This is the precise Fourier-odd orientation law required by the relative
response.

The distinction between \(\Omega_p\) and \(\mathcal J_p\) matters globally.
The alternating form may descend as a distributional pairing even when the
metric-normalized endomorphism does not act boundedly on one common Hilbert
completion. Any Clifford formulation must therefore state whether it uses:

1. the orientation form;
2. the positive Gram metric;
3. or the induced complex structure.

Transporting one as though it were another repeats the forbidden Riesz
collapse between primitive state and primitive covector.

## The incidence operator, not the normalized quarter-turn, carries det-three

Two operators must not be conflated.

The metric-normalized complex structure \(\mathcal J_p\) is an isometry. In
normalized even and odd coordinates, its off-diagonal singular value is one.
The direct sum of a full exchange at every prime is not a restricted
polarization change; its off-diagonal Hilbert--Schmidt sum already diverges by
counting primes.

The minimum-conductor incidence is different. It sends a unit even source
coordinate to the physical unnormalized odd vector:

\[
K_p:
\mathbb C e_p^+
\longrightarrow
\mathbb C e_p^-.
\]

Its singular value is

\[
\sigma_p
=
\|e_p^-\|_2
=
\sqrt{\frac{2}{p-1}}.
\]

Consequently the global diagonal incidence \(K=\bigoplus_pK_p\) satisfies

\[
K\in\mathcal S_q
\quad
(q>2),
\qquad
K\notin\mathcal S_2.
\]

This is the operator whose local Gram data authorize an order-three
regularized determinant. Its quadratic connected amplitude is square
summable but not trace summable, and its cubic and higher amplitudes are trace
summable.

If the eventual source-derived Bogoliubov or boundary sewing operator has
\(K\) as its polarization-changing block, the ordinary Fock implementability
gate fails exactly at the primitive grade. That conclusion is conditional on
constructing the full block operator. It must not be inferred merely from the
existence of \(\mathcal J_p\).

The durable result is therefore narrower:

1. \(\mathcal J_p\) supplies the local metric-compatible orientation;
2. \(K_p\) supplies the physical minimum-conductor incidence;
3. only \(K=\bigoplus_pK_p\) carries the source-derived Schatten-three
   filtration.

This still supplies provenance rather than RH positivity. Hostile prime
weights with the same norm profile can reproduce the filtration. The
unresolved law must use the oriented response and archimedean sewing, not
only the Schatten class of \(K\).

## Ordinary Clifford doubling destroys the cubic determinant grade

The incidence \(K_p\) is rectangular between the even and odd local ports.
The most obvious self-adjoint completion is

\[
\mathcal D_p
=
\begin{pmatrix}
0&K_p^*\\
K_p&0
\end{pmatrix}.
\]

Its nonzero eigenvalues are

\[
\{+\sigma_p,-\sigma_p\}.
\]

The local order-three regularized determinant is therefore

\[
\det_3(I+\mathcal D_p)
=
(1-\sigma_p^2)e^{\sigma_p^2}.
\]

Its logarithm is

\[
\log(1-\sigma_p^2)+\sigma_p^2
=
-\frac{\sigma_p^4}{2}
-
\frac{\sigma_p^6}{3}
-
\cdots.
\]

All odd connected degrees cancel between the two spectral sheets. The cubic
term is absent. Hence ordinary self-adjoint doubling converts the
source-authorized order-three filtration into an even filtration beginning at
degree four.

There is also an immediate one-prime falsifier. At \(p=3\),

\[
\sigma_3^2=\frac{2}{3-1}=1,
\]

so

\[
\det_3(I+\mathcal D_3)=0.
\]

The local Tate transition is invertible. Therefore it cannot be represented
by this raw self-adjoint doubled determinant.

The skew Clifford completion

\[
\mathcal C_p
=
\begin{pmatrix}
0&-K_p^*\\
K_p&0
\end{pmatrix}
\]

avoids the spurious \(p=3\) zero. Its spectrum is

\[
\{+i\sigma_p,-i\sigma_p\}.
\]

But its paired determinant still has only even connected powers:

\[
\log\det_3(I+\mathcal C_p)
=
\log(1+\sigma_p^2)-\sigma_p^2
=
-\frac{\sigma_p^4}{2}
+
\frac{\sigma_p^6}{3}
-
\cdots.
\]

Thus skew doubling also erases the cubic orientation channel.

## The determinant must remain chiral

The source determinant cannot be the ordinary determinant of a carrier in
which the even-to-odd incidence and its adjoint have already been aggregated.
That aggregation pairs every singular value with its opposite and forgets
the odd Fock character.

The viable determinant object must retain one of the following equivalent
types before any final real or positive doubling:

1. a chiral determinant line for \(K:\mathcal H_+\to\mathcal H_-\);
2. an oriented relative determinant of the two polarizations;
3. a graded determinant or superdeterminant with separately typed sheets;
4. a Pfaffian line together with the missing orientation data.

The adjoint sheet remains necessary for Green balance and reality. It must
not be inserted into the determinant in a way that cancels all odd connected
grades.

This supplies a finite compiler rule: construct the chiral determinant first,
retain its primitive and square anomaly lines, and only then compare it with
the adjoint or reciprocal determinant. Any compiler that forms
\(\mathcal D_p\) or \(\mathcal C_p\) first and takes an ordinary determinant
has already erased the source orientation required by the Tate response.

## The chiral diagonal operator exists and is zero-free

The minimum-conductor Mellin ratio constructs a canonical chiral eigenvalue.
Define

\[
\lambda_p(s)
=
\gamma_p(s)-1.
\]

Using the local response symbol,

\[
\lambda_p(s)
=
-\frac{1-p^{-1}}{1-p^{s-1}}
\rho_p(s).
\]

Thus \(\lambda_p\) is derived from the odd response column and the even local
denominator; it is not fitted from a global scalar determinant.

On the prime-labelled one-particle module, define the diagonal chiral
operator

\[
L_s e_p=\lambda_p(s)e_p.
\]

If \(\sigma=\operatorname{Re}s\), then on compact subsets of the critical
strip

\[
|\lambda_p(s)|
=
O\left(
p^{-\min(\sigma,1-\sigma)}
\right).
\]

Therefore

\[
L_s\in\mathcal S_3
\]

throughout the central strip

\[
\frac13<\operatorname{Re}s<\frac23.
\]

Its order-three determinant is

\[
\det_3(I+L_s)
=
\prod_p
\gamma_p(s)
\exp
\left(
-\lambda_p(s)
+
\frac{\lambda_p(s)^2}{2}
\right).
\]

This is the precise chiral determinant whose first two Taylor cumulants are
exported to the primitive and square boundary lines.

But

\[
(I+L_s)e_p=\gamma_p(s)e_p.
\]

Every local factor \(\gamma_p(s)\) is nonzero in the central strip. On compact
subsets, the diagonal inverse is uniformly bounded. Hence \(I+L_s\) is
invertible there and

\[
\det_3(I+L_s)\ne0.
\]

This is a decisive no-go theorem. The diagonal local-sewing determinant
constructs the correct regularization class and arithmetic provenance, but it
cannot carry the Riemann divisor.

The missing determinant must involve a genuinely global non-diagonal
operation, such as:

- the theta/Mellin boundary incidence;
- a seam-mediated Schur complement;
- an archimedean coupling;
- or a relative determinant of nontransverse global polarizations.

Multiplying the zero-free chiral determinant by independently invertible
counterterms cannot create zeros. Therefore at least one completed boundary
factor must be operator-valued before determinant formation or must cease to
be invertible on the characteristic states. Treating every anomaly channel
as a nowhere-vanishing scalar normalization makes reproduction of
\(\Xi\) impossible.

This sharply relocates the zero-to-state bridge. The local Euler/Tate
operator supplies a zero-free diagonal background. The characteristic
divisor, if realized operatorially, must be created by the global boundary
interaction that is absent from the diagonal prime module.

## Every characteristic state must be boundary-induced

Let the completed source operator, at finite cutoff first, have block form

\[
\mathcal M_{s,X}
=
\begin{pmatrix}
I+L_{s,X}&B_{s,X}\\
C_{s,X}&E_{s,X}
\end{pmatrix}.
\]

The first block is the chiral diagonal Tate background. The other blocks must
come from the endpoint, seam, archimedean, and response incidences.

Since \(I+L_{s,X}\) is invertible, Gaussian elimination gives the boundary
Schur operator

\[
\mathcal S_{s,X}
=
E_{s,X}
-
C_{s,X}
(I+L_{s,X})^{-1}
B_{s,X}.
\]

The kernel relation is exact:

\[
\mathcal M_{s,X}
\begin{pmatrix}
x\\u
\end{pmatrix}
=0
\]

if and only if

\[
\mathcal S_{s,X}u=0
\]

and

\[
x
=
-(I+L_{s,X})^{-1}B_{s,X}u.
\]

Therefore every characteristic state is induced by a boundary vector \(u\).
There is no independent prime-bulk kernel in the central strip.

At determinant level, the zero-free chiral determinant factors out. Up to
the declared nonvanishing regularized multiplicative anomaly, zeros of the
full determinant are zeros of the boundary Schur determinant.

This gives the first forward zero-to-state bridge that does not manufacture a
complex from \(\Xi\):

1. local Tate data construct \(L_s\);
2. source boundary incidence constructs \(B_s,C_s,E_s\);
3. a scalar characteristic zero produces
   \(u\in\ker\mathcal S_s\);
4. the bulk state is reconstructed uniquely from \(u\).

The bridge remains conditional because the three boundary blocks have not
yet been assembled on one completed rigged carrier. But its logical location
is now exact.

## The RH mechanism is a boundary theorem

Any independent orientation law must act on \(\mathcal S_s\), not on the
already invertible diagonal background. A source-derived maximal neutral
boundary relation, self-adjoint boundary triple, or lossless response law
would constrain the characteristic values of this Schur family.

The construction is circular if \(B_s,C_s,E_s\) are chosen to make

\[
\det\mathcal S_s
\]

equal to the completed scalar section. They must instead be derived from the
minimum-conductor quotient extension, theta/Mellin trace, seam graph, and
archimedean cell before determinant evaluation.

The decisive finite residual is now

\[
R_{s,X}^{\mathrm{Schur}}
=
\mathcal S_{s,X}^{\mathrm{source}}
-
\left(
E_{s,X}
-
C_{s,X}
(I+L_{s,X})^{-1}
B_{s,X}
\right).
\]

Any nonzero typed entry closes the proposed boundary realization. Scalar
agreement after determinant formation cannot cancel a nonzero block
residual.

If the residual vanishes at every cutoff, the next completion gates are:

1. continuity of \(B_s\) and \(C_s\) across the exponential primitive
   rigging;
2. closedness of the limiting Schur family;
3. convergence of its determinant line;
4. and a source-derived spectral-parameter-independent neutral domain.

## The real place has the same minimum-complexity splitting

Use the self-dual real Fourier convention

\[
(\mathcal F_\infty f)(\xi)
=
\int_{\mathbb R}
f(x)e^{-2\pi i x\xi}\,dx.
\]

The minimum Fourier-even source is the Gaussian

\[
e_\infty^+(x)=e^{-\pi x^2}.
\]

It satisfies

\[
\mathcal F_\infty e_\infty^+=e_\infty^+,
\qquad
e_\infty^+(0)=1,
\qquad
\int_{\mathbb R}e_\infty^+(x)\,dx=1.
\]

The first even Hermite excitation with Fourier character \(-1\) is

\[
e_\infty^-(x)
=
(1-4\pi x^2)e^{-\pi x^2}.
\]

Direct Fourier differentiation gives

\[
\mathcal F_\infty e_\infty^-=-e_\infty^-.
\]

Its endpoint coordinates are

\[
e_\infty^-(0)=1,
\qquad
\int_{\mathbb R}e_\infty^-(x)\,dx=-1.
\]

Thus the real place has the same ordered quotient characters \((1,1)\) and
\((1,-1)\) as every unramified finite place.

The additive Gram is also diagonal:

\[
\langle e_\infty^+,e_\infty^-\rangle=0,
\]

\[
\|e_\infty^+\|_2^2=\frac1{\sqrt2},
\qquad
\|e_\infty^-\|_2^2=\sqrt2.
\]

After normalizing the even coordinate, the relative odd Gram weight is two.

## The archimedean odd response is exactly linear

Define the real multiplicative Mellin integral

\[
\mathcal Z_\infty(f,s)
=
\int_{\mathbb R^\times}
f(x)|x|^s\,d^\times x.
\]

The even Gaussian gives

\[
\mathcal Z_\infty(e_\infty^+,s)
=
\pi^{-s/2}\Gamma\left(\frac{s}{2}\right).
\]

Using the gamma recurrence,

\[
\mathcal Z_\infty(e_\infty^-,s)
=
(1-2s)
\mathcal Z_\infty(e_\infty^+,s).
\]

Hence the minimum-complexity archimedean response symbol is

\[
\rho_\infty(s)
=
\frac{
\mathcal Z_\infty(e_\infty^-,s)
}{
\mathcal Z_\infty(e_\infty^+,s)
}
=
1-2s.
\]

It has the exact reciprocal character

\[
\rho_\infty(1-s)=-\rho_\infty(s).
\]

In centered coordinates,

\[
\rho_\infty\left(\frac12+z\right)=-2z.
\]

The finite and infinite places now exhibit one source pattern:

- minimum invariant even source;
- minimum-complexity Fourier-odd excitation;
- endpoint coordinates \((1,-1)\);
- and an odd Mellin response under \(s\leftrightarrow1-s\).

At finite \(p\), the response is a normalized hyperbolic sine in
\(z\log p\). At infinity, it is the linear normal coordinate \(-2z\). This
constructs the previously missing archimedean odd response without fitting a
gamma derivative or inspecting the zero set.

The remaining global task is to place

\[
\rho_\infty
\]

and the prime response hyperfunction in one adelic boundary relation. Their
sum should not be assumed to vanish or be positive. The source must determine
their transported cocycle law and the seam/endpoint incidence that enters the
boundary Schur operator.

## Finite and infinite responses form one deformation family

Put

\[
q=p^{-1}.
\]

The finite-place response can be written

\[
\rho_q(s)
=
\frac{q^s-q^{1-s}}{1-q}.
\]

This is a reciprocal finite-difference quotient. Its undeformed limit is

\[
\lim_{q\to1}
\rho_q(s)
=
1-2s
=
\rho_\infty(s).
\]

Equivalently, in centered coordinates,

\[
\lim_{q\to1}
\frac{
q^{1/2+z}
-
q^{1/2-z}
}{
1-q
}
=
-2z.
\]

Thus the archimedean odd response is the differential member of the same
deformation family whose finite-place members are valuation differences.
The coefficient \(-2\) is forced by the common quotient normalization; it is
not an independently fitted gamma correction.

This should not be interpreted as a sequence of actual primes approaching
one. It is an algebraic degeneration of the local response law. Its value is
coherence: the finite and infinite ports are two realizations of one
source-defined reciprocal-difference constructor.

The corresponding compiler gate is exact. A proposed archimedean response
must agree with the \(q\to1\) degeneration of the normalized finite response
and with the minimum Hermite calculation. Failure of either equality means
that the finite and infinite boundary columns do not belong to one adelic
constructor family.

This is the first explicit coherence relation in the present route that joins
the finite prime response and the archimedean response before scalar
projection. It supplies normalization and orientation, but not global
zero-exclusion.

## Scope

This packet identifies and types the only remaining location for a
divisor-coherence obstruction after finite flatness. It does not construct
the common theta complex, establish a uniform gap, identify an asymptotic
class with a Riemann zero, or prove RH.
