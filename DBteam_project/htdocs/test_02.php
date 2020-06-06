<?php
error_reporting(E_ALL);
ini_set("display_errors", 1);
$conn = mysqli_connect('localhost', 'root', '123456', 'mysql');

$RestsPerStation = array();
$placesPerStation = array();
$actsPerStation = array();
$stationArray = array();

$sql = "SELECT STATION_NAME, count(RESTAURANT_NAME) AS unit FROM RESTAURANTS GROUP BY STATION_NAME";
$result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
while ($row = mysqli_fetch_array($result)) {
    array_push($RestsPerStation, $row['unit']);
}
$sql = "SELECT STATION_NAME, count(PLACE_NAME) AS unit FROM PLACES GROUP BY STATION_NAME";
$result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
while ($row = mysqli_fetch_array($result)) {
    array_push($placesPerStation, $row['unit']);
}
$sql = "SELECT STATION_NAME, count(ACTIVITY_NAME) AS unit FROM ACTIVITIES GROUP BY STATION_NAME";
$result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
while ($row = mysqli_fetch_array($result)) {
    array_push($actsPerStation, $row['unit']);
}
$sql = "SELECT STATION_NAME as stationName FROM STATIONS";
$result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
while ($row = mysqli_fetch_array($result)) {
    array_push($stationArray, $row['stationName']);
}    
$dataSet = array();
$i = 0;
foreach ($stationArray as $key) {
    $dataSet[$key] = [$actsPerStation[$i], $placesPerStation[$i], $RestsPerStation[$i]];
    $i++;
}

echo "역 이름 배열: <br/>";
var_dump($stationArray);

echo "<br/>역별 식당 수 배열: <br/>";
var_dump($RestsPerStation);

echo "<br/>결합된 배열: <br/>";
var_dump($dataSet);
?>