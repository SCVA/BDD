Feature: Inicio de sesión
  Para acceder a mi cuenta
  Como usuaria registrada
  Quiero iniciar sesión correctamente

  Background:
    Given existe una usuaria "ana@example.com" con contraseña "s3cr3ta"

  Scenario: Login válido
    When inicio sesión con email "ana@example.com" y contraseña "s3cr3ta"
    Then debo ver el panel principal

  Scenario Outline: Login inválido
    When inicio sesión con email "<email>" y contraseña "<password>"
    Then debo ver el error "<mensaje>"
    Examples:
      | email             | password | mensaje                |
      | ana@example.com   | wrong    | Credenciales inválidas |
      | nadie@example.com | s3cr3ta  | Usuario no existe      |
