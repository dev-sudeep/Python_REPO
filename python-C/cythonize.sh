mv "$1" "${1}x"
a="${1}x"

python setup.py build_ext $a --inplace