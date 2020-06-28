<?php
    header("Content-Type:application/json");
    $ctgrAct = $_POST["ctgrAct"];
    $ctgrPlace = $_POST["ctgrPlace"];
    $ctgrRest = $_POST["ctgrRest"];
    $conn = mysqli_connect('localhost', 'root', '123456', 'teamdb');

    // 1. 역 별 카테고리량 Top5 출력 함수
    /// i. 막대 그래프
    //// 역 별 체크된 카테고리에 해당되는 개수 파악
    $sqlStation = "SELECT STATION_NAME FROM STATIONS";
    $resultStation = mysqli_query($conn, $sqlStation) or die(mysqli_error($conn));
    $resultSum = array();
    //// resultSum: ['역이름' => 개수] 형태의 어레이
    while ($row = mysqli_fetch_array($resultStation)) {
        $resultSum[$row['STATION_NAME']] = 0;
    }

    if ($ctgrAct != '') {
        $sqlAct = 'SELECT STATION_NAME, COUNT(*) AS NUM FROM ACTIVITIES WHERE CTGRGROUP IN ('.$ctgrAct.') GROUP BY STATION_NAME;';
        $resultAct = mysqli_query($conn, $sqlAct) or die(mysqli_error($conn));
        while ($row = mysqli_fetch_array($resultAct)) {
            $resultSum[$row['STATION_NAME']] += $row['NUM'];
        }
    }
    if ($ctgrPlace != '') {
        $sqlPlace = 'SELECT STATION_NAME, COUNT(*) AS NUM FROM PLACES WHERE CTGRGROUP IN ('.$ctgrPlace.') GROUP BY STATION_NAME;';
        $resultPlace = mysqli_query($conn, $sqlPlace) or die(mysqli_error($conn));
        while ($row = mysqli_fetch_array($resultPlace)) {
            $resultSum[$row['STATION_NAME']] += $row['NUM'];
        }
    }
    if ($ctgrRest != '') {
        $sqlRest = 'SELECT STATION_NAME, COUNT(*) AS NUM FROM RESTAURANTS WHERE CTGRGROUP IN ('.$ctgrRest.') GROUP BY STATION_NAME;';
        $resultRest = mysqli_query($conn, $sqlRest) or die(mysqli_error($conn));
        while ($row = mysqli_fetch_array($resultRest)) {
            $resultSum[$row['STATION_NAME']] += $row['NUM'];
        }
    }
    
    //// resultSum을 내림차순으로 정렬 후, 상위 5개역만 남기고 버리기 + 평균 하나 더해주기
    arsort($resultSum);
    $average = array_sum($resultSum) / sizeof($resultSum);
    $resultSum = array_slice($resultSum, 1, 5);
    $resultSum['Average'] = $average;
    echo json_encode($resultSum);
?>