//! Exact typing audit for the D03 finite-ringed carrier.

use std::collections::{BTreeSet, VecDeque};

const N: u8 = 6;
const EXCEPTIONAL: u16 = 1 << 9;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Diagonal(u8, u8);

fn diagonal(a: u8, b: u8) -> Diagonal {
    if a < b {
        Diagonal(a, b)
    } else {
        Diagonal(b, a)
    }
}

fn boundary_edge(d: Diagonal) -> bool {
    d.1 - d.0 == 1 || d == Diagonal(0, N - 1)
}

fn between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + N - first) % N;
    let position = (vertex + N - first) % N;
    position > 0 && position < span
}

fn crosses(a: Diagonal, b: Diagonal) -> bool {
    if [a.0, a.1].contains(&b.0) || [a.0, a.1].contains(&b.1) {
        return false;
    }
    between(b.0, a.0, a.1) != between(b.1, a.0, a.1)
        && between(a.0, b.0, b.1) != between(a.1, b.0, b.1)
}

fn old_faces(ds: &[Diagonal]) -> BTreeSet<u16> {
    (0_u16..(1_u16 << ds.len()))
        .filter(|face| face.count_ones() <= 3)
        .filter(|face| {
            (0..ds.len()).all(|i| {
                ((i + 1)..ds.len())
                    .all(|j| face & (1 << i) == 0 || face & (1 << j) == 0 || !crosses(ds[i], ds[j]))
            })
        })
        .collect()
}

fn blowup(old: &BTreeSet<u16>, d03: u16, x1: u16) -> BTreeSet<u16> {
    let mut result = BTreeSet::new();
    for face in old {
        if face & d03 == 0 || face & x1 == 0 {
            result.insert(*face);
        } else {
            let rest = face & !d03 & !x1;
            result.extend([
                rest | EXCEPTIONAL,
                rest | EXCEPTIONAL | d03,
                rest | EXCEPTIONAL | x1,
            ]);
        }
    }
    result
}

fn extend_chains(faces: &[u16], chain: &mut Vec<u16>, result: &mut Vec<Vec<u16>>) {
    result.push(chain.clone());
    let last = *chain.last().unwrap();
    for next in faces {
        if last != *next && last & *next == last {
            chain.push(*next);
            extend_chains(faces, chain, result);
            chain.pop();
        }
    }
}

fn barycentric(faces: &BTreeSet<u16>) -> Vec<Vec<u16>> {
    let faces: Vec<_> = faces.iter().copied().collect();
    let mut result = Vec::new();
    for face in &faces {
        extend_chains(&faces, &mut vec![*face], &mut result);
    }
    result
}

fn blowdown(face: u16, d03: u16, x1: u16) -> u16 {
    (face & !EXCEPTIONAL) | if face & EXCEPTIONAL == 0 { 0 } else { d03 | x1 }
}

fn subsets(face: u16) -> impl Iterator<Item = u16> {
    (0_u16..=face).filter(move |normal| normal & !face == 0)
}

fn target_reachable(source: (u16, u16), target: (u16, u16)) -> bool {
    // Radial faces may only be added; normal-circle marks may only be deleted.
    source.0 & target.0 == source.0 && target.1 & source.1 == target.1 && source.1 & !target.0 == 0
}

fn source_leq(left: &(Vec<u16>, u16), right: &(Vec<u16>, u16)) -> bool {
    right.0.iter().all(|face| left.0.contains(face)) && right.1 & !left.1 == 0
}

fn cell_degree(point: &(Vec<u16>, u16)) -> usize {
    point.0.len() - 1 + point.1.count_ones() as usize
}

fn rank_mod(mut matrix: Vec<Vec<i64>>, prime: i64) -> usize {
    if matrix.is_empty() || matrix[0].is_empty() {
        return 0;
    }
    let rows = matrix.len();
    let columns = matrix[0].len();
    let mut rank = 0;
    for column in 0..columns {
        let Some(pivot) = (rank..rows).find(|row| matrix[*row][column].rem_euclid(prime) != 0)
        else {
            continue;
        };
        matrix.swap(rank, pivot);
        let mut inverse = 1;
        let mut base = matrix[rank][column].rem_euclid(prime);
        let mut exponent = prime - 2;
        while exponent > 0 {
            if exponent % 2 == 1 {
                inverse = inverse * base % prime;
            }
            base = base * base % prime;
            exponent /= 2;
        }
        for value in &mut matrix[rank] {
            *value = value.rem_euclid(prime) * inverse % prime;
        }
        for row in 0..rows {
            if row == rank {
                continue;
            }
            let factor = matrix[row][column].rem_euclid(prime);
            if factor != 0 {
                for entry in column..columns {
                    matrix[row][entry] =
                        (matrix[row][entry] - factor * matrix[rank][entry]).rem_euclid(prime);
                }
            }
        }
        rank += 1;
        if rank == rows {
            break;
        }
    }
    rank
}

fn extend_target_chains(
    points: &[(u16, u16)],
    present: &mut Vec<(u16, u16)>,
    result: &mut Vec<Vec<(u16, u16)>>,
) {
    result.push(present.clone());
    let last = *present.last().unwrap();
    for next in points {
        if last != *next && target_reachable(last, *next) {
            present.push(*next);
            extend_target_chains(points, present, result);
            present.pop();
        }
    }
}

fn main() {
    let ds: Vec<_> = (0..N)
        .flat_map(|a| ((a + 1)..N).map(move |b| diagonal(a, b)))
        .filter(|d| !boundary_edge(*d))
        .collect();
    let d03 = 1 << ds.iter().position(|d| *d == diagonal(0, 3)).unwrap();
    let x1 = 1 << ds.iter().position(|d| *d == diagonal(1, 3)).unwrap();
    let old = old_faces(&ds);
    let blown = blowup(&old, d03, x1);
    let simplices = barycentric(&blown);

    let target: BTreeSet<_> = old
        .iter()
        .flat_map(|face| subsets(*face).map(|normal| (*face, normal)))
        .collect();
    let corrected: Vec<_> = simplices
        .iter()
        .flat_map(|simplex| {
            let face = blowdown(simplex[0], d03, x1);
            subsets(face).map(move |normal| (simplex.clone(), normal))
        })
        .collect();

    assert_eq!(old.len(), 45);
    assert_eq!(blown.len(), 51);
    assert_eq!(simplices.len(), 581);
    assert_eq!(target.len(), 215);
    assert_eq!(corrected.len(), 1169);

    // Every cellular boundary cover of the corrected carrier maps to an
    // incidence relation (possibly an identity) of the 215-point target.
    let corrected_set: BTreeSet<_> = corrected.iter().cloned().collect();
    let mut cover_count = 0_usize;
    for (simplex, normal) in &corrected {
        let source = (blowdown(simplex[0], d03, x1), *normal);
        for removed in 0..simplex.len() {
            let mut boundary = simplex.clone();
            boundary.remove(removed);
            if boundary.is_empty() || !corrected_set.contains(&(boundary.clone(), *normal)) {
                continue;
            }
            let target_point = (blowdown(boundary[0], d03, x1), *normal);
            assert!(target_reachable(source, target_point));
            cover_count += 1;
        }
        let mut queue: VecDeque<_> = (0..ds.len())
            .filter(|bit| normal & (1 << bit) != 0)
            .collect();
        while let Some(bit) = queue.pop_front() {
            let target_point = (source.0, normal & !(1 << bit));
            assert!(corrected_set.contains(&(simplex.clone(), target_point.1)));
            assert!(target_reachable(source, target_point));
            cover_count += 1;
        }
    }

    // A face-only map has no datum from which to recover a general H.
    let face_only_image_count = simplices
        .iter()
        .map(|simplex| blowdown(simplex[0], d03, x1))
        .collect::<BTreeSet<_>>()
        .len();
    assert_eq!(face_only_image_count, 45);
    assert_ne!(face_only_image_count, target.len());

    // The standard-resolution dualizing bicomplex has one coefficient for
    // every strict source chain.  Census it by chain length and by the
    // number of new target localizations between its endpoints.
    let max_degree = corrected.iter().map(cell_degree).max().unwrap();
    assert_eq!(max_degree, 4);
    let images: Vec<_> = corrected
        .iter()
        .map(|(simplex, normal)| (blowdown(simplex[0], d03, x1), *normal))
        .collect();
    let greater: Vec<Vec<_>> = (0..corrected.len())
        .map(|i| {
            (0..corrected.len())
                .filter(|j| {
                    cell_degree(&corrected[*j]) < cell_degree(&corrected[i])
                        && source_leq(&corrected[i], &corrected[*j])
                })
                .collect()
        })
        .collect();

    // Compactness test for the pushforward of every source representable.
    // For y and x, the relevant section space is U_y intersect f^{-1}(U_x).
    // A unique initial point m with f(m)=x makes its loaded standard complex
    // contract to A_x by unit faces, naturally for the pulled-back ring.
    let target_points: Vec<_> = target.iter().copied().collect();
    let mut empty_intersections = 0_usize;
    let mut initial_intersections = 0_usize;
    let mut noninitial_intersections = 0_usize;
    let mut first_noninitial = None;
    for y in 0..corrected.len() {
        let open_y: Vec<_> = std::iter::once(y)
            .chain(greater[y].iter().copied())
            .collect();
        for x in &target_points {
            let intersection: Vec<_> = open_y
                .iter()
                .copied()
                .filter(|z| target_reachable(*x, images[*z]))
                .collect();
            if intersection.is_empty() {
                empty_intersections += 1;
                continue;
            }
            let max_degree = intersection
                .iter()
                .map(|z| cell_degree(&corrected[*z]))
                .max()
                .unwrap();
            let candidates: Vec<_> = intersection
                .iter()
                .copied()
                .filter(|z| cell_degree(&corrected[*z]) == max_degree)
                .collect();
            let initial = (candidates.len() == 1)
                .then_some(candidates[0])
                .filter(|m| {
                    images[*m] == *x
                        && intersection
                            .iter()
                            .all(|z| source_leq(&corrected[*m], &corrected[*z]))
                });
            if initial.is_some() {
                initial_intersections += 1;
            } else {
                noninitial_intersections += 1;
                first_noninitial.get_or_insert((y, *x, intersection.len()));
            }
        }
    }
    assert_eq!(
        empty_intersections + initial_intersections + noninitial_intersections,
        corrected.len() * target.len()
    );
    let mut term_census = vec![vec![0_u64; 10]; max_degree + 1];
    for start in 0..corrected.len() {
        let initial_units = images[start].0 & !images[start].1;
        let mut paths = vec![vec![0_u64; corrected.len()]; max_degree + 1];
        paths[0][start] = 1;
        for length in 0..max_degree {
            for at in 0..corrected.len() {
                let count = paths[length][at];
                if count == 0 {
                    continue;
                }
                for next in &greater[at] {
                    paths[length + 1][*next] += count;
                }
            }
        }
        for length in 0..=max_degree {
            for end in 0..corrected.len() {
                let count = paths[length][end];
                if count == 0 {
                    continue;
                }
                let final_units = images[end].0 & !images[end].1;
                let jump = (final_units & !initial_units).count_ones() as usize;
                term_census[length][jump] += count;
            }
        }
    }
    let term_census = term_census
        .iter()
        .map(|row| {
            let last = row.iter().rposition(|value| *value != 0).unwrap_or(0);
            format!(
                "[{}]",
                row[..=last]
                    .iter()
                    .map(u64::to_string)
                    .collect::<Vec<_>>()
                    .join(",")
            )
        })
        .collect::<Vec<_>>()
        .join(",");

    // One-normal completion sector.  Let a=({u},empty), so A_a=A[u^-1],
    // and take the degree-zero source point over a.  The u-noninverted
    // associated sector in the bar dual is indexed by target chains whose
    // first point lies below a and whose last point still does not invert u.
    let u = 1_u16;
    let a = (u, 0_u16);
    assert!(target.contains(&a));
    let witness_sources: Vec<_> = corrected
        .iter()
        .enumerate()
        .filter(|(_, point)| cell_degree(point) == 0)
        .filter(|(index, _)| images[*index] == a)
        .collect();
    assert_eq!(witness_sources.len(), 1);
    let witness_y = witness_sources[0].0;
    assert!(greater[witness_y].is_empty());
    let no_u: Vec<_> = target_points
        .iter()
        .copied()
        .filter(|(face, normal)| (face & !normal) & u == 0)
        .collect();
    let starts: Vec<_> = no_u
        .iter()
        .copied()
        .filter(|point| target_reachable(*point, a))
        .collect();
    assert_eq!(starts.len(), 2);
    let mut completion_chains = Vec::new();
    for start in &starts {
        extend_target_chains(&no_u, &mut vec![*start], &mut completion_chains);
    }
    completion_chains.sort();
    completion_chains.dedup();
    let max_length = completion_chains.iter().map(Vec::len).max().unwrap();
    let by_length: Vec<Vec<_>> = (1..=max_length)
        .map(|length| {
            completion_chains
                .iter()
                .filter(|chain| chain.len() == length)
                .cloned()
                .collect()
        })
        .collect();
    let mut boundary_ranks = vec![0_usize; max_length];
    for degree in 1..max_length {
        let rows = &by_length[degree - 1];
        let columns = &by_length[degree];
        let row_index: std::collections::BTreeMap<_, _> = rows
            .iter()
            .cloned()
            .enumerate()
            .map(|(index, chain)| (chain, index))
            .collect();
        let mut matrix = vec![vec![0_i64; columns.len()]; rows.len()];
        for (column, chain) in columns.iter().enumerate() {
            for removed in 0..chain.len() {
                let mut face = chain.clone();
                face.remove(removed);
                if face.is_empty() || !target_reachable(face[0], a) {
                    continue;
                }
                if let Some(row) = row_index.get(&face) {
                    matrix[*row][column] += if removed % 2 == 0 { 1 } else { -1 };
                }
            }
        }
        boundary_ranks[degree] = rank_mod(matrix, 101);
    }
    let completion_homology: Vec<_> = (0..max_length)
        .map(|degree| {
            by_length[degree].len()
                - boundary_ranks[degree]
                - boundary_ranks.get(degree + 1).copied().unwrap_or(0)
        })
        .collect();
    let completion_euler: i64 = by_length
        .iter()
        .enumerate()
        .map(|(degree, cells)| if degree % 2 == 0 { 1 } else { -1 } * cells.len() as i64)
        .sum();
    assert_eq!(completion_euler, 1);
    assert_eq!(completion_homology, [0, 0, 1, 0]);

    println!(
        "{{\"claim\":\"The corrected D03 dualizing complex has a rank-one one-normal telescope-dual sector and therefore no bounded finite-projective compression over the unlocalized target ring\",\"status\":\"omega_q_nonperfect\",\"target_points\":{},\"face_only_domain_points\":{},\"corrected_domain_points\":{},\"verified_boundary_covers\":{},\"face_only_image_count\":{},\"corrected_map\":\"(sigma,H)->(blowdown(initial(sigma)),H)\",\"representable_open_intersections\":{{\"empty\":{},\"unique_initial_over_x\":{},\"noninitial\":{},\"first_noninitial\":\"{:?}\"}},\"one_normal_witness\":{{\"source_index\":{},\"target_face_mask\":1,\"target_normal_mask\":0,\"source_open_is_singleton\":true}},\"one_normal_completion_sector\":{{\"starts\":{},\"chain_ranks\":{:?},\"boundary_ranks_mod_101\":{:?},\"homology_mod_101\":{:?},\"euler_characteristic\":{}}},\"standard_chain_term_census_by_degree_and_localization_jump\":[{}]}}",
        target.len(),
        simplices.len(),
        corrected.len(),
        cover_count,
        face_only_image_count,
        empty_intersections,
        initial_intersections,
        noninitial_intersections,
        first_noninitial,
        witness_y,
        starts.len(),
        by_length.iter().map(Vec::len).collect::<Vec<_>>(),
        boundary_ranks,
        completion_homology,
        completion_euler,
        term_census
    );
}
