#!/usr/bin/env node
"use strict";

const fs = require("fs");
const crypto = require("crypto");

function modBigInt(text, modulus) {
  const m = BigInt(modulus);
  let value = BigInt(text) % m;
  if (value < 0n) value += m;
  return Number(value);
}

function leadingOdd(row) {
  let pivot = Infinity;
  for (const [column, value] of row) {
    if ((value & 1) && column < pivot) pivot = column;
  }
  return pivot;
}

function leading(row) {
  let pivot = Infinity;
  for (const column of row.keys()) if (column < pivot) pivot = column;
  return pivot;
}

function reduceAgainstUnitPivots(row, pivots) {
  for (const [pivot, basis] of pivots) {
    const factor = row.get(pivot) || 0;
    if (!factor) continue;
    for (const [column, value] of basis) {
      let reduced = (row.get(column) || 0) - factor * value;
      reduced %= 4;
      if (reduced < 0) reduced += 4;
      if (reduced) row.set(column, reduced);
      else row.delete(column);
    }
  }
}

function parseRow(line, modulus) {
  const row = new Map();
  for (const entry of line.split(",")) {
    const split = entry.indexOf(":");
    const column = Number(entry.slice(0, split));
    const value = modBigInt(entry.slice(split + 1), modulus);
    if (value) row.set(column, value);
  }
  return row;
}

function unitPivotsMod4(lines) {
  const pivots = new Map();
  for (let lineIndex = 1; lineIndex < lines.length; lineIndex++) {
    const line = lines[lineIndex];
    if (!line) continue;
    const row = parseRow(line, 4);
    reduceAgainstUnitPivots(row, pivots);
    const pivot = leadingOdd(row);
    if (pivot === Infinity) continue;
    const inverse = row.get(pivot) === 1 ? 1 : 3;
    for (const [column, value] of row) {
      const normalized = (value * inverse) % 4;
      if (normalized) row.set(column, normalized);
      else row.delete(column);
    }
    pivots.set(pivot, row);
  }
  return pivots;
}

function rankMod2(rows) {
  const pivots = new Map();
  for (const source of rows) {
    const row = new Map(source);
    while (row.size) {
      const pivot = leading(row);
      const basis = pivots.get(pivot);
      if (!basis) {
        pivots.set(pivot, row);
        break;
      }
      for (const column of basis.keys()) {
        if (row.has(column)) row.delete(column);
        else row.set(column, 1);
      }
    }
  }
  return pivots;
}

if (process.argv.length !== 3) {
  throw new Error("usage: node census_interaction_net_two_adic_first_layer.cjs MATRIX");
}

const matrixPath = process.argv[2];
const data = fs.readFileSync(matrixPath, "utf8");
const lines = data.split(/\r?\n/);
const header = JSON.parse(lines[0]);
const started = Date.now();

const unitPivots = unitPivotsMod4(lines);
const dividedRows = [];
let oddResidualRows = 0;
let nonzeroEvenResidualRows = 0;

for (let lineIndex = 1; lineIndex < lines.length; lineIndex++) {
  const line = lines[lineIndex];
  if (!line) continue;
  const row = parseRow(line, 4);
  reduceAgainstUnitPivots(row, unitPivots);
  const divided = new Map();
  let hasOdd = false;
  for (const [column, value] of row) {
    if (value & 1) {
      hasOdd = true;
      break;
    }
    if (value === 2) divided.set(column, 1);
  }
  if (hasOdd) {
    oddResidualRows++;
    continue;
  }
  if (divided.size) {
    nonzeroEvenResidualRows++;
    dividedRows.push(divided);
  }
}

if (oddResidualRows) {
  throw new Error(`unit reduction left ${oddResidualRows} rows with odd residual coefficients`);
}

const firstLayerPivots = rankMod2(dividedRows);
const unitPivotColumns = [...unitPivots.keys()].sort((a, b) => a - b);
const firstLayerPivotColumns = [...firstLayerPivots.keys()].sort((a, b) => a - b);
const unitRank = unitPivots.size;
const firstLayerRank = firstLayerPivots.size;

process.stdout.write(JSON.stringify({
  schema: "marici.two-adic-first-layer-census.v1",
  matrix: matrixPath,
  header,
  unit_rank_mod_2: unitRank,
  quotient_dimension_mod_2: header.columns - unitRank,
  nonzero_even_residual_rows: nonzeroEvenResidualRows,
  first_bockstein_rank: firstLayerRank,
  quotient_dimension_after_first_layer: header.columns - unitRank - firstLayerRank,
  unit_pivot_sha256: crypto.createHash("sha256").update(JSON.stringify(unitPivotColumns)).digest("hex"),
  first_layer_pivot_sha256: crypto.createHash("sha256").update(JSON.stringify(firstLayerPivotColumns)).digest("hex"),
  interpretation: "Conditional on characteristic-zero rank equalling unit_rank_mod_2 + first_bockstein_rank, all positive two-adic Smith valuations equal one.",
  milliseconds: Date.now() - started
}, null, 2) + "\n");
