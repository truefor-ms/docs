$ErrorActionPreference = 'Stop'
$docsRoot = Split-Path $PSScriptRoot -Parent
$workspaceRoot = Split-Path $docsRoot -Parent
foreach ($folder in @('docs', 'ui', 'frontend', 'backend')) {
    if (-not (Test-Path -LiteralPath (Join-Path $workspaceRoot $folder) -PathType Container)) {
        throw "Expected the Trueforms workspace layout; missing $folder in $workspaceRoot"
    }
}

$destination = Join-Path $workspaceRoot '.agents/skills'
New-Item -ItemType Directory -Path $destination -Force | Out-Null
foreach ($skill in Get-ChildItem -LiteralPath (Join-Path $PSScriptRoot 'skills') -Directory) {
    $target = Join-Path $destination $skill.Name
    New-Item -ItemType Directory -Path $target -Force | Out-Null
    Get-ChildItem -LiteralPath $skill.FullName -Force | Copy-Item -Destination $target -Recurse -Force
}
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'AGENTS.md') -Destination (Join-Path $workspaceRoot 'AGENTS.md') -Force
Write-Output "Installed five project skills and workspace instructions in $workspaceRoot"
