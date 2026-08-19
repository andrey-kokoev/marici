mod rank_engine {
    include!("triangle_wall_dual_rank.rs");

    pub fn export_source_lifts() -> io::Result<()> {
        let arguments: Vec<String> = env::args().collect();
        let path = arguments
            .get(1)
            .expect("usage: triangle_wall_source_lifts <packet>");
        let mut bytes = Vec::new();
        File::open(path)?.read_to_end(&mut bytes)?;
        let version = &bytes[..8];
        assert!(version == b"MRCIDR02" || version == b"MRCIDR03" || version == b"MRCIDR04");
        let mut cursor = 8;
        assert_eq!(u32_at(&bytes, &mut cursor), P);
        let ambient = u32_at(&bytes, &mut cursor);
        let columns = u32_at(&bytes, &mut cursor) as usize;
        let rows = u32_at(&bytes, &mut cursor) as usize;
        let _declared_central_rank = u32_at(&bytes, &mut cursor) as usize;

        let mut central_pivots: Vec<Option<Row>> = vec![None; columns];
        let mut records = Vec::with_capacity(rows);
        let mut central_generators = Vec::new();
        for _ in 0..rows {
            let family = if version == b"MRCIDR03" || version == b"MRCIDR04" {
                u32_at(&bytes, &mut cursor)
            } else {
                0
            };
            let central = row_at(&bytes, &mut cursor);
            let derivative = row_at(&bytes, &mut cursor);
            let second = row_at(&bytes, &mut cursor);
            if version == b"MRCIDR04" {
                let _ = row_at(&bytes, &mut cursor);
                let _ = row_at(&bytes, &mut cursor);
                let _ = row_at(&bytes, &mut cursor);
            }
            let index = records.len();
            records.push((family, central.clone(), derivative, second));
            if insert(central, &mut central_pivots) {
                central_generators.push(index);
            }
        }
        let central_rank = central_generators.len();

        // Provenance indices encode raw source jets without choosing a reduced
        // representative: i is R_i, rows+i is Lambda R_i, and 2*rows+i is
        // Lambda^2 R_i.
        let mut tracked_dual: Vec<Option<(Row, Provenance)>> = vec![None; 2 * columns];
        for &index in &central_generators {
            insert_tracked(
                shifted(&records[index].1, columns),
                [(rows + index, 1)].into(),
                &mut tracked_dual,
            );
        }
        for &index in &central_generators {
            let (_, central, derivative, _) = &records[index];
            let mut first = central.clone();
            for (&column, &value) in derivative {
                add_value(&mut first, columns + column, value);
            }
            insert_tracked(first, [(index, 1)].into(), &mut tracked_dual);
        }
        let mut first_lifts = Vec::new();
        for (index, (_, central, derivative, _)) in records.iter().enumerate() {
            let mut first = central.clone();
            for (&column, &value) in derivative {
                add_value(&mut first, columns + column, value);
            }
            if let Some((_, provenance)) =
                insert_tracked(first, [(index, 1)].into(), &mut tracked_dual)
            {
                first_lifts.push(provenance);
            }
        }
        let first_normal = first_lifts.len();

        let lift_to_length_three = |provenance: &Provenance| {
            let mut out = Row::new();
            for (&source, &coefficient) in provenance {
                let order = source / rows;
                let index = source % rows;
                let (_, central, derivative, second) = &records[index];
                if order == 0 {
                    for (&column, &value) in central {
                        add_value(&mut out, column, mul(coefficient, value));
                    }
                    for (&column, &value) in derivative {
                        add_value(&mut out, columns + column, mul(coefficient, value));
                    }
                    for (&column, &value) in second {
                        add_value(&mut out, 2 * columns + column, mul(coefficient, value));
                    }
                } else if order == 1 {
                    for (&column, &value) in central {
                        add_value(&mut out, columns + column, mul(coefficient, value));
                    }
                    for (&column, &value) in derivative {
                        add_value(&mut out, 2 * columns + column, mul(coefficient, value));
                    }
                } else {
                    assert_eq!(order, 2);
                    for (&column, &value) in central {
                        add_value(&mut out, 2 * columns + column, mul(coefficient, value));
                    }
                }
            }
            out
        };

        let mut filtered: Vec<Option<(Row, Provenance)>> = vec![None; 3 * columns];
        for &index in &central_generators {
            insert_tracked(
                shifted(&records[index].1, 2 * columns),
                [(2 * rows + index, 1)].into(),
                &mut filtered,
            );
        }
        for (index, (_, central, derivative, _)) in records.iter().enumerate() {
            let mut grade_one = shifted(central, columns);
            for (&column, &value) in derivative {
                add_value(&mut grade_one, 2 * columns + column, value);
            }
            insert_tracked(grade_one, [(rows + index, 1)].into(), &mut filtered);
        }
        for &index in &central_generators {
            let provenance: Provenance = [(index, 1)].into();
            insert_tracked(lift_to_length_three(&provenance), provenance, &mut filtered);
        }
        for provenance in &first_lifts {
            insert_tracked(
                lift_to_length_three(provenance),
                provenance.clone(),
                &mut filtered,
            );
        }
        let baseline_rank = filtered.iter().flatten().count();
        assert_eq!(baseline_rank, 3 * central_rank + 2 * first_normal);

        let mut quadratic: Vec<Option<(Row, Provenance)>> = vec![None; 3 * columns];
        let mut lifts = Vec::new();
        for (index, (_, central, derivative, second)) in records.iter().enumerate() {
            let mut raw = central.clone();
            for (&column, &value) in derivative {
                add_value(&mut raw, columns + column, value);
            }
            for (&column, &value) in second {
                add_value(&mut raw, 2 * columns + column, value);
            }
            let (residual, mut elimination) = reduce_tracked(raw, &filtered);
            add_value(&mut elimination, index, 1);
            if let Some((pivot, provenance)) = insert_tracked(residual, elimination, &mut quadratic)
            {
                let normalized = &quadratic[pivot].as_ref().unwrap().0;
                assert_eq!(&lift_to_length_three(&provenance), normalized);
                lifts.push((records[index].0, index, pivot, provenance));
            }
        }

        println!("{{\"prime\":{P},\"ambient\":{ambient},\"columns\":{columns},\"rows\":{rows},\"central_rank\":{central_rank},\"first_normal_rank\":{first_normal},\"second_normal_rank\":{},\"lifts\":[{}]}}",
            lifts.len(),
            lifts.iter().map(|(family, witness, pivot, provenance)| {
                let terms = provenance.iter().map(|(&source, &value)| {
                    format!("[{}, {}, {}]", source / rows, source % rows, value)
                }).collect::<Vec<_>>().join(",");
                format!("{{\"family\":{family},\"witness\":{witness},\"pivot\":{pivot},\"source_terms\":[{terms}]}}")
            }).collect::<Vec<_>>().join(",")
        );
        Ok(())
    }
}

fn main() -> std::io::Result<()> {
    rank_engine::export_source_lifts()
}
