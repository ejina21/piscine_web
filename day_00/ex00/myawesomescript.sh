#!/bin/bash
res=$(curl -Ls -I -w %{url_effective} $1 | grep Location | cut -d ' ' -f 2)
echo $res