#!/usr/bin/bash

cat drawing.flag.svg | grep '</tspan>' | cut -d '>' -f2 | cut -d '<' -f1 | paste -s -d ' ' | tr -d ' '
