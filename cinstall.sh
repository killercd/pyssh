#!/bin/bash

mkdir -p "$HOME/kcdscript"

cat << EOF > "$HOME/kcdscript/pyssh"
#!/bin/bash

python3  "$HOME/kcdscript/pyssh.py"

EOF

chmod +x "$HOME/kcdscript/pyssh"
cp pyssh.py "$HOME/kcdscript/pyssh.py"
sed -i '/alias pyssh/d' "$HOME/.bashrc"

if [[ -f "$HOME/.bash_profile" ]];
then

cat << EOF >> "$HOME/.bash_profile"
export PATH=\$PATH:"\$HOME/kcdscript"
EOF

else

cat << EOF >> "$HOME/.bashrc"
export PATH=\$PATH:"\$HOME/kcdscript"
EOF

fi



