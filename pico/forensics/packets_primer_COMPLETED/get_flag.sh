#!/usr/bin/bash

strings network-dump.flag.pcap | tr -d ' ' | grep -E 'picoCTF{.*}'
