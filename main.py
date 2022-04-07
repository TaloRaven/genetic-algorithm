
from statistics import mean
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from functions.gen_alg import gen_alg

if __name__ == "__main__":
    start=datetime.now()    
    gen_alg('berlin52')
    print (f"Runtime of the program is {datetime.now()-start}")
    