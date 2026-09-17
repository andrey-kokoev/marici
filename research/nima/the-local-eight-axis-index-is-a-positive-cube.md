# The local eight-axis index is a positive cube

The local coordinate geometry is

$$
\mathcal P_8=[0,1]^8
$$

with ordered coordinates

$$
(H,V,D,q,L,C,O,R).
$$

Its canonical form is

$$
\Omega_8
=
\bigwedge_{a=1}^{8}
d\log\frac{x_a}{1-x_a}.
$$

The cubical face vector is

$$
(256,1024,1792,1792,1120,448,112,16,1).
$$

The Freudenthal triangulation has

$$
8!=40320
$$

oriented maximal simplices. The signed simplicial boundary cancels every interior facet and leaves

$$
16\cdot7!=80640
$$

oriented boundary simplices. The cubical boundary operator satisfies

$$
\partial^2=0.
$$

Each maximal simplex is one total order of the eight generators. The history representation assigns a distinct path map to each simplex.

Named codimension-six square decorations include:

| Face | Coefficient |
|---|---|
| $$H\times V$$ | strict Beck--Chevalley cell |
| $$D\times L$$ | left/right successor dagger cell |
| $$q\times R$$ | leakage cell |
| $$L\times O$$ | endpoint multiplier naturality |
| $$C\times R$$ | forward realization/completion naturality |

The leakage coefficient is

$$
A_X=P_X\mathcal F(I-P_X).
$$

The positive cube supplies the incidence and residue scaffold. An operator-valued canonical form assigns maps to edges, comparison cells to squares, and higher modifications to higher faces. Completing that form requires a decoration registry for all face types and verification that its operator residues agree on shared boundaries.

The checker `check_eight_axis_positive_cube.py` verifies the face vector, all 40320 simplex orientations, cancellation of interior facets, the 80640 triangulated boundary facets, and the cubical identity.
