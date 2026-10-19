# Deligne comparison: every rational Hodge class lifts, not every lift is algebraic

## Question and source complexes

Execute the fresh workbench's degree-six Deligne comparison on the unchanged smooth projective sixfold. SCC obligations: typed rational/filtered comparison, homotopy-coherent matching and projection to the class. This is an actual standard cohomological interface, not a hypothetical cycle library.

Write A=R Gamma(X,Q(3)), F=F^3 R Gamma_dR(X,C), C=R Gamma(X,C), with comparison maps i:A->C and j:F->C. The Tate twist Q(3)=(2 pi i)^3 Q fixes the comparison normalization; it is not discarded when identifying the rational Hodge subspace. After choosing compatible cochain models, the rational Deligne complex is the homotopy fiber

    D = Cone(i-j:A direct_sum F -> C)[-1].

In degree n its elements have three components (a,f,h) with h in C^(n-1), and differential

    d_D(a,f,h)=(d_A a,d_F f,i(a)-j(f)-d_C h).

Thus a degree-six cocycle consists of closed a,f and an actual homotopy satisfying i(a)-j(f)=d_C h. Requiring equality of the raw representatives instead of equality up to h would impose an unjustified stricter condition.

## Exact sequence and the fixed alpha

For smooth projective X, Hodge-de Rham degeneration and strictness identify H^n(F) with F^3 H^n(X,C). The long exact sequence of the cone yields

    0 -> J_Q^3(X) -> H_D^6(X,Q(3)) -> Hdg^3(X,Q(3)) -> 0,

where

    J_Q^3(X)=H^5(X,C)/(F^3 H^5(X,C)+H^5(X,Q(3))).

The last group is the rational degree-six classes whose complex comparison lies in F^3; rational conjugation and weight six identify this with type(3,3), with the Tate twist retained. These are standard imported Deligne/Hodge facts; the exact-sequence inference is the written argument here.

In particular the fixed alpha has a Deligne lift. Choose a rational cocycle a for its twisted class, a filtered representative f of the same complex cohomology class, and h with d h=i(a)-j(f). The existence of h follows from equality of cohomology classes, not algebraicity. Its choice is not canonical. The fiber of the projection over alpha is a nonempty torsor under J_Q^3(X).

At the fixed abelian sixfold, h^(r,s)=binomial(6,r)binomial(6,s). Hence b5=792 and dim_C F^3 H^5=396. The complex vector space H^5/F^3 has dimension396. After quotienting also by the rational period subgroup, J_Q^3 is NOT being treated as a Hausdorff complex vector space of that dimension. This prevents an unjustified dimension or finite-fiber claim.

## The algebraic map is a separate arrow

The Deligne cycle regulator gives

    CH^3(X)_Q --cl_D--> H_D^6(X,Q(3)) --pi--> Hdg^3(X,Q(3)),

with pi cl_D=cl (with consistent twist). The ordinary Hodge question for alpha is

    pi^(-1)(alpha) intersects im(cl_D) nontrivially.

It is NOT whether pi^(-1)(alpha) is nonempty; that has already been proved. It is also not whether a separately selected Deligne lift lies in im(cl_D). A chosen lift could fail while another lift differing by J_Q^3 comes from an algebraic cycle. Even a proof of Hodge would not imply that every Deligne lift is an algebraic regulator value.

There is also a precise lift-independence test. A linear reader on H_D^6 descends to Hdg^3 exactly when it kills J_Q^3. Otherwise two lifts of the same class can have different values, including lifts of a known algebraic class. After removing both algebraic images and lift ambiguity, the canonical quotient is

    H_D^6/(im(cl_D)+J_Q^3) isomorphic to Hdg^3/im(cl).

This follows from surjectivity of pi and ker(pi)=J_Q^3. The quotient contains no additional obstruction information merely from using the larger Deligne target; evaluating it on alpha still requires the unknown algebraic image.

Thus the proposed detector 'alpha has no coherent rational/filtered Deligne realization' is rejected at this scope. Declaring the complement of im(cl_D) to be the obstruction simply renames an unknown image unless an independently evaluable invariant and all-cycle necessity theorem are supplied.

## Exact cochain control

The checker retains a finite Q-linear cone with C^5=Q^2, C^6=Q^3, d(h1,h2)=(0,h2,0), A^6=Q^2 mapping (a1,a2) to (a1,0,a2), and F^6=Q mapping f to (f,f,0). The cocycle equations are

    a1-f=0,  -f-h2=0,  a2=0.

The Hodge-compatible class (1,0) has the lift (a1,a2,f,h1,h2)=(1,0,1,0,-1), despite having no lift with h=0. Adding any value to h1 preserves its class and cocycle equation. The class (0,1) does not lift because its comparison is not filtered even modulo dC; this is a non-Hodge control, not a Hodge counterexample. Rank and exact-kernel calculations verify the abstract short exact sequence in this finite fixture.

The fixture is not the actual sixfold cochain model and does not compute its periods or regulator. It tests the signs, homotopy retention, lift ambiguity and non-Hodge rejection independently of the imported general theorem.

## Disposition and next geometric interface

The degree-six cohomological realization map is constructed. It is surjective onto rational Hodge classes, including alpha, without constructing algebraic cycles. Together with the earlier chain tests, this separates source algebraic realizations, their coherent cohomological images and the still-unknown algebraic image.

The next independently specified geometric test is support localization: use H_Z^6(X,Q)->H^6(X,Q) for algebraic supports of codimension at least three, and determine exactly what purity supplies and what universal support exclusion would require. This replaces the known-surjective Deligne lift test with an algebraic-specific source condition. It must not be satisfied by a merely topological support or by an arbitrary support chosen from the unknown cycle image.

No fixed-alpha algebraicity, nonalgebraicity, regulator-surjectivity theorem or proof-assistant certification is claimed.
