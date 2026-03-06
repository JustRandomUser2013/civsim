# Основные параметры экрана и производительности
SCREEN_SIZE = 800
FPS = 60

# Размеры игрового мира в клетках и пикселях
W_TILES = 100
H_TILES = 100
CELL_SIZE = 16

# Коэффициенты масштабирования (зум)
MIN_ZOOM = 0.5
MAX_ZOOM = 3.0
ZOOM_STEP = 0.1

# Конфигурация генерации объектов (леса и горы)
FOREST_CLUSTERS = 20
FOREST_SIZE = 60
MOUNTAIN_CLUSTERS = 10
MOUNTAIN_SIZE = 40

# Вероятности (от 0.0 до 1.0)
CLUSTER_PROBABILITY = 0.7  # Шанс роста клетки в кластере
IRON_PROBABILITY = 0.1     # Шанс появления железа в горах

# Идентификаторы типов объектов
TILE_PLAIN = 0
TILE_FOREST = 1
TILE_MOUNTAIN = 2
OVERLAY_IRON = 1
