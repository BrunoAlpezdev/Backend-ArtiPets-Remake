import multiprocessing
bind = "0.0.0.0:10000"
workers = 1  # Solo un worker por la CPU limitada
threads = 2  # Dos hilos para manejar múltiples solicitudes
timeout = 60  # Evita que Render mate el proceso si se congela
loglevel = "info"  # Puedes cambiar a "debug" si necesitas más detalles

