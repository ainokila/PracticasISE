import pstats
p = pstats.Stats('salida')
p.strip_dirs().sort_stats(-1).print_stats()