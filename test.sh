if ! command -v flake8 &> /dev/null; then
  not_found=flake8
elif ! command -v isort &> /dev/null; then
  not_found=isort
else
  not_found=""
fi

if [ "$not_found" != "" ]; then
  echo "Command '$not_found' was not found"
  echo "You can try \`pip install .[dev]\` before doing this"
  exit 1
fi

returncode=0

_run () {
  echo "Execute \`$@\`"
  $@
  r=$?

  if [ $r -eq 0 ]; then
    echo "Success"
  else
    echo "Failure"
  fi

  return $r
}

if ! _run flake8 ./src/; then
  returncode=1
fi

if ! _run isort --check --diff ./src/; then
  returncode=1
fi

exit $returncode
