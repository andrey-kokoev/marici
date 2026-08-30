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

function inverseOdd(value, modulus) {
  let a = value, b = modulus, x0 = 1, x1 = 0;
  while (b !== 0) {
    const q = Math.floor(a / b);
    [a, b] = [b, a - q * b];
    [x0, x1] = [x1, x0 - q * x1];
  }
  if (a !== 1) throw new Error(`nonunit pivot ${value} modulo ${modulus}`);
  return ((x0 % modulus) + modulus) % modulus;
}

function leadingOdd(row) {
  let pivot = Infinity;
  for (const [column, value] of row) {
    if ((value & 1) && column < pivot) pivot = column;
  }
  return pivot;
}

function cloneRow(row) {
  return new Map(row);
}

function reduceAgainstPivots(row, pivots, modulus) {
  for (const [pivot, basis] of pivots) {
    const factor = row.get(pivot) || 0;
    if (!factor) continue;
    for (const [column, value] of basis) {
      let reduced = (row.get(column) || 0) - factor * value;
      reduced %= modulus;
      if (reduced < 0) reduced += modulus;
      if (reduced) row.set(column, reduced);
      else row.delete(column);
    }
  }
}

function localLayer(rows, modulus) {
  const pivots = new Map();
  for (const source of rows) {
    const row = cloneRow(source);
    reduceAgainstPivots(row, pivots, modulus);
    const pivot = leadingOdd(row);
    if (pivot === Infinity) continue;
    const scale = inverseOdd(row.get(pivot), modulus);
    for (const [column, value] of row) {
      const normalized = (value * scale) % modulus;
      if (normalized) row.set(column, normalized);
      else row.delete(column);
    }
    pivots.set(pivot, row);
  }

  const nextRows = [];
  let oddResidualRows = 0;
  for (const source of rows) {
    const row = cloneRow(source);
    reduceAgainstPivots(row, pivots, modulus);
    const divided = new Map();
    let hasOdd = false;
    for (const [column, value] of row) {
      if (value & 1) {
        hasOdd = true;
        break;
      }
      const next = value / 2;
      if (next) divided.set(column, next);
    }
    if (hasOdd) {
      oddResidualRows++;
      continue;
    }
    if (divided.size) nextRows.push(divided);
  }
  if (oddResidualRows) {
    throw new Error(`layer modulo ${modulus} left ${oddResidualRows} odd residual rows`);
  }
  return {pivots, nextRows};
}

const arguments_ = process.argv.slice(2);
const summaryOnly = arguments_.includes("--summary");
const exportAfter = Number((arguments_.find(argument => argument.startsWith("--export-after=")) || "").split("=", 2)[1]);
const exportTail = (arguments_.find(argument => argument.startsWith("--export-tail=")) || "").split("=", 2)[1];
if ((exportTail && !Number.isInteger(exportAfter)) || (!exportTail && Number.isInteger(exportAfter))) {
  throw new Error("--export-after=VALUATION and --export-tail=PATH must be supplied together");
}
const positional = arguments_.filter(argument => !argument.startsWith("--"));
if (positional.length < 1 || positional.length > 2) {
  throw new Error("usage: node census_interaction_net_two_adic_layers.cjs MATRIX [DEPTH] [--summary] [--export-after=K --export-tail=PATH]");
}

const matrixPath = positional[0];
const depth = positional[1] ? Number(positional[1]) : 6;
if (!Number.isInteger(depth) || depth < 1 || depth > 26) {
  throw new Error("DEPTH must be an integer from 1 through 26; larger depths require BigInt arithmetic");
}
if (exportTail && (exportAfter < 0 || exportAfter >= depth)) {
  throw new Error("--export-after must be an integer from 0 through DEPTH - 1");
}
const modulus = 2 ** depth;
const data = fs.readFileSync(matrixPath, "utf8");
const lines = data.split(/\r?\n/);
const header = JSON.parse(lines[0]);
let rows = [];
for (let lineIndex = 1; lineIndex < lines.length; lineIndex++) {
  const line = lines[lineIndex];
  if (!line) continue;
  const row = new Map();
  for (const entry of line.split(",")) {
    const split = entry.indexOf(":");
    const column = Number(entry.slice(0, split));
    const value = modBigInt(entry.slice(split + 1), modulus);
    if (value) row.set(column, value);
  }
  rows.push(row);
}

const started = Date.now();
const layers = [];
let currentModulus = modulus;
let cumulativeRank = 0;
const cumulativePivotColumns = [];

for (let valuation = 0; valuation < depth; valuation++) {
  const layerStarted = Date.now();
  const result = localLayer(rows, currentModulus);
  const pivotColumns = [...result.pivots.keys()].sort((a, b) => a - b);
  cumulativePivotColumns.push(...pivotColumns);
  cumulativeRank += result.pivots.size;
  layers.push({
    valuation,
    modulus: currentModulus,
    rank: result.pivots.size,
    cumulative_rank: cumulativeRank,
    residual_row_count: result.nextRows.length,
    pivot_sha256: crypto.createHash("sha256").update(JSON.stringify(pivotColumns)).digest("hex"),
    pivot_columns: summaryOnly || valuation === 0 ? undefined : pivotColumns,
    milliseconds: Date.now() - layerStarted
  });
  rows = result.nextRows;
  currentModulus /= 2;
  if (exportTail && valuation === exportAfter) {
    const activeColumns = [...new Set(rows.flatMap(row => [...row.keys()]))].sort((a, b) => a - b);
    const tailHeader = {
      schema: "marici.two-adic-tail-presentation.v1",
      source_matrix: matrixPath,
      source_presentation_sha256: header.source_presentation_sha256,
      depth,
      exported_after_valuation: valuation,
      divided_by_power_of_two: valuation + 1,
      modulus: currentModulus,
      rows: rows.length,
      original_columns: header.columns,
      active_columns: activeColumns,
      cumulative_pivot_columns: [...cumulativePivotColumns].sort((a, b) => a - b),
      cumulative_pivot_sha256: crypto.createHash("sha256").update(JSON.stringify([...cumulativePivotColumns].sort((a, b) => a - b))).digest("hex")
    };
    const serializedRows = rows.map(row =>
      [...row.entries()].sort((a, b) => a[0] - b[0]).map(([column, value]) => `${column}:${value}`).join(",")
    );
    fs.writeFileSync(exportTail, JSON.stringify(tailHeader) + "\n" + serializedRows.join("\n") + "\n");
  }
  if (!rows.length) break;
}

process.stdout.write(JSON.stringify({
  schema: "marici.two-adic-layer-census.v1",
  matrix: matrixPath,
  header,
  depth,
  initial_modulus: modulus,
  layers,
  cumulative_detected_rank: cumulativeRank,
  unresolved_quotient_dimension_after_depth: header.columns - cumulativeRank,
  interpretation: "Layer rank at valuation k counts Smith invariants whose exact two-adic valuation is k, provided the computed depth reaches the characteristic-zero rank.",
  milliseconds: Date.now() - started
}, null, 2) + "\n");
