#!/bin/bash
# usage: assemble.sh <key> <target md name> <pages desc> <scope>
key=$1; target=$2; pages=$3; scope=$4
out="$key/assembled.md"
{
printf -- '---\nsource: "%s"\npages: %s\ntranscription: vision, page-by-page from 200 dpi renders\ntranscribed: %s\nscope: %s\nfurigana: "{漢字|かな} (markdown-furigana)"\ntags: [lahde]\n---\n\n' "${target%.md}.pdf" "$pages" "$(date +%F)" "$scope"
first=1
for f in $(ls $key/out/p*.md | sort); do
  [ -s "$f" ] || continue
  [ $first = 1 ] || printf '\n\n'
  first=0
  sed -e 's/[[:space:]]*$//' "$f" | perl -0pe 's/\n+\z//'
done
printf '\n'
} > "$out"
# sanity: unbalanced furigana braces
perl -ne 'my $o=()=/\{/g; my $c=()=/\}/g; print "brace mismatch line $.: $_" if $o!=$c' "$out"
perl -ne 'print "bad ruby line $.: $_" if /\{[^|}]*\}/' "$out"
wc -lc "$out"
