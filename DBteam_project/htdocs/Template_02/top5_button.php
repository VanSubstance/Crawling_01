<?php
    header("Content-Type:application/json");
    $station = $_POST["station"];
    $ctgrAct = $_POST["ctgrAct"];
    $ctgrPlace = $_POST["ctgrPlace"];
    $ctgrRest = $_POST["ctgrRest"];
    $conn = mysqli_connect('localhost', 'root', '123456', 'teamdb');

    // 1. 역 별 카테고리에 해당되는 애들 출력 함수
    /// i. 각 카테고리별 해당 역 + 해당 하위카테고리 개체중 revnum top 5
    $top5Act = [];
    $top5Rest = [];
    $top5Place = [];

    if ($ctgrAct != '') {
        $sqlAct = 'SELECT ACTIVITY_NAME, REV_NUM, URL FROM ACTIVITIES WHERE CTGRGROUP IN ('.$ctgrAct.') AND STATION_NAME = '.$station.' ORDER BY REV_NUM;';
        $resultAct = mysqli_query($conn, $sqlAct) or die(mysqli_error($conn));
        $i = 0;
        while ($row = mysqli_fetch_array($resultAct)) {
            array_push($top5Act, $row);
        }
    }
    if ($ctgrPlace != '') {
        $sqlPlace = 'SELECT PLACE_NAME, REV_NUM, URL FROM PLACES WHERE CTGRGROUP IN ('.$ctgrPlace.') AND STATION_NAME = '.$station.' ORDER BY REV_NUM;';
        $resultPlace = mysqli_query($conn, $sqlPlace) or die(mysqli_error($conn));
        $i = 0;
        while ($row = mysqli_fetch_array($resultPlace)) {
            array_push($top5Place, $row);
        }
    }
    if ($ctgrRest != '') {
        $sqlRest = 'SELECT RESTAURANT_NAME, REV_NUM, URL FROM RESTAURANTS WHERE CTGRGROUP IN ('.$ctgrRest.') AND STATION_NAME = '.$station.' ORDER BY REV_NUM;';
        $resultRest = mysqli_query($conn, $sqlRest) or die(mysqli_error($conn));
        $i = 0;
        while ($row = mysqli_fetch_array($resultRest)) {
            array_push($top5Rest, $row);
        }
    }
    $resultSum = [];
    array_push($resultSum, $top5Act);
    array_push($resultSum, $top5Place);
    array_push($resultSum, $top5Rest);

    echo json_encode($resultSum);
?>