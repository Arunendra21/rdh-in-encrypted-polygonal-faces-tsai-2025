import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_toolkit"))
import build_tierc_paper as B
B._demo(29, os.path.join(os.path.dirname(__file__),"..","figures"),
        os.path.join(os.path.dirname(__file__),"..","outputs"))
print("demo done paper 29")
