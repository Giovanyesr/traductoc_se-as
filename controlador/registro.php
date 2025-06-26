<?php
// Mostrar errores durante el desarrollo
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Conexión a la base de datos
$conexion = new mysqli("localhost", "root", "", "bd_tuvozjunin");
if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

// Obtener datos del formulario
$nombre = $_POST['nombre'];
$email = $_POST['email'];
$password = password_hash($_POST['password'], PASSWORD_DEFAULT);
$telefono = $_POST['telefono'];
$direccion = $_POST['direccion'];
$distrito = $_POST['distrito'];
$provincia = $_POST['provincia'];
$departamento = $_POST['departamento'];

// Insertar en la base de datos
$sql = "INSERT INTO usuarios (nombre, email, password, telefono, direccion, distrito, provincia, departamento)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)";

$stmt = $conexion->prepare($sql);
$stmt->bind_param("ssssssss", $nombre, $email, $password, $telefono, $direccion, $distrito, $provincia, $departamento);

if ($stmt->execute()) {
    echo "<script>alert('Registro exitoso'); window.location.href='login.html';</script>";
} else {
    echo "Error al registrar: " . $stmt->error;
}

$stmt->close();
$conexion->close();
?>
