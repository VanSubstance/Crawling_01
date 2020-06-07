<?php
$stationArray = $_POST[station];
$ctgrArray = $_POST[ctgr];
foreach ($stationArray as $station) {
    echo '<p style= " font-size: 20px;">'.$station;
    echo '</p>';
}
foreach ($ctgrArray as $ctgr) {
    echo '<p style= " font-size: 20px;">'.$ctgr;
    echo '</p>';
}
?>