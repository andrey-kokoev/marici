//! Exact integral audit of the global Möbius orientation quotient against the
//! local D=03 three-road costalk.
//!
//! Entry 91 identifies the Cut nerve with the eight-vertex Möbius ladder
//! Gamma_8.  Its four zero-core square boundaries span a saturated lattice S
//! in H_1(Gamma_8), and L_or=H_1/S is an integral line.  This checker:
//!
//! * constructs a primitive quotient coordinate, with outer octagon = 2g;
//! * computes D8 transport and the polarity-loaded character;
//! * restricts to the actual D=03 stabilizer and compares with chi_N;
//! * tests whether cellular restriction to the three incident roads descends
//!   through L_or, and whether it canonically determines the six supports of
//!   entry 66's alternating conductor.
//!
//! No Gysin map is introduced unless it is induced by the cellular graph.

use std::collections::BTreeMap;

const N: usize = 8;
type Int = i64;
type Matrix = Vec<Vec<Int>>;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

fn edge(a: usize, b: usize) -> Edge {
    if a < b {
        Edge(a, b)
    } else {
        Edge(b, a)
    }
}

fn crosses(a: Edge, b: Edge) -> bool {
    if a.0 == b.0 || a.0 == b.1 || a.1 == b.0 || a.1 == b.1 {
        return false;
    }
    (a.0 < b.0 && b.0 < a.1 && a.1 < b.1) || (b.0 < a.0 && a.0 < b.1 && b.1 < a.1)
}

fn physical_diagonal(i: usize) -> Edge {
    edge(i % N, (i + 3) % N)
}

fn physical_label(value: Edge) -> usize {
    (0..N).find(|&i| physical_diagonal(i) == value).unwrap()
}

fn transform_vertex(i: usize, reflected: bool, shift: usize) -> usize {
    if reflected {
        (shift + N - i) % N
    } else {
        (i + shift) % N
    }
}

fn transform_edge(value: Edge, reflected: bool, shift: usize) -> Edge {
    edge(
        transform_vertex(value.0, reflected, shift),
        transform_vertex(value.1, reflected, shift),
    )
}

fn physical_target(i: usize, reflected: bool, shift: usize) -> usize {
    physical_label(transform_edge(physical_diagonal(i), reflected, shift))
}

fn graph_edges() -> Vec<(usize, usize)> {
    let physicals: Vec<_> = (0..N).map(physical_diagonal).collect();
    let mut result = Vec::new();
    for i in 0..N {
        for j in i + 1..N {
            if !crosses(physicals[i], physicals[j]) {
                result.push((i, j));
            }
        }
    }
    assert_eq!(result.len(), 12);
    result
}

fn graph_cycle(vertices: &[usize], edges: &[(usize, usize)]) -> Vec<Int> {
    let index: BTreeMap<_, _> = edges
        .iter()
        .copied()
        .enumerate()
        .map(|(i, value)| (value, i))
        .collect();
    let mut result = vec![0; edges.len()];
    for i in 0..vertices.len() {
        let a = vertices[i];
        let b = vertices[(i + 1) % vertices.len()];
        let value = if a < b { (a, b) } else { (b, a) };
        result[index[&value]] += if a < b { 1 } else { -1 };
    }
    result
}

fn graph_boundary(chain: &[Int], edges: &[(usize, usize)]) -> Vec<Int> {
    let mut result = vec![0; N];
    for (&coefficient, &(a, b)) in chain.iter().zip(edges) {
        result[a] -= coefficient;
        result[b] += coefficient;
    }
    result
}

fn transform_chain(
    chain: &[Int],
    edges: &[(usize, usize)],
    reflected: bool,
    shift: usize,
) -> Vec<Int> {
    let index: BTreeMap<_, _> = edges
        .iter()
        .copied()
        .enumerate()
        .map(|(i, value)| (value, i))
        .collect();
    let mut result = vec![0; edges.len()];
    for (i, &(a, b)) in edges.iter().enumerate() {
        let x = physical_target(a, reflected, shift);
        let y = physical_target(b, reflected, shift);
        let value = if x < y { (x, y) } else { (y, x) };
        result[index[&value]] += chain[i] * if x < y { 1 } else { -1 };
    }
    result
}

fn determinant(mut a: Matrix) -> Int {
    let n = a.len();
    if n == 0 {
        return 1;
    }
    assert!(a.iter().all(|row| row.len() == n));
    let mut sign = 1;
    let mut previous = 1;
    for k in 0..n - 1 {
        let Some(pivot) = (k..n).find(|&row| a[row][k] != 0) else {
            return 0;
        };
        if pivot != k {
            a.swap(k, pivot);
            sign = -sign;
        }
        let p = a[k][k];
        for i in k + 1..n {
            for j in k + 1..n {
                let numerator = a[i][j] * p - a[i][k] * a[k][j];
                assert_eq!(numerator % previous, 0);
                a[i][j] = numerator / previous;
            }
        }
        previous = p;
    }
    sign * a[n - 1][n - 1]
}

fn gcd(a: Int, b: Int) -> Int {
    if b == 0 {
        a.abs()
    } else {
        gcd(b, a % b)
    }
}

fn unit_smith_rank(value: &Matrix) -> usize {
    if value.is_empty() || value[0].is_empty() {
        return 0;
    }
    let mut a = value.clone();
    let rows = a.len();
    let columns = a[0].len();
    let mut p = 0;
    while p < rows && p < columns {
        let found =
            (p..rows).find_map(|i| (p..columns).find(|&j| a[i][j].abs() == 1).map(|j| (i, j)));
        let Some((i0, j0)) = found else { break };
        a.swap(p, i0);
        for row in &mut a {
            row.swap(p, j0);
        }
        if a[p][p] == -1 {
            for x in &mut a[p] {
                *x = -*x;
            }
        }
        for i in 0..rows {
            if i == p {
                continue;
            }
            let q = a[i][p];
            for j in p..columns {
                a[i][j] -= q * a[p][j];
            }
        }
        for j in 0..columns {
            if j == p {
                continue;
            }
            let q = a[p][j];
            for i in 0..rows {
                a[i][j] -= q * a[i][p];
            }
        }
        p += 1;
    }
    assert!(a[p..]
        .iter()
        .all(|row| row[p.min(columns)..].iter().all(|&x| x == 0)));
    p
}

fn find(parent: &mut [usize], x: usize) -> usize {
    if parent[x] != x {
        parent[x] = find(parent, parent[x]);
    }
    parent[x]
}

fn tree_path(
    current: usize,
    target: usize,
    parent_vertex: Option<usize>,
    adjacency: &[Vec<usize>],
) -> Option<Vec<usize>> {
    if current == target {
        return Some(vec![current]);
    }
    for &next in &adjacency[current] {
        if Some(next) == parent_vertex {
            continue;
        }
        if let Some(mut tail) = tree_path(next, target, Some(current), adjacency) {
            let mut result = vec![current];
            result.append(&mut tail);
            return Some(result);
        }
    }
    None
}

fn add_scaled(target: &mut [Int], source: &[Int], coefficient: Int) {
    for (x, &y) in target.iter_mut().zip(source) {
        *x += coefficient * y;
    }
}

fn chord_coordinates(chain: &[Int], chords: &[usize]) -> Vec<Int> {
    chords.iter().map(|&i| chain[i]).collect()
}

fn dot(a: &[Int], b: &[Int]) -> Int {
    a.iter().zip(b).map(|(x, y)| x * y).sum()
}

fn egcd_nonnegative(a: Int, b: Int) -> (Int, Int, Int) {
    if b == 0 {
        (a, 1, 0)
    } else {
        let (g, x, y) = egcd_nonnegative(b, a % b);
        (g, y, x - (a / b) * y)
    }
}

fn bezout(values: &[Int]) -> Vec<Int> {
    let mut coefficients = vec![0; values.len()];
    let mut current_gcd = 0;
    for (i, &value) in values.iter().enumerate() {
        if value == 0 {
            continue;
        }
        if current_gcd == 0 {
            current_gcd = value.abs();
            coefficients[i] = value.signum();
            continue;
        }
        let (new_gcd, x, y) = egcd_nonnegative(current_gcd, value.abs());
        for coefficient in &mut coefficients[..i] {
            *coefficient *= x;
        }
        coefficients[i] = y * value.signum();
        current_gcd = new_gcd;
    }
    assert_eq!(current_gcd, 1);
    assert_eq!(dot(values, &coefficients), 1);
    coefficients
}

fn local_road_restriction(chain: &[Int], edges: &[(usize, usize)]) -> [Int; 3] {
    let index: BTreeMap<_, _> = edges
        .iter()
        .copied()
        .enumerate()
        .map(|(i, value)| (value, i))
        .collect();
    // The three roads incident at D=03=p_0 are p_3,p_4,p_5, ordered by the
    // ambient cyclic orientation. All corresponding graph edges are 0 -> j.
    std::array::from_fn(|i| chain[index[&(0, i + 3)]])
}

fn conductor_supports(roads: [Int; 3]) -> [Int; 6] {
    // Entry 66: d0=dx5-dx2, d1=dx3-dx0, d2=dx1-dx4.
    let [d0, d1, d2] = roads;
    [-d1, d2, -d0, d1, -d2, d0]
}

fn permutation_sign(permutation: &[usize]) -> Int {
    let inversions = (0..permutation.len())
        .map(|i| {
            (i + 1..permutation.len())
                .filter(|&j| permutation[i] > permutation[j])
                .count()
        })
        .sum::<usize>();
    if inversions % 2 == 0 {
        1
    } else {
        -1
    }
}

fn main() {
    let edges = graph_edges();

    // Spanning-tree/chord coordinates identify H1(Gamma8;Z) with Z^5.
    let mut parent: Vec<_> = (0..N).collect();
    let mut tree_indices = Vec::new();
    let mut chords = Vec::new();
    for (index, &(a, b)) in edges.iter().enumerate() {
        let ra = find(&mut parent, a);
        let rb = find(&mut parent, b);
        if ra != rb {
            parent[ra] = rb;
            tree_indices.push(index);
        } else {
            chords.push(index);
        }
    }
    assert_eq!((tree_indices.len(), chords.len()), (7, 5));
    let mut tree_adjacency = vec![Vec::new(); N];
    for &index in &tree_indices {
        let (a, b) = edges[index];
        tree_adjacency[a].push(b);
        tree_adjacency[b].push(a);
    }
    let mut fundamental = Vec::new();
    for (chord_position, &index) in chords.iter().enumerate() {
        let (a, b) = edges[index];
        let path = tree_path(b, a, None, &tree_adjacency).unwrap();
        let mut vertices = vec![a];
        vertices.extend_from_slice(&path[..path.len() - 1]);
        let cycle = graph_cycle(&vertices, &edges);
        assert!(graph_boundary(&cycle, &edges).iter().all(|&x| x == 0));
        let coordinates = chord_coordinates(&cycle, &chords);
        assert_eq!(coordinates[chord_position], 1);
        assert_eq!(coordinates.iter().filter(|&&x| x != 0).count(), 1);
        fundamental.push(cycle);
    }

    let outer_vertices: Vec<_> = (0..N).map(|j| (3 * j) % N).collect();
    let outer = graph_cycle(&outer_vertices, &edges);
    let square_vertices: Vec<Vec<usize>> = (0..4)
        .map(|j| {
            let q = |offset: usize| (3 * (j + offset)) % N;
            vec![q(0), q(1), q(5), q(4)]
        })
        .collect();
    let squares: Vec<_> = square_vertices
        .iter()
        .map(|v| graph_cycle(v, &edges))
        .collect();
    let square_matrix: Matrix = chords
        .iter()
        .map(|&row| squares.iter().map(|cycle| cycle[row]).collect())
        .collect();
    assert_eq!(unit_smith_rank(&square_matrix), 4);

    // The signed maximal minors are a primitive generator of the left kernel
    // of the saturated 5x4 square matrix: the exact quotient coordinate ell.
    let mut quotient_coordinate = Vec::new();
    for omitted in 0..5 {
        let minor: Matrix = square_matrix
            .iter()
            .enumerate()
            .filter(|(row, _)| *row != omitted)
            .map(|(_, row)| row.clone())
            .collect();
        quotient_coordinate.push(if omitted % 2 == 0 {
            determinant(minor)
        } else {
            -determinant(minor)
        });
    }
    let divisor = quotient_coordinate.iter().fold(0, |a, &b| gcd(a, b));
    for value in &mut quotient_coordinate {
        *value /= divisor;
    }
    assert_eq!(quotient_coordinate.iter().fold(0, |a, &b| gcd(a, b)), 1);
    for column in 0..4 {
        let square_column: Vec<_> = square_matrix.iter().map(|row| row[column]).collect();
        assert_eq!(dot(&quotient_coordinate, &square_column), 0);
    }
    let outer_coordinates = chord_coordinates(&outer, &chords);
    if dot(&quotient_coordinate, &outer_coordinates) < 0 {
        for value in &mut quotient_coordinate {
            *value = -*value;
        }
    }
    assert_eq!(dot(&quotient_coordinate, &outer_coordinates), 2);

    // Construct an explicit primitive cycle g with ell(g)=1.
    let primitive_chord_coordinates = bezout(&quotient_coordinate);
    let mut primitive_cycle = vec![0; edges.len()];
    for (coefficient, cycle) in primitive_chord_coordinates.iter().zip(&fundamental) {
        add_scaled(&mut primitive_cycle, cycle, *coefficient);
    }
    assert!(graph_boundary(&primitive_cycle, &edges)
        .iter()
        .all(|&x| x == 0));
    assert_eq!(
        dot(
            &quotient_coordinate,
            &chord_coordinates(&primitive_cycle, &chords)
        ),
        1
    );

    // Full D8 transport on the quotient. The un-loaded line is the global
    // orientation character. Tensoring shift parity gives the loaded line.
    let mut d8_transport = Vec::new();
    for reflected in [false, true] {
        for shift in 0..N {
            let orientation_sign = if reflected { -1 } else { 1 };
            for (basis_index, cycle) in fundamental.iter().enumerate() {
                let transformed = transform_chain(cycle, &edges, reflected, shift);
                let transformed_value = dot(
                    &quotient_coordinate,
                    &chord_coordinates(&transformed, &chords),
                );
                assert_eq!(
                    transformed_value,
                    orientation_sign * quotient_coordinate[basis_index]
                );
            }
            let polarity_sign = if shift % 2 == 0 { 1 } else { -1 };
            let loaded_sign = orientation_sign * polarity_sign;
            d8_transport.push((
                reflected,
                shift,
                orientation_sign,
                polarity_sign,
                loaded_sign,
            ));
        }
    }

    // The actual D8 stabilizer of D=03=p0 has only two elements. Its
    // reflection f_3 simultaneously swaps roads p3<->p5 and exchanges
    // polarity. It therefore tests only the product of the two local signs.
    let stabilizer: Vec<_> = d8_transport
        .iter()
        .copied()
        .filter(|&(reflected, shift, _, _, _)| physical_target(0, reflected, shift) == 0)
        .collect();
    assert_eq!(stabilizer.len(), 2);
    let roads = [3_usize, 4, 5];
    let mut stabilizer_audit = Vec::new();
    for &(reflected, shift, orientation_sign, polarity_sign, loaded_sign) in &stabilizer {
        let road_permutation: Vec<_> = roads
            .iter()
            .map(|&road| {
                let target = physical_target(road, reflected, shift);
                roads
                    .iter()
                    .position(|&candidate| candidate == target)
                    .unwrap()
            })
            .collect();
        let road_orientation = permutation_sign(&road_permutation);
        let chi_n_composite = road_orientation * polarity_sign;
        assert_eq!(orientation_sign, road_orientation);
        assert_eq!(loaded_sign, chi_n_composite);
        stabilizer_audit.push((reflected, shift, road_permutation, loaded_sign));
    }
    assert!(stabilizer_audit
        .iter()
        .any(|entry| entry.0 && entry.1 == 3 && entry.2 == vec![2, 1, 0] && entry.3 == 1));

    // No D8 stabilizer element gives a three-cycle of the roads, a pure road
    // reflection without polarity exchange, or pure polarity exchange with
    // roads fixed. Hence D8 alone cannot separate the three chi_N generator
    // signs. With the independently established polarity deck involution,
    // however, the abstract line character is (+1,-1,-1): C3 rotations must
    // act +1 on an integral line, L_or supplies road reflection -1, and the
    // polarity line supplies core exchange -1.
    assert!(!stabilizer_audit
        .iter()
        .any(|entry| entry.2 == vec![1, 2, 0] || entry.2 == vec![2, 0, 1]));
    let abstract_local_character = (1, -1, -1);

    // Cellular restriction to the D03 star lands in the local A2 road
    // lattice, by the cycle boundary equation at p0.
    for cycle in &fundamental {
        assert_eq!(local_road_restriction(cycle, &edges).iter().sum::<Int>(), 0);
    }
    let square_restrictions: Vec<_> = squares
        .iter()
        .map(|cycle| local_road_restriction(cycle, &edges))
        .collect();
    let square_restriction_matrix: Matrix = (0..3)
        .map(|row| square_restrictions.iter().map(|value| value[row]).collect())
        .collect();
    assert_eq!(unit_smith_rank(&square_restriction_matrix), 2);
    // The image is the full saturated A2 lattice: two displayed differences
    // occur as integer combinations (Smith factors are all one).
    assert!(square_restrictions.iter().any(|value| *value != [0, 0, 0]));

    // Passing both sides to primitive quotients does give a commutative
    // square H1/S -> P_D/A2, but its bottom map is zero. Every graph cycle
    // satisfies conservation at p0, so its three road coefficients have
    // augmentation zero. It is not a primitive road counit.
    for cycle in &fundamental {
        assert_eq!(local_road_restriction(cycle, &edges).iter().sum::<Int>(), 0);
    }

    // Two representatives of the same primitive quotient class have
    // different local restrictions. Thus raw cellular restriction does not
    // descend through H1 -> L_or.
    let primitive_restriction = local_road_restriction(&primitive_cycle, &edges);
    let witness_square = squares
        .iter()
        .find(|cycle| local_road_restriction(cycle, &edges) != [0, 0, 0])
        .unwrap();
    let mut second_representative = primitive_cycle.clone();
    add_scaled(&mut second_representative, witness_square, 1);
    assert_eq!(
        dot(
            &quotient_coordinate,
            &chord_coordinates(&second_representative, &chords)
        ),
        1
    );
    let second_restriction = local_road_restriction(&second_representative, &edges);
    assert_ne!(primitive_restriction, second_restriction);

    // Character alone allows a rank-one family of stabilizer-equivariant maps
    // from the loaded line (trivial on the composite f3) to local A2: its
    // fixed lattice under road reversal is Z*(1,-2,1). No scale or sign is
    // selected by the character.
    let invariant_local_generator = [1, -2, 1];
    assert_eq!(invariant_local_generator.iter().sum::<Int>(), 0);
    let reflected_local = [
        invariant_local_generator[2],
        invariant_local_generator[1],
        invariant_local_generator[0],
    ];
    assert_eq!(reflected_local, invariant_local_generator);

    // Entry 66 has six conductor supports. Even after choosing a local road
    // vector, its polarity-forgetting lift is nonunique: [I3 I3] has kernel
    // rank three and no nonzero integral polarity-equivariant section. The
    // entry-66 polarity-odd support embedding is explicit, but changing the
    // representative by S changes its six-vector.
    let plus_minus_restriction: Matrix = vec![
        vec![1, 0, 0, 1, 0, 0],
        vec![0, 1, 0, 0, 1, 0],
        vec![0, 0, 1, 0, 0, 1],
    ];
    assert_eq!(unit_smith_rank(&plus_minus_restriction), 3);
    let polarity_kernel = [
        [1, 0, 0, -1, 0, 0],
        [0, 1, 0, 0, -1, 0],
        [0, 0, 1, 0, 0, -1],
    ];
    for vector in polarity_kernel {
        let image: Vec<Int> = plus_minus_restriction
            .iter()
            .map(|row| dot(row, &vector))
            .collect();
        assert_eq!(image, vec![0, 0, 0]);
    }
    // A polarity-fixed section would have a=b and therefore 2a=v; it cannot
    // lift the primitive vector (1,-2,1) integrally. A polarity-odd lift has
    // a=-b and restricts to zero.
    assert!(invariant_local_generator.iter().any(|value| value % 2 != 0));
    let first_six = conductor_supports(primitive_restriction);
    let second_six = conductor_supports(second_restriction);
    assert_ne!(first_six, second_six);

    println!("n=8 global orientation to D03 costalk audit: PASS");
    println!("primitive_quotient_coordinate_on_chords={quotient_coordinate:?}");
    println!("primitive_cycle_chord_coordinates={primitive_chord_coordinates:?} quotient_value=1");
    println!("outer_octagon_quotient_value=2");
    println!("D8_transport=(orientation=(-1)^reflection, polarity=(-1)^shift, loaded=product)");
    println!("D03_stabilizer={stabilizer_audit:?}");
    println!("abstract_local_loaded_character_rotation_reflection_core={abstract_local_character:?} MATCH_chi_N");
    println!("D8_stabilizer_separates_local_generators=false only_composite_reflection_times_core_is_seen");
    println!("square_restrictions_to_D03_roads={square_restrictions:?} rank=2 saturated_A2=true");
    println!("primitive_same_class_restriction_witness={primitive_restriction:?} vs {second_restriction:?}");
    println!("cellular_restriction_descends_to_L_or=false");
    println!(
        "induced_L_or_to_P_over_A2=zero image_rank=0 cokernel_rank=1 index=infinite sign=undefined"
    );
    println!("Hom_stabilizer(L_loaded,A2_local)=Z generator={invariant_local_generator:?} canonical_scale=false");
    println!("six_support_witness={first_six:?} vs {second_six:?}");
    println!(
        "six_support_polarity_forgetting_kernel_rank=3 equivariant_integral_section=none_nonzero"
    );
    println!("sigma_alt_identification=NOT_TYPED character_match_only");
}
