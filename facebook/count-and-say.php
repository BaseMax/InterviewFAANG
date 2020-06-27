<?php
// Max Base
// https://github.com/BaseMax/FAANGInterview
// https://en.wikipedia.org/wiki/Look-and-say_sequence
function counting($n) { 
	if($n == 1)
		return "1";
	if($n == 2)
		return "11";
	$result = "11";
	for ($i=3;$i<=$n;$i++) {
		$result = $result.'@';
		$length = strlen($result);
		$current = 1;
		$temp = "";
		for($j=1;$j<$length;$j++) {
			if($result[$j] != $result[$j - 1]) {
				$temp = $temp.$current . $result[$j - 1];
				$current = 1;
			}
			else $current++;
		}
		$result = $temp;
	}
	return $result;
} 
print counting(5)."\n";
