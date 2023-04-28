#!/bin/bash
# Print size downloaded in bytes
curl -ws '%{size_download}\n' -o /dev/null "$1"
