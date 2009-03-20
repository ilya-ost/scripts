#!/bin/bash

cat "$1" | iconv -f cp1251 -t utf8 > "$1".new

