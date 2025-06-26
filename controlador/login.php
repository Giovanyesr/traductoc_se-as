<?php
session_start();
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Conexión a la base de datos
$conexion = new mysqli("localhost", "root", "", "bd_tuvozjunin");
if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

// Obtener datos del formulario
$email = $_POST['email'];
$password = $_POST['password'];

// Buscar el usuario
$sql = "SELECT * FROM usuarios WHERE email = ?";
$stmt = $conexion->prepare($sql);
$stmt->bind_param("s", $email);
$stmt->execute();
$resultado = $stmt->get_result();

if ($resultado->num_rows === 1) {
    $usuario = $resultado->fetch_assoc();
    
    // Verificar la contraseña
    if (password_verify($password, $usuario['password'])) {
        // Opcional: guardar sesión
        $_SESSION['usuario'] = $usuario['nombre'];
        
        // Redirigir al menú principal
        header("Location: ../Menu_Principal/menuprincipal.html");

        exit();
    } else {
        echo "<script>alert('Contraseña incorrecta'); window.location.href='login.html';</script>";
    }
} else {
    echo "<script>alert('Correo no registrado'); window.location.href='login.html';</script>";
}

$stmt->close();
$conexion->close();
?>
