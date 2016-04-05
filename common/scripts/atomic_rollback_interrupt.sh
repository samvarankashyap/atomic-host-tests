#!/bin/bash

if [ -z "$1" ]; then
    LOOP="10"
else
    LOOP=$1
fi

if [ -z "$2" ]; then
    DELAY=".5"
else
    DELAY="$2"
fi

ROLLBACK='atomic host rollback'
FAILED_FILE='/var/qe/atomic_rollback_failed'

if [ -e "$FAILED_FILE" ]; then
    rm $FAILED_FILE
fi

for l in $(seq $LOOP); do
    echo "Attempting rollback iteration $l of $LOOP with a delay of $DELAY seconds"
    timeout --signal=SIGINT $DELAY $ROLLBACK
    ROLLBACK_RV=$?
    if [ "$ROLLBACK_RV" -ne 124 ] && [ "$ROLLBACK_RV" -ne 0 ]; then
        echo "ERROR! The '$ROLLBACK' command did not exit successfully or via SIGINT"
        echo "ERROR! The reported exit status was: $ROLLBACK_RV"
        touch $FAILED_FILE
        exit $ROLLBACK_RV
    fi
    sleep 5
    echo -e "\n"
done
