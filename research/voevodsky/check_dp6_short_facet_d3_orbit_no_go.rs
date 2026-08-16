use std::collections::{BTreeMap, BTreeSet};

fn source_rotation(i: usize) -> usize {
    (i + 2) % 6
}

fn source_reflection(i: usize) -> usize {
    (7 - i) % 6
}

fn target_rotation(i: usize) -> usize {
    (i + 2) % 6
}

fn target_reflection(i: usize) -> usize {
    (6 - i) % 6
}

fn decode(mut code: usize) -> [usize; 6] {
    let mut map = [0; 6];
    for value in &mut map {
        *value = code % 6;
        code /= 6;
    }
    map
}

fn equivariant(map: &[usize; 6]) -> bool {
    (0..6).all(|i| {
        map[source_rotation(i)] == target_rotation(map[i])
            && map[source_reflection(i)] == target_reflection(map[i])
    })
}

fn main() {
    let source_rotation_orbits = [
        [0, source_rotation(0), source_rotation(source_rotation(0))],
        [1, source_rotation(1), source_rotation(source_rotation(1))],
    ];
    assert_eq!(source_rotation_orbits, [[0, 2, 4], [1, 3, 5]]);
    assert!((0..6).all(|i| source_reflection(i) != i));

    let target_rotation_orbits = [[0, 2, 4], [1, 3, 5]];
    assert_eq!(target_rotation_orbits[0].map(target_rotation), [2, 4, 0]);
    assert_eq!(target_rotation_orbits[1].map(target_rotation), [3, 5, 1]);
    assert_eq!(
        (0..6)
            .filter(|i| target_reflection(*i) == *i)
            .collect::<Vec<_>>(),
        [0, 3]
    );

    let maps = (0..6_usize.pow(6))
        .map(decode)
        .filter(equivariant)
        .collect::<Vec<_>>();
    assert_eq!(maps.len(), 6);

    let mut bijections = 0;
    for map in &maps {
        let image = map.iter().copied().collect::<BTreeSet<_>>();
        assert_eq!(image.len(), 3);
        assert!(image
            .iter()
            .all(|value| value % 2 == image.first().unwrap() % 2));
        let mut fibres = BTreeMap::new();
        for value in map {
            *fibres.entry(*value).or_insert(0) += 1;
        }
        assert!(fibres.values().all(|multiplicity| *multiplicity == 2));
        if image.len() == 6 {
            bijections += 1;
        }
    }
    assert_eq!(bijections, 0);

    println!(
        "{{\"status\":\"falsified_scoped_equivariant_sector_relabelling\",\"source_sectors\":6,\"source_D3_orbits\":1,\"source_reflection_fixed_points\":0,\"target_short_facets\":6,\"target_D3_orbits\":2,\"target_reflection_fixed_points\":2,\"equivariant_maps\":{},\"equivariant_bijections\":{},\"every_equivariant_map_image_size\":3,\"every_nonempty_fibre_multiplicity\":2,\"sheetwise_Gysin_quotient_required\":true,\"global_correspondence_no_go\":false}}",
        maps.len(),
        bijections
    );
}
