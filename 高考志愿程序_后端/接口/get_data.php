<?php
 function gbk2utf8($data){
    if(is_array($data)){
      return array_map('gbk2utf8', $data);
    }
    return iconv('gbk','utf-8',$data);
  }
/*
$a=50;
$b=10.5;
echo shell_exec("python C:/Users/lenovvo/test_py.py $a $b 2>&1")
//echo $res;
*/
$res=array();
//$res['result1']='啦啦啦';
exec("python C:/Users/lenovvo/test_py.py 2>&1",$res);

//$res_array = explode(",", $res);

$json = json_encode(
    //array()是组织要显示的数据结构
   gbk2utf8( $res)
);
//print_r ($res);
//echo $res_array[1];
echo gettype($json)
?>