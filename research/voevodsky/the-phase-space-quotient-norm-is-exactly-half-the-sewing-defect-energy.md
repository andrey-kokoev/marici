# The phase-space quotient norm is exactly half the sewing-defect energy

## Question

Does the ordinary quotient by the sewing graph carry a canonical quantitative norm, and how is it related to distance from the maximal-isotropic boundary condition?

## Claim boundary

Yes on the response Hilbert rung. The quotient norm is exactly \(2^{-1/2}\) times the norm of the defect \(y-Tx\). Equivalently, squared distance to the sewing graph is one half of the defect energy. This supplies a canonical nonnegative measure of Evans sewing failure without choosing a complement.

## Hilbert phase space

Equip

$$
\mathcal P_\partial=H\oplus H
$$

with the positive Hilbert norm

$$
\|(x,y)\|_\oplus^2
=\|x\|^2+\|y\|^2.
$$

Let

$$
\Lambda_T=\{(h,Th):h\in H\}
$$

for unitary \(T\), and define

$$
d_T(x,y)=y-Tx.
$$

## Quotient minimization

Fix a defect \(d\in H\). Every representative of its quotient class has

$$
y=Tx+d.
$$

Its energy is

$$
F_d(x)=\|x\|^2+\|Tx+d\|^2.
$$

Using unitarity and completing the square,

$$
F_d(x)
=2\left\|x+\frac12T^*d\right\|^2
+\frac12\|d\|^2.
$$

Therefore the unique minimal representative is

$$
\boxed{
\left(-\frac12T^*d,\frac12d\right),
}
$$

and

$$
\boxed{
\|[(x,y)]\|_{\mathcal P_\partial/\Lambda_T}
=\frac1{\sqrt2}\|y-Tx\|.
}
$$

## Orthogonal transverse space

The positive-Hilbert orthogonal complement of \(\Lambda_T\) is

$$
\Lambda_T^{\perp_\oplus}
=
\{(-T^*k,k):k\in H\}.
$$

The minimal representative above lies in this space with \(k=d/2\). Hence the quotient has a canonical orthogonal realization, even though the Green-form orthogonal complement of the maximal-isotropic graph equals the graph itself.

The positive Hilbert orthogonal and indefinite Green orthogonal must not be conflated.

## Distance formula

For an arbitrary boundary pair,

$$
\boxed{
\operatorname{dist}\bigl((x,y),\Lambda_T\bigr)^2
=\frac12\|y-Tx\|^2.
}
$$

The closest sewn pair is

$$
\left(
\frac12(x+T^*y),
\frac12(Tx+y)
\right).
$$

## Evans defect energy

For \(e=(e_-,e_+)\), define

$$
\mathcal E_{\rm def}(e)
=\frac12\|e_+-Te_-\|^2.
$$

Then

$$
\mathcal E_{\rm def}(e)=0
\quad\Longleftrightarrow\quad
e\in\Lambda_T.
$$

Thus Evans sewing is equivalent to zero distance from the G4 sewing graph. Unlike an indefinite boundary flux, this defect energy is manifestly nonnegative.

## Character decomposition

Since the Fourier projectors are orthogonal,

$$
\mathcal E_{\rm def}(e)
=
\frac12\sum_{\lambda\in\mu_4}
\|P_\lambda e_+-\lambda P_\lambda e_-\|^2.
$$

Every term is nonnegative. This gives a quantitative strengthening of the statement that character defects cannot cancel.

## Holomorphic/Xi boundary

At a divisor point \(z_0\) of multiplicity \(m\), chain promotion requires the defect and its first \(m-1\) derivatives to vanish. Equivalently, every jet-distance energy

$$
\frac12\left\|
\partial_z^j(e_+-Te_-)(z_0)
\right\|^2
$$

vanishes. These are pointwise diagnostics; holomorphic Xi-divisibility remains the invariant global statement.

## Disposition

The ordinary phase-space quotient is not merely an abstract defect carrier. Its canonical Hilbert quotient norm is exactly the distance to the sewing graph, with squared norm \(\|e_+-Te_-\|^2/2\). The four Fourier-character contributions form a sum of nonnegative defect energies.