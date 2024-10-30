# El enunciado para el ejercicio resuelto en Flask podría ser algo como:

# Enunciado del ejercicio:
# Objetivo: Implementar una API REST que permita actualizar la contraseña de un usuario mediante una petición HTTP PUT.

# Descripción:

# Implementa una ruta en una aplicación Flask que permita actualizar la contraseña de un usuario, identificado por su correo electrónico.
# La ruta debe recibir el correo electrónico del usuario como un parámetro en la URL y los nuevos datos a través del cuerpo de la petición en formato JSON. El JSON debe incluir la clave "newpass" con el nuevo valor de la contraseña.
# La lógica debe validar si la nueva contraseña fue proporcionada. Si no fue enviada, debe devolver un mensaje de error con un código 404 indicando que no se proporcionó la contraseña.
# Si el usuario con el correo dado existe en la lista de usuarios, la contraseña debe ser actualizada, y la respuesta debe devolver un mensaje indicando "usuario actualizado" con el código 200.
# Si no se encuentra el usuario en la lista, la API debe responder con un mensaje de "usuario no encontrado" y un código 404.