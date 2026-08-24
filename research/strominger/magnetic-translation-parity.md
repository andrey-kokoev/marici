# Transfer parity is an endpoint collision on the depth-two lattice

At newly admitted pole depth `a`, the minus branch begins at target row

\[
r_-=-a-g.
\]

The translated plus branch begins at

\[
r_+=-a-g+q.
\]

An older minus column `d` pole pairs behind has depth `a-2d` and begins at

\[
r_-^{\mathrm{old}}=-a+2d-g.
\]

The endpoint collision equation is therefore

\[
r_+=r_-^{\mathrm{old}}
\quad\Longleftrightarrow\quad
d=\frac q2.
\]

For odd `q`, there is no integral solution.  The Hall extension can use the
left endpoint `B0` of both new branches.  Their product is

\[
-(a^{\overline g})^2
(a+g-q-1)(a+g+q-1),
\]

which is exactly the odd stable character.

For even `q=2w`, the plus endpoint collides exactly with the minus endpoint
`w` pole pairs behind.  The Hall extension must move one row inward to `B1`:

\[
r_+^{\mathrm{repair}}=-a-g+q+1.
\]

This row has opposite parity from every minus endpoint, so it cannot collide
again.  Its coefficient is the adjacent response `X`.  Consequently:

\[
\boxed{
\text{odd q}: B0/B0 endpoint localization,
\qquad
\text{even q}: B0/B1 Schur response.
}
\]

The collision occurs exactly `w=floor(q/2)` pole pairs behind, giving the
previously observed memory law a direct arithmetic explanation.

This mechanism is hard to vary.  It uses the pole-depth spacing two forced by
the admitted even lattice.  On a unit-spaced pole lattice every integer `q`
would collide, and the even/odd split would disappear.

The theorem concerns support selection and endpoint characters.  For the even
lane, converting the raw `B1` response into the normalized positive scalar
transfer still uses the finite Schur elimination established separately.
