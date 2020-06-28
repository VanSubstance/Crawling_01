<?php
    for ($i=0; $i < count($_POST['a']); $i++) { 
        $position = $_POST['a'];
        echo "
        <script>
            console.log(".$position[i].");
        </script>        
        ";
    }
?>