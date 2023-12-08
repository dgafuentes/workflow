# workflow
Instalación y ejecución del flujp

```bash
pip install prefect
prefect version
prefect server start
python main.py
# Crear un deployment
prefect deployment build main.py:main -n demo1
prefect deployment apply main-deployment.yaml
prefect agent start -q 'default'
```
