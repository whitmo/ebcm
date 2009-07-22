import os
try:
    import paver.tasks
except ImportError:
    if os.path.exists("paver-minilib.zip"):
        import sys
        sys.path.insert(0, "paver-minilib.zip")
    else:
        raise ValueError('No Paver. No minilib')

paver.tasks.main()
