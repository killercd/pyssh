#!/bin/bash

mkdir -p "$HOME/kcdscript"
cp pyssh.py "$HOME/kcdscript/pyssh.py"

sed -i '/alias pyssh/d' "$HOME/.bashrc"

cat << EOF >> "$HOME/.bashrc"
alias pyssh="python $HOME/kcdscript/pyssh.py"
EOF

