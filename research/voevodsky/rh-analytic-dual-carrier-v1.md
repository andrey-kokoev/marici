# Iteration7: a fixed analytic test/antidual carrier and explicit triangle operations

## Construction boundary

This is an **added analytic source decoration**, not a derivation of arithmetic
from the bare seed. The original triangle cycles still permute amplitudes.
The inherited finite signed form cannot encode the complete test domain, as
iteration6's positive15-test witness proves.

We now define one fixed infinite test/antidual pairing and actual weak source
operators. The same construction can be attached beside either native carrier.
It reproduces signed finite restrictions, including the15-test witness, without
an input-dependent positive-square repair. Global estimates below are analytic
proofs; the checker verifies their scalar anchors and finite restrictions, not
machine-formalized functional analysis.

## 1. Complete analytic test domain

Let T be the smooth logarithmic functions with all seminorms

    p(k,m)(f)=max_(j<=m) sup_x exp(k|x|)|f^(j)(x)|

finite, for integers k>=1,m>=0. Weighted uniform derivative convergence makes
T a complete Frechet space. It contains C_c^infinity and every Gaussian feature
used in the earlier certificates.

Define Ff(z)=integral f(x)exp(-izx)dx. Superexponential decay makes Ff entire.
Integration by parts gives rapid horizontal decay uniformly on every fixed
strip: choose k greater than the strip width. Thus

    h_fg(z)=conjugate(Ff(conjugate(z))) Fg(z)

and its evenization are admissible for the inspected explicit formula.
Conjugation at the conjugate argument is essential; this is not an absolute
square at a complex zero.

Let T^x be the continuous **antidual**: conjugate-linear functionals on T,
with its strong topology of uniform convergence on bounded test sets.
A Hermitian form b is conjugate-linear in f and linear in g. Define

    (W_b g)(f)=b(f,g).

Then W_b:T->T^x is linear. This avoids the variance error of treating an
ordinary complex-linear dual as a linear target for this formula.

## 2. Operators defined by source kernels, not Gram tables

Put A_±(f)=integral f(x)exp(±x/2)dx, T_ell g(x)=g(x+ell), and
omega(u)=Re psi(1/4+iu/2)-log pi. Define

    b_E(f,g)=[conjugate(A_-(f))A_+(g)
             +conjugate(A_+(f))A_-(g)]/2,

    b_Gamma(f,g)=(1/(4pi)) integral omega(u)conjugate(Ff(u))Fg(u)du,

    b_P(f,g)=-(1/2) sum_n Lambda(n)/sqrt(n)
                       [<f,T_(log n)g>+<f,T_(-log n)g>],

    b_Z(f,g)=(1/2) sum_rho m(rho)
                       conjugate(Ff(conjugate(u_rho)))Fg(u_rho),
    u_rho=(rho-1/2)/i.

All sums and integrals converge absolutely on T. The prime form is Hermitian
because translations are paired with their adjoints. The divisor form is
Hermitian by unconditional rho->1-conjugate(rho), which sends u->conjugate(u).
Endpoint and gamma Hermiticity are immediate.

Set W_A=W_E+W_Gamma+W_P. The primary formula on h_fg(u)+h_fg(-u), divided by
four, gives

    b_A=b_Z, hence W_A=W_Z

on all T. This uses analytic admissibility and unconditional divisor reflection,
not a presumed numerical equality of finite midpoints.

### Explicit joint continuity estimates

Write p=p(1,2), with p(1,0) sufficient in the endpoint/prime estimates.

- |A_±(f)|<=4p(1,0)(f), so |b_E(f,g)|<=16p(f)p(g).
- |Ff(u)|<=4p(f)/(1+u²). The digamma series gives
  |omega(u)|<=12+2u². Integrating against (1+u²)^(-2) gives
  |b_Gamma(f,g)|<=28p(f)p(g).
- |<f,T_ell g>|<=(|ell|+1)exp(-|ell|)p(1,0)(f)p(1,0)(g).
  Using Lambda(n)<=log n, the prime coefficient sum is bounded by
  sum_(n>=2)log n(log n+1)n^(-3/2)<21. The summand decreases from3 onward;
  its two initial terms sum to less than1 and its integral from1 is20.
- For |Im z|<=1/2, integration by parts in the real frequency gives
  |Ff(z)|<=13p(f)/(1+(Re z)²): the zeroth derivative integral is at most4p,
  and the second derivative integral is at most9p.
  With N(13)=0, freshly certified by the total count, and the unconditional
  Jensen bound N(v)<=(v+3)^2 for v>=13, integration by parts yields

      sum_(gamma>0) m/(1+gamma²)²
       <= integral_13^infinity 4v(v+3)²/(1+v²)^3 dv
       <=512/(13^4).

  The half-divisor factor cancels the two conjugate ordinate halves.
  Therefore |b_Z(f,g)|<= (512/169)p(f)p(g)<4p(f)p(g).

No nontrivial real zero contributes: the real critical-strip zeta function is
negative by the alternating eta expression, as noted in iteration5. All
positive/negative ordinate zeros are included, with multiplicity.

Thus b_A is bounded by65p(f)p(g), and each W_b is continuous into the strong
antidual: for a bounded set B, sup_(f in B)|b(f,g)|<=C sup_B p(f) p(g).
These bounds are global domain statements, not conclusions from a finite
positive packet or a scout of zero ordinates.

## 3. Fixed Hermitian dual pairing

On E=T direct_sum T^x define

    H_dual((f,l),(g,m))=[m(f)+conjugate(l(g))]/2.

This is a fixed nondegenerate Hermitian dual pairing. It is separately
continuous; we do **not** claim joint continuity on the entire product,
a positive Hilbert metric or a Hilbert completion of the antidual. On the
source graphs below its pullback is jointly continuous by the preceding bounds.
The word analytic completion refers to the complete test domain and its
antidual enlargement, not an assumed positive ambient Hilbert space.

For each source form define the continuous reversible shear

    U_b(f,l)=(f,l+W_b f).

It is a linear operation on a whole functional register, not a state factory
that first calculates the scalar b(f,f). We have

    U_b U_c=U_(b+c), U_b^-1=U_(-b),
    H_dual((f,W_b f),(g,W_b g))=b(f,g).

The shear is generally **not** pairing-unitary: its pairing defect on general
states is b(f,g). Reversibility is not conservation of a physical norm.
No form positivity is imposed; negative and complex-Hermitian controls pass.

These are mathematical functional operators, not a universal program for all
smooth inputs. T also contains noncomputable functions. Effective evaluation
requires a function representation/oracle and certified derivative/seminorm
bounds. The existing Gaussian algorithms implement particular finite
restrictions; no general effective test-oracle interface is asserted here.

The carrier has arbitrarily many positive and negative directions. Choose
any finite L2-orthonormal family v_i of disjoint smooth compact tests and
Jv_i(f)=<f,v_i>. Then (v_i,+Jv_i) and (v_i,-Jv_i) give positive and negative
orthogonal subspaces of any chosen dimension. This is why the finite native
positive-index14 barrier no longer applies to the **enlarged** carrier.

## 4. One explicit, noncanonical triangular decoration

Put identical copies of E at A,B,C,D. This example assigns

| Directed occurrence | Source operation |
|---|---|
| AB | U_E |
| BC | U_Gamma |
| CA | U_P |
| BA | U_(-E)=U_E^-1 |
| AD | U_Z |
| DB | U_E |

Each operation retains the input test f. Starting at (f,0), the arithmetic
loop AB,BC,CA ends at (f,W_A f), and its paired readout is b_A(f,f).
The spectral loop BA,AD,DB ends at (f,W_Z f): it subtracts the shared endpoint
register, evaluates the divisor and restores the endpoint register. The
A-rooted ordering AD,DB,BA gives the same source output.

The common edge identifies one test frame and one endpoint generator with
opposite sign. Fourier convention, analytic continuation and multiplicities
belong to the shared source-interface declaration. This **endpoint assignment
is an added choice**, not something forced by the seed geometry. For example,
change AB to2E, BA to-2E, DB to2E and CA toP-E; both face outputs are unchanged.
The checker verifies this gauge freedom, so no uniqueness is manufactured.

Both faces traversed forward compute A+Z, not the comparison. The composable
comparison path is left face followed by the inverse A-rooted right face:

    AB,BC,CA,AB,BD,DA.

It computes U_(A-Z), which is the identity by the classical source theorem.
The alternative AB,BC,CA,BA,AD,DB is not composable and is rejected.

Exact numeric midpoint restrictions do not assert this identity. Their small
nonzero defect is retained with certified correction envelopes; corrections
are bounded, not set to zero. Equality of source operators and finite numerical
consistency are different statements.

## 5. Compatible enlargement beside both native carriers

Freshly reconstruct the weighted native H and M_s. Choose one inherited
transient source/sink pair x,y with

    W x=y, W y=0,
    x*H x=y*H y=0, x*H y=d/2,
    x*M_s x=y*M_s y=d>0, x*M_s y=0.

Normalize both tags by sqrt(d). Their mixed pairing is exactly1/2, and the
native clock maps the normalized source tag to the normalized sink tag.
The checker verifies squared normalization exactly without assuming sqrt(d)
lies in the coefficient field Q(sqrt(-3)). The neutron metric is retained.

Replace the scalar coordinates of this one hyperbolic plane by T and T^x.
Keep its H-orthogonal106-dimensional native remainder unchanged. The exact
plane projector is

    Pi=[x x* M_s+y y* M_s]/d.

The checker verifies that Pi reduces W, and that plane/remainder H cross terms
vanish. This gives a genuine enlargement compatible with the original finite
form, not a claim that its finite positive index was secretly infinite.

To embed the original finite plane, fix v in T with L2 norm1 and mu=Jv.
Then mu(v)=1; scalar coordinates(alpha,beta) embed as(alpha v,beta mu).
The new pairing reproduces the original normalized finite pairing exactly.
The untouched remainder embeds identically.

The same source operators U_b act on the common T/antidual register beside
either native carrier. Relabeling the normalized paired tags preserves the
pairing and these added operators. Finite source restrictions of dimensions3
and15, negative15 and a complex-Hermitian control are checked exactly.

### Still not native processing equivalence

A lift of the selected native nilpotent clock is W_0(f,l)=(0,Jf), with W_0²=0;
on the fixed vacuum plane it reproduces the original clock. The untouched
remainder retains its original W. The completed clock still satisfies

    W_completed^5=W_completed².

The native identity is freshly checked. But for a nonzero source shear
U=I+N, N²=0,

    U^5-U²=3N !=0.

An injective linear intertwiner into this native clock would imply3EN=0,
contradicting injectivity. Thus supplying this analytic domain does not turn
the inherited clock into the source accumulators.

There is also a full-stage obstruction for **this specific one-plane
completion**. The selected A=L-N mode has G-N=0, so enlarging it leaves the
three-stage G-minus-N projector finite rank6 in the protonlike carrier and33
in the neutron carrier. An invertible intertwiner preserving G and N would
preserve those ranks; it cannot exist. Other enlargements/readout choices
are not ruled out by this particular rank argument.

## 6. RH condition and remaining gates

The two analytic loops compare the same completed functional beside both
structures. Their equality is unconditional. RH-bearing positivity is

    b_A(f,f)=b_Z(f,f)>=0 for EVERY f in the appropriate complete test domain.

Under RH, every u_rho is real and this follows from the signed divisor expression
becoming a positive square sum. Conversely T contains compact smooth tests;
using the standard compact Weil positivity criterion gives RH. That classical
criterion is an explicit imported theorem, not proved by this constructor.
No all-test positivity, positive quotient Hilbert completion or RH proof is
claimed here.

The new analytic source operators are additional structure. They are not
physical pulse laws, native seed arrows or a source of particle masses.

Artifacts:

- `inputs/rh-analytic-dual-carrier-v1.json`.
- `checkers/check_rh_analytic_dual_carrier.py`.
- `results/rh-analytic-dual-carrier-v1.json`.
- `scc-models/rh-analytic-dual-carrier-v1.json`.

Next nonredundant step: audit source covariance and the radical/conditional
positive quotient. In particular separate invariant signed analytic pairings
from positive-unitary native dynamics, and retain multiplicity information
when discussing any spectral Hilbert completion.
