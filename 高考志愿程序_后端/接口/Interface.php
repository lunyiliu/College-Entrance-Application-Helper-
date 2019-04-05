<?php
//插入乱码一定要检查数据库编码！！！
//现在数据库表utf8m64是可以用的
//PHP字符串拼接是用点号！
header("content-type:text/html;charset=utf-8");
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
//微信前端调用wx.request接口，其中的传入数据data要按照以下格式，首先，最后一个参数必须是，键：command，值：以下五个值之一：
//  ‘get_recommend_school_major_priority':按照专业优先的方式返回推荐学校。输入：第一个参数是用户昵称，键:user_nickname，值：具体的昵称；
//																				第二个参数是用户ID， 键：user_ID，值：具体的ID；
//																				最后一个参数指定前端要执行的功能，这里应该是，command: ‘get_recommend_school_major_priority'
//										  										输出：推荐的十个学校的16/17/18年的1个分数，是一个10x3x2的json数组，和一个1x10的json数组
//  'get_recommend_school_school_priority':按照学校优先的方式返回推荐学校。输入输出同上
//  'insert_data' 向数据库中插入数据（前端传入的json数据应遵循以下格式：第一个参数是表名，键："table",值：表名，
//																		第二个至倒数第二个参数是按栏位顺序的插入的值,键:随意，值:要插入的值，
//																		最后一个参数指定前端要执行的功能，这里应该是，command: 'insert_data'）
//  'handle_data'向数据库中更新/查询数据（前端传入的json数据应遵循以下格式：第一个参数是sql语句，键：'sql'，值：字符串类型，查询条件中的栏值一律以？替代，示例："select *from test where name=?"；
//																			第二个参数表征查询变量类型，键：'format'，值：字符串，示例，"issii"，从查询条件中的第一个栏位看起，若该栏是字符则增添一个's'，若是数字则增添一个'i'；
//																			第三个参数确定到底是要查询还是更新，键：'mode'，值：字符串，只允许两个值，'update'和'select'
//																			第四个参数到倒数第二个参数是查询条件里的变量，键：随意。
//																			最后一个参数指定前端要执行的功能，这里应该是，command: 'handle_data')
//  'intention_analyze'：根据用户的志愿填报返回分析。输入：第一个参数是用户昵称，键:user_nickname，值：具体的昵称
//														   第二个参数是用户ID， 键：user_ID，值：具体的ID；
//														   最后一个参数指定前端要执行的功能，这里应该是，command: ‘intention_analyze'
// 														   输出，216个排名，36个成功率，6个学校的近五年最低分，（所在省市一本线）。
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
	/*
		$userID=$_GET['userID'];
		$user_nickname=$_GET['user_nickname'];
		$score=$_GET['score'];
		$province=$_GET['province'];
		$subject=$_GET['subject'];
		$year=$_GET['year'];
		$pici=$_GET['pici'];
		$choose_list=$_GET['choose_list'];
		$focus=$_GET['focus'];
		$rank=$_GET['rank'];
		$history=$_GET['history'];	
		$mysqli = new mysqli('39.97.100.184','root','8612260','gaokao','3306');
		$mysqli -> query('set names utf8');
		//$sql_major = "insert into majors values('$major','$school',$avg,$lowest,$highest,'$province','$subject',$year,'$pici','$category','$upper_major','$major_rank',1)";
		$sql_major = "insert into majors values(?,?,?,?,?,?,?,?,?,?,?,?,1)";
		$mysqli_stmt =$mysqli->prepare($sql_major);
		$a='安徽中国语大学';
		$b=3;
		$mysqli_stmt-> bind_param('ssiiississss',$userID,$a,$score,$b,$b,$subject,$pici,$b,$focus,$rank,$history,$a);
		$b=$mysqli_stmt -> execute();
		
		if(!$b){
		die("failed".$mysqli_stmt->error);
		exit();
	}else{
		echo "success<br/>";
	}
		//$mysqli -> query($sql_major);
		$mysqli -> close();
		break;
		*/
		//echo $_GET['user_nickname'];
		$mysqli = new mysqli('39.97.100.184','root','8612260','gaokao','3306');
		$sql = "insert into ";
		$format="";
		$table=$_GET['table'];
		$sql=$sql.$table;
		$sql=$sql." values ( ";
		$param=array_slice($_GET,1,-1);
		$para_ref=array();
		foreach($param as $key => $value){
			//echo gettype($value);
			//echo '<br>';
				$sql=$sql."?,";
				if(is_int($value)){
					$format=$format."i";
				}else{
					$format=$format."s";
				}	
			if ($value=='null'){
				$param[$key]=null;
			}
		}
		//null似乎只需要直接写null
		//echo $format;
		//这里一定要注意! 传入 mysqli_stmt的参数一定要是引用，而foreach的过程是para3=para1[para2].
		foreach($param as $key => &$value){
			array_push($para_ref,$value);
			unset($value);//这里很危险，因为foreach之后变量不会被自动销毁。
		}

		$sql=chop($sql,",");
		$sql=$sql.")";
		//注意，如果传入的sql不正确，就会返回一个0，而非一个对象
		$mysqli_stmt =$mysqli->prepare($sql);
		//echo $mysqli_stmt;
		array_unshift($para_ref,$format);
			//print_r($para_ref);
			//echo '<br>';
		$ref= new ReflectionClass('mysqli_stmt');
		$method = $ref->getMethod("bind_param"); 
		$method->invokeArgs($mysqli_stmt,$para_ref); 
		
		//print_r($para_ref);
		$mysqli_stmt -> execute();
		if ($mysqli_stmt->errno!=0){
		printf("Error: %s.\n", $mysqli_stmt->error);}
		//去重
		$mysqli_stmt->close();
		
		$mysqli -> close();
		break;
	case 'handle_data':
		$mysqli = new mysqli('39.97.100.184','root','8612260','gaokao','3306');
		$sql=$_GET['sql'];
		$format=$_GET['format'];
		$mode=$_GET['mode'];
		$values=array_slice($_GET,3,-1);
		$values_ref=array();
		//这里一定要注意! 传入 mysqli_stmt的参数一定要是引用，而foreach的过程是para3=para1[para2].
		foreach($values as $key => &$value){
			array_push($values_ref,$value);
			unset($value);
		}
		array_unshift($values_ref,$format);
		$mysqli -> query('set names utf8');
		$mysqli_stmt =$mysqli->prepare($sql);
		if (is_bool($mysqli_stmt)){
			echo "sql 语句似乎出现了问题，sql:";
			echo '<br>';
			echo $sql;
			break;
		}
		$ref= new ReflectionClass('mysqli_stmt');
		$method = $ref->getMethod("bind_param"); 
		$method->invokeArgs($mysqli_stmt,$values_ref); 
		if ($mode=="update"){
			//echo '即将执行';
			$mysqli_stmt -> execute();
			//echo '已执行';
		//if ($mysqli_stmt->errno!=0){
		printf("Error: %s.\n", $mysqli_stmt->error);
		//}
		}
		else{
			
			if($mode=="select"){
				$mysqli_stmt -> execute();
			if ($mysqli_stmt->errno!=0){
				printf("Error: %s.\n", $mysqli_stmt->error);}
				$result = $mysqli_stmt->get_result();
				$res=$result->fetch_all(MYSQLI_NUM);
				//print_r($res);
				//echo is_array($res);
				foreach($res as $key =>$value){
					if (count($value)==1){
						$res[$key]=$value[0];
					}
				}
				//echo $res[7];
				
				$json = json_encode(
				//gbk2utf8( $res)
				$res,JSON_UNESCAPED_UNICODE //为了解决html测试时的中文乱码，我在前面加了header，同时json_encode加了参数
				);
				echo $json;	
			
			
			}
		else{
			echo "illegal parameters: key->mode,value->"+$mode;
			}
		}
		$mysqli_stmt->close();
		$mysqli -> close();
		break;
	case "get_recommend_school_major_priority":
		//$res=array();
		//从微信端获取用户ID
		$arg=$_GET['user_ID'];
		$arg2=$_GET['user_nickname'];
		$arg2 = iconv("UTF-8","GB2312",$arg2);
		exec("python C:/Interface.py $command $arg $arg2 2>&1",$res);
		$json = json_encode(
		gbk2utf8( $res)
		);
		echo $json;
		break;
	case 'get_recommend_school_school_priority':
		$arg=$_GET['user_ID'];
		$arg2=$_GET['user_nickname'];
		$arg2 = iconv("UTF-8","GB2312",$arg2);
		//echo '六六六';
		exec("python C:/Interface.py $command $arg $arg2 2>&1",$res);
		$json = json_encode(
		gbk2utf8( $res)
		);
		echo $json;
		break;	
	case 'intention_analyze':
		$res=array();
		//从微信端获取用户ID
		$arg=$_GET['user_ID'];
		$arg2=$_GET['user_nickname'];
		//echo $arg2;
		exec("python C:/Interface.py $command $arg $arg2 2>&1",$res);
		//返回的参数里有216个排名，36个成功率，6个学校的近五年最低分，（所在省市一本线）
		//$res_array = explode(",", $res);
		$json = json_encode(
		gbk2utf8( $res)
		);
		echo $json;
		break;
	default :break;
}

?>