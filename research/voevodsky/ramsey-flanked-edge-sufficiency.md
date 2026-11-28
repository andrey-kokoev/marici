# Construct a minimum two-link repair from a flanked, clear blue edge

Write the four columns as `u,x,z,v` in path order (or its reversal). The missed edge `uv` is blue on the outside pentagon. Neither site of the other movable pair is physically adjacent to u or v. In the remaining outside triple let ab be its only red edge and h the third site. In the pentagon h is red to both u and v and blue to a and b. Assign the other movable pair names y,w so that a is not adjacent to y and b is not adjacent to w. This is always possible: each of a,b can forbid at most one of two consecutive columns, and no site of the movable pair can be adjacent to both a and b unless it uses its other path neighbor, already occupied by its movable partner. Thus the forbidden assignments form at most a matching in a two-by-two table.

Use P={x,h,b}, Q={x,h,a}, L={z,y,a}, R={z,w,b}. Link P to L and Q to R in red. All four supports are separated and free of red edges: x,z have no other physical neighbors but each other and the flanking sites; y,w are not path neighbors of x,z. The matched supports are disjoint and hit every square corner between them (they use both x and z). Hence no red triangle arises, including through a square port. Leave other new-port links blue.

**Necessity of each link.** P,Q,L with u,v,w and square port (f,x,y) gives a blue seven unless P–L is red. Its other two port links are forced blue by shared support. Likewise P,Q,R with u,v,y and (f,x,w) forces Q–R. The clear-axis condition gives the needed blue site edges.

**No blue seven after repair.** Three new ports include a matched red link. For one new port, at most two outside pentagon sites can join it in blue. At most three square ports can join it, since it misses a corner. With zero, one, two or three square ports, the number of covered sites available in blue is at most three, two, one or zero. Thus a blue set with one new port has size at most six. With zero, use legality of the original square.

It remains to bound old vertices in a blue set through two unmatched new ports:

- P,Q: the only missed outside sites are u,v. With at most one of these, the usual three-vertex covered-site/port bound suffices. With both, z is excluded by a red path edge. Apart from the outside sites, at most two old vertices remain mutually blue: without square ports take at most f and one Y site; one port excludes f and one Y site; both common ports exclude all three.
- L,R: the missed outside sites are h,u,v. Only u,v can be used as a blue pair. With both, x is excluded. Only f is left among covered sites; it cannot join a square port. The only common square ports are the two through z. With at most one outside site use the usual three-vertex bound.
- P,R or Q,L: both x and z and one Y site are covered by the two rows. At most two covered sites remain (f and the other Y site). There is just one common square port, which excludes f. Thus at most two covered sites and square ports combined can join the two new ports, plus at most two outside sites.

Each unmatched pair can therefore join at most four old vertices. This proves sufficiency without testing candidate rows or enumerating cycles.
