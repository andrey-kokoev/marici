[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateScript({ Test-Path -LiteralPath $_ -PathType Leaf })]
    [string] $InputPath,

    [Parameter(Position = 1)]
    [string] $OutputDirectory = (Join-Path $PSScriptRoot "extractions\marker-no-ocr"),

    [string] $PageRange,

    [ValidateSet("markdown", "json", "html", "chunks")]
    [string] $OutputFormat = "markdown",

    [switch] $PaginateOutput
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$python = Join-Path $PSScriptRoot ".local-tools\marker-py313\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python -PathType Leaf)) {
    throw "Marker Python environment not found at: $python"
}

$resolvedInput = (Resolve-Path -LiteralPath $InputPath).Path
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputDirectory)

$markerArgs = @(
    $resolvedInput
    "--mode", "fast"
    "--disable_ocr"
    "--output_format", $OutputFormat
    "--output_dir", $resolvedOutput
)

if ($PageRange) {
    $markerArgs += @("--page_range", $PageRange)
}

if ($PaginateOutput) {
    $markerArgs += "--paginate_output"
}

$global:LASTEXITCODE = 0
$markerCli = "from marker.scripts.convert_single import convert_single_cli; convert_single_cli()"
& $python "-c" $markerCli @markerArgs
$markerExitCode = $LASTEXITCODE
if ($markerExitCode -ne 0) {
    throw "Marker failed with exit code $markerExitCode."
}
