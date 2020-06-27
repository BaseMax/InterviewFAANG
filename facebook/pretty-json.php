<?php
// Max Base
// https://github.com/BaseMax/FAANGInterview
function repeat($t) {
  if($t > 0) {
    return str_repeat("\t", $t);
  }
  return "";
}
function prettyJSON($a) {
  $res="";
  $ident=0;
  $lines=[];
  $len=strlen($a);
  $i=0;
  while($i<$len) {
    if($a[$i] == '{' || $a[$i] == '[') {
      if($res != "") {
        $lines[]=$res;
        $res="";
      }
      $res.=repeat($ident);
      $res.=$a[$i];
      $lines[]=$res;
      $res="";
      $ident++;
    }
    else if($a[$i] == '}' || $a[$i] == ']') {
      if($res != "") {
        $lines[]=$res;
        $res="";
      }
      $ident--;
      $lines[]=repeat($ident).$a[$i];
    }
    else {
      if($res == "") {
        $res=repeat($ident);
      }
      if($a[$i] == ",") {
        $res.=$a[$i];
        $lines[]=$res;
        $res="";
      }
      else {
        $res.=$a[$i];
      }
    }
    $i++;
  }
  print_r($lines);
  return $res;
}
print prettyJSON('{A:"B۱",C:{D:"E",F:{G:"H",I:"J"}}}')."\n";
print prettyJSON('["foo",5,{"bar":["baz",null,1.0,2]}]')."\n";
print prettyJSON('["foo",5,["bar",1,2]]')."\n";
print prettyJSON('[123,456]')."\n";
