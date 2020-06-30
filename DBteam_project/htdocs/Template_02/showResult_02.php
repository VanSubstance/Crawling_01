<?php
// RESULT 버튼 눌렀을 때의 반환값:
// 선 그래프를 위한 좌표 
// Array: [ 상위 5개역에 대한 { 역 이름 : [ 1 ~ 5주차 숫자 ] } ]
    header("Content-Type:application/json");
    $stationArray = $_POST["station"];
    $stationArray = explode(', ', $stationArray);
    $result = array();
    foreach ($stationArray as $station) {
        exec("cd py_code && graph.py \"".$station."\"", $output);
        $result[$station] = $output;
        $output = [];
    }
    echo json_encode($result);
?>