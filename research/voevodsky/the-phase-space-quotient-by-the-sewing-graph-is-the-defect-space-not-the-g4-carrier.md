# The phase-space quotient by the sewing graph is the defect space, not the G4 carrier

## Question

Can G4 be interpreted as a quotient of boundary phase space?

## Claim boundary

There are two different quotients. Symplectic reduction by the maximal-isotropic sewing graph is zero. The ordinary linear quotient by that graph is nontrivial and canonically identifies with one copy of the response space; it measures sewing defects. Thus a quotient interpretation is useful for the final Evans obstruction, but it should not replace the faithful G4 carrier.

## Boundary phase space

Let \(H\) be the complete response Hilbert space and let \(T:H\to H\) be the unitary Fourier quarter turn. Define incoming/outgoing phase space

$$
\mathcal P_\partial=H_-\oplus H_+.
$$

Its Green boundary form is

$$
[(x_-,x_+),(y_-,y_+)]_\partial
=
\langle x_-,y_-\rangle
-
\langle x_+,y_+\rangle.
$$

The sewing relation is

$$
\Lambda_T=\operatorname{Graph}(T)
=
\{(x,Tx):x\in H\}.
$$

Because \(T\) is unitary,

$$
\Lambda_T^{\perp_\partial}=\Lambda_T.
$$

## Symplectic reduction is trivial

For a coisotropic constraint \(C\), reduction is

$$
C/C^{\perp_\partial}.
$$

Taking \(C=\Lambda_T\) gives

$$
\Lambda_T/\Lambda_T^{\perp_\partial}
=
\Lambda_T/\Lambda_T
=0.
$$

Therefore G4 cannot be the symplectic reduction of its own maximal-isotropic sewing graph unless the desired reduced object is trivial.

This is the standard fact that a Lagrangian is already a complete boundary condition, not a residual phase space.

## Ordinary quotient and defect map

Define

$$
d_T:\mathcal P_\partial\to H,
\qquad
d_T(x_-,x_+)=x_+-Tx_-.
$$

Then

$$
\ker d_T=\Lambda_T.
$$

The map is surjective because

$$
d_T(0,h)=h.
$$

Hence the first isomorphism theorem gives

$$
\boxed{
\mathcal P_\partial/\Lambda_T
\simeq H.
}
$$

This quotient is the **sewing-defect space**. A boundary pair represents zero exactly when it satisfies the G4 sewing law.

## Explicit splitting

Every boundary pair decomposes uniquely as

$$
(x_-,x_+)
=(x_-,Tx_-)+(0,x_+-Tx_-).
$$

The first term lies in \(\Lambda_T\); the second is a chosen transverse defect representative. Thus the quotient does not require an arbitrary complement.

## Evans interpretation

For an Evans boundary trace \(e=(e_-,e_+)\), its quotient class is

$$
[e]
\longleftrightarrow
d_T(e)
=e_+-Te_-.
$$

Evans membership is exactly

$$
[e]=0
\quad\Longleftrightarrow\quad
e_+=Te_-.
$$

After prime-shell projection and contragredient arithmetic readout, this is the residual

$$
B_\Sigma^\dagger\partial_z^ju=0.
$$

Thus the RH-bearing object is naturally a defect class in the quotient phase space.

## Xi-ideal refinement

For holomorphic families, chain promotion only requires the defect class to be Xi-divisible:

$$
d_T(e(z))=\tau(z)h(z).
$$

Therefore the chain-level obstruction lives in

$$
\frac{\mathcal O(H)}{\tau\mathcal O(H)}.
$$

This quotient records the defect restricted to the completed Xi divisor, including multiplicities.

## Safe quotient architecture

A safe hierarchy is:

1. retain the faithful source-response graph as G4;
2. form boundary phase space \(H_-\oplus H_+\);
3. retain \(\Lambda_T\) as the maximal-isotropic sewing condition;
4. use \(\mathcal P_\partial/\Lambda_T\) only as the obstruction/defect readout;
5. quotient further by the Xi ideal for chain-level divisor comparison.

Do not quotient the original source carrier or erase labels before constructing these maps.

## Disposition

G4 itself should remain the faithful joint graph. But its failure-to-sew has a canonical phase-space quotient realization:

$$
\mathcal P_\partial/\operatorname{Graph}(T)
\cong H,
$$

with quotient coordinate \(x_+-Tx_-\). The final Evans/RH obstruction is precisely this defect class modulo the Xi ideal.