from behave import given, when, then
from hamcrest import assert_that, equal_to

users = {}
catalog = []
dashboard_visible = False
last_error = None
query = None

@given('existe una usuaria "{email}" con contraseña "{pwd}"')
def step_impl(context, email, pwd):
    users[email] = pwd

@when('inicio sesión con email "{email}" y contraseña "{pwd}"')
def step_impl(context, email, pwd):
    global dashboard_visible, last_error
    if email not in users:
        last_error = "Usuario no existe"
    elif users[email] != pwd:
        last_error = "Credenciales inválidas"
    else:
        dashboard_visible = True

@then("debo ver el panel principal")
def step_impl(context):
    assert dashboard_visible is True

@then('debo ver el error "{msg}"')
def step_impl(context, msg):
    assert_that(last_error, equal_to(msg))

@given("el catálogo contiene:")
def step_impl(context):
    global catalog
    # DataTable con encabezado 'nombre'
    catalog = [row["nombre"] for row in context.table]

@when('busco "{q}"')
def step_impl(context, q):
    global query
    query = q

@then('los resultados deben incluir "{name}"')
def step_impl(context, name):
    assert name in catalog

@then('veo el mensaje "No se encontraron resultados"')
def step_impl(context):
    if query not in catalog:
        shown = "No se encontraron resultados"
        assert "No se encontraron" in shown
    else:
        raise AssertionError("Se esperaba no encontrar resultados, pero sí había.")
