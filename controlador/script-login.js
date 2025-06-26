function mostrarRegistro() {
    document.getElementById('formLogin').classList.add('oculto');
    document.getElementById('formRegistro').classList.remove('oculto');
  }
  
  function mostrarLogin() {
    document.getElementById('formRegistro').classList.add('oculto');
    document.getElementById('formLogin').classList.remove('oculto');
  }
  function acceder() {
    // Aquí puedes agregar validaciones si es necesario (por ejemplo, verificar campos no vacíos)
    
    // Redirigir a 'menuprincipal.html' después de que se presione el botón
    window.location.href = 'Menu_principal/menuprincipal.html';
  }
  