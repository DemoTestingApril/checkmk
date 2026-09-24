# Python dependency-tree demo

Poetry project used to demonstrate Semgrep SCA **dependency path** rendering.

`poetry.lock` is a real, resolved lockfile (Poetry 2.5.1). Poetry is one of the
few lockfile formats Semgrep parses into a dependency *graph*, so findings here
render a package-to-package path rather than just a flat "transitive" label.

Deepest vulnerable chain:

    apache-airflow -> apache-airflow-providers-http -> requests -> urllib3

Ten vulnerable packages are present across depths 1-4.
