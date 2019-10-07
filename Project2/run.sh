#!/bin/bash

cd `dirname $0`
python3 app.py &
node nodejs_server.js

