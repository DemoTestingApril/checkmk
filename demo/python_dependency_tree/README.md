# Python dependency-tree demo

Poetry project used to demonstrate Semgrep SCA **dependency path** rendering.

`poetry.lock` is a real, resolved lockfile (Poetry 2.5.1). Poetry is one of the
few lockfile formats Semgrep parses into a dependency *graph*, so findings here
render a package-to-package path rather than just a flat "transitive" label.

Deepest vulnerable chain:

    apache-airflow -> apache-airflow-providers-http -> requests -> urllib3

Ten vulnerable packages are present across depths 1-4.

## Manifest format matters

`pyproject.toml` deliberately uses the legacy `[tool.poetry.dependencies]`
format. Semgrep's poetry manifest parser reads only that table:

    parsed_manifest.get("tool", {}).get("poetry", {}).get("dependencies", {})

With the modern PEP 621 `[project] dependencies = [...]` form (the Poetry 2.x
default), `manifest_deps` is empty, every package resolves to transitivity
`Unknown`, and no dependency path is rendered.
