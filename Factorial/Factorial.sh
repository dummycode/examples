#!/bin/bash
getFactorial() {
    if [ $1 -lt 1 ]; then 
        return 1
    else
        getFactorial $[$1 - 1]
        return $[$1 * $?]
    fi
}
if [ $1 ]; then
    getFactorial $1
    echo $?
else
    echo 'Invalid arguments'
fi
