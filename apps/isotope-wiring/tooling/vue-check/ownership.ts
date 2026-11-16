import ts from "typescript";

export function canonicalPath(path: string): string {
  const normalized = ts.sys.resolvePath(path).replaceAll("\\", "/");
  return ts.sys.useCaseSensitiveFileNames ? normalized : normalized.toLowerCase();
}

/** Only Vue-coupled entrypoints/stores/composables belong to the TS6 project. */
export function isVueOwned(path: string): boolean {
  return canonicalPath(path).startsWith(`${canonicalPath("src/vue")}/`);
}
