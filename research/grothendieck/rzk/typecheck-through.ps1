param(
    [Parameter(Mandatory = $true)] [string] $Target,
    [ValidateRange(1, 86400)] [int] $TimeoutSeconds = 6000
)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$sourceDirectory = Join-Path $root 'src'
$targetPath = Join-Path $sourceDirectory $Target
if (-not (Test-Path -LiteralPath $targetPath -PathType Leaf)) {
    throw "Target is not an Rzk source file: $Target"
}

$files = Get-ChildItem -LiteralPath $sourceDirectory -Filter '*.rzk.md' -File |
    Where-Object { $_.Name -le $Target } |
    Sort-Object Name |
    ForEach-Object { Join-Path 'src' $_.Name }

$resultsDirectory = Join-Path $root 'results'
New-Item -ItemType Directory -Force -Path $resultsDirectory | Out-Null
$stem = [IO.Path]::GetFileNameWithoutExtension([IO.Path]::GetFileNameWithoutExtension($Target))
$stdoutPath = Join-Path $resultsDirectory "$stem.stdout.log"
$stderrPath = Join-Path $resultsDirectory "$stem.stderr.log"
$arguments = @('typecheck') + $files

Write-Output "Typechecking $($files.Count) files through $Target"
& (Join-Path $root 'run-contained.ps1') `
    -Executable 'rzk' `
    -WorkingDirectory $root `
    -ChildArgument $arguments `
    -StdoutPath $stdoutPath `
    -StderrPath $stderrPath `
    -TimeoutSeconds $TimeoutSeconds

if (Test-Path -LiteralPath $stdoutPath) { Get-Content -LiteralPath $stdoutPath }
if (Test-Path -LiteralPath $stderrPath) { Get-Content -LiteralPath $stderrPath | Write-Error }
