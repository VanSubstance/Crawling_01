<?php
    error_reporting(E_ALL);
    ini_set("display_errors", 1);
    $conn = mysqli_connect('localhost', 'root', '123456', 'teamdb');

    #Restaurant category
    $ctgrRest = array();
    $sql = "SELECT CTGRGROUP FROM RESTAURANTS GROUP BY CTGRGROUP";
    $result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
    while ($row = mysqli_fetch_array($result)) {
        array_push($ctgrRest, $row['CTGRGROUP']);
    }   

    #Activity category
    $ctgrAct = array();
    $sql = "SELECT CTGRGROUP FROM ACTIVITIES GROUP BY CTGRGROUP";
    $result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
    while ($row = mysqli_fetch_array($result)) {
        array_push($ctgrAct, $row['CTGRGROUP']);
    }

    #Place category
    $ctgrPlace = array();
    $sql = "SELECT CTGRGROUP FROM PLACES GROUP BY CTGRGROUP";
    $result = mysqli_query($conn, $sql) or die(mysqli_error($conn));
    while ($row = mysqli_fetch_array($result)) {
        array_push($ctgrPlace, $row['CTGRGROUP']);
    }
?>