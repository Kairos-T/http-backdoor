#!/bin/bash

DIR="/home/cure51/server/uploads"
ARCHIVE="/tmp/$(date +%Y%m%d_%H%M%S).tar.gz"

tar -czf $ARCHIVE -C $DIR .

wget --method=POST --body-file=$ARCHIVE --header="Content-Type: application/octet-stream" http://192.168.1.10:8123 -O /dev/null &> /dev/null
