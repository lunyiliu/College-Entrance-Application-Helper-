<?php
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
switch(command=='insert_data'){
	case 'insert_data':
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
		$mysqli = new mysqli('39.107.97.123','root','123456','gaokao','3306');
		$sql = "insert into majors values('$major','$school',$avg,$highest,'$province','$subject',$year,'$pici','$category','$upper_major','$major_rank',1)";
		//$mysqli -> query('set names utf8');
		$mysqli -> query($sql);
		$mysqli -> close();
		break;
	case 'update_data':
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
		$mysqli = new mysqli('39.107.97.123','root','123456','gaokao','3306');
		$sql = "update majors
				set 录取平均分= case when majors.录取平均分 is Null then $avg else majors.录取平均分 end ,
					录取最高分= case when majors.录取最高分 is Null then $highest else majors.录取最高分 end,
					门类='$category',
					一级学科='$upper_major',
					学科评级='$major_rank' ,
					flag_finish=1 where 专业名称='$major' and 学校名称='$school' and 省份='$province' and 科类='$subject' and 年份='$year' and 批次='$pici'";
		//$mysqli -> query('set names utf8');
		$mysqli -> query($sql);
		$mysqli -> close();
		break;
	case 'get_school':
		$res=array();
		//从微信端获取用户ID
		$arg=$_GET['userID']
		exec("python C:/Users/lenovvo/DataInsert.py $command $arg 2>&1",$res);
		$json = json_encode(
		gbk2utf8( $res)
		);
		echo gettype($json)
		break;
	case 'next_school':
		$res=array();
		//从微信端获取用户ID
		$arg_user=$_GET['userID']
		//从微信端获取用户当前学校
		$arg_current=$_GET['current_school']
		exec("python C:/Users/lenovvo/DataInsert.py $command $arg_user $arg_current 2>&1",$res);
		$json = json_encode(
		gbk2utf8( $res)
		);
		echo gettype($json)
		break;		
	case 'get_major':
		$res=array();
		//从微信端获取用户ID
		$arg=$_GET['userID']
		exec("python C:/Users/lenovvo/DataInsert.py $command 2>&1",$res);
		//返回的参数里有'专业名称','学校名称','录取平均分','录取最高分','省份','科类','年份','批次'
		$json = json_encode(
		gbk2utf8( $res)
		);
		echo gettype($json)
		break;
	default :
}

?>