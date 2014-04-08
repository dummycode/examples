<?php
    if(count($argv) == 2)
        echo getFactorial($argv[1]) . PHP_EOL;
    else
        echo 'Invalid arguments' . PHP_EOL;
    function getFactorial($i) {
        if($i < 1)
            return 1;
        else
            return $i *= getFactorial($i - 1);
    }
?>
