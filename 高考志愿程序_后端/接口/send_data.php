<?php
$data_got1=$_GET['trans_data1'];
$data_got2=$_GET['trans_data2'];
$mysqli = new mysqli('39.107.97.123','root','123456','gaokao','3306');
$sql = "insert into user_test values('$data_got1','$data_got2')";
//$mysqli -> query('set names utf8');
$mysqli -> query($sql);
$mysqli -> close();
?>