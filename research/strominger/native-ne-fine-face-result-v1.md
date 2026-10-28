# The retained NE5->15 interface is the actual fine face F736

Registered before lookup in net revision38 and
`contracts/native-ne-fine-face-attempt.v1.json`.

## Full coordinate bridge

For signed coordinates x with sum(x)=1 and x_i<=2, set

    b_i = 2-x_i,
    v = (b_0, b_0+b_1, b_0+b_1+b_2).

Then b_i>=0, sum(b_i)=7 and0<=v_0<=v_1<=v_2<=7. The inverse is
`b=(v_0,v_1-v_0,v_2-v_1,7-v_2)`, `x=2-b`.

The checker independently generates the native target primitives and the
ordered-chamber attachment complex. Their complete343 primitive sets match
exactly under this bridge, not merely their counts. Every coordinate inverts.
The authoritative prototype binding is recomputed and matched to its retained
assignment/face tables before selecting the native face.

## Actual lookup

The face of retained NE operation15, from neutron packet5 to electron packet15,
is **F736**, with vertices **V104,V111,V113**.

| Native packet | Native source cell | Target component | Fine tetrahedron | Source registry | Local role |
| --- | ---: | ---: | --- | --- | --- |
|5 (N)|1|329|T325|esd7:4,5,5|H134|
|15 (E)|5|330|T324|esd7:5,4,5|H134|

The triangle's composite route is **E514 then E539**; its direct edge is
**E515**. Both incident roles are the source's **regulator-transport face with
Hermitian and skew placement coordinates**. This is not the earlier F006
H234/H123 comparison, and tetrahedron/component identifiers are not zipped by
position.

External C0=(-3,1,3,0) maps to cumulative coordinates(5,6,5), outside the ordered
chamber because6>5. It receives no fabricated internal vertex ID. Its previously
constructed finite flux readout remains a coefficient functional, not a spatial
identification with a Mellin endpoint.

## Result and remaining gate

Thirteen checks pass. The native shared-face identity and both registry contexts
are established. The registry still records the analytical comparison and
homotopy as undischarged.

The remaining concrete obligation is the **H134 regulator-transport comparison
on F736**, not another generic endpoint or geometry comparison. Bind source
operators for E514,E539,E515 in both incident presentations, three fine-vertex
comparison frames and their retained endpoint/flux readouts on admitted domains.
Then evaluate the intended source residual and its Hermitian/skew placement
witnesses. Native NE transports between the two tetrahedral presentations across
the face; it is not the triangle's two-edge-versus-direct-edge filler.

In particular, the old faithful-whiskering H234 argument must not be substituted
for these H134 data. No identity defaults, completed Pb target or new regulator
commutation assumptions are installed by this lookup.

## Reproduce

```sh
python research/strominger/checkers/check_native_ne_fine_face.py
```

`results/native-ne-fine-face/binding.json` retains the actual operation, incident
packets, full face contexts, external coordinates and typed missing inputs.
`results/native-ne-fine-face/verification.json` retains live source provenance.
