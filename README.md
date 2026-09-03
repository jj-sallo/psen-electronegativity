# Conda-forge Template with Devcontainers

This repo is a template for a conda-forge environment
that uses condaforge's miniforge3 image as a base
to setup a reproducible dev environment using
conda and conda-lock.

NOTE: using miniforge3 implies that Anaconda's
defaults channel is NOT included by default. The only
channel included is conda-forge.

# Managing conda packages

You should avoid installing packages using `conda install`.
The preferred method is adding the packages to the
`environment.yml` file and updating the environment using
the below Make targets.

# Make targets

The Makefile provides a few helper targets for keeping the environment and
lockfile in sync:

- `make env-update` updates the conda environment from `environment.yml`.
- `make lock-generate` regenerates `conda-linux-64.lock` from `environment.yml`.
- `make lock-refresh` runs `env-update` and then `lock-generate`.
- `make lock-check` regenerates the lockfile and fails if `conda-linux-64.lock`
	is out of date. Intended for CI.