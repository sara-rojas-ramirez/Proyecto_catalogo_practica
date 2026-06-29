// // Funcionalidad para las validaciones de login

// console.log("¡El archivo JS está conectado y funcionando!");

// document.addEventListener('DOMContentLoaded', function() {
//     const formLogin = document.getElementById('form-login');
    
//     // Capturamos los inputs generados por Django (por defecto usan id_nombrecampo)
//     const inputUsername = document.getElementById('id_username');
//     const inputPassword = document.getElementById('id_password');
    
//     // Capturamos los spans de error
//     const errorUsername = document.getElementById('error-username');
//     const errorPassword = document.getElementById('error-password');
//     const errorGlobal = document.getElementById('error-global');

//     // Función auxiliar para pintar bordes
//     function setEstadoCampo(input, errorSpan, valido, mensaje = '') {
//         if (valido) {
//             input.style.borderColor = '#28a745'; // Verde éxito
//             errorSpan.textContent = '';
//         } else {
//             input.style.borderColor = '#D9534F'; // Rojo error
//             errorSpan.textContent = mensaje;
//         }
//     }

//     if (formLogin) {
//         formLogin.addEventListener('submit', function(e) {
//             e.preventDefault();

//             // 1. Limpiar errores globales
//             errorGlobal.textContent = '';
//             let validacionLocal = true;

//             // 2. Validación básica frontend (campos vacíos)
//             if (inputUsername.value.trim() === '') {
//                 setEstadoCampo(inputUsername, errorUsername, false, 'El usuario es requerido.');
//                 validacionLocal = false;
//             } else {
//                 setEstadoCampo(inputUsername, errorUsername, true);
//             }

//             if (inputPassword.value.trim() === '') {
//                 setEstadoCampo(inputPassword, errorPassword, false, 'La contraseña es requerida.');
//                 validacionLocal = false;
//             } else {
//                 setEstadoCampo(inputPassword, errorPassword, true);
//             }

//             // Si falla la validación local, no enviamos al servidor
//             if (!validacionLocal) return;

//             // 3. Petición AJAX al servidor
//             const urlBase = formLogin.getAttribute('data-url');
//             const formData = new FormData(formLogin);

//             fetch(urlBase, {
//                 method: 'POST',
//                 body: formData,
//                 headers: {
//                     'X-Requested-With': 'XMLHttpRequest',
//                 }
//             })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.valido) {
//                     // Login exitoso: pintar verde y redirigir
//                     setEstadoCampo(inputUsername, errorUsername, true);
//                     setEstadoCampo(inputPassword, errorPassword, true);
//                     window.location.href = data.redirect_url;
//                 } else {
//                     // Login fallido: mostrar error global y pintar inputs de rojo
//                     errorGlobal.textContent = data.mensaje;
//                     inputUsername.style.borderColor = '#D9534F';
//                     inputPassword.style.borderColor = '#D9534F';
//                 }
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//                 errorGlobal.textContent = 'Ocurrió un error en el servidor.';
//             });
//         });
//     }
// });


