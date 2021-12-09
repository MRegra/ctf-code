#!/bin/bash

chmod +x generate_message_script.sh;
./generate_message_script.sh > message.out
nc jupiter.challenges.picoctf.org 9745 < message.out
