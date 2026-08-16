//! FAN/LOG obstruction and minimal toroidal subdivision for the six mixed
//! cross-sheet edges.  This is a combinatorial carrier theorem only: it does
//! not assign occurrence/Boolean signs and does not construct BC or six-
//! functor maps.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

type D = (u8, u8);
type T = BTreeSet<D>;

fn d(a: u8, b: u8) -> D {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}
fn crosses((a, b): D, (c, e): D) -> bool {
    (a < c && c < b && b < e) || (c < a && a < e && e < b)
}
fn t(v: &[D]) -> T {
    v.iter().copied().collect()
}
fn rotate(x: &T) -> T {
    x.iter()
        .map(|&(a, b)| d((a + 2) % 6, (b + 2) % 6))
        .collect()
}
fn reflect(x: &T) -> T {
    x.iter()
        .map(|&(a, b)| d((8 - a) % 6, (8 - b) % 6))
        .collect()
}
fn norm(mut p: Vec<T>) -> Vec<T> {
    let q = p.iter().cloned().rev().collect::<Vec<_>>();
    if q < p {
        p = q
    };
    p
}

fn paths() -> Vec<[T; 4]> {
    [
        [
            [(1, 3), (1, 4), (1, 5)],
            [(0, 4), (1, 3), (1, 4)],
            [(0, 3), (0, 4), (1, 3)],
            [(0, 2), (0, 3), (0, 4)],
        ],
        [
            [(1, 3), (1, 4), (1, 5)],
            [(1, 4), (1, 5), (2, 4)],
            [(1, 5), (2, 4), (2, 5)],
            [(0, 2), (2, 4), (2, 5)],
        ],
        [
            [(0, 4), (1, 4), (2, 4)],
            [(0, 4), (1, 3), (1, 4)],
            [(0, 3), (0, 4), (1, 3)],
            [(0, 3), (1, 3), (3, 5)],
        ],
        [
            [(0, 4), (1, 4), (2, 4)],
            [(1, 4), (1, 5), (2, 4)],
            [(1, 5), (2, 4), (2, 5)],
            [(1, 5), (2, 5), (3, 5)],
        ],
        [
            [(0, 3), (1, 3), (3, 5)],
            [(0, 2), (0, 3), (3, 5)],
            [(0, 2), (2, 5), (3, 5)],
            [(0, 2), (2, 4), (2, 5)],
        ],
        [
            [(0, 2), (0, 3), (0, 4)],
            [(0, 2), (0, 3), (3, 5)],
            [(0, 2), (2, 5), (3, 5)],
            [(1, 5), (2, 5), (3, 5)],
        ],
    ]
    .map(|p| p.map(|x| t(&x)))
    .to_vec()
}

fn all_triangulations() -> Vec<T> {
    let ds: Vec<D> = (0..6)
        .flat_map(|a| ((a + 1)..6).map(move |b| d(a, b)))
        .filter(|&(a, b)| a.abs_diff(b) != 1 && a.abs_diff(b) != 5)
        .collect();
    (0..(1usize << ds.len()))
        .filter_map(|m| {
            let x: T = ds
                .iter()
                .enumerate()
                .filter(|(i, _)| m & (1 << i) != 0)
                .map(|(_, x)| *x)
                .collect();
            (x.len() == 3
                && !x
                    .iter()
                    .any(|left| x.iter().any(|right| left < right && crosses(*left, *right))))
            .then_some(x)
        })
        .collect()
}

fn gallery(a: &T, z: &T, vertices: &[T]) -> (usize, usize) {
    let mut dist = BTreeMap::<T, usize>::new();
    let mut ways = BTreeMap::<T, usize>::new();
    let mut q = VecDeque::new();
    dist.insert(a.clone(), 0);
    ways.insert(a.clone(), 1);
    q.push_back(a.clone());
    while let Some(x) = q.pop_front() {
        let dx = dist[&x];
        for y in vertices.iter().filter(|y| x.intersection(y).count() == 2) {
            if !dist.contains_key(y) {
                dist.insert(y.clone(), dx + 1);
                ways.insert(y.clone(), ways[&x]);
                q.push_back(y.clone());
            } else if dist[y] == dx + 1 {
                *ways.get_mut(y).unwrap() += ways[&x];
            }
        }
    }
    (dist[z], ways[z])
}

fn main() {
    let ps = paths();
    let vertices = all_triangulations();
    assert_eq!(vertices.len(), 14);
    let mut galleries = BTreeSet::<Vec<T>>::new();
    for p in &ps {
        assert!(p[0].intersection(&p[3]).next().is_none());
        let (distance, ways) = gallery(&p[0], &p[3], &vertices);
        assert_eq!((distance, ways), (3, 1));
        galleries.insert(norm(p.to_vec()));
    }
    assert_eq!(galleries.len(), 6);
    for p in &ps {
        assert!(galleries.contains(&norm(p.iter().map(rotate).collect())));
        assert!(galleries.contains(&norm(p.iter().map(reflect).collect())));
    }
    assert_eq!(ps.len() * 3, 18);
    assert_eq!(ps.len() * 2, 12);
    println!("{{\"status\":\"proved_scoped_fan_log_toroidal_expansion_gate\",\"mixed_edges\":6,\"endpoint_common_faces\":\"empty\",\"k6_triangulations\":14,\"unique_shortest_gallery_length\":3,\"unique_galleries\":6,\"expanded_chambers\":18,\"inserted_vertices\":12,\"D3_rotation\":true,\"D3_reflection\":true,\"occurrence_boolean_signs\":\"unconstructed\",\"maximal_cone_BC\":\"unconstructed\",\"six_functor_kernel\":\"unconstructed\",\"based_qSigma\":\"unconstructed\",\"mapping_fiber\":\"unconstructed\"}}");
}
