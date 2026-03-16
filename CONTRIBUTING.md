# Contributing to mtl-escrow-python-sdk

Thank you for your interest in contributing! We welcome all contributions — bug reports, feature requests, documentation improvements, and code changes.

## How to Contribute

1. **Fork** the repository
2. **Create a branch** from `main` using our naming convention:
   - `feature/` — new functionality
   - `fix/` — bug fixes
   - `chore/` — maintenance tasks
   - `docs/` — documentation changes
3. **Make your changes** and ensure they follow existing code patterns
4. **Run tests** before submitting:
   ```bash
   poetry install
   poetry run pytest -v
   ```
5. **Commit** using [Conventional Commits](https://www.conventionalcommits.org/) format:
   - `feat:` — new feature
   - `fix:` — bug fix
   - `docs:` — documentation only
   - `chore:` — maintenance, dependencies, tooling
   - `refactor:` — code change that neither fixes a bug nor adds a feature
   - `test:` — adding or updating tests
6. **Open a Pull Request** against `main`

## Code Style

- Format code with `black` and `autopep8`
- Lint with `flake8`
- Keep changes focused — one PR per concern

## Reporting Issues

If you find a bug or have a feature request, please [open an issue](https://github.com/musictechlab/mtl-escrow-python-sdk/issues).

## Security

If you discover a security vulnerability, **do not** open a public issue. Please see [SECURITY.md](SECURITY.md) for responsible disclosure instructions.

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## Questions?

Reach out at [musictechlab.io/contact](https://musictechlab.io/contact).
