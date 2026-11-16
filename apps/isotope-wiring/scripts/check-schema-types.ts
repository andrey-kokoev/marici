import type { z } from "zod";
import * as schemas from "../src/schemas/index.js";

// Compile-time verification utilities, not parallel application data shapes.
type SchemaNames = keyof typeof schemas;
type SafeData<T> = 0 extends 1 & T
  ? false
  : T extends string | number | boolean | null | undefined
    ? true
    : T extends readonly (infer Element)[]
      ? false extends SafeData<Element>
        ? false
        : true
      : T extends object
        ? false extends { [Key in keyof T]-?: SafeData<T[Key]> }[keyof T]
          ? false
          : true
        : false;

// Both sides of every exported schema must have concrete application data types,
// recursively. A top type or an unsafe nested property makes compilation fail.
type InputSafety = { [Key in SchemaNames]: SafeData<z.input<(typeof schemas)[Key]>> };
type OutputSafety = { [Key in SchemaNames]: SafeData<z.output<(typeof schemas)[Key]>> };
export const schemaInputsAreSafe: false extends InputSafety[SchemaNames] ? false : true = true;
export const schemaOutputsAreSafe: false extends OutputSafety[SchemaNames] ? false : true = true;
