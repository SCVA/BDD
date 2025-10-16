from pathlib import Path
from pytest_bdd import scenarios, given, when, then, parsers

FEATURE_FILE = Path(__file__).resolve().parents[1] / "features" / "login.feature"
scenarios(str(FEATURE_FILE))

users = {}
dashboard_visible = False
last_error = None

@given(parsers.parse('existe una usuaria "{email}" con contraseña "{pwd}"'))
def seed_user(email, pwd):
    users[email] = pwd

@when(parsers.parse('inicio sesión con email "{email}" y contraseña "{pwd}"'))
def do_login(email, pwd):
    global dashboard_visible, last_error
    if email not in users:
        last_error = "Usuario no existe"
    elif users[email] != pwd:
        last_error = "Credenciales inválidas"
    else:
        dashboard_visible = True

@then("debo ver el panel principal")
def see_dashboard():
    assert dashboard_visible

@then(parsers.parse('debo ver el error "{msg}"'))
def see_error(msg):
    assert last_error == msg
