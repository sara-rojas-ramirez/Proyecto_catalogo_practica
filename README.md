# 🛒 E-Commerce Django - 

Una plataforma de comercio electrónico desarrollada en Django con integración a MySQL. Este proyecto abarca la lógica central de una tienda online, gestionando desde la autenticación de usuarios y la visualización del catálogo hasta la administración del carrito de compras y la generación de pedidos.

---

## Tecnologías Utilizadas

| Componente | Tecnología |
| :--- | :--- |
| **Backend** | Python, Django |
| **Base de Datos** | MySQL (Tablas y relaciones implementadas) |
| **Frontend** | HTML, CSS, JavaScript, Boostrap |
| **Recursos** | Estructura nativa para directorios `static/` y `media/` |

---

## Funcionalidades Actuales

* **Autenticación de Usuarios:** Sistema completo de registro e inicio de sesión con control de acceso basado en roles (Administrador y Cliente).
* **Catálogo de Productos:** Visualización de productos mediante diseño de tarjetas (*cards*) con botón de agregación rápida al carrito y filtros de búsqueda básicos por categoría.
* **Gestión del Carrito de Compras:** Interfaz dedicada que permite al usuario actualizar la cantidad de productos, eliminar artículos individuales, vaciar el carrito, y visualizar el cálculo automático del subtotal y el total a pagar.
* **Checkout y Pedidos:** Flujo de finalización de compra que transfiere los datos del carrito para la creación formal del pedido.

---

## Estructura de Archivos Estáticos

El proyecto está configurado para el manejo de archivos multimedia y estáticos esenciales para el e-commerce:
* `static/`: Contiene las hojas de estilo (CSS), scripts (JavaScript) y recursos visuales base de la plataforma.
* `media/`: Gestiona el almacenamiento de los archivos dinámicos, principalmente las imágenes de los productos del catálogo.

---

## Trabajo Futuro (Roadmap)

El desarrollo del proyecto continúa activo. Las próximas características a implementar son:
* Desarrollo del panel de control (*dashboard*) para la administración integral de la tienda.
* Creación del perfil de usuario (cliente) con acceso al historial de pedidos.
* Implementación de validaciones asíncronas en tiempo real para los formularios utilizando JavaScript/AJAX.
* Integración de una pasarela de pago funcional.
* Refuerzo de las políticas de seguridad y protección de rutas.

Este es un sistema de comercio electrónico desarrollado en **Django** que cuenta con un flujo avanzado de Checkout, selección geográfica en cascada automatizada mediante **AJAX** y un módulo robusto para la gestión y resumen de pedidos.

---

