#!/bin/bash
# send data to server
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
