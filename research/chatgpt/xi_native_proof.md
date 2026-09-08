# Native conductor comparison and its exact lifting obstruction

## Result and scope

A based comparison from the full native dual on the conductor to the supported
resonance complex is constructed as an explicit 16-by-245 matrix. It sends the
chosen positive exceptional dual class to the previously calculated class tau.

That comparison does not extend to the existing native complex on the glued
normalization ring. The failure is an explicit two-column cocycle. The obstruction
has a canonical copy of D=C/(u03,t04,t35), with the center comparison representing
its unit. The other two exceptional components have explicit ambient lifts.

This constructs a comparison and proves its precise extension obstruction. It does
not identify the native dual with RHom(J,F0), construct H_cond, or evaluate the
physical conductor--Morse difference. Those identifications are not inferred from
unit residues, matrix ranks, or agreement of boundary signatures.

## 1. Rings, complexes, and signs

Let B be the previously supplied alternating-normalization Rees ring. Its short
occurrence coordinates obey X_e X_o=0 for the two alternating parity sets. Let
I=(X02,X04,X13,X15,X24,X35), and C=B/I. Retain all six Rees parameters, long
occurrence coordinates, and the three independent long normal parameters. Put

- x=X04, y=X35;
- s=t04, t=t35, u=u03;
- f=u+(1+u)t13 X13, so f|C=u;
- A=C/(u), D=C/(u,s,t).

No normal, Rees, occurrence parameter, or integer is inverted. Compatible monodromy
units can be inverted; none changes the arguments.

The actual ten-state exceptional packet N_B has homological bases

N1=(p04,p35),
N2=(r0,r04,r35,y04,y35),
N3=(z0,z04,z35),

and differential

    d r0  = -x p04-y p35,
    d r04 = -s x p04,          d r35 = -t y p35,
    d y04 = -f p04,            d y35 = -f p35,
    d z0  = f r0-x y04-y y35,
    d z04 = f r04-s x y04,     d z35 = f r35-t y y35.

These matrices are rederived by the packaged 245-to-225 native deformation retract,
not fitted for this calculation. The embedding N_B -> native_B is supplied by that
retract. All its endpoint and native-Q components vanish. Every old-target-to-N
attachment contains X13 and hence vanishes on the conductor.

On C the packet splits into two signed copies of K(u)[1] and three copies of
K(u)[2]. Consequently H1(N_C)=A^2 and H2(N_C)=A^3.

Use the actual conductor comparison resolution P:

    P2=C z --w--> P1=C^4 --M--> P0=C^3,

    w=(t,s,t,s)^T,
    M=((0,-t,s,0),(1,0,-1,0),(0,1,0,-1)).

Define Q_f=K_B(f) tensor P_B and Q=Q_f tensor_B C=K_C(u) tensor P_C. Their ranks
are (3,7,5,1) in homological degrees (0,1,2,3). The target of the requested local
coefficient calculation is

    M_loc=Hom_C(Q,C)[2].

The positive pair class and positive resonance class are alpha=-z^vee and
 tau=(e_u tensor z)^vee in cohomological degrees zero and one, respectively.
The actual differential gives d alpha=u tau.

## 2. Correction to the preceding proposed factorization

The graded insertion of P_C^vee[2] into the K(u)-degree-zero components of M_loc
is not a cochain map before u=0: it takes the closed pair generator to alpha,
whose differential is u tau, not zero. A Bockstein on specialized cohomology is
also not a degree-zero morphism from the unspecialized pair complex.

The correct derived statement, with B_pair=P_C^vee[2], is the triangle

    M_loc -> B_pair --u--> B_pair -> M_loc[1].

It follows by applying RHom(-,B_pair) to the one-parameter Koszul triangle.
The coefficient Bockstein is instead a degree-one operation on the u-specialized
cohomology (with its conormal line): beta([alpha mod u])=[u] tensor [tau mod u].

Thus the previously proposed chain factorization Xi_coeff=beta_u o j_u is not
used. In particular, a degree-zero factorization through the unshifted pair dual
would annihilate H1, because H1(P^vee)=0. Constructing a new comparison must keep
the resonance factor from the outset.

## 3. Explicit comparison on the conductor

Let Theta_0:Q -> N_C have its only nonzero columns

    Theta_0(z)=-r0,
    Theta_0(e_u tensor z)=-z0.

The sign is the preceding ordered (s,t) Gysin convention. Both equations in the
chain condition are immediate:

    d(-r0)=0=Theta_0(w),
    d(-z0)=-u r0=Theta_0(u z-e_u tensor w).

Every other column is zero on both sides of the chain equation. Compose with the
checked inclusion N_C -> native_C and dualize. This gives

    Xi_C:Hom_C(native_C,C)[2] -> Hom_C(Q,C)[2]=M_loc.

The entire 16-by-245 dual matrix is exported. It has two nonzero output rows,
seven polynomial entries, and nine monomials. It is not obtained by claiming that
a comparison of scalar signatures is a comparison of complexes.

For the exceptional dual coordinates,

    Xi_C(r0^vee)=alpha,
    Xi_C(z0^vee)=-tau,
    Xi_C(-z0^vee)=tau.

All other exceptional dual basis columns are zero. The full native form uses the
actual embedding of r0 and z0. With a=03, b=13, E the exceptional ray, and q_a=1+u,
that embedding on the conductor is

    r0 -> u[E,empty]+[aE,a]-q_a[bE,b]+[bE,E],
    z0 -> u[E,E]+[aE,aE]-q_a[bE,bE].

Theta_0 is the negative of each displayed column. These are genuine normal-marked
states, not the five barycentric Morse triangles.

Neither column has an endpoint or native-Q component. The complete chain equation,
including the endpoint off-diagonals, is checked in the original 245-state basis.
No independent physical Q homotopy is introduced. Normal lines are retained in the
same ordered bases as the input Gysin resolution; their geometric comparison to
RHom(J,F0) is not inferred from these scalar coordinates.

## 4. All exceptional comparison classes on the conductor

For i=0,04,35, let Theta_i replace r0,z0 in the preceding construction by r_i,z_i.
These three maps give a basis of

    H0 Hom_C(Q,N_C) = D^3.

Proof: Q is a finite free resolution of D, while
N_C is quasi-isomorphic to A[1]^2 direct-sum A[2]^3. The Koszul resolution for
(u,s,t) with coefficients in A has Ext1_C(D,A)=0 and Ext2_C(D,A)=D. Its extra
Ext3 term does not enter this degree. Thus the only degree-zero comparison classes
are the three Ext2 components. Their top Koszul coefficients are precisely the
three Theta_i above, up to the displayed ordered sign.

This is a based family, not a uniqueness theorem for the physical connector. The
center component Theta_0 is singled out here because r0 is the retained conductor
center in the actual matrix M.

## 5. Its ambient failure is a two-column cocycle

Lift the two columns of Theta_0 unchanged to B. This gives a graded map, not a
chain map. Its exact defect

    A0=d_N Theta_0-Theta_0 d_Qf

has the two nonzero columns

    A0(z)=x p04+y p35,
    A0(e_f tensor z)=x y04+y y35.

All coefficients lie in I. The full equation d_N A0+A0 d_Qf=0 holds.

There is a degreewise exact sequence of Hom complexes

    0 -> Hom_B(Q_f,I N_B)
      -> Hom_B(Q_f,N_B)
      -> Hom_C(Q,N_C) -> 0.

The connecting homomorphism therefore sends [Theta_0] to [A0]. This is an actual
comparison obstruction, not an arbitrarily declared secondary scalar.

## 6. The two spectator components lift explicitly

For Theta_04 the following additional columns give a chain map over B:

    z -> -r04,
    second P1 basis -> x p04,
    e_f tensor second P1 basis -> -x y04,
    e_f tensor z -> -z04.

For Theta_35 use

    z -> -r35,
    first P1 basis -> y p35,
    e_f tensor first P1 basis -> -y y35,
    e_f tensor z -> -z35.

All other columns are zero. For example, w's second coordinate is s, so the first
map's degree-two equation is

    d(-r04)=s x p04=Theta_04(w).

Its degree-three equation is

    d(-z04)=-f r04+s x y04
             =Theta_04(f z-e_f tensor w).

The second map is verified with w's first coordinate t. Both maps are checked
against every column of Q_f and, after the original inclusion, against the full
245-state native differential. Both reduce to the corresponding based maps on C.
Their endpoint and Q components are zero.

## 7. No correction lifts the primitive center component

This statement concerns all ordinary coefficient chain maps, not just the two-column
ansatz. Specialize B by setting all short occurrence coordinates other than
x=X04,y=X35 to zero and then set u=s=t=0, leaving every other conductor parameter
and long coefficient free. The coefficient ring is

    B'=D[x,y]/(xy),

up to the already admitted spectator localizations. The source top z has boundary
w=0. The exceptional degree-two differential has only

    r0 -> -x p04-y p35;

r04,r35,y04,y35 have zero boundary. Every incoming attachment from the old target
vanishes since it contains X13. Thus the same test applies to maps into the full
native source, by composing with its checked retraction and exceptional projection.

For any chain map F, write a for the r0 coefficient of F(z). Its chain equation
forces x a=y a=0. The unique normal form in B' is

    a=a_0+x a_x(x)+y a_y(y).

Multiplying by x first forces a_0=a_x=0; multiplying by y then forces a_y=0.
Hence a=0. Further restriction x=y=0 forces the center comparison coefficient to
be zero in D.

This coefficient is invariant under homotopy after restriction to D: both source
and exceptional differentials on the relevant top states vanish there. More
explicitly, before setting u=0 and after setting s=t=0, the degree-three chain
equation on C implies that the z0 coefficient of F(e_u tensor z) agrees with the
r0 coefficient of F(z), since u is a nonzerodivisor. Thus the test detects the
actual Ext2 comparison coordinate, not a changeable chain representative.

Together with the two explicit spectator lifts, this proves

    image[H0 Hom_B(Q_f,N_B) -> H0 Hom_C(Q,N_C)]
       = 0 direct-sum D direct-sum D.

Its cokernel is exactly D, generated by the class of Theta_0. The same necessary
center-zero condition holds for full-native lifts, including any old-target
components. In particular, allowing those components does not repair the center
unit because their attachments vanish in the witness specialization.

The connecting class [A0] is therefore nonzero. The exact sequence identifies a
canonical submodule D[A0] inside H1 Hom_B(Q_f,I N_B), with annihilator

    (I,u,s,t)=(I,f,s,t)

in B. This does not assert that the entire H1 of that Hom complex is only D.

## 8. Relation to the supported conductor extension

On the common support u=s=t=0, the actual conductor matrix becomes

    ((0,0,0,0),(1,0,-1,0),(0,1,0,-1)).

Its image is exactly the two spectator coordinates that have just been lifted.
Its cokernel is the center line. The identification on cokernels is explicit:

    [r0] -> [Theta_0] -> [A0].

The first arrow sends the ordered center basis to the based comparison above;
the second is the connecting homomorphism of the full Hom sequence. It sends the
unit of the previously computed D-valued conductor cokernel to a nonzero lifting
obstruction with the same exact annihilator. No appeal to equal dimensions or
product of residues is needed.

This identifies the supported conductor coefficient with a concrete obstruction to
extending the local dual comparison. It does not identify it with the physical
conductor--Morse invariant. In particular, the nonzero tau image after restricting
to C cannot be used to declare that the desired physical Xi already exists over B.

## 9. Remaining physical interpretation

The desired source is RHom(J,F0). The source of the constructed Xi_C is the dual
of the specified native complex AFTER conductor base change. Those sources have
not been identified.

The ordinary base-linear lift of the primitive center component is ruled out above.
A normalization-derived extraordinary comparison could have a different domain,
include additional conductor resolution terms, or act on the relative obstruction
complex Hom_B(Q_f,I N_B). Such a construction must be supplied, not assumed. This
calculation does not compute H_cond, the transported Morse nullhomotopy, or the
coefficient of their difference.

## Reproduction

Run `python check_xi_native.py` after extracting the package. It needs Python 3.10+
and the standard library. The script replays the normalization and native
construction, verifies 1,432 new exact identities, and exports the matrices and
certificate. The rank-three classification, exact image, and universal no-lift
statement are proved above; finite checks are not substituted for those proofs.

Sources: Marici commit d1947b67a60d3e88ba77f4ca60ea02c2a306ee61, Entries 93, 109,
115 and the supplied native/normalization/supported-Gysin matrix packages.
Standard conventions: Stacks Project tags 0A8H (Hom and adjunction), 0621 (Koszul
complexes), 0117 (connecting homomorphisms), and 0B4B (Cartier duality).
