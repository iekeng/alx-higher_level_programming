#!/bin/bash
# Print size downloaded in bytes
curl -s -w '%{size_download}\n' -o /dev/null "$1"
