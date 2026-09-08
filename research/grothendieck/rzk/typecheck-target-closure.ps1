param(
    [Parameter(Mandatory = $true)] [string] $ProjectRoot,
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

$owners = @{}
$sourceFiles = Get-ChildItem -LiteralPath $sourceDirectory -Filter '*.rzk.md' -File
foreach ($file in $sourceFiles) {
    $text = Get-Content -LiteralPath $file.FullName -Raw
    foreach ($match in [regex]::Matches($text, '(?m)^\s*#(?:define|assume|data)\s+([A-Za-z][A-Za-z0-9-]*)')) {
        $owners[$match.Groups[1].Value] = $file
    }
}

$selected = @{}
$pending = [Collections.Generic.Queue[IO.FileInfo]]::new()
$pending.Enqueue((Get-Item -LiteralPath $targetPath))
while ($pending.Count -gt 0) {
    $file = $pending.Dequeue()
    if ($selected.ContainsKey($file.Name)) { continue }
    $selected[$file.Name] = $file
    $text = Get-Content -LiteralPath $file.FullName -Raw
    foreach ($match in [regex]::Matches($text, '[A-Za-z][A-Za-z0-9-]*')) {
        $name = $match.Value
        if ($owners.ContainsKey($name) -and -not $selected.ContainsKey($owners[$name].Name)) {
            $pending.Enqueue($owners[$name])
        }
    }
}

$stage = Join-Path $ProjectRoot 'src/marici-target'
if (Test-Path -LiteralPath $stage) { Remove-Item -LiteralPath $stage -Recurse -Force }
New-Item -ItemType Directory -Path $stage -Force | Out-Null
$mariciFiles = $selected.Values | Sort-Object Name
foreach ($file in $mariciFiles) { Copy-Item -LiteralPath $file.FullName -Destination $stage }

$coreFiles = @(
    Get-ChildItem -LiteralPath (Join-Path $ProjectRoot 'src/hott') -Filter '*.rzk.md' -File -Recurse
    Get-ChildItem -LiteralPath (Join-Path $ProjectRoot 'src/simplicial-hott') -Filter '*.rzk.md' -File -Recurse
) | Sort-Object FullName | ForEach-Object { [IO.Path]::GetRelativePath($ProjectRoot, $_.FullName) }
$targetFiles = $mariciFiles | ForEach-Object { Join-Path 'src/marici-target' $_.Name }
$arguments = @('typecheck') + $coreFiles + $targetFiles

$resultsDirectory = Join-Path $root 'results'
New-Item -ItemType Directory -Force -Path $resultsDirectory | Out-Null
$stem = [IO.Path]::GetFileNameWithoutExtension([IO.Path]::GetFileNameWithoutExtension($Target))
$stdoutPath = Join-Path $resultsDirectory "$stem.target-closure.stdout.log"
$stderrPath = Join-Path $resultsDirectory "$stem.target-closure.stderr.log"
Write-Output "Typechecking $($coreFiles.Count) core and $($targetFiles.Count) Marici files"
& (Join-Path $root 'run-contained.ps1') -Executable 'rzk' -WorkingDirectory $ProjectRoot -ChildArgument $arguments -StdoutPath $stdoutPath -StderrPath $stderrPath -TimeoutSeconds $TimeoutSeconds
if (Test-Path -LiteralPath $stdoutPath) { Get-Content -LiteralPath $stdoutPath }
if (Test-Path -LiteralPath $stderrPath) { Get-Content -LiteralPath $stderrPath | Write-Output }
