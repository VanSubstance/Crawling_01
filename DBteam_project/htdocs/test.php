<?php
error_reporting(E_ALL);
ini_set("display_errors", 1);
echo "Test 01<br/>";
$test = 1;
echo "echo 되는지 확인<br/>";
echo "변수값 출력 확인: $test <br/>";
$conn = mysqli_connect('localhost', 'root', '123456', 'mysql');
echo "connect 활성화<br/>";

$RestsPerStation = array();
$sql = "SELECT STATION_NAME, count(RESTAURANT_NAME) AS unit FROM RESTAURANTS GROUP BY STATION_NAME";
echo "삽입할 쿼리: $sql<br/>";
$result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
while ($row = mysqli_fetch_array($result)) {
    array_push($RestsPerStation, $row['unit']);
    echo '<p>'.$row['STATION_NAME'].
    '|'.$row['unit'].
    '</p>';
}
$placesPerStation = array();
$sql = "SELECT STATION_NAME, count(PLACE_NAME) AS unit FROM PLACES GROUP BY STATION_NAME";
echo "삽입할 쿼리: $sql<br/>";
$result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
while ($row = mysqli_fetch_array($result)) {
    array_push($placesPerStation, $row['unit']);
    echo '<p>'.$row['STATION_NAME'].
    '|'.$row['unit'].
    '</p>';
}
$actsPerStation = array();
$sql = "SELECT STATION_NAME, count(ACTIVITY_NAME) AS unit FROM ACTIVITIES GROUP BY STATION_NAME";
echo "삽입할 쿼리: $sql<br/>";
$result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
while ($row = mysqli_fetch_array($result)) {
    array_push($actsPerStation, $row['unit']);
    echo '<p>'.$row['STATION_NAME'].
    '|'.$row['unit'].
    '</p>';
}

$sql = "SELECT * FROM RESTAURANTS where STATION_NAME = 'Chunho'";
echo "삽입할 쿼리: $sql<br/>";
$result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
while ($row = mysqli_fetch_array($result)) {
    echo '<p>'.$row['STATION_NAME'].
    '|'.$row['RESTAURANT_NAME'].
    '|'.$row['REV_NUM'].
    '|'.$row['URL'].
    '</p>';
}

$stationArray = array();

$sql = "SELECT STATION_NAME as stationName FROM STATIONS";
echo "삽입할 쿼리: $sql<br/>";
$result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
while ($row = mysqli_fetch_array($result)) {
    array_push($stationArray, $row['stationName']);
    echo '<p>'.$row['stationName'].
    '</p>';
}
echo "역 이름 배열: <br/>";
var_dump($stationArray);
echo "<br/>역별 식당 수 배열: <br/>";
var_dump($RestsPerStation);
?>