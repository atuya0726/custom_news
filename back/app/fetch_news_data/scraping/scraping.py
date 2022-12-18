import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir)+"/connector")
print(sys.path)
from yahoo import result
def scraping():
    yahoo_result = result()
    return yahoo_result
