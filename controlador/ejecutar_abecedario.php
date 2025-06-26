<?php
// Ruta absoluta o relativa al script Python
$salida = shell_exec("python abecedario_final.py 2>&1");
echo "<pre>$salida</pre>";
?>
