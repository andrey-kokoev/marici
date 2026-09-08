# A chain-level first-conductor-jet comparison

## Result

The two-row supported readout from the preceding calculation has a chain-level
promotion on the **first conductor jet of the full native mapping complex**.
The promotion keeps `u03`, `t04`, and `t35` as independent parameters. It maps
the positive-sheet cocycle to the complete supported resonance cocycle `tau`,
not just to its residue after setting those parameters to zero.

Two extra, fully marked native rows are required. They correct the failure of
the naive two-row operator to commute with the differential before support
specialization.

There is also a nonextension theorem. A B-linear derived map on the original
unaugmented ambient native mapping complex cannot detect the primitive class
`b`. This is an obstruction to the proposed linear promotion, not a global
nonexistence theorem for a physical realization using conductor symbols.

All constructions below concern the supplied native coefficient complexes.
They do not identify their domain with RHom(J,F0), construct H_cond, or assign
a physical value to the conductor--Morse difference.

## 1. Coefficients, complexes, and frames

Retain the alternating normalization--Rees coefficient ring B, its conductor
ideal I, and its split coefficient ring C=B/I. In this model C is also the
specified subring of spectator coefficients in B. Put

\[
x=X_{04},\quad y=X_{35},\quad s=t_{04},\quad t=t_{35},\quad
u=u_{03},\quad D=\mathcal C/(u,s,t),
\]

The six conductor coordinates are

\[
\mathcal I=(X_{02},X_{04},X_{13},X_{15},X_{24},X_{35}).
\]

Products of an even-sheet and odd-sheet short occurrence vanish. All six Rees
parameters and all three long normal parameters remain; only the six short
normal equations u_i=t_i X_i have been substituted. The exceptional parameter
is

\[
f=u+(1+u)t_{13}X_{13}.
\]

No occurrence, Rees, or normal parameter is inverted. The calculations commute
with subsequent localization at the admitted monodromy units.

Let N denote the ten-state exceptional packet in the preceding native
retraction. Its homological bases are

\[
N_1=(p_{04},p_{35}),\quad
N_2=(r_0,r_{04},r_{35},y_{04},y_{35}),\quad
N_3=(z_0,z_{04},z_{35}).
\]

Its differential is

\[
\begin{aligned}
dr_0&=-xp_{04}-yp_{35}, &dr_{04}&=-sxp_{04}, &dr_{35}&=-typ_{35},\\
dy_{04}&=-fp_{04}, &dy_{35}&=-fp_{35},\\
dz_0&=fr_0-xy_{04}-yy_{35},\\
dz_{04}&=fr_{04}-sxy_{04}, &dz_{35}&=fr_{35}-tyy_{35}.
\end{aligned}
\]

Here y04 and y35 are basis labels, not scalar variables. The ordered conductor
resolution P has matrices

\[
P_2=\mathcal B z\xrightarrow{w}\mathcal B^4
\xrightarrow{M}\mathcal B^3=P_0,
\qquad w=(t,s,t,s)^T,
\]
\[
M=\begin{pmatrix}0&-t&s&0\\1&0&-1&0\\0&1&0&-1\end{pmatrix}.
\]

Set Q_f=K_B(f) tensor P, with the K(f) factor first. It has ranks (3,7,5,1)
and top generator e_f tensor z. Denote its restriction to C by Q_u.

The two mapping complexes used here are

\[
\mathcal M_N=\operatorname{Hom}_{\mathcal B}(Q_f,N),\qquad
\mathcal M_E=\operatorname{Hom}_{\mathcal B}(Q_f,\widetilde E),
\]

where E-tilde is the complete 245-state native complex. These are bounded
complexes of finite free B-modules. A cohomological degree-n cochain lowers
homological degree by n, with differential

\[
\delta F=d_EF-(-1)^nFd_{Q_f}.
\]

The supported target is the same complete local complex as before:

\[
\mathcal M_{\rm loc}=\operatorname{Hom}_{\mathcal C}(Q_u,\mathcal C)[2].
\]

It has ranks (3,7,5,1) in degrees (-2,-1,0,1), and its only cohomology is
D tau in degree one. The coordinate tau evaluates to one on e_u tensor z.
The endpoint-difference line, ordered (s,t) dual conormal determinant, and
independent u-normal line are inherited unchanged. Scalar matrices refer to
these fixed frames; no physical channel coordinate is substituted for them.

The prior two sheet cocycles are

\[
\begin{array}{c|cc}
 &z&e_f\otimes z\\\hline
\mathfrak a_{04}&xp_{04}&xy_{04}\\
\mathfrak a_{35}&yp_{35}&yy_{35}.
\end{array}
\]

Their diagonal is the boundary of the graded center lift Theta:
Theta(z)=-r0, Theta(e_f tensor z)=-z0. The primitive ambient class is
b=[a35]=-[a04]. Full native embeddings of these cochains and Theta are
reconstructed from the supplied retraction.

## 2. No B-linear ambient derived readout detects b

**Theorem.** Every morphism in D(B) from either M_N or M_E to M_loc sends b
to zero.

Indeed, the source is a bounded complex of free B-modules. Every derived
morphism out of it is represented by an actual B-linear cochain map into the
given target complex. Every term of M_loc is annihilated by I, whereas both
representatives a04 and a35 have all coefficients in I. Thus every such
cochain map kills these representatives identically.

Equivalently one may compose with the quasi-isomorphism M_loc -> D[-1] and
use the same argument there. In particular the cohomological readout in the
previous result is not the restriction of a B-linear ambient derived map
that takes b to tau.

This does not contradict the B-linear relative symbol map on I M. Elements
of I/I^2 can map to the conormal coefficient module even though the inclusion
I M -> M has no compatible extension of this readout. It also does not
contradict a C-linear differential-operator comparison: C and B impose
different linearity requirements.

The theorem is an all-coefficient argument using projective complexes
(Stacks Project 064B), not a conclusion inferred from finite samples.

## 3. The intrinsic first-principal-parts domain

Let J_delta be the kernel of multiplication B tensor_C B -> B. The module of
first principal parts is

\[
\mathcal P^1_{\mathcal B/\mathcal C}
=(\mathcal B\otimes_{\mathcal C}\mathcal B)/J_\delta^2.
\]

The two B-actions must be distinguished. After conductor restriction on the
**left** action, define the C--B bimodule

\[
W_{\mathcal C}
=\mathcal C\otimes_{\mathcal B,\mathrm{left}}
\mathcal P^1_{\mathcal B/\mathcal C}.
\]

Its left action factors through C; its right B-action retains the first
conductor terms. In the specified split normalization algebra,

\[
W_{\mathcal C}\cong\mathcal B/\mathcal I^2
\cong\mathcal C\oplus\mathcal I/\mathcal I^2
\]

as C-modules. It has rank seven. All products of two conductor symbols are
zero; all six first conductor symbols are retained.

Define the first-jet operation on the mapping complex by

\[
\mathcal J^1_{\mathcal C}(\mathcal M)
=W_{\mathcal C}\otimes^L_{\mathcal B,\mathrm{right}}\mathcal M.
\]

The supplied bounded free M computes this derived tensor without any new
resolution. This definition uses the displayed bimodule, not a claim that
arbitrary derived restriction commutes with principal parts on a singular
ring. The map F -> 1 tensor F is C-linear and is a differential operator of
order at most one over B/C; it is not B-linear for the left conductor action.

At this stage u,s,t have not been set to zero. For example the right action
of f is still

\[
f=u+(1+u)t_{13}[X_{13}]\quad\bmod\mathcal I^2.
\]

Its first-order term is retained in every computed source differential.
The order-one property follows from the universal principal-parts
construction (Stacks Project 09CH, Lemmas 10.133.3 and 10.133.9). It is not an
arbitrary truncation of a polynomial computation.

## 4. The correction to the two-row operator

For a jet cochain F, let sigma_j F be its coefficient of [X_j], and let F0
be its constant conductor coefficient. First define the raw operator

\[
V(F)(q)
=(\sigma_{35}F(q))_{y_{35}}-(\sigma_{04}F(q))_{y_{04}}.
\]

It has degree zero from the jet of M_N to M_loc. For the full native target,
use the corresponding rows of its actual conductor retraction.

Define two degree-one maps

\[
Z_{04}(F)(q)=F_0(q)_{z_{04}},\qquad
Z_{35}(F)(q)=F_0(q)_{z_{35}}.
\]

They satisfy

\[
\delta Z_{04}=\delta Z_{35}=0,\qquad
\delta V=-sZ_{04}+tZ_{35}.
\]

For example d z0 has equal coefficients -x and -y on the two selected
normal states, so their signed difference cancels. The terms
-sx y04 and -ty y35 in d z04 and d z35 leave exactly the two displayed
multiples. The source variation contributes nothing in the x and y
first-symbol directions because f-u has direction X13. Every such term is
nevertheless retained before taking the stated coefficient.

The same equation holds on the full 245-state native target. The supplied
retraction gives the two y-rows with coefficient one, and its extra
old-target attachments have conductor factor X13. The checker verifies the
equation on every full native first-jet Hom column.

The complete target M_loc has explicit degree-minus-one multiplication
homotopies

\[
dh_s+h_sd=s\operatorname{id},\qquad
 dh_t+h_td=t\operatorname{id}.
\]

They are the duals of the s and t Koszul homotopies on Q_u, transported
through the actual P-to-Koszul deformation retract. If H_s is the source
homotopy and phi has degree n in M_loc, the precise sign is
h_s(phi)=(-1)^n phi H_s; likewise for t. All their matrices are exported.

It follows that

\[
\boxed{\Xi_{\rm jet}=V+h_sZ_{04}-h_tZ_{35}}
\]

is a degree-zero C-linear cochain map

\[
\Xi_{\rm jet}:\mathcal J^1_{\mathcal C}(\mathcal M_E)
\longrightarrow\mathcal M_{\rm loc}.
\]

Indeed the graded composition rule gives

\[
\delta\Xi_{\rm jet}
=(-sZ_{04}+tZ_{35})+sZ_{04}-tZ_{35}=0.
\]

This supplies the lower comparison terms that were absent from a two-row
cohomological readout. The uncorrected operator has 32 nonzero defect
columns. No parameter is inverted to correct them.

## 5. The four native rows and the exact matrix

The two first-symbol rows are

\[
v_{04}=[\{03,04,E\},\{03,E\}],\qquad
v_{35}=[\{03,35,E\},\{03,E\}].
\]

They are native rows 162 and 170 in the exported zero-based ordering.
The required zero-order correction rows are their fully marked partners

\[
w_{04}=[\{03,04,E\},\{03,04,E\}],\qquad
w_{35}=[\{03,35,E\},\{03,35,E\}].
\]

They are native rows 164 and 172. Each is an exact coefficient-one row of
the actual conductor retraction. These are four selected native rows, not
four omitted source degrees: all sixteen Q_f basis states and every native
state remain in the domain.

The exceptional Hom has total rank 160 over B; its first jet has rank 1120
over C. The complete native Hom has rank 3920 over B; its first jet has rank
27440 over C. The constructed matrix to the sixteen target cochain states
therefore has size 16 by 27440. It has 48 nonzero columns containing 52 signed
polynomial monomials.

The verifier exports the full comparison matrix, all target homotopies,
the exceptional first-jet differential, and the labelled full native Hom
basis. It constructs and checks the full native first-jet differential and
records its hash; the latter differential can be regenerated by the checker
rather than trusted as external data.

## 6. Primitive values and a chain-level supported summand

The entire parameter-retaining map satisfies

\[
\Xi_{\rm jet}(j^1\mathfrak a_{35})=\tau,\quad
\Xi_{\rm jet}(j^1\mathfrak a_{04})=-\tau,\quad
\Xi_{\rm jet}(j^1\widetilde\Theta)=0.
\]

Consequently it sends the total lifting obstruction to zero. The values hold
as cochain identities in M_loc, not merely after passage to H1.

Now additionally set u=s=t=0 in the first-jet domain. The terminal supported
readout is

\[
\chi(F)=
\left(
\operatorname{coeff}^{(1)}_{X_{35}}F(e_f\otimes z)_{v_{35}}
-\operatorname{coeff}^{(1)}_{X_{04}}F(e_f\otimes z)_{v_{04}}
\right)\bmod(u,s,t).
\]

It is a D-linear cochain map to D[-1]. The full degree-one row has 4046
columns, with exactly two nonzero entries. Sending 1 to the positive-sheet
jet gives a chain section; hence D[-1] is a strict chain direct summand of
this **supported first-jet complex**. This does not state that its complement
is acyclic or that the entire first-jet object is a single line.

The negative-sheet section, with its sign reversed, is homotopic to the
positive-sheet section through j1 Theta. That homotopy has zero readout.
This is a comparison of the native sheet representatives; the two sections
are not asserted to be the physical conductor and Morse trivializations.

The necessity of conductor order one is explicit. Let E_y be the elementary
cochain whose e_f tensor z column is y35 with coefficient one. Then

\[
\chi(E_y)=0,\qquad\chi(yE_y)=1.
\]

A B-linear map into D would give zero on y E_y. Every second commutator with
coefficient multiplication vanishes. Thus the operator has order exactly
one. Among the two stated derivative rows, closure on delta Theta forces the
sum of their coefficients to vanish; the prescribed positive-minus-negative
sheet orientation selects the primitive row (-1,+1), without dividing by two.

## 7. Endpoint and normal-line control

All sixteen native endpoint states and all seven native Q states are
retained, with all seven first-principal-parts components. The comparison is
zero on every Hom column taking values in these states. Both sheet sections
and their comparison homotopy have no endpoint or Q component. Their actual
endpoint connecting maps, obtained by projecting the native differential
into the endpoint subcomplex, vanish as well.

The first-derivative rows are paired conormal coefficients, not unframed
scalar divisions. For instance under x'=a x, keeping dr0 fixed requires
p04'=a^{-1}p04 and y04'=a^{-1}y04. The coefficient of y04' acquires a, while
the conormal-dual coefficient extraction acquires a^{-1}. They cancel. The
same statement holds on the y sheet. This describes normal-frame covariance
in the supplied chart; it does not assert new global reflection coherence.

The endpoint-difference line and the ordered (s,t) determinant are inherited
from the preceding supported map, as is the separate u-normal. The homotopies
h_s,h_t retain their shifts and weights. No external Cartier level is
reinterpreted as a cellular chain degree.

## 8. Physical scope

The coefficient-level comparison now has a fully specified cochain map and
its necessary first-order domain. A B-linear map from the unaugmented native
Hom cannot replace it and still detect b.

The original physical expression Delta_J=H_cond-e_F h_Morse has not been
identified with j1 a35 or any other jet cochain here. Its two independently
constructed homotopies must still be transported from their physical source
into this native first-jet model. This is the common-complex requirement of
Marici Entry 109. The new computation supplies the receiving map, including
its lower correction terms; it does not supply the missing physical input.

## References and reproduction

Repository: `andrey-kokoev/marici`, pinned commit
`d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

- Entry 93, `Alternating Fusion Normalization-Conductor Square`: the two
  augmented sheets, mixed-product relations, first conductor symbol, and
  positive-minus-negative orientation.
- Entry 109, `Closed Dual-Star No-Go and the Seven-Triangle Secondary
  Cobordism`: the common-mapping-complex requirement for Delta_J.
- Supplied `conductor_obstruction_descent_package.zip`: actual native
  matrices, conductor restriction, primitive sheet cochains, and retraction.
- Stacks Project 09CH, especially Lemmas 10.133.3 and 10.133.9: differential
  operators represented by principal parts and the diagonal-ideal formula.
- Stacks Project 064B: derived maps out of bounded projective complexes.
- Stacks Project 0A8H: Hom-complex differential and graded composition.

Run `python check_conductor_jet.py` with Python 3.10+; no third-party package
is required. It reconstructs and replays the native dependency calculations,
constructs the two first-jet differentials (both before and after support
specialization), verifies the correction identities, and exports the
comparison matrix and certificate. The general nonextension and
principal-parts statements are proved above; assertion counts do not
substitute for those proofs.
