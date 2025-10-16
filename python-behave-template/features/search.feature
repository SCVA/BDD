Feature: Búsqueda de productos
  Scenario: Búsqueda simple
    Given el catálogo contiene:
      | nombre  |
      | teclado |
      | monitor |
    When busco "teclado"
    Then los resultados deben incluir "teclado"

  Scenario Outline: Búsqueda sin resultados
    When busco "<query>"
    Then veo el mensaje "No se encontraron resultados"
    Examples:
      | query       |
      | zzz-inexist |
