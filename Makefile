# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = .

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile final

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	sphinx-build -b gettext "$(SOURCEDIR)" "$(BUILDDIR)/gettext"
	sphinx-intl update -p build/gettext -l it -l en
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

all:
	sphinx-build -b gettext "$(SOURCEDIR)" "$(BUILDDIR)/gettext"
	sphinx-intl update -p "$(BUILDDIR)/gettext" -l it -l en
	@$(SPHINXBUILD) -b html -D language='it' "$(SOURCEDIR)" "$(BUILDDIR)/docs/it" $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -b html -D language='en' "$(SOURCEDIR)" "$(BUILDDIR)/docs/en" $(SPHINXOPTS) $(O)
