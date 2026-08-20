export const katexOptions = Object.freeze({
  throwOnError: true,
  strict: 'error',
})

export function convertTexMath(body) {
  // Source files use \( ... \) and \[ ... \] for math delimiters.
  // remark-math understands $ ... $ and $$ ... $$, so convert before render.
  return body
    .replace(/^(\s*)\\\[[ \t]*$/gm, '$1$$')
    .replace(/^(\s*)\\\][ \t]*$/gm, '$1$$')
    .replace(/\\\((.*?)\\\)/g, '$$$1$$')
}
