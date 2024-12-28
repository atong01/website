# Makefile for richtong/lib
#
# Release tag
TAG=0.9

# adjust this for where ./src/lib is and add your own
# Note that current directory is always included so you can
# can insert your own include in the CWD if you want to override
# https://runebook.dev/en/docs/gnu_make/include
# this directive does not seem to work
# note that .INCLUDE_DIRS is a read-only list so we need our own variable
# if you are in a ws controlled repo otherwise you  need a path
# INCLUDE_DIRS ?= ../lib
# INCLUDE_DIRS ?= $(HOME)/ws/git/src/lib
INCLUDE_DIRS ?= $(WS_DIR)/git/src/lib
# adjust for your org
ORG ?= tne


## Local Make commands
## ---
## test: test the library
.PHONY: test
test:
	@echo "insert test code here..."

## clean: remove the build directory
.PHONY: clean
clean:
	@echo "insert clear code here..."

## all: build all
.PHONY: all

# list these in reverse order so the most general is last

# Adjust these assuming this is a ./src submodule
# https://www.gnu.org/software/make/manual/html_node/Foreach-Function.html
# Note that - means to ignore errors, but this is actually checks
# LIB_PATH ?= ../lib
# ifneq ($(wildcard include.mk),)
# include "$(LIB_PATH)/include.mk"
# endif
-include $(INCLUDE_DIRS)/include.mk
# -include $(INCLUDE_DIRS)/include.ai.mk
# -include $(INCLUDE_DIRS)/include.airflow.mk
# -include $(INCLUDE_DIRS)/include.docker.mk
# -include $(INCLUDE_DIRS)/include.gcp.base.mk
# -include $(INCLUDE_DIRS)/include.gcp.mk
-include $(INCLUDE_DIRS)/include.hugo.mk
# -include $(INCLUDE_DIRS)/include.jupyter.mk
# -include $(INCLUDE_DIRS)/include.node.mk
# -include $(INCLUDE_DIRS)/include.python.mk
# -include $(INCLUDE_DIRS)/include.rhash.mk

# normally your organization stuff appears last
# -include $(INCLUDE_DIRS)/include.$(ORG).mk
