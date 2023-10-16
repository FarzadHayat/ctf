#!/usr/bin/bash

./run 'Hello!' | grep -oE "picoCTF{.*}" --color=none\n
