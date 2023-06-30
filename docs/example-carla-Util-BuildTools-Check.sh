#!/bin/bash

#
# Parse arguments
#
DOC_STRING="Run unit tests."

USAGE_STRING=$(cat <<- END
Usage: $0 [-h|--help] [--gdb] [--xml] [--gtest_args=ARGS] [--python-version=VERSION]

Then either ran all the tests

    [--all]

Or choose one or more of the following

    [--libcarla-release] [--libcarla-debug]
    [--benchmark]

You can also set the command-line arguments passed to GTest on a ".gtest"
config file in the Carla project main folder. E.g.

    # Contents of ${CARLA_ROOT_FOLDER}/.gtest
    gtest_shuffle
    gtest_filter=misc*
END
)

OPTS=`getopt -o h --long help,gdb,xml,gtest_args:,all,libcarla-release,libcarla-debug,python-api,smoke,benchmark,python-version:, -n 'parse-options' -- "$@"`

eval set -- "$OPTS"

GDB=
XML_OUTPUT=false
GTEST_ARGS=`sed -e 's/#.*$//g' ${CARLA_ROOT_FOLDER}/.gtest | sed -e '/^[[:space:]]*$/!s/^/--/g' | sed -e ':a;N;$!ba;s/\n/ /g'`
LIBCARLA_RELEASE=false
LIBCARLA_DEBUG=false
SMOKE_TESTS=false
PYTHON_API=false
RUN_BENCHMARK=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --gdb )
      GDB="gdb --args";
      shift ;;
    --xml )
      XML_OUTPUT=true;
      # Create the folder for the test-results
      mkdir -p "${CARLA_TEST_RESULTS_FOLDER}"
      shift ;;
    --gtest_args )
      GTEST_ARGS="$2";
      shift 2 ;;
    --all )
      LIBCARLA_RELEASE=true;
      LIBCARLA_DEBUG=true;
      PYTHON_API=true;
      shift ;;
    --libcarla-release )
      LIBCARLA_RELEASE=true;
      shift ;;
    --libcarla-debug )
      LIBCARLA_DEBUG=true;
      shift ;;
    --smoke )
      SMOKE_TESTS=true;
      shift ;;
    --python-api )
      PYTHON_API=true;
      shift ;;
    --benchmark )
      LIBCARLA_RELEASE=true;
      RUN_BENCHMARK=true;
      GTEST_ARGS="--gtest_filter=benchmark*";
      shift ;;
    --python-version )
      PY_VERSION_LIST="$2"
      shift 2 ;;
    -h | --help )
      echo "$DOC_STRING"
      echo -e "$USAGE_STRING"
      exit 1
      ;;
    * )
      shift ;;
  esac
done

log "Running LibCarla.client unit tests (debug)."
echo "Running: ${GDB} libcarla_test_client_debug ${GTEST_ARGS} ${EXTRA_ARGS}"
${GDB} ${LIBCARLA_INSTALL_CLIENT_FOLDER}/test/libcarla_test_client_debug ${GTEST_ARGS} ${EXTRA_ARGS}
