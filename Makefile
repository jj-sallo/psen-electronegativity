SHELL := /bin/bash

.PHONY: env-update lock-generate lock-refresh lock-check

env-update:
	conda env update --file environment.yml --prune

lock-generate:
	conda run -n base conda-lock lock -f environment.yml -p linux-64 --kind explicit

lock-refresh:
	$(MAKE) env-update
	$(MAKE) lock-generate

lock-check:
	$(MAKE) lock-generate
	git diff --exit-code -- conda-linux-64.lock
