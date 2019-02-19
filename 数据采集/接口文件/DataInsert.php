<?php
function _error_handler($errno, $errstr ,$errfile, $errline)
{
    echo "错误编号errno: $errno<br>";
    echo "错误信息errstr: $errstr<br>";
    echo "出错文件errfile: $errfile<br>";
    echo "出错行号errline: $errline<br>";
}
 
set_error_handler('_error_handler', E_ALL | E_STRICT);  // 注册错误处理方法来处理所有错误

 function gbk2utf8($data){
    if(is_array($data)){
      return array_map('gbk2utf8', $data);
    }
    return iconv('gbk','utf-8',$data);
  }
//需要从微信端获得‘command’命令参数，以区分不同的功能：
//  ‘get_school’向用户返回需要填写的学校;
//	'get_major'返回一个还没有填写一级学科的专业（如果没有了就返回空）
//  'insert_data' 向数据库中插入新的专业以及其它属性
//  'update_data'向数据库中更新某个已存专业的其它属性
//  'next_school'检查该用户是否已经完成当前学校，若是，则返回新的学校
$command=$_GET['command'];
switch($command){
	/*
	case 'insert_user':
		//获取用户ID
		$userID=$_GET['userID'];
		$res=array();
		exec("python C:/Users/lenovvo/DataInsert.py $command $userID 2>&1",$res);
		$json = json_encode(
		gbk2utf8( $res)
		);
		echo $json;
		break;
		*/
	case 'insert_data':
		$userID=$_GET['userID'];
		$major=$_GET['trans_major'];
		$user_nickname=$_GET['user_nickname'];
		$school=$_GET['trans_school'];
		$avg=$_GET['trans_avg'];
		$highest=$_GET['trans_highest'];
		$province=$_GET['trans_province'];
		$subject=$_GET['trans_subject'];
		$year=$_GET['trans_year'];
		$pici=$_GET['trans_pici'];
		$category=$_GET['trans_category'];
		$upper_major=$_GET['trans_upper_major'];
		$major_rank=$_GET['trans_major_rank'];
		$lowest=$_GET['trans_lowest'];
		$mysqli = new mysqli('39.96.168.183','root','123456','gaokao','3306');
		$sql_major = "insert into majors values('$major','$school',$avg,$lowest,$highest,'$province','$subject',$year,'$pici','$category','$upper_major','$major_rank',1)";
		$sql_user="update user set insert_number=insert_number+1 where user_ID='$userID' and user_nickname='$user_nickname'";
		$sql_is_existed="select 
							case when exists ( select flag_finish from majors where 专业名称='$major' and 学校名称='$school' and 省份='$province' and 科类='$subject' and 年份='$year' and 批次='$pici' limit 1) 
							then 1 else 0 end
								as result";
		$mysqli -> query('set names utf8');
		//去重
		$result=$mysqli -> query($sql_is_existed);
		if ($result->fetch_row()[0]==0)//不存在
		{	$mysqli -> query($sql_major);
			$mysqli -> query($sql_user);
			echo 1;}
			else{				
			echo 0;
			}
		$mysqli -> close();
		break;
	case 'update_data':
		$userID=$_GET['userID'];
		$user_nickname=$_GET['user_nickname'];
		$major=$_GET['trans_major'];
		$school=$_GET['trans_school'];
		$avg=$_GET['trans_avg'];
		$highest=$_GET['trans_highest'];
		$province=$_GET['trans_province'];
		$subject=$_GET['trans_subject'];
		$year=$_GET['trans_year'];
		$pici=$_GET['trans_pici'];
		$category=$_GET['trans_category'];
		$upper_major=$_GET['trans_upper_major'];
		$major_rank=$_GET['trans_major_rank'];
		$lowest=$_GET['trans_lowest'];
		$mysqli = new mysqli('39.96.168.183','root','123456','gaokao','3306');
		$sql_major = "update majors
				set 录取平均分= case when majors.录取平均分 is Null then $avg else majors.录取平均分 end ,
					录取最高分= case when majors.录取最高分 is Null then $highest else majors.录取最高分 end,
					门类='$category',
					一级学科='$upper_major',
					学科评级='$major_rank' ,
					录取最低分='$lowest',
					flag_finish=1 where 专业名称='$major' and 学校名称='$school' and 省份='$province' and 科类='$subject' and 年份='$year' and 批次='$pici'";
		//echo($userID);
		//echo($user_nickname);
		$sql_user="update user set update_number=update_number+1 where user_ID='$userID' and user_nickname='$user_nickname'";
		$mysqli -> query('set names utf8');
		//echo $sql;
		
		if (!$mysqli -> query($sql_major)) 
{ 
    echo("错误描述: " . $mysqli->error); 
} 
		if (!$mysqli -> query($sql_user)) 
{ 
    echo("错误描述: " . $mysqli->error); 
} 
		$mysqli -> close();
		echo 1;
		break;
	case 'get_school':
		//$res=array();
		//从微信端获取用户ID
		$arg=$_GET['userID'];
		$arg2=$_GET['user_nickname'];
		$arg2 = iconv("UTF-8","GB2312",$arg2);
		exec("python C:/DataInsert.py $command $arg $arg2 2>&1",$res);
		$json = json_encode(
		gbk2utf8( $res)
		);
		echo $json;
		break;
	case 'next_school':
		$res=array();
		//从微信端获取用户ID
		$arg_user=$_GET['userID'];
		$arg2=$_GET['user_nickname'];
		//从微信端获取用户当前学校
		$arg_current=$_GET['current_school'];
		$encode = mb_detect_encoding($arg_current, array("ASCII","UTF-8","GB2312","GBK","BIG5")); 
		if ($encode == "UTF-8"){ 
		$arg_current = iconv("UTF-8","GB2312",$arg_current); } 
		//$encode = mb_detect_encoding($arg_current, array("ASCII","UTF-8","GB2312","GBK","BIG5")); 
		//echo $encode;
		
		exec("python C:/DataInsert.py $command $arg_user $arg2 $arg_current 2>&1",$res);
		$json = json_encode(
		gbk2utf8( $res)
		);
		echo $json;
		
		break;	
	
	case 'get_major':
		$res=array();
		//从微信端获取用户ID
		$arg=$_GET['userID'];
		$arg2=$_GET['user_nickname'];
		//echo $arg2;
		exec("python C:/DataInsert.py $command $arg $arg2 2>&1",$res);
		//返回的参数里有'专业名称','学校名称','录取平均分','录取最高分','省份','科类','年份','批次'
		//$res_array = explode(",", $res);
		$json = json_encode(
		gbk2utf8( $res)
		);
		echo $json;
		break;
	default :break;
}

?>