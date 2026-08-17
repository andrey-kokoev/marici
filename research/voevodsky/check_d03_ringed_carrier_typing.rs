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

    println!(
        "{{\"claim\":\"The loaded D03 pullback is typed only on the normal-state Grothendieck carrier (sigma,H), not on the face-only barycentric carrier sigma\",\"status\":\"correspondence_repair_required\",\"target_points\":{},\"face_only_domain_points\":{},\"corrected_domain_points\":{},\"verified_boundary_covers\":{},\"face_only_image_count\":{},\"corrected_map\":\"(sigma,H)->(blowdown(initial(sigma)),H)\"}}",
        target.len(), simplices.len(), corrected.len(), cover_count, face_only_image_count
    );
}
