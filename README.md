# Plantillas BDD (Java + Python) con Workflows de GitHub Actions

Este paquete contiene tres plantillas listas para usar y dos *workflows*:

- `java-bdd-template/` — Maven + JUnit + Cucumber-JVM.
- `python-behave-template/` — Behave.
- `python-pytest-bdd-template/` — pytest-bdd.
- `.github/workflows/ci-java-bdd.yml` y `ci-python-bdd.yml` — configurados para ejecutarse dentro de estas carpetas.
  - Si tu repo tiene el código en la raíz, cambia `working-directory` por `.` o elimina esa sección.

## Uso rápido

### Java
```bash
cd java-bdd-template
mvn test
```

### Python (Behave)
```bash
cd python-behave-template
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
behave
```

### Python (pytest-bdd)
```bash
cd python-pytest-bdd-template
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
