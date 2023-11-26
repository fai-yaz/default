alias vim="nvim"

function newfile() {
  template_file="/Users/faiyaz/default/seerat/template.md"
  echo -n "Enter new file name: "
  read filename
  cp "$template_file" "$filename.md"
  vim "$filename.md"
}

