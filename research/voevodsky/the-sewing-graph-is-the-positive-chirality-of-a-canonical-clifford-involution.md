# The sewing graph is the positive chirality of a canonical Clifford involution

## Question

Can the phase-space quotient picture be encoded by a single bounded operator whose eigenspaces are the sewn and defect sectors?

## Claim boundary

Yes. The sewing operator determines a canonical self-adjoint unitary on doubled boundary phase space. Its positive eigenspace is the sewing graph, its negative eigenspace is the defect graph, and it anticommutes with the Green-sign involution. The Evans defect energy is exactly its negative-chirality energy.

## Canonical involution

Let \(T:H\to H\) be unitary. On \(H\oplus H\), define

$$
\mathcal S_T
=
\begin{pmatrix}
0&T^*\\
T&0
\end{pmatrix}.
$$

Then

$$
\mathcal S_T^*=\mathcal S_T,
$$

and

$$
\mathcal S_T^2
=
\begin{pmatrix}T^*T&0\\0&TT^*\end{pmatrix}
=I.
$$

Thus \(\mathcal S_T\) is a self-adjoint unitary involution.

## Eigenspaces

The equation

$$
\mathcal S_T(x,y)=(x,y)
$$

is equivalent to

$$
y=Tx.
$$

Therefore

$$
\ker(\mathcal S_T-I)=\operatorname{Graph}(T).
$$

Likewise,

$$
\ker(\mathcal S_T+I)
=
\{(x,-Tx):x\in H\}
=
\operatorname{Graph}(-T).
$$

This negative graph is the same transverse defect sector as
\(\{(-T^*k,k)\}\) after the change \(x=-T^*k\).

## Orthogonal projectors

The spectral projectors are

$$
P_+
=\frac12(I+\mathcal S_T)
=
\frac12
\begin{pmatrix}
I&T^*\\
T&I
\end{pmatrix},
$$

$$
P_-
=\frac12(I-\mathcal S_T)
=
\frac12
\begin{pmatrix}
I&-T^*\\
-T&I
\end{pmatrix}.
$$

For \(e=(x,y)\),

$$
P_-e
=\frac12
\begin{pmatrix}
x-T^*y\\y-Tx
\end{pmatrix}
=
\frac12
\begin{pmatrix}-T^*d\\d\end{pmatrix},
$$

where \(d=y-Tx\).

Hence

$$
\boxed{
\|P_-e\|^2
=\frac12\|d\|^2.
}
$$

This is exactly the previously derived quotient distance.

## Sewing as chirality

A boundary pair is sewn exactly when

$$
P_-e=0,
$$

or equivalently

$$
\mathcal S_Te=e.
$$

Thus the sewing condition is positive chirality, while the quotient defect is the negative-chirality component.

For a holomorphic Evans family, chain promotion is

$$
P_-e(z)\in\tau\mathcal O(H\oplus H).
$$

The four Fourier-character defect classes are the simultaneous decomposition of this negative-chirality section under the commuting boundary Fourier action.

## Clifford relation with Green sign

Let

$$
\mathcal J
=
\begin{pmatrix}I&0\\0&-I\end{pmatrix}
$$

represent the Green boundary form. Direct multiplication gives

$$
\boxed{
\mathcal J\mathcal S_T+
\mathcal S_T\mathcal J=0.
}
$$

Also

$$
\mathcal J^2=I,
\qquad
\mathcal S_T^2=I.
$$

Therefore the Green sign and sewing chirality generate a canonical complex Clifford/hyperbolic two-generator structure on boundary phase space.

The anticommutation explains why \(\mathcal J\) exchanges the sewn and defect chiralities and why its quadratic flux is a mixed pairing rather than a positive defect norm.

## Coherencer interpretation

In this precise sense, G4 has a rung-four coherencer-like phase-space role:

- \(T\) carries the quarter-turn sewing;
- \(\mathcal S_T\) packages its graph as a polarization/chirality;
- \(\mathcal J\) carries the Green orientation;
- their Clifford relation controls passage between sewn and defect sectors;
- \(P_-\) is the obstruction projector.

This operator package lives over the faithful G4 response carrier; it is not a quotient that erases that carrier.

## Disposition

The phase-space exploration produces a canonical bounded obstruction operator:

$$
P_-=rac12
\begin{pmatrix}I&-T^*\\-T&I\end{pmatrix}.
$$

Its kernel is exactly the G4 sewing graph, its norm is the sewing-defect distance, and modulo Xi its Evans image is the complete chain obstruction. The Green involution anticommutes with sewing chirality, giving the quotient geometry a canonical Clifford structure.