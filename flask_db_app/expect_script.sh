#!/bin/bash
 

set timeout -1

spawn python flask_db_app/app.py

 

expect "Ctrl+C to quit"

send "\003"

interact
